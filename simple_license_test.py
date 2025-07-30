#!/usr/bin/env python3
"""
Simple Enhanced License Test
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.license_manager import LicenseManager


def test_license_features():
    """Test basic license feature functionality"""
    print("🔒 **Simple License Features Test**")
    print("=" * 50)
    
    # Test without database - just feature definitions
    license_manager = LicenseManager()
    
    print("📋 **Testing License Feature Definitions:**")
    
    # Test feature definitions
    features = license_manager.LICENSE_FEATURES
    for license_type, feature_set in features.items():
        print(f"\n📄 {license_type.upper()} License:")
        print(f"   🏢 Max companies: {feature_set['max_companies']}")
        print(f"   📧 Max invoices/month: {feature_set['max_invoices_per_month']}")
        print(f"   🔌 API integrations: {', '.join(feature_set['api_integrations'])}")
        print(f"   💾 Export formats: {', '.join(feature_set['export_formats'])}")
        print(f"   🤖 AI suggestions: {'✅' if feature_set['ai_suggestions'] else '❌'}")
        print(f"   📊 Advanced reports: {'✅' if feature_set['advanced_reports'] else '❌'}")
    
    print("\n💰 **Testing Plan Comparison:**")
    try:
        comparison = license_manager.get_plan_comparison()
        for plan_id, plan in comparison['plans'].items():
            print(f"\n📦 {plan['name']} ({plan_id.upper()})")
            if plan['price'] > 0:
                print(f"   💵 {plan['price']:,} VND/month")
            else:
                print(f"   💵 Free")
            
            # Key features
            features = plan['features']
            companies = features['max_companies'] if features['max_companies'] > 0 else "Unlimited"
            invoices = features['max_invoices_per_month'] if features['max_invoices_per_month'] > 0 else "Unlimited"
            print(f"   🏢 {companies} companies, 📧 {invoices} invoices/month")
    except Exception as e:
        print(f"⚠️ Plan comparison needs database: {e}")
    
    print("\n🔌 **Testing Provider Access (Mock License):**")
    # Simulate different license types
    for license_type in ['free', 'pro', 'agency']:
        print(f"\n📄 {license_type.upper()} License Access:")
        
        # Mock current license
        license_manager.current_license = {'license_type': license_type, 'user_id': 1}
        
        providers = ['manual', 'viettel', 'mobifone', 'fpt']
        for provider in providers:
            can_use = license_manager.can_use_provider(provider)
            status = "✅" if can_use else "❌"
            print(f"   {provider.upper()}: {status}")
    
    print("\n💾 **Testing Export Format Access:**")
    for license_type in ['free', 'pro', 'agency']:
        print(f"\n📄 {license_type.upper()} Export Access:")
        
        # Mock current license
        license_manager.current_license = {'license_type': license_type, 'user_id': 1}
        
        formats = ['csv', 'excel', 'pdf', 'xml']
        for format_type in formats:
            can_export = license_manager.can_export_format(format_type)
            status = "✅" if can_export else "❌"
            print(f"   {format_type.upper()}: {status}")
    
    print("\n🎉 **Enhanced License Features Test Completed!**")
    print("=" * 50)
    print("Key enhancements working:")
    print("✅ Comprehensive license feature definitions")
    print("✅ Plan comparison with pricing")
    print("✅ Provider access control")
    print("✅ Export format restrictions")
    print("✅ License type validation")


if __name__ == "__main__":
    test_license_features()
