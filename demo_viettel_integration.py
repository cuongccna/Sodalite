#!/usr/bin/env python3
"""
FinanTidy Viettel eInvoice Integration Demo
Demonstrates how to configure and use Viettel electronic invoice functionality
"""

import sys
import os
import json
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def demo_viettel_integration():
    """Demonstrate Viettel eInvoice integration setup and usage"""
    
    print("🎯 FinanTidy Professional v2.0 - Viettel eInvoice Integration Demo")
    print("=" * 70)
    
    # Import the integration components
    try:
        from integrations.viettel_einvoice import ViettelEInvoiceService, ViettelEInvoiceConfig
        print("✅ Viettel integration modules loaded successfully")
    except ImportError as e:
        print(f"❌ Failed to load integration: {e}")
        return
    
    print("\n📋 Step 1: Configuration Setup")
    print("-" * 40)
    
    # Create configuration instance
    config = ViettelEInvoiceConfig()
    print(f"📊 Current configuration status: {'✅ Configured' if config.is_configured() else '❌ Not configured'}")
    
    # Example configuration (for demonstration - use test credentials)
    demo_config = {
        'base_url': 'https://sinvoice-demo.viettel.vn',  # Demo environment
        'username': '0100109106-509',  # Test account format
        'password': 'test_password',    # Contact Viettel for actual test credentials
        'supplier_tax_code': '0100109106',
        'template_code': '01GTKT0/001',
        'invoice_series': 'C22T',
        'auth_method': 'token',
        'company_name': 'FinanTidy Test Company',
        'company_address': '123 Test Street, Hanoi, Vietnam',
        'company_phone': '+84 123 456 789',
        'company_email': 'test@finantidy.com'
    }
    
    print("\n📝 Example Configuration:")
    for key, value in demo_config.items():
        if 'password' in key.lower():
            print(f"  {key}: {'*' * len(str(value))}")
        else:
            print(f"  {key}: {value}")
    
    print("\n📋 Step 2: Sample Invoice Data")
    print("-" * 40)
    
    # Sample invoice data in FinanTidy format
    sample_invoice = {
        'invoice_id': 'INV-2025-001',
        'invoice_date': datetime.now().strftime('%Y-%m-%d'),
        'currency': 'VND',
        'description': 'Software Development Services',
        'buyer_name': 'ABC Technology Solutions Ltd.',
        'buyer_tax_code': '0123456789',
        'buyer_address': '456 Innovation Street, Ho Chi Minh City',
        'buyer_email': 'accounting@abc-tech.com',
        'items': [
            {
                'item_name': 'Custom Software Development',
                'quantity': 1,
                'unit_price': 50000000,  # 50 million VND
                'tax_rate': 10,
                'discount_rate': 0,
                'description': 'Full-stack web application development'
            },
            {
                'item_name': 'Technical Support (3 months)',
                'quantity': 3,
                'unit_price': 5000000,   # 5 million VND per month
                'tax_rate': 10,
                'discount_rate': 5,
                'description': 'Post-deployment technical support'
            }
        ]
    }
    
    print("📄 Sample Invoice:")
    print(f"  Invoice ID: {sample_invoice['invoice_id']}")
    print(f"  Date: {sample_invoice['invoice_date']}")
    print(f"  Buyer: {sample_invoice['buyer_name']}")
    print(f"  Items: {len(sample_invoice['items'])} items")
    
    # Calculate totals
    subtotal = 0
    for item in sample_invoice['items']:
        item_total = item['quantity'] * item['unit_price'] * (1 - item['discount_rate']/100)
        subtotal += item_total
        print(f"    - {item['item_name']}: {item['quantity']:,} x {item['unit_price']:,} VND")
    
    tax_total = subtotal * 0.1  # 10% VAT
    total = subtotal + tax_total
    print(f"  Subtotal: {subtotal:,.0f} VND")
    print(f"  Tax (10%): {tax_total:,.0f} VND")
    print(f"  Total: {total:,.0f} VND")
    
    print("\n📋 Step 3: Integration Workflow")
    print("-" * 40)
    
    print("🔧 Configuration Process:")
    print("  1. Access: Main Dashboard → '📋 Viettel eInvoice' button")
    print("  2. OR: Settings → Viettel eInvoice category")
    print("  3. Enter API credentials and company information")
    print("  4. Test connection with Viettel demo environment")
    print("  5. Save configuration")
    
    print("\n📤 Invoice Creation Process:")
    print("  1. Create invoice in FinanTidy invoice management")
    print("  2. Click '📋 Configure eInvoice' in invoice details")
    print("  3. Verify invoice data mapping")
    print("  4. Click '📤 Create eInvoice' to submit to Viettel")
    print("  5. Download PDF once processing is complete")
    
    print("\n🔐 Security Features:")
    print("  ✅ Encrypted credential storage")
    print("  ✅ Secure API authentication (Token/Basic)")
    print("  ✅ Local configuration file protection")
    print("  ✅ Test environment support for safe testing")
    
    print("\n📚 Documentation & Support:")
    print("  • Viettel SInvoice Portal: https://sinvoice.viettel.vn")
    print("  • API Documentation: Available in your Viettel account")
    print("  • Test Environment: https://sinvoice-demo.viettel.vn")
    print("  • Contact Viettel for API access and test credentials")
    
    print("\n🎉 Integration Benefits:")
    print("  ✅ Vietnamese regulatory compliance")
    print("  ✅ Automated electronic invoice generation")
    print("  ✅ Real-time invoice status tracking")
    print("  ✅ Professional PDF invoice output")
    print("  ✅ Seamless FinanTidy workflow integration")
    
    print("\n⚠️ Important Notes:")
    print("  • Always test with demo environment first")
    print("  • Ensure company registration with Vietnamese tax authorities")
    print("  • Keep API credentials secure and confidential")
    print("  • Respect Viettel API rate limits and usage policies")
    
    print("\n" + "=" * 70)
    print("🚀 Ready to use Viettel eInvoice integration!")
    print("Start by configuring your credentials in FinanTidy Settings.")

def demo_ui_access():
    """Show how to access Viettel features through the UI"""
    
    print("\n🖥️ UI Access Methods:")
    print("-" * 30)
    
    print("📊 Main Dashboard:")
    print("  → Click 'Quick Actions' → '📋 Viettel eInvoice'")
    
    print("\n⚙️ Settings Menu:")
    print("  → Settings → 'Viettel eInvoice' category")
    
    print("\n📄 Invoice Management:")
    print("  → Invoices → Select Invoice → '📋 Configure eInvoice'")
    print("  → Invoices → Select Invoice → '📤 Create eInvoice'")
    print("  → Invoices → Select Invoice → '📄 Download PDF'")
    
    print("\n🔧 Configuration Window Features:")
    print("  • API endpoint and authentication settings")
    print("  • Company information management")
    print("  • Invoice template configuration")
    print("  • Connection testing functionality")
    print("  • Secure credential storage")

if __name__ == "__main__":
    demo_viettel_integration()
    demo_ui_access()
    
    print(f"\n📁 Integration Files:")
    print(f"  • Service: src/integrations/viettel_einvoice.py")
    print(f"  • Config UI: src/ui/modern/viettel_config_window.py")
    print(f"  • Settings: Enhanced settings_window.py")
    print(f"  • Invoices: Enhanced invoices_window.py")
    print(f"  • Main Window: Added quick access button")
    
    input("\nPress Enter to exit...")
