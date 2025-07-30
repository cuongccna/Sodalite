"""
FinanTidy Business Models
Database models for business operations (invoices, providers, transactions)
"""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Enum, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()

# Enums for better data integrity
class InvoiceStatus(enum.Enum):
    DRAFT = "draft"
    SENT = "sent"
    PAID = "paid"
    OVERDUE = "overdue"
    CANCELLED = "cancelled"

class TransactionType(enum.Enum):
    INCOME = "income"
    EXPENSE = "expense"
    TRANSFER = "transfer"

class TransactionStatus(enum.Enum):
    COMPLETED = "completed"
    PENDING = "pending"
    FAILED = "failed"
    CANCELLED = "cancelled"

class ProviderType(enum.Enum):
    SUPPLIER = "supplier"
    SERVICE_PROVIDER = "service_provider"
    CONTRACTOR = "contractor"
    CONSULTANT = "consultant"
    OTHER = "other"


class Invoice(Base):
    """Invoice model for invoice management"""
    __tablename__ = 'invoices'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_number = Column(String(50), unique=True, nullable=False)
    company_id = Column(Integer, nullable=False)  # Reference to company
    provider_id = Column(Integer, ForeignKey('providers.id'), nullable=True)
    
    # Invoice details
    invoice_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    due_date = Column(DateTime, nullable=True)
    description = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    
    # Financial fields
    subtotal = Column(Numeric(15, 2), nullable=False, default=0)
    tax_amount = Column(Numeric(15, 2), nullable=False, default=0)
    discount_amount = Column(Numeric(15, 2), nullable=False, default=0)
    total_amount = Column(Numeric(15, 2), nullable=False, default=0)
    paid_amount = Column(Numeric(15, 2), nullable=False, default=0)
    
    # Status and metadata
    status = Column(Enum(InvoiceStatus), nullable=False, default=InvoiceStatus.DRAFT)
    payment_terms = Column(Integer, nullable=True)  # Payment terms in days
    currency = Column(String(3), nullable=False, default='VND')
    
    # Audit fields
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column(Integer, nullable=True)  # User ID
    
    # Relationships
    provider = relationship("Provider", back_populates="invoices")
    invoice_items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")
    transactions = relationship("Transaction", back_populates="invoice")
    
    @property
    def is_overdue(self):
        """Check if invoice is overdue"""
        if self.due_date and self.status in [InvoiceStatus.SENT]:
            return datetime.utcnow() > self.due_date
        return False
    
    @property
    def remaining_amount(self):
        """Calculate remaining unpaid amount"""
        return self.total_amount - self.paid_amount


class InvoiceItem(Base):
    """Invoice line items"""
    __tablename__ = 'invoice_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'), nullable=False)
    
    # Item details
    item_name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    quantity = Column(Numeric(10, 2), nullable=False, default=1)
    unit_price = Column(Numeric(15, 2), nullable=False)
    total_price = Column(Numeric(15, 2), nullable=False)
    
    # Tax and discounts
    tax_rate = Column(Numeric(5, 2), nullable=False, default=0)  # Percentage
    discount_rate = Column(Numeric(5, 2), nullable=False, default=0)  # Percentage
    
    # Relationships
    invoice = relationship("Invoice", back_populates="invoice_items")


class Provider(Base):
    """Provider/Supplier model"""
    __tablename__ = 'providers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, nullable=False)  # Reference to company
    
    # Basic information
    provider_name = Column(String(200), nullable=False)
    provider_code = Column(String(50), nullable=True)  # Internal code
    tax_id = Column(String(20), nullable=True)  # Tax identification number
    provider_type = Column(Enum(ProviderType), nullable=False, default=ProviderType.SUPPLIER)
    
    # Contact information
    contact_person = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    website = Column(String(200), nullable=True)
    address = Column(Text, nullable=True)
    
    # Business details
    services = Column(Text, nullable=True)  # JSON array of services
    payment_terms = Column(Integer, nullable=True)  # Default payment terms in days
    credit_limit = Column(Numeric(15, 2), nullable=True)
    
    # Rating and status
    rating = Column(Numeric(2, 1), nullable=True)  # 1.0 to 5.0
    is_active = Column(Boolean, default=True)
    is_preferred = Column(Boolean, default=False)
    
    # Notes and metadata
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    invoices = relationship("Invoice", back_populates="provider")
    transactions = relationship("Transaction", back_populates="provider")


class Transaction(Base):
    """Financial transaction model"""
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, nullable=False)  # Reference to company
    
    # Transaction identification
    transaction_number = Column(String(50), unique=True, nullable=False)
    reference_number = Column(String(100), nullable=True)  # External reference
    
    # Transaction details
    transaction_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    category = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    
    # Financial fields
    amount = Column(Numeric(15, 2), nullable=False)
    currency = Column(String(3), nullable=False, default='VND')
    
    # Account information
    account_from = Column(String(100), nullable=True)  # Source account
    account_to = Column(String(100), nullable=True)    # Destination account
    
    # Related entities
    invoice_id = Column(Integer, ForeignKey('invoices.id'), nullable=True)
    provider_id = Column(Integer, ForeignKey('providers.id'), nullable=True)
    
    # Status and metadata
    status = Column(Enum(TransactionStatus), nullable=False, default=TransactionStatus.PENDING)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_by = Column(Integer, nullable=True)  # User ID
    
    # Relationships
    invoice = relationship("Invoice", back_populates="transactions")
    provider = relationship("Provider", back_populates="transactions")


class Account(Base):
    """Chart of accounts model"""
    __tablename__ = 'accounts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, nullable=False)  # Reference to company
    
    # Account details
    account_code = Column(String(20), nullable=False)
    account_name = Column(String(200), nullable=False)
    account_type = Column(String(50), nullable=False)  # Asset, Liability, Equity, Revenue, Expense
    parent_account_id = Column(Integer, ForeignKey('accounts.id'), nullable=True)
    
    # Account properties
    is_active = Column(Boolean, default=True)
    is_system = Column(Boolean, default=False)  # System accounts cannot be deleted
    opening_balance = Column(Numeric(15, 2), nullable=False, default=0)
    current_balance = Column(Numeric(15, 2), nullable=False, default=0)
    
    # Metadata
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    parent_account = relationship("Account", remote_side=[id])
    child_accounts = relationship("Account")


class Setting(Base):
    """Application settings model"""
    __tablename__ = 'settings'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, nullable=False)  # Reference to company
    
    # Setting details
    setting_key = Column(String(100), nullable=False)
    setting_value = Column(Text, nullable=True)
    setting_type = Column(String(20), nullable=False, default='string')  # string, number, boolean, json
    category = Column(String(50), nullable=False, default='general')
    
    # Metadata
    description = Column(Text, nullable=True)
    is_system = Column(Boolean, default=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updated_by = Column(Integer, nullable=True)  # User ID


class AuditLog(Base):
    """Audit trail for data changes"""
    __tablename__ = 'audit_logs'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, nullable=False)
    
    # Audit details
    table_name = Column(String(50), nullable=False)
    record_id = Column(Integer, nullable=False)
    action = Column(String(20), nullable=False)  # CREATE, UPDATE, DELETE
    old_values = Column(Text, nullable=True)  # JSON of old values
    new_values = Column(Text, nullable=True)  # JSON of new values
    
    # Metadata
    user_id = Column(Integer, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String(45), nullable=True)
