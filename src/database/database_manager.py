"""
FinanTidy Database Manager
Handles database connections, initialization, and operations
"""

import os
import sqlite3
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import OperationalError
from contextlib import contextmanager
import logging
from typing import Optional, Dict, Any, List
import json
from datetime import datetime, timedelta
import uuid

from .models import Base as MasterBase, User, Company, UserCompanyAccess, License
from .business_models import Base as BusinessBase, Invoice, InvoiceItem, Provider, Transaction, Account, Setting, AuditLog

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DatabaseManager:
    """Centralized database management for FinanTidy"""
    
    def __init__(self, base_dir: str = None):
        """Initialize database manager"""
        if base_dir is None:
            base_dir = os.path.join(os.path.expanduser("~"), "FinanTidy", "data")
        
        self.base_dir = base_dir
        self.master_db_path = os.path.join(base_dir, "master.sqlite")
        self.company_dbs = {}  # Cache for company database connections
        
        # Ensure data directory exists
        os.makedirs(base_dir, exist_ok=True)
        
        # Initialize master database
        self.master_engine = None
        self.master_session_factory = None
        self.init_master_database()
    
    def init_master_database(self):
        """Initialize master database for users and companies"""
        try:
            self.master_engine = create_engine(
                f"sqlite:///{self.master_db_path}",
                echo=False,  # Set to True for SQL debugging
                pool_pre_ping=True
            )
            
            # Create tables
            MasterBase.metadata.create_all(self.master_engine)
            
            # Create session factory
            self.master_session_factory = scoped_session(
                sessionmaker(bind=self.master_engine)
            )
            
            # Create default admin user if not exists
            self.create_default_admin()
            
            logger.info(f"Master database initialized: {self.master_db_path}")
            
        except Exception as e:
            logger.error(f"Failed to initialize master database: {e}")
            raise
    
    def get_company_db_path(self, company_id: int) -> str:
        """Get database path for specific company"""
        return os.path.join(self.base_dir, f"company_{company_id}.sqlite")
    
    def init_company_database(self, company_id: int):
        """Initialize database for specific company"""
        try:
            db_path = self.get_company_db_path(company_id)
            engine = create_engine(
                f"sqlite:///{db_path}",
                echo=False,
                pool_pre_ping=True
            )
            
            # Create tables
            BusinessBase.metadata.create_all(engine)
            
            # Create session factory
            session_factory = scoped_session(sessionmaker(bind=engine))
            
            # Cache the connection
            self.company_dbs[company_id] = {
                'engine': engine,
                'session_factory': session_factory,
                'db_path': db_path
            }
            
            # Initialize default settings and accounts
            self.init_company_defaults(company_id)
            
            logger.info(f"Company database initialized: {db_path}")
            
        except Exception as e:
            logger.error(f"Failed to initialize company database {company_id}: {e}")
            raise
    
    def get_company_session(self, company_id: int):
        """Get database session for specific company"""
        if company_id not in self.company_dbs:
            self.init_company_database(company_id)
        
        return self.company_dbs[company_id]['session_factory']()
    
    @contextmanager
    def master_session(self):
        """Context manager for master database session"""
        session = self.master_session_factory()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"Database error: {e}")
            raise
        finally:
            session.close()
    
    @contextmanager
    def company_session(self, company_id: int):
        """Context manager for company database session"""
        session = self.get_company_session(company_id)
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"Database error for company {company_id}: {e}")
            raise
        finally:
            session.close()
    
    def create_default_admin(self):
        """Create default admin user if not exists"""
        with self.master_session() as session:
            # Check if admin user exists
            admin_user = session.query(User).filter_by(username='admin').first()
            
            if not admin_user:
                # Create admin user
                admin_user = User(
                    username='admin',
                    email='admin@finantidy.com',
                    full_name='System Administrator',
                    is_active=True,
                    first_login=True
                )
                admin_user.set_password('admin')
                session.add(admin_user)
                session.flush()  # Get the ID
                
                # Create default company
                default_company = Company(
                    tax_code='0123456789',
                    company_name='FinanTidy Demo Company',
                    legal_name='FinanTidy Demo Company Ltd.',
                    address='123 Business Street, City, Country',
                    phone='+84 123 456 789',
                    email='demo@finantidy.com',
                    business_type='Technology Services'
                )
                session.add(default_company)
                session.flush()  # Get the ID
                
                # Create access relationship
                access = UserCompanyAccess(
                    user_id=admin_user.id,
                    company_id=default_company.id,
                    role='owner'
                )
                session.add(access)
                
                # Create free license
                license = License(
                    user_id=admin_user.id,
                    license_type='free',
                    max_companies=1,
                    max_invoices_per_month=100,
                    is_active=True
                )
                session.add(license)
                
                session.commit()
                
                # Initialize company database
                self.init_company_database(default_company.id)
                
                logger.info("Default admin user and company created")
    
    def init_company_defaults(self, company_id: int):
        """Initialize default settings and accounts for company"""
        with self.company_session(company_id) as session:
            # Default settings
            default_settings = [
                ('company_name', 'FinanTidy Demo Company', 'string', 'company'),
                ('company_address', '123 Business Street, City, Country', 'string', 'company'),
                ('company_phone', '+84 123 456 789', 'string', 'company'),
                ('company_email', 'demo@finantidy.com', 'string', 'company'),
                ('currency', 'VND', 'string', 'general'),
                ('date_format', 'DD/MM/YYYY', 'string', 'general'),
                ('number_format', '1,234,567.89', 'string', 'general'),
                ('invoice_prefix', 'INV', 'string', 'invoice'),
                ('invoice_auto_number', 'true', 'boolean', 'invoice'),
                ('payment_terms_default', '30', 'number', 'invoice'),
                ('tax_rate_default', '10', 'number', 'tax'),
                ('theme', 'dark', 'string', 'ui'),
                ('language', 'Vietnamese', 'string', 'ui')
            ]
            
            for key, value, type_, category in default_settings:
                setting = Setting(
                    company_id=company_id,
                    setting_key=key,
                    setting_value=value,
                    setting_type=type_,
                    category=category,
                    is_system=True
                )
                session.add(setting)
            
            # Default accounts (Chart of Accounts)
            default_accounts = [
                ('1000', 'Cash', 'Asset', None),
                ('1100', 'Bank Account', 'Asset', None),
                ('1200', 'Accounts Receivable', 'Asset', None),
                ('1300', 'Inventory', 'Asset', None),
                ('2000', 'Accounts Payable', 'Liability', None),
                ('2100', 'Accrued Expenses', 'Liability', None),
                ('3000', 'Owner Equity', 'Equity', None),
                ('4000', 'Sales Revenue', 'Revenue', None),
                ('4100', 'Service Revenue', 'Revenue', None),
                ('5000', 'Cost of Goods Sold', 'Expense', None),
                ('6000', 'Operating Expenses', 'Expense', None),
                ('6100', 'Office Supplies', 'Expense', None),
                ('6200', 'Marketing Expenses', 'Expense', None),
                ('6300', 'Travel Expenses', 'Expense', None),
                ('6400', 'Utilities', 'Expense', None)
            ]
            
            for code, name, type_, parent_id in default_accounts:
                account = Account(
                    company_id=company_id,
                    account_code=code,
                    account_name=name,
                    account_type=type_,
                    parent_account_id=parent_id,
                    is_system=True,
                    opening_balance=0,
                    current_balance=0
                )
                session.add(account)
            
            session.commit()
            logger.info(f"Default settings and accounts created for company {company_id}")
    
    def authenticate_user(self, username: str, password: str) -> Optional[Dict[str, Any]]:
        """Authenticate user credentials"""
        try:
            with self.master_session() as session:
                user = session.query(User).filter_by(
                    username=username,
                    is_active=True
                ).first()
                
                if user and user.check_password(password):
                    # Get user's companies
                    companies = session.query(Company).join(UserCompanyAccess).filter(
                        UserCompanyAccess.user_id == user.id,
                        UserCompanyAccess.is_active == True,
                        Company.is_active == True
                    ).all()
                    
                    # Get user's license
                    license = session.query(License).filter_by(
                        user_id=user.id,
                        is_active=True
                    ).first()
                    
                    return {
                        'user': {
                            'id': user.id,
                            'username': user.username,
                            'email': user.email,
                            'full_name': user.full_name,
                            'first_login': user.first_login
                        },
                        'companies': [
                            {
                                'id': company.id,
                                'name': company.company_name,
                                'tax_code': company.tax_code,
                                'role': session.query(UserCompanyAccess).filter_by(
                                    user_id=user.id,
                                    company_id=company.id
                                ).first().role
                            }
                            for company in companies
                        ],
                        'license': {
                            'type': license.license_type if license else 'free',
                            'max_companies': license.max_companies if license else 1,
                            'max_invoices': license.max_invoices_per_month if license else 100
                        } if license else None
                    }
                
                return None
                
        except Exception as e:
            logger.error(f"Authentication error: {e}")
            return None
    
    def get_company_statistics(self, company_id: int) -> Dict[str, Any]:
        """Get statistics for company dashboard"""
        try:
            with self.company_session(company_id) as session:
                # Invoice statistics
                total_invoices = session.query(Invoice).filter_by(company_id=company_id).count()
                paid_invoices = session.query(Invoice).filter(
                    Invoice.company_id == company_id,
                    Invoice.status == 'paid'
                ).count()
                pending_invoices = session.query(Invoice).filter(
                    Invoice.company_id == company_id,
                    Invoice.status == 'sent'
                ).count()
                overdue_invoices = session.query(Invoice).filter(
                    Invoice.company_id == company_id,
                    Invoice.status == 'sent',
                    Invoice.due_date < datetime.utcnow()
                ).count()
                
                # Financial statistics
                total_revenue = session.query(Invoice.total_amount).filter(
                    Invoice.company_id == company_id,
                    Invoice.status == 'paid'
                ).scalar() or 0
                
                pending_amount = session.query(Invoice.total_amount).filter(
                    Invoice.company_id == company_id,
                    Invoice.status == 'sent'
                ).scalar() or 0
                
                # Provider statistics
                total_providers = session.query(Provider).filter_by(
                    company_id=company_id,
                    is_active=True
                ).count()
                
                # Transaction statistics
                this_month_start = datetime.utcnow().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
                monthly_transactions = session.query(Transaction).filter(
                    Transaction.company_id == company_id,
                    Transaction.transaction_date >= this_month_start
                ).count()
                
                return {
                    'invoices': {
                        'total': total_invoices,
                        'paid': paid_invoices,
                        'pending': pending_invoices,
                        'overdue': overdue_invoices
                    },
                    'financial': {
                        'total_revenue': float(total_revenue),
                        'pending_amount': float(pending_amount)
                    },
                    'providers': {
                        'total': total_providers
                    },
                    'transactions': {
                        'monthly': monthly_transactions
                    }
                }
                
        except Exception as e:
            logger.error(f"Error getting company statistics: {e}")
            return {}
    
    def generate_invoice_number(self, company_id: int) -> str:
        """Generate next invoice number for company"""
        try:
            with self.company_session(company_id) as session:
                # Get invoice prefix from settings
                prefix_setting = session.query(Setting).filter_by(
                    company_id=company_id,
                    setting_key='invoice_prefix'
                ).first()
                prefix = prefix_setting.setting_value if prefix_setting else 'INV'
                
                # Get last invoice number
                last_invoice = session.query(Invoice).filter_by(
                    company_id=company_id
                ).order_by(Invoice.id.desc()).first()
                
                if last_invoice:
                    # Extract number part from last invoice
                    last_number = last_invoice.invoice_number.replace(prefix, '')
                    try:
                        next_number = int(last_number) + 1
                    except ValueError:
                        next_number = 1
                else:
                    next_number = 1
                
                return f"{prefix}{next_number:04d}"
                
        except Exception as e:
            logger.error(f"Error generating invoice number: {e}")
            return f"INV{uuid.uuid4().hex[:8].upper()}"
    
    def generate_transaction_number(self, company_id: int) -> str:
        """Generate next transaction number for company"""
        try:
            with self.company_session(company_id) as session:
                # Get current date for transaction number
                date_part = datetime.utcnow().strftime("%Y%m%d")
                
                # Count transactions for today
                today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
                today_end = today_start + timedelta(days=1)
                
                today_count = session.query(Transaction).filter(
                    Transaction.company_id == company_id,
                    Transaction.transaction_date >= today_start,
                    Transaction.transaction_date < today_end
                ).count()
                
                return f"TXN{date_part}{(today_count + 1):03d}"
                
        except Exception as e:
            logger.error(f"Error generating transaction number: {e}")
            return f"TXN{uuid.uuid4().hex[:8].upper()}"
    
    def backup_company_data(self, company_id: int, backup_path: str = None) -> str:
        """Create backup of company data"""
        try:
            if backup_path is None:
                timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
                backup_path = os.path.join(self.base_dir, f"backup_company_{company_id}_{timestamp}.sqlite")
            
            source_path = self.get_company_db_path(company_id)
            
            # Simple file copy for SQLite
            import shutil
            shutil.copy2(source_path, backup_path)
            
            logger.info(f"Company {company_id} data backed up to: {backup_path}")
            return backup_path
            
        except Exception as e:
            logger.error(f"Error backing up company data: {e}")
            raise
    
    def restore_company_data(self, company_id: int, backup_path: str):
        """Restore company data from backup"""
        try:
            target_path = self.get_company_db_path(company_id)
            
            # Close existing connections
            if company_id in self.company_dbs:
                self.company_dbs[company_id]['engine'].dispose()
                del self.company_dbs[company_id]
            
            # Restore from backup
            import shutil
            shutil.copy2(backup_path, target_path)
            
            # Reinitialize connection
            self.init_company_database(company_id)
            
            logger.info(f"Company {company_id} data restored from: {backup_path}")
            
        except Exception as e:
            logger.error(f"Error restoring company data: {e}")
            raise
    
    def close_all_connections(self):
        """Close all database connections"""
        try:
            # Close master connection
            if self.master_engine:
                self.master_engine.dispose()
            
            # Close company connections
            for company_id, db_info in self.company_dbs.items():
                db_info['engine'].dispose()
            
            self.company_dbs.clear()
            logger.info("All database connections closed")
            
        except Exception as e:
            logger.error(f"Error closing connections: {e}")


# Global database manager instance
db_manager = None

def get_db_manager() -> DatabaseManager:
    """Get global database manager instance"""
    global db_manager
    if db_manager is None:
        db_manager = DatabaseManager()
    return db_manager

def init_database():
    """Initialize database system"""
    return get_db_manager()

def close_database():
    """Close database system"""
    global db_manager
    if db_manager:
        db_manager.close_all_connections()
        db_manager = None
