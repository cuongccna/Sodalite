"""
FinanTidy Database Initialization Script
Creates database structure and loads sample data for testing
"""

import os
import sys
from datetime import datetime, timedelta
from decimal import Decimal
import random

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from src.database.database_manager import get_db_manager
from src.database.business_services import (
    get_invoice_service, get_provider_service, 
    get_transaction_service, get_analytics_service
)
from src.database.business_models import InvoiceStatus, TransactionType, ProviderType


def create_sample_providers(provider_service):
    """Create sample providers"""
    print("Creating sample providers...")
    
    providers_data = [
        {
            'provider_name': 'Tech Solutions Vietnam',
            'provider_code': 'TECH001',
            'tax_id': '0123456789',
            'provider_type': 'service_provider',
            'contact_person': 'Nguyen Van A',
            'email': 'contact@techsolutions.vn',
            'phone': '+84 901 234 567',
            'website': 'https://techsolutions.vn',
            'address': '123 Tech Street, District 1, Ho Chi Minh City',
            'services': ['Software Development', 'IT Consulting', 'System Integration'],
            'payment_terms': 30,
            'credit_limit': 50000000,
            'rating': 4.8,
            'is_preferred': True,
            'notes': 'Reliable technology partner with excellent track record'
        },
        {
            'provider_name': 'Marketing Pro Agency',
            'provider_code': 'MKT001',
            'tax_id': '0987654321',
            'provider_type': 'service_provider',
            'contact_person': 'Tran Thi B',
            'email': 'info@marketingpro.vn',
            'phone': '+84 902 345 678',
            'website': 'https://marketingpro.vn',
            'address': '456 Marketing Ave, District 3, Ho Chi Minh City',
            'services': ['Digital Marketing', 'SEO', 'Social Media Management'],
            'payment_terms': 15,
            'credit_limit': 30000000,
            'rating': 4.5,
            'is_preferred': True,
            'notes': 'Creative marketing solutions with proven ROI'
        },
        {
            'provider_name': 'Office Supplies Central',
            'provider_code': 'OFF001',
            'tax_id': '0111222333',
            'provider_type': 'supplier',
            'contact_person': 'Le Van C',
            'email': 'sales@officesupplies.vn',
            'phone': '+84 903 456 789',
            'website': 'https://officesupplies.vn',
            'address': '789 Supply Road, District 7, Ho Chi Minh City',
            'services': ['Office Equipment', 'Stationery', 'Furniture'],
            'payment_terms': 7,
            'credit_limit': 10000000,
            'rating': 4.2,
            'is_preferred': False,
            'notes': 'Quick delivery and competitive pricing'
        },
        {
            'provider_name': 'Legal Advisory Partners',
            'provider_code': 'LEG001',
            'tax_id': '0444555666',
            'provider_type': 'consultant',
            'contact_person': 'Pham Thi D',
            'email': 'contact@legaladvisory.vn',
            'phone': '+84 904 567 890',
            'website': 'https://legaladvisory.vn',
            'address': '321 Law Street, District 1, Ho Chi Minh City',
            'services': ['Legal Consultation', 'Contract Review', 'Compliance'],
            'payment_terms': 30,
            'credit_limit': 25000000,
            'rating': 4.9,
            'is_preferred': True,
            'notes': 'Expert legal advice for business operations'
        },
        {
            'provider_name': 'Cloud Infrastructure Co.',
            'provider_code': 'CLD001',
            'tax_id': '0777888999',
            'provider_type': 'service_provider',
            'contact_person': 'Hoang Van E',
            'email': 'support@cloudinfra.vn',
            'phone': '+84 905 678 901',
            'website': 'https://cloudinfra.vn',
            'address': '654 Cloud Avenue, District 2, Ho Chi Minh City',
            'services': ['Cloud Hosting', 'Data Backup', 'Security Services'],
            'payment_terms': 30,
            'credit_limit': 40000000,
            'rating': 4.6,
            'is_preferred': True,
            'notes': 'Reliable cloud infrastructure with 99.9% uptime'
        }
    ]
    
    created_providers = []
    for provider_data in providers_data:
        try:
            provider = provider_service.create_provider(provider_data)
            created_providers.append(provider)
            print(f"✓ Created provider: {provider_data['provider_name']}")
        except Exception as e:
            print(f"✗ Error creating provider {provider_data['provider_name']}: {e}")
    
    return created_providers


def create_sample_invoices(invoice_service, providers):
    """Create sample invoices"""
    print("Creating sample invoices...")
    
    # Get current date for realistic data
    today = datetime.now()
    
    invoices_data = [
        {
            'provider_id': providers[0]['id'] if providers else None,
            'invoice_date': (today - timedelta(days=30)).strftime('%Y-%m-%d'),
            'due_date': (today - timedelta(days=0)).strftime('%Y-%m-%d'),
            'description': 'Software development services - Q1 2025',
            'payment_terms': 30,
            'currency': 'VND',
            'items': [
                {
                    'item_name': 'Web Application Development',
                    'description': 'Custom web application with React frontend',
                    'quantity': 1,
                    'unit_price': 25000000,
                    'tax_rate': 10,
                    'discount_rate': 0
                },
                {
                    'item_name': 'Database Design',
                    'description': 'PostgreSQL database design and optimization',
                    'quantity': 1,
                    'unit_price': 8000000,
                    'tax_rate': 10,
                    'discount_rate': 5
                },
                {
                    'item_name': 'Testing & QA',
                    'description': 'Comprehensive testing and quality assurance',
                    'quantity': 1,
                    'unit_price': 5000000,
                    'tax_rate': 10,
                    'discount_rate': 0
                }
            ]
        },
        {
            'provider_id': providers[1]['id'] if len(providers) > 1 else None,
            'invoice_date': (today - timedelta(days=15)).strftime('%Y-%m-%d'),
            'due_date': (today + timedelta(days=15)).strftime('%Y-%m-%d'),
            'description': 'Digital marketing campaign - January 2025',
            'payment_terms': 30,
            'currency': 'VND',
            'items': [
                {
                    'item_name': 'SEO Optimization',
                    'description': 'Search engine optimization for website',
                    'quantity': 1,
                    'unit_price': 12000000,
                    'tax_rate': 10,
                    'discount_rate': 10
                },
                {
                    'item_name': 'Social Media Management',
                    'description': 'Facebook and Instagram management',
                    'quantity': 1,
                    'unit_price': 8000000,
                    'tax_rate': 10,
                    'discount_rate': 0
                }
            ]
        },
        {
            'provider_id': providers[2]['id'] if len(providers) > 2 else None,
            'invoice_date': (today - timedelta(days=5)).strftime('%Y-%m-%d'),
            'due_date': (today + timedelta(days=25)).strftime('%Y-%m-%d'),
            'description': 'Office supplies and equipment',
            'payment_terms': 30,
            'currency': 'VND',
            'items': [
                {
                    'item_name': 'Office Chairs',
                    'description': 'Ergonomic office chairs (Set of 10)',
                    'quantity': 10,
                    'unit_price': 1500000,
                    'tax_rate': 10,
                    'discount_rate': 15
                },
                {
                    'item_name': 'Desk Accessories',
                    'description': 'Monitor stands, keyboard trays, etc.',
                    'quantity': 1,
                    'unit_price': 3000000,
                    'tax_rate': 10,
                    'discount_rate': 5
                }
            ]
        },
        {
            'provider_id': providers[3]['id'] if len(providers) > 3 else None,
            'invoice_date': (today - timedelta(days=45)).strftime('%Y-%m-%d'),
            'due_date': (today - timedelta(days=15)).strftime('%Y-%m-%d'),
            'description': 'Legal consultation services',
            'payment_terms': 30,
            'currency': 'VND',
            'items': [
                {
                    'item_name': 'Contract Review',
                    'description': 'Review of partnership agreements',
                    'quantity': 3,
                    'unit_price': 2500000,
                    'tax_rate': 10,
                    'discount_rate': 0
                },
                {
                    'item_name': 'Legal Compliance Audit',
                    'description': 'Annual compliance review',
                    'quantity': 1,
                    'unit_price': 15000000,
                    'tax_rate': 10,
                    'discount_rate': 5
                }
            ]
        },
        {
            'provider_id': providers[4]['id'] if len(providers) > 4 else None,
            'invoice_date': (today - timedelta(days=10)).strftime('%Y-%m-%d'),
            'due_date': (today + timedelta(days=20)).strftime('%Y-%m-%d'),
            'description': 'Cloud infrastructure services - January 2025',
            'payment_terms': 30,
            'currency': 'VND',
            'items': [
                {
                    'item_name': 'Cloud Hosting',
                    'description': 'Monthly cloud hosting service',
                    'quantity': 1,
                    'unit_price': 5000000,
                    'tax_rate': 10,
                    'discount_rate': 0
                },
                {
                    'item_name': 'Data Backup Service',
                    'description': 'Automated daily backup solution',
                    'quantity': 1,
                    'unit_price': 2000000,
                    'tax_rate': 10,
                    'discount_rate': 0
                }
            ]
        }
    ]
    
    created_invoices = []
    for invoice_data in invoices_data:
        try:
            invoice = invoice_service.create_invoice(invoice_data)
            created_invoices.append(invoice)
            print(f"✓ Created invoice: {invoice['invoice_number']}")
        except Exception as e:
            print(f"✗ Error creating invoice: {e}")
    
    return created_invoices


def create_sample_transactions(transaction_service, invoices):
    """Create sample transactions"""
    print("Creating sample transactions...")
    
    # Create income transactions from paid invoices
    # Create expense transactions
    # Create transfer transactions
    
    transactions_data = [
        # Income transactions
        {
            'transaction_date': (datetime.now() - timedelta(days=20)).strftime('%Y-%m-%d'),
            'transaction_type': 'income',
            'category': 'Service Revenue',
            'description': 'Payment received for software development services',
            'amount': 35000000,
            'currency': 'VND',
            'account_from': 'Customer Payment',
            'account_to': 'Main Business Account',
            'invoice_id': invoices[0]['id'] if invoices else None,
            'status': 'completed',
            'notes': 'Payment received via bank transfer'
        },
        {
            'transaction_date': (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d'),
            'transaction_type': 'income',
            'category': 'Service Revenue',
            'description': 'Payment for marketing services',
            'amount': 18000000,
            'currency': 'VND',
            'account_from': 'Customer Payment',
            'account_to': 'Main Business Account',
            'invoice_id': invoices[1]['id'] if len(invoices) > 1 else None,
            'status': 'completed',
            'notes': 'Monthly marketing retainer payment'
        },
        # Expense transactions
        {
            'transaction_date': (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d'),
            'transaction_type': 'expense',
            'category': 'Office Expenses',
            'description': 'Office rent - January 2025',
            'amount': 15000000,
            'currency': 'VND',
            'account_from': 'Main Business Account',
            'account_to': 'Landlord',
            'status': 'completed',
            'notes': 'Monthly office rent payment'
        },
        {
            'transaction_date': (datetime.now() - timedelta(days=8)).strftime('%Y-%m-%d'),
            'transaction_type': 'expense',
            'category': 'Utilities',
            'description': 'Electricity and internet bills',
            'amount': 3500000,
            'currency': 'VND',
            'account_from': 'Main Business Account',
            'account_to': 'Utility Companies',
            'status': 'completed',
            'notes': 'Monthly utility payments'
        },
        {
            'transaction_date': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'),
            'transaction_type': 'expense',
            'category': 'Professional Services',
            'description': 'Accounting services fee',
            'amount': 5000000,
            'currency': 'VND',
            'account_from': 'Main Business Account',
            'account_to': 'Accounting Firm',
            'status': 'completed',
            'notes': 'Monthly accounting and bookkeeping services'
        },
        # Transfer transactions
        {
            'transaction_date': (datetime.now() - timedelta(days=12)).strftime('%Y-%m-%d'),
            'transaction_type': 'transfer',
            'category': 'Account Transfer',
            'description': 'Transfer to savings account',
            'amount': 20000000,
            'currency': 'VND',
            'account_from': 'Main Business Account',
            'account_to': 'Business Savings Account',
            'status': 'completed',
            'notes': 'Monthly savings transfer'
        },
        {
            'transaction_date': (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d'),
            'transaction_type': 'transfer',
            'category': 'Cash Withdrawal',
            'description': 'Cash withdrawal for petty expenses',
            'amount': 2000000,
            'currency': 'VND',
            'account_from': 'Main Business Account',
            'account_to': 'Petty Cash',
            'status': 'completed',
            'notes': 'Weekly petty cash withdrawal'
        }
    ]
    
    created_transactions = []
    for transaction_data in transactions_data:
        try:
            transaction = transaction_service.create_transaction(transaction_data)
            created_transactions.append(transaction)
            print(f"✓ Created transaction: {transaction['transaction_number']}")
        except Exception as e:
            print(f"✗ Error creating transaction: {e}")
    
    return created_transactions


def main():
    """Main initialization function"""
    print("=" * 60)
    print("🚀 FinanTidy Database Initialization")
    print("📅 Creating database structure and sample data")
    print("=" * 60)
    print()
    
    try:
        # Initialize database manager
        print("🔧 Initializing database manager...")
        db_manager = get_db_manager()
        print("✅ Database manager initialized successfully")
        print()
        
        # Get default company ID (created during initialization)
        company_id = 1  # Default company created by database manager
        
        # Initialize services
        print("🔧 Initializing business services...")
        provider_service = get_provider_service(company_id)
        invoice_service = get_invoice_service(company_id)
        transaction_service = get_transaction_service(company_id)
        analytics_service = get_analytics_service(company_id)
        print("✅ Business services initialized successfully")
        print()
        
        # Create sample data
        print("📊 Creating sample data...")
        print()
        
        # Create providers
        providers = create_sample_providers(provider_service)
        print(f"✅ Created {len(providers)} providers")
        print()
        
        # Create invoices
        invoices = create_sample_invoices(invoice_service, providers)
        print(f"✅ Created {len(invoices)} invoices")
        print()
        
        # Create transactions
        transactions = create_sample_transactions(transaction_service, invoices)
        print(f"✅ Created {len(transactions)} transactions")
        print()
        
        # Generate summary
        print("📈 Database Summary:")
        try:
            stats = db_manager.get_company_statistics(company_id)
            print(f"   • Total Invoices: {stats['invoices']['total']}")
            print(f"   • Total Revenue: ₫{stats['financial']['total_revenue']:,.0f}")
            print(f"   • Active Providers: {stats['providers']['total']}")
            print(f"   • Monthly Transactions: {stats['transactions']['monthly']}")
        except Exception as e:
            print(f"   • Error getting statistics: {e}")
        
        print()
        print("=" * 60)
        print("🎉 Database initialization completed successfully!")
        print("🎯 FinanTidy is ready to use with sample data")
        print("=" * 60)
        print()
        print("📋 Default Login Credentials:")
        print("   Username: admin")
        print("   Password: admin")
        print()
        print("🚀 Run the application:")
        print("   python run_finantidy.py")
        print()
        
    except Exception as e:
        print(f"❌ Error during database initialization: {e}")
        print("Please check your database configuration and try again.")
        return False
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
