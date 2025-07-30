"""
FinanTidy Business Services
Service layer for business operations with database integration
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timedelta
from decimal import Decimal
import json

from .database_manager import get_db_manager
from .business_models import (
    Invoice, InvoiceItem, Provider, Transaction, Account, Setting, AuditLog,
    InvoiceStatus, TransactionType, TransactionStatus, ProviderType
)


class InvoiceService:
    """Service for invoice management operations"""
    
    def __init__(self, company_id: int):
        self.company_id = company_id
        self.db_manager = get_db_manager()
    
    def get_all_invoices(self, limit: int = 100, offset: int = 0, 
                        filters: Dict[str, Any] = None) -> Tuple[List[Dict], int]:
        """Get all invoices with pagination and filtering"""
        try:
            with self.db_manager.company_session(self.company_id) as session:
                query = session.query(Invoice).filter_by(company_id=self.company_id)
                
                # Apply filters
                if filters:
                    if filters.get('status'):
                        query = query.filter(Invoice.status == filters['status'])
                    
                    if filters.get('date_from'):
                        query = query.filter(Invoice.invoice_date >= filters['date_from'])
                    
                    if filters.get('date_to'):
                        query = query.filter(Invoice.invoice_date <= filters['date_to'])
                    
                    if filters.get('search'):
                        search_term = f"%{filters['search']}%"
                        query = query.filter(
                            Invoice.invoice_number.like(search_term) |
                            Invoice.description.like(search_term)
                        )
                
                # Get total count
                total_count = query.count()
                
                # Apply pagination
                invoices = query.order_by(Invoice.invoice_date.desc())\
                              .limit(limit).offset(offset).all()
                
                # Convert to dict format
                invoice_list = []
                for invoice in invoices:
                    invoice_dict = {
                        'id': invoice.id,
                        'invoice_number': invoice.invoice_number,
                        'invoice_date': invoice.invoice_date.strftime('%Y-%m-%d'),
                        'due_date': invoice.due_date.strftime('%Y-%m-%d') if invoice.due_date else None,
                        'description': invoice.description,
                        'total_amount': float(invoice.total_amount),
                        'paid_amount': float(invoice.paid_amount),
                        'remaining_amount': float(invoice.remaining_amount),
                        'status': invoice.status.value,
                        'is_overdue': invoice.is_overdue,
                        'provider_name': invoice.provider.provider_name if invoice.provider else None,
                        'currency': invoice.currency
                    }
                    invoice_list.append(invoice_dict)
                
                return invoice_list, total_count
                
        except Exception as e:
            raise Exception(f"Error fetching invoices: {e}")
    
    def get_invoice_by_id(self, invoice_id: int) -> Optional[Dict[str, Any]]:
        """Get detailed invoice information"""
        try:
            with self.db_manager.company_session(self.company_id) as session:
                invoice = session.query(Invoice).filter_by(
                    id=invoice_id,
                    company_id=self.company_id
                ).first()
                
                if not invoice:
                    return None
                
                # Get invoice items
                items = []
                for item in invoice.invoice_items:
                    items.append({
                        'id': item.id,
                        'item_name': item.item_name,
                        'description': item.description,
                        'quantity': float(item.quantity),
                        'unit_price': float(item.unit_price),
                        'total_price': float(item.total_price),
                        'tax_rate': float(item.tax_rate),
                        'discount_rate': float(item.discount_rate)
                    })
                
                return {
                    'id': invoice.id,
                    'invoice_number': invoice.invoice_number,
                    'invoice_date': invoice.invoice_date.strftime('%Y-%m-%d'),
                    'due_date': invoice.due_date.strftime('%Y-%m-%d') if invoice.due_date else None,
                    'description': invoice.description,
                    'notes': invoice.notes,
                    'subtotal': float(invoice.subtotal),
                    'tax_amount': float(invoice.tax_amount),
                    'discount_amount': float(invoice.discount_amount),
                    'total_amount': float(invoice.total_amount),
                    'paid_amount': float(invoice.paid_amount),
                    'remaining_amount': float(invoice.remaining_amount),
                    'status': invoice.status.value,
                    'payment_terms': invoice.payment_terms,
                    'currency': invoice.currency,
                    'provider': {
                        'id': invoice.provider.id,
                        'name': invoice.provider.provider_name,
                        'email': invoice.provider.email,
                        'phone': invoice.provider.phone
                    } if invoice.provider else None,
                    'items': items,
                    'created_at': invoice.created_at.strftime('%Y-%m-%d %H:%M:%S')
                }
                
        except Exception as e:
            raise Exception(f"Error fetching invoice: {e}")
    
    def create_invoice(self, invoice_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create new invoice"""
        try:
            with self.db_manager.company_session(self.company_id) as session:
                # Generate invoice number
                invoice_number = self.db_manager.generate_invoice_number(self.company_id)
                
                # Create invoice
                invoice = Invoice(
                    company_id=self.company_id,
                    invoice_number=invoice_number,
                    provider_id=invoice_data.get('provider_id'),
                    invoice_date=datetime.strptime(invoice_data['invoice_date'], '%Y-%m-%d'),
                    due_date=datetime.strptime(invoice_data['due_date'], '%Y-%m-%d') if invoice_data.get('due_date') else None,
                    description=invoice_data.get('description', ''),
                    notes=invoice_data.get('notes', ''),
                    status=InvoiceStatus.DRAFT,
                    payment_terms=invoice_data.get('payment_terms', 30),
                    currency=invoice_data.get('currency', 'VND'),
                    created_by=invoice_data.get('created_by')
                )
                
                session.add(invoice)
                session.flush()  # Get the invoice ID
                
                # Add invoice items
                subtotal = Decimal('0')
                tax_amount = Decimal('0')
                discount_amount = Decimal('0')
                
                for item_data in invoice_data.get('items', []):
                    item = InvoiceItem(
                        invoice_id=invoice.id,
                        item_name=item_data['item_name'],
                        description=item_data.get('description', ''),
                        quantity=Decimal(str(item_data['quantity'])),
                        unit_price=Decimal(str(item_data['unit_price'])),
                        tax_rate=Decimal(str(item_data.get('tax_rate', 0))),
                        discount_rate=Decimal(str(item_data.get('discount_rate', 0)))
                    )
                    
                    # Calculate item totals
                    line_total = item.quantity * item.unit_price
                    line_discount = line_total * (item.discount_rate / 100)
                    line_net = line_total - line_discount
                    line_tax = line_net * (item.tax_rate / 100)
                    
                    item.total_price = line_net + line_tax
                    
                    subtotal += line_total
                    discount_amount += line_discount
                    tax_amount += line_tax
                    
                    session.add(item)
                
                # Update invoice totals
                invoice.subtotal = subtotal
                invoice.tax_amount = tax_amount
                invoice.discount_amount = discount_amount
                invoice.total_amount = subtotal - discount_amount + tax_amount
                
                session.commit()
                
                return self.get_invoice_by_id(invoice.id)
                
        except Exception as e:
            raise Exception(f"Error creating invoice: {e}")
    
    def update_invoice_status(self, invoice_id: int, status: str) -> bool:
        """Update invoice status"""
        try:
            with self.db_manager.company_session(self.company_id) as session:
                invoice = session.query(Invoice).filter_by(
                    id=invoice_id,
                    company_id=self.company_id
                ).first()
                
                if not invoice:
                    return False
                
                old_status = invoice.status.value
                invoice.status = InvoiceStatus(status)
                
                # If marking as paid, update paid amount
                if status == 'paid':
                    invoice.paid_amount = invoice.total_amount
                
                session.commit()
                
                # Log the change
                self._log_invoice_change(invoice_id, 'UPDATE', 
                                       {'status': old_status}, 
                                       {'status': status})
                
                return True
                
        except Exception as e:
            raise Exception(f"Error updating invoice status: {e}")
    
    def _log_invoice_change(self, invoice_id: int, action: str, old_values: Dict, new_values: Dict):
        """Log invoice changes for audit trail"""
        try:
            with self.db_manager.company_session(self.company_id) as session:
                log_entry = AuditLog(
                    company_id=self.company_id,
                    table_name='invoices',
                    record_id=invoice_id,
                    action=action,
                    old_values=json.dumps(old_values) if old_values else None,
                    new_values=json.dumps(new_values) if new_values else None
                )
                session.add(log_entry)
                session.commit()
                
        except Exception as e:
            # Don't fail the main operation if audit logging fails
            pass


class ProviderService:
    """Service for provider management operations"""
    
    def __init__(self, company_id: int):
        self.company_id = company_id
        self.db_manager = get_db_manager()
    
    def get_all_providers(self, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """Get all providers with filtering"""
        try:
            with self.db_manager.company_session(self.company_id) as session:
                query = session.query(Provider).filter_by(company_id=self.company_id)
                
                # Apply filters
                if filters:
                    if filters.get('provider_type'):
                        query = query.filter(Provider.provider_type == filters['provider_type'])
                    
                    if filters.get('is_active') is not None:
                        query = query.filter(Provider.is_active == filters['is_active'])
                    
                    if filters.get('search'):
                        search_term = f"%{filters['search']}%"
                        query = query.filter(
                            Provider.provider_name.like(search_term) |
                            Provider.contact_person.like(search_term) |
                            Provider.email.like(search_term)
                        )
                
                providers = query.order_by(Provider.provider_name).all()
                
                provider_list = []
                for provider in providers:
                    provider_dict = {
                        'id': provider.id,
                        'provider_name': provider.provider_name,
                        'provider_code': provider.provider_code,
                        'provider_type': provider.provider_type.value,
                        'contact_person': provider.contact_person,
                        'email': provider.email,
                        'phone': provider.phone,
                        'website': provider.website,
                        'address': provider.address,
                        'rating': float(provider.rating) if provider.rating else None,
                        'is_active': provider.is_active,
                        'is_preferred': provider.is_preferred,
                        'services': json.loads(provider.services) if provider.services else [],
                        'payment_terms': provider.payment_terms,
                        'credit_limit': float(provider.credit_limit) if provider.credit_limit else None
                    }
                    provider_list.append(provider_dict)
                
                return provider_list
                
        except Exception as e:
            raise Exception(f"Error fetching providers: {e}")
    
    def create_provider(self, provider_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create new provider"""
        try:
            with self.db_manager.company_session(self.company_id) as session:
                provider = Provider(
                    company_id=self.company_id,
                    provider_name=provider_data['provider_name'],
                    provider_code=provider_data.get('provider_code'),
                    tax_id=provider_data.get('tax_id'),
                    provider_type=ProviderType(provider_data.get('provider_type', 'supplier')),
                    contact_person=provider_data.get('contact_person'),
                    email=provider_data.get('email'),
                    phone=provider_data.get('phone'),
                    website=provider_data.get('website'),
                    address=provider_data.get('address'),
                    services=json.dumps(provider_data.get('services', [])),
                    payment_terms=provider_data.get('payment_terms'),
                    credit_limit=Decimal(str(provider_data['credit_limit'])) if provider_data.get('credit_limit') else None,
                    rating=Decimal(str(provider_data['rating'])) if provider_data.get('rating') else None,
                    is_preferred=provider_data.get('is_preferred', False),
                    notes=provider_data.get('notes')
                )
                
                session.add(provider)
                session.commit()
                
                return {
                    'id': provider.id,
                    'provider_name': provider.provider_name,
                    'provider_type': provider.provider_type.value,
                    'email': provider.email,
                    'phone': provider.phone,
                    'is_active': provider.is_active
                }
                
        except Exception as e:
            raise Exception(f"Error creating provider: {e}")


class TransactionService:
    """Service for transaction management operations"""
    
    def __init__(self, company_id: int):
        self.company_id = company_id
        self.db_manager = get_db_manager()
    
    def get_all_transactions(self, limit: int = 100, offset: int = 0,
                           filters: Dict[str, Any] = None) -> Tuple[List[Dict], int]:
        """Get all transactions with pagination and filtering"""
        try:
            with self.db_manager.company_session(self.company_id) as session:
                query = session.query(Transaction).filter_by(company_id=self.company_id)
                
                # Apply filters
                if filters:
                    if filters.get('transaction_type'):
                        query = query.filter(Transaction.transaction_type == filters['transaction_type'])
                    
                    if filters.get('status'):
                        query = query.filter(Transaction.status == filters['status'])
                    
                    if filters.get('date_from'):
                        query = query.filter(Transaction.transaction_date >= filters['date_from'])
                    
                    if filters.get('date_to'):
                        query = query.filter(Transaction.transaction_date <= filters['date_to'])
                    
                    if filters.get('search'):
                        search_term = f"%{filters['search']}%"
                        query = query.filter(
                            Transaction.description.like(search_term) |
                            Transaction.reference_number.like(search_term)
                        )
                
                # Get total count
                total_count = query.count()
                
                # Apply pagination
                transactions = query.order_by(Transaction.transaction_date.desc())\
                                  .limit(limit).offset(offset).all()
                
                # Convert to dict format
                transaction_list = []
                for transaction in transactions:
                    transaction_dict = {
                        'id': transaction.id,
                        'transaction_number': transaction.transaction_number,
                        'transaction_date': transaction.transaction_date.strftime('%Y-%m-%d'),
                        'transaction_type': transaction.transaction_type.value,
                        'category': transaction.category,
                        'description': transaction.description,
                        'amount': float(transaction.amount),
                        'currency': transaction.currency,
                        'account_from': transaction.account_from,
                        'account_to': transaction.account_to,
                        'status': transaction.status.value,
                        'reference_number': transaction.reference_number,
                        'provider_name': transaction.provider.provider_name if transaction.provider else None,
                        'invoice_number': transaction.invoice.invoice_number if transaction.invoice else None
                    }
                    transaction_list.append(transaction_dict)
                
                return transaction_list, total_count
                
        except Exception as e:
            raise Exception(f"Error fetching transactions: {e}")
    
    def create_transaction(self, transaction_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create new transaction"""
        try:
            with self.db_manager.company_session(self.company_id) as session:
                # Generate transaction number
                transaction_number = self.db_manager.generate_transaction_number(self.company_id)
                
                transaction = Transaction(
                    company_id=self.company_id,
                    transaction_number=transaction_number,
                    reference_number=transaction_data.get('reference_number'),
                    transaction_date=datetime.strptime(transaction_data['transaction_date'], '%Y-%m-%d'),
                    transaction_type=TransactionType(transaction_data['transaction_type']),
                    category=transaction_data['category'],
                    description=transaction_data['description'],
                    amount=Decimal(str(transaction_data['amount'])),
                    currency=transaction_data.get('currency', 'VND'),
                    account_from=transaction_data.get('account_from'),
                    account_to=transaction_data.get('account_to'),
                    invoice_id=transaction_data.get('invoice_id'),
                    provider_id=transaction_data.get('provider_id'),
                    status=TransactionStatus.COMPLETED,
                    notes=transaction_data.get('notes'),
                    created_by=transaction_data.get('created_by')
                )
                
                session.add(transaction)
                session.commit()
                
                return {
                    'id': transaction.id,
                    'transaction_number': transaction.transaction_number,
                    'transaction_type': transaction.transaction_type.value,
                    'amount': float(transaction.amount),
                    'status': transaction.status.value
                }
                
        except Exception as e:
            raise Exception(f"Error creating transaction: {e}")


class AnalyticsService:
    """Service for analytics and reporting"""
    
    def __init__(self, company_id: int):
        self.company_id = company_id
        self.db_manager = get_db_manager()
    
    def get_financial_overview(self, period_days: int = 30) -> Dict[str, Any]:
        """Get financial overview for specified period"""
        try:
            with self.db_manager.company_session(self.company_id) as session:
                end_date = datetime.utcnow()
                start_date = end_date - timedelta(days=period_days)
                
                # Revenue analysis
                revenue_query = session.query(Transaction).filter(
                    Transaction.company_id == self.company_id,
                    Transaction.transaction_type == TransactionType.INCOME,
                    Transaction.status == TransactionStatus.COMPLETED,
                    Transaction.transaction_date >= start_date
                )
                
                total_revenue = sum(float(t.amount) for t in revenue_query.all())
                revenue_count = revenue_query.count()
                
                # Expense analysis
                expense_query = session.query(Transaction).filter(
                    Transaction.company_id == self.company_id,
                    Transaction.transaction_type == TransactionType.EXPENSE,
                    Transaction.status == TransactionStatus.COMPLETED,
                    Transaction.transaction_date >= start_date
                )
                
                total_expenses = sum(float(t.amount) for t in expense_query.all())
                expense_count = expense_query.count()
                
                # Invoice analysis
                invoice_stats = session.query(Invoice).filter(
                    Invoice.company_id == self.company_id,
                    Invoice.invoice_date >= start_date
                ).all()
                
                invoice_summary = {
                    'total': len(invoice_stats),
                    'paid': len([i for i in invoice_stats if i.status == InvoiceStatus.PAID]),
                    'pending': len([i for i in invoice_stats if i.status == InvoiceStatus.SENT]),
                    'overdue': len([i for i in invoice_stats if i.is_overdue])
                }
                
                return {
                    'period_days': period_days,
                    'revenue': {
                        'total': total_revenue,
                        'count': revenue_count,
                        'average': total_revenue / revenue_count if revenue_count > 0 else 0
                    },
                    'expenses': {
                        'total': total_expenses,
                        'count': expense_count,
                        'average': total_expenses / expense_count if expense_count > 0 else 0
                    },
                    'net_income': total_revenue - total_expenses,
                    'invoices': invoice_summary
                }
                
        except Exception as e:
            raise Exception(f"Error getting financial overview: {e}")


# Service factory functions
def get_invoice_service(company_id: int) -> InvoiceService:
    """Get invoice service instance"""
    return InvoiceService(company_id)

def get_provider_service(company_id: int) -> ProviderService:
    """Get provider service instance"""
    return ProviderService(company_id)

def get_transaction_service(company_id: int) -> TransactionService:
    """Get transaction service instance"""
    return TransactionService(company_id)

def get_analytics_service(company_id: int) -> AnalyticsService:
    """Get analytics service instance"""
    return AnalyticsService(company_id)
