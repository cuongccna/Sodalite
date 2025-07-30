#!/usr/bin/env python3
"""
Provider System Demo
Demonstrates the invoice provider system functionality
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from datetime import date, timedelta
from providers import (
    ProviderFactory,
    ProviderType,
    ProviderConfig,
    InvoiceData,
    create_manual_provider,
    create_viettel_provider,
    list_available_providers
)


def demo_provider_listing():
    """Demo listing available providers"""
    print("🔍 **Available Invoice Providers:**")
    print("=" * 50)
    
    providers = list_available_providers()
    for provider in providers:
        print(f"✅ **{provider['type'].upper()}**")
        print(f"   📋 Class: {provider['class_name']}")
        print(f"   🔑 Required credentials: {provider['required_credentials']}")
        print(f"   🌐 Real-time support: {'Yes' if provider['supports_real_time'] else 'No'}")
        print()


def demo_manual_provider():
    """Demo manual provider functionality"""
    print("📝 **Manual Provider Demo:**")
    print("=" * 50)
    
    # Create manual provider
    provider = create_manual_provider("0123456789")
    print(f"✅ Created provider: {provider.config.provider_type.value}")
    print(f"✅ Company tax code: {provider.config.company_tax_code}")
    print(f"✅ Authenticated: {provider.is_authenticated}")
    
    # Test connection
    success, message = provider.test_connection()
    print(f"✅ Connection test: {success} - {message}")
    
    # Create sample invoice
    today = date.today()
    sample_invoice = InvoiceData(
        invoice_number="INV-2024-001",
        provider_tax_code="0987654321",
        provider_name="Công ty ABC",
        issue_date=today,
        subtotal=1000000,
        vat_amount=100000,
        total_amount=1100000,
        description="Demo invoice from manual entry",
        currency="VND"
    )
    
    # Add invoice
    result = provider.add_invoice(sample_invoice)
    print(f"✅ Added invoice: {result}")
    
    # Retrieve invoices
    invoices = provider.get_invoices(today, today)
    print(f"✅ Retrieved {len(invoices)} invoices")
    
    if invoices:
        inv = invoices[0]
        print(f"   📄 Invoice: {inv.invoice_number}")
        print(f"   🏢 Provider: {inv.provider_name}")
        print(f"   💰 Total: {inv.total_amount:,.0f} {inv.currency}")
    
    print()


def demo_viettel_provider():
    """Demo Viettel provider functionality"""
    print("📡 **Viettel Provider Demo:**")
    print("=" * 50)
    
    # Create Viettel provider with demo credentials
    provider = create_viettel_provider(
        company_tax_code="0123456789",
        username="demo_user",
        password="demo_pass",
        api_key="demo_api_key_123",
        name="Demo Viettel Provider"
    )
    
    print(f"✅ Created provider: {provider.config.provider_type.value}")
    print(f"✅ Company tax code: {provider.config.company_tax_code}")
    print(f"✅ API endpoint: {provider.config.api_endpoint}")
    print(f"✅ Authenticated: {provider.is_authenticated}")
    
    # Validate credentials
    is_valid, errors = provider.validate_credentials()
    print(f"✅ Credentials valid: {is_valid}")
    if errors:
        print(f"   ⚠️ Validation errors: {errors}")
    
    # Test connection (will fail since this is demo)
    success, message = provider.test_connection()
    print(f"📶 Connection test: {success} - {message}")
    
    # Demo signature generation
    test_data = {"username": "demo_user", "timestamp": 1234567890}
    signature = provider._generate_signature(test_data)
    print(f"✅ Generated signature: {signature[:16]}...")
    
    # Demo API data conversion
    api_data = {
        "invoice_id": "VT-001",
        "invoice_number": "INV-001",
        "invoice_series": "AA/24E",
        "seller_tax_code": "0987654321",
        "seller_name": "Công ty XYZ",
        "issue_date": "2024-01-15",
        "subtotal": "500000.00",
        "vat_amount": "50000.00",
        "total_amount": "550000.00",
        "currency": "VND"
    }
    
    invoice_data = provider._convert_api_to_invoice_data(api_data)
    print(f"✅ Converted API data:")
    print(f"   📄 Invoice: {invoice_data.invoice_number}")
    print(f"   🏢 Provider: {invoice_data.provider_name}")
    print(f"   💰 Total: {invoice_data.total_amount:,.0f} {invoice_data.currency}")
    
    print()


def demo_factory_pattern():
    """Demo factory pattern usage"""
    print("🏭 **Factory Pattern Demo:**")
    print("=" * 50)
    
    # List available provider types
    available = ProviderFactory.get_available_providers()
    print(f"✅ Available provider types: {[p.value for p in available]}")
    
    # Create providers using factory
    for provider_type in available:
        print(f"\n📦 Creating {provider_type.value} provider...")
        
        if provider_type == ProviderType.MANUAL:
            config = ProviderConfig(
                provider_type=provider_type,
                company_tax_code="0123456789"
            )
        elif provider_type == ProviderType.VIETTEL:
            config = ProviderConfig(
                provider_type=provider_type,
                company_tax_code="0123456789",
                credentials={
                    "username": "demo",
                    "password": "demo",
                    "api_key": "demo"
                }
            )
        
        provider = ProviderFactory.create_provider(provider_type, config)
        print(f"   ✅ Created: {provider.__class__.__name__}")
        print(f"   🔑 Required fields: {provider.get_required_credential_fields()}")
    
    print()


def demo_error_handling():
    """Demo error handling"""
    print("⚠️ **Error Handling Demo:**")
    print("=" * 50)
    
    # Try to create unsupported provider
    try:
        from unittest.mock import Mock
        fake_type = Mock()
        fake_type.value = "FAKE_PROVIDER"
        
        config = ProviderConfig(
            provider_type=fake_type,
            company_tax_code="0123456789"
        )
        
        ProviderFactory.create_provider(fake_type, config)
    except ValueError as e:
        print(f"✅ Caught expected error: {e}")
    
    # Test invalid credentials for Viettel
    viettel_config = ProviderConfig(
        provider_type=ProviderType.VIETTEL,
        company_tax_code="0123456789",
        credentials={"username": "only_username"}  # Missing required fields
    )
    
    provider = ProviderFactory.create_provider(ProviderType.VIETTEL, viettel_config)
    is_valid, errors = provider.validate_credentials()
    print(f"✅ Invalid credentials detected: {not is_valid}")
    print(f"   📋 Validation errors: {errors}")
    
    print()


def main():
    """Run all demos"""
    print("🚀 **FinanTidy Provider System Demo**")
    print("=" * 60)
    print("Demonstrating invoice provider architecture and functionality")
    print("=" * 60)
    print()
    
    # Run demos
    demo_provider_listing()
    demo_manual_provider()
    demo_viettel_provider()
    demo_factory_pattern()
    demo_error_handling()
    
    print("🎉 **Demo completed successfully!**")
    print("=" * 60)
    print("The provider system is ready for:")
    print("✅ Manual invoice entry")
    print("✅ Viettel API integration (when credentials are available)")
    print("✅ Additional providers (MobiFone, VNPT, etc.)")
    print("✅ Robust error handling and validation")
    print("✅ Factory pattern for easy provider creation")


if __name__ == "__main__":
    main()
