"""
Database Manager
Handles database connections, initialization, and operations
"""

import os
from pathlib import Path
from typing import Optional, List, Dict, Any
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

from database.models import Base, User, Company, UserCompanyAccess, License
from database.company_models import CompanyBase, CompanyInfo, Provider, Invoice, InvoiceItem


class DatabaseManager:
    """Manages both master database and company-specific databases"""
    
    def __init__(self, data_dir: Optional[str] = None):
        self.data_dir = Path(data_dir) if data_dir else Path.home() / "FinanTidy" / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Master database connection
        self.master_engine = None
        self.master_session_factory = None
        
        # Company database connections cache
        self.company_engines = {}
        self.company_session_factories = {}
    
    def initialize_master_db(self):
        """Initialize master database with all tables"""
        master_db_path = self.data_dir / "master.sqlite"
        
        self.master_engine = create_engine(
            f"sqlite:///{master_db_path}",
            echo=False,  # Set to True for SQL debugging
            pool_pre_ping=True
        )
        
        # Create all tables
        Base.metadata.create_all(self.master_engine)
        
        # Create session factory
        self.master_session_factory = sessionmaker(bind=self.master_engine)
        
        # Initialize with default admin user if empty
        self._create_default_admin_if_needed()
    
    def _create_default_admin_if_needed(self):
        """Create default admin user if no users exist"""
        with self.get_master_session() as session:
            user_count = session.query(User).count()
            if user_count == 0:
                admin_user = User(
                    username="admin",
                    email="admin@finantiday.local",
                    full_name="Quản trị viên",
                    first_login=True
                )
                admin_user.set_password("admin123")  # Change this in production!
                
                # Create free license for admin
                free_license = License(
                    user=admin_user,
                    license_type="free",
                    max_companies=1,
                    max_invoices_per_month=100
                )
                
                session.add(admin_user)
                session.add(free_license)
                session.commit()
    
    def get_master_session(self) -> Session:
        """Get a session for master database"""
        if not self.master_session_factory:
            raise RuntimeError("Master database not initialized")
        return self.master_session_factory()
    
    def initialize_company_db(self, tax_code: str) -> bool:
        """Initialize company-specific database"""
        try:
            company_db_path = self.data_dir / f"{tax_code}.sqlite"
            
            engine = create_engine(
                f"sqlite:///{company_db_path}",
                echo=False,
                pool_pre_ping=True
            )
            
            # Create all company tables
            CompanyBase.metadata.create_all(engine)
            
            # Cache engine and session factory
            self.company_engines[tax_code] = engine
            self.company_session_factories[tax_code] = sessionmaker(bind=engine)
            
            return True
            
        except SQLAlchemyError as e:
            print(f"Error initializing company database for {tax_code}: {e}")
            return False
    
    def get_company_session(self, tax_code: str) -> Session:
        """Get a session for company-specific database"""
        if tax_code not in self.company_session_factories:
            if not self.initialize_company_db(tax_code):
                raise RuntimeError(f"Failed to initialize database for company {tax_code}")
        
        return self.company_session_factories[tax_code]()
    
    def authenticate_user(self, username: str, password: str) -> Optional[Dict[str, Any]]:
        """Authenticate user and return user data"""
        with self.get_master_session() as session:
            user = session.query(User).filter(
                User.username == username,
                User.is_active == True
            ).first()
            
            if user and user.check_password(password):
                # Update first_login flag if needed
                if user.first_login:
                    user.first_login = False
                    session.commit()
                
                return {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'full_name': user.full_name,
                    'first_login': user.first_login
                }
        
        return None
    
    def get_user_companies(self, user_id: int) -> List[Dict[str, Any]]:
        """Get all companies accessible by user"""
        with self.get_master_session() as session:
            accesses = session.query(UserCompanyAccess).join(Company).filter(
                UserCompanyAccess.user_id == user_id,
                UserCompanyAccess.is_active == True,
                Company.is_active == True
            ).all()
            
            companies = []
            for access in accesses:
                companies.append({
                    'id': access.company.id,
                    'tax_code': access.company.tax_code,
                    'company_name': access.company.company_name,
                    'role': access.role
                })
            
            return companies
    
    def create_company(self, user_id: int, company_data: Dict[str, Any]) -> bool:
        """Create new company and give user access"""
        try:
            with self.get_master_session() as session:
                # Create company record
                company = Company(**company_data)
                session.add(company)
                session.flush()  # Get company ID
                
                # Create user access
                access = UserCompanyAccess(
                    user_id=user_id,
                    company_id=company.id,
                    role='owner'
                )
                session.add(access)
                session.commit()
                
                # Initialize company database
                self.initialize_company_db(company.tax_code)
                
                # Add company info to company database
                with self.get_company_session(company.tax_code) as company_session:
                    company_info = CompanyInfo(
                        tax_code=company.tax_code,
                        company_name=company.company_name,
                        legal_name=company_data.get('legal_name'),
                        address=company_data.get('address'),
                        phone=company_data.get('phone'),
                        email=company_data.get('email'),
                        business_type=company_data.get('business_type')
                    )
                    company_session.add(company_info)
                    company_session.commit()
                
                return True
                
        except SQLAlchemyError as e:
            print(f"Error creating company: {e}")
            return False
    
    def get_user_license(self, user_id: int) -> Optional[Dict[str, Any]]:
        """Get active license for user"""
        with self.get_master_session() as session:
            license = session.query(License).filter(
                License.user_id == user_id,
                License.is_active == True
            ).first()
            
            if license:
                return {
                    'license_type': license.license_type,
                    'max_companies': license.max_companies,
                    'max_invoices_per_month': license.max_invoices_per_month,
                    'expires_at': license.expires_at
                }
        
        return None
    
    def close_all_connections(self):
        """Close all database connections"""
        if self.master_engine:
            self.master_engine.dispose()
        
        for engine in self.company_engines.values():
            engine.dispose()
        
        self.company_engines.clear()
        self.company_session_factories.clear()
