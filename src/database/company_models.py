"""
Company Database Models
Models for company-specific database ([TaxCode].sqlite files)
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, date

CompanyBase = declarative_base()


class CompanyInfo(CompanyBase):
    """Company information table (duplicated in each company DB for consistency)"""
    __tablename__ = 'company_info'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tax_code = Column(String(20), nullable=False)
    company_name = Column(String(200), nullable=False)
    legal_name = Column(String(200), nullable=True)
    address = Column(Text, nullable=True)
    phone = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)
    business_type = Column(String(100), nullable=True)
    accounting_period_start = Column(Date, default=date.today)
    vat_rate = Column(Numeric(5, 2), default=10.00)  # Default 10% VAT
    currency = Column(String(3), default='VND')
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Provider(CompanyBase):
    """Invoice providers/suppliers"""
    __tablename__ = 'providers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tax_code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    address = Column(Text, nullable=True)
    phone = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)
    bank_account = Column(String(50), nullable=True)
    bank_name = Column(String(100), nullable=True)
    
    # Provider categorization
    category = Column(String(50), nullable=True)  # office_supplies, utilities, etc.
    is_frequent = Column(Boolean, default=False)
    
    # API integration settings
    api_type = Column(String(20), nullable=True)  # viettel, mobifone, fpt, manual
    api_credentials = Column(Text, nullable=True)  # Encrypted JSON
    auto_sync = Column(Boolean, default=False)
    last_sync = Column(DateTime, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    invoices = relationship("Invoice", back_populates="provider")


class Invoice(CompanyBase):
    """Main invoice table"""
    __tablename__ = 'invoices'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # Invoice identification
    invoice_number = Column(String(50), nullable=False)
    invoice_series = Column(String(10), nullable=True)
    invoice_template = Column(String(20), nullable=True)
    
    # Provider information
    provider_id = Column(Integer, ForeignKey('providers.id'), nullable=False)
    
    # Invoice dates
    issue_date = Column(Date, nullable=False)
    payment_date = Column(Date, nullable=True)
    due_date = Column(Date, nullable=True)
    
    # Financial data
    subtotal = Column(Numeric(15, 2), nullable=False, default=0)
    vat_amount = Column(Numeric(15, 2), nullable=False, default=0)
    total_amount = Column(Numeric(15, 2), nullable=False, default=0)
    currency = Column(String(3), default='VND')
    exchange_rate = Column(Numeric(10, 4), default=1.0000)
    
    # Invoice type and status
    invoice_type = Column(String(20), default='purchase')  # purchase, sale, adjustment
    status = Column(String(20), default='pending')  # pending, paid, overdue, cancelled
    payment_method = Column(String(30), nullable=True)  # cash, bank_transfer, card, etc.
    
    # Categorization and AI suggestions
    expense_category = Column(String(50), nullable=True)  # office_supplies, utilities, etc.
    ai_category_confidence = Column(Numeric(3, 2), nullable=True)  # 0.00 to 1.00
    is_deductible = Column(Boolean, default=True)
    
    # Additional metadata
    description = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    attachment_path = Column(String(500), nullable=True)  # Path to scanned invoice
    
    # Data source tracking
    source = Column(String(20), default='manual')  # manual, api_sync, import
    external_id = Column(String(100), nullable=True)  # ID from external system
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    provider = relationship("Provider", back_populates="invoices")
    items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")


class InvoiceItem(CompanyBase):
    """Individual line items within invoices"""
    __tablename__ = 'invoice_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'), nullable=False)
    
    # Item details
    description = Column(Text, nullable=False)
    quantity = Column(Numeric(10, 3), nullable=False, default=1)
    unit = Column(String(20), nullable=True)  # piece, kg, hour, etc.
    unit_price = Column(Numeric(15, 2), nullable=False)
    
    # Calculated amounts
    line_total = Column(Numeric(15, 2), nullable=False)
    vat_rate = Column(Numeric(5, 2), nullable=False, default=10.00)
    vat_amount = Column(Numeric(15, 2), nullable=False, default=0)
    
    # Item categorization
    item_category = Column(String(50), nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    invoice = relationship("Invoice", back_populates="items")
