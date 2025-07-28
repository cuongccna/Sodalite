"""
Database Models for Master Database
Contains user management, companies, and licensing tables
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import hashlib

Base = declarative_base()


class User(Base):
    """User model for authentication and user management"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=True)
    is_active = Column(Boolean, default=True)
    first_login = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    company_accesses = relationship("UserCompanyAccess", back_populates="user")
    licenses = relationship("License", back_populates="user")
    
    def set_password(self, password: str):
        """Hash and set password"""
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password: str) -> bool:
        """Check if password matches"""
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()


class Company(Base):
    """Company model for multi-tenant support"""
    __tablename__ = 'companies'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tax_code = Column(String(20), unique=True, nullable=False)  # Mã số thuế
    company_name = Column(String(200), nullable=False)
    legal_name = Column(String(200), nullable=True)
    address = Column(Text, nullable=True)
    phone = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)
    business_type = Column(String(100), nullable=True)  # Loại hình kinh doanh
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user_accesses = relationship("UserCompanyAccess", back_populates="company")


class UserCompanyAccess(Base):
    """Junction table for user-company many-to-many relationship"""
    __tablename__ = 'user_company_access'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    role = Column(String(20), nullable=False, default='owner')  # owner, admin, user, viewer
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="company_accesses")
    company = relationship("Company", back_populates="user_accesses")


class License(Base):
    """License model for subscription management"""
    __tablename__ = 'licenses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    license_type = Column(String(20), nullable=False, default='free')  # free, pro, agency
    features = Column(Text, nullable=True)  # JSON string of enabled features
    max_companies = Column(Integer, default=1)
    max_invoices_per_month = Column(Integer, default=100)
    expires_at = Column(DateTime, nullable=True)  # NULL for free/lifetime licenses
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="licenses")
