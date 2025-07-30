#!/usr/bin/env python3
"""
Enhanced License System Demo
Demonstrates the new license features and capabilities
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.license_manager import LicenseManager
from database.manager import DatabaseManager
import tempfile
import json


def demo_enhanced_license_features():
    """Demo enhanced license functionality"""
    print("🔒 **Enhanced License System Demo**")
    print("=" * 60)
    
    # Create temporary database
    db_file = tempfile.NamedTemporaryFile(delete=False, suffix='.sqlite')
    db_file.close()
    
    try:
        # Create database manager
        from pathlib import Path
        db_manager = DatabaseManager()
        db_manager.master_db_path = db_file.name
        db_manager.data_dir = Path(os.path.dirname(db_file.name))
        db_manager.initialize_master_db()
        
        # Create license manager
        license_manager = LicenseManager(db_manager)
        
        # Create test user and company
        user = db_manager.create_user(
            username="testuser",
            email="test@example.com",
            password="password123",
            full_name="Test User"
        )
        
        company = db_manager.create_company(
            tax_code="0123456789",
            company_name="Test Company Ltd",
            creator_user_id=user['id']
        )
        
        # Load user license
        license_manager.load_user_license(user['id'])
        
        print("✅ Test environment set up successfully!")
        print(f"👤 User: {user['full_name']} ({user['email']})")
        print(f"🏢 Company: {company['company_name']} (MST: {company['tax_code']})")
        print()
        
        # Demo 1: Usage Statistics
        print("📊 **Usage Statistics (Free License):**")
        print("-" * 40)
        
        stats = license_manager.get_feature_usage_stats()
        print(f"📄 License Type: {stats['license_type'].upper()}")
        print(f"🏢 Companies: {stats['companies']['current']}/{stats['companies']['max']} "
              f"({stats['companies']['usage_percent']:.0f}% used)")
        print(f"📧 Invoices This Month: {stats['invoices_this_month']['current']}/{stats['invoices_this_month']['max']}")
        print(f"🔌 Available Integrations: {', '.join(stats['available_integrations'])}")
        print(f"💾 Export Formats: {', '.join(stats['export_formats'])}")
        print()
        
        premium_features = stats['premium_features']
        print("🌟 **Premium Features:**")
        for feature, enabled in premium_features.items():
            status = "✅" if enabled else "❌"
            print(f"   {status} {feature.replace('_', ' ').title()}")
        print()
        
        # Demo 2: Upgrade Recommendations
        print("💡 **Upgrade Recommendations:**")
        print("-" * 40)
        
        recommendations = license_manager.check_upgrade_recommendations()
        for i, rec in enumerate(recommendations, 1):
            priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(rec['priority'], "ℹ️")
            print(f"{i}. {priority_icon} **{rec['type'].replace('_', ' ').title()}**")
            print(f"   📝 {rec['message']}")
            print(f"   🎯 Suggested: {rec['suggested_plan'].upper()}")
            print()
        
        # Demo 3: Plan Comparison
        print("💰 **Plan Comparison:**")
        print("-" * 40)
        
        comparison = license_manager.get_plan_comparison()
        current_plan = comparison['current_plan']
        
        for plan_id, plan in comparison['plans'].items():
            current_marker = " ← CURRENT" if plan_id == current_plan else ""
            highlight = " ⭐ RECOMMENDED" if plan.get('highlight') else ""
            
            print(f"📦 **{plan['name']}** ({plan_id.upper()}){current_marker}{highlight}")
            
            if plan['price'] > 0:
                print(f"   💵 {plan['price']:,} {plan['currency']}/{plan['period']}")
                if plan.get('discount'):
                    print(f"   🎁 {plan['discount']}")
            else:
                print(f"   💵 Free")
            
            if plan.get('contact_sales'):
                print(f"   📞 Contact sales for pricing")
            
            # Show key features
            features = plan['features']
            print(f"   🏢 Companies: {features['max_companies'] if features['max_companies'] > 0 else 'Unlimited'}")
            print(f"   📧 Invoices/month: {features['max_invoices_per_month'] if features['max_invoices_per_month'] > 0 else 'Unlimited'}")
            print(f"   🔌 Integrations: {', '.join(features['api_integrations'])}")
            
            if features.get('ai_suggestions'):
                print(f"   🤖 AI Suggestions included")
            if features.get('white_label'):
                print(f"   🏷️ White label available")
            
            print()
        
        # Demo 4: Provider Access Control
        print("🔌 **Provider Access Control:**")
        print("-" * 40)
        
        providers_to_test = ['manual', 'viettel', 'mobifone', 'fpt']
        for provider in providers_to_test:
            can_use = license_manager.can_use_provider(provider)
            status = "✅ Available" if can_use else "❌ Requires upgrade"
            print(f"   {provider.upper()}: {status}")
        print()
        
        # Demo 5: Export Format Control
        print("💾 **Export Format Access:**")
        print("-" * 40)
        
        formats_to_test = ['csv', 'excel', 'pdf', 'xml']
        for format_type in formats_to_test:
            can_export = license_manager.can_export_format(format_type)
            status = "✅ Available" if can_export else "❌ Requires upgrade"
            print(f"   {format_type.upper()}: {status}")
        print()
        
        # Demo 6: Feature Gating Integration
        print("🚪 **Feature Gating Examples:**")
        print("-" * 40)
        
        test_cases = [
            ('use_api', {'api_type': 'viettel'}),
            ('export', {'format': 'excel'}),
            ('ai_suggestion', {}),
            ('add_company', {}),
        ]
        
        for action, kwargs in test_cases:
            result = license_manager.check_feature_access(action, **kwargs)
            status = "✅ Allowed" if result['allowed'] else "❌ Blocked"
            print(f"   {action}: {status}")
            if not result['allowed']:
                print(f"      💬 {result['message']}")
        print()
        
        # Demo 7: Simulate Upgrade to Pro
        print("⬆️ **Simulating Upgrade to Pro:**")
        print("-" * 40)
        
        # Simulate license upgrade
        with db_manager.get_session() as session:
            from database.models import License
            
            license_record = session.query(License).filter_by(
                user_id=user['id']
            ).first()
            
            license_record.license_type = 'pro'
            session.commit()
        
        # Reload license
        license_manager.load_user_license(user['id'])
        
        print("✅ Upgraded to Pro license!")
        print(f"📄 New license type: {license_manager.get_license_type().upper()}")
        
        # Show new capabilities
        print("\n🌟 **New Capabilities:**")
        print(f"   🔌 Viettel API: {'✅' if license_manager.can_use_provider('viettel') else '❌'}")
        print(f"   💾 Excel export: {'✅' if license_manager.can_export_format('excel') else '❌'}")
        print(f"   🤖 AI suggestions: {'✅' if license_manager.is_feature_enabled('ai_suggestions') else '❌'}")
        
        # Updated stats
        new_stats = license_manager.get_feature_usage_stats()
        print(f"   🏢 Company limit: {new_stats['companies']['max']}")
        print(f"   📧 Invoice limit: {new_stats['invoices_this_month']['max']}/month")
        print()
        
        print("🎉 **Enhanced License System Demo Completed!**")
        print("=" * 60)
        print("New features working perfectly:")
        print("✅ Advanced usage statistics")
        print("✅ Smart upgrade recommendations")
        print("✅ Plan comparison data")
        print("✅ Provider access control")
        print("✅ Export format restrictions")
        print("✅ Seamless license upgrades")
        print("✅ Enhanced feature gating")
    
    except Exception as e:
        print(f"❌ Demo error: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Clean up
        try:
            os.unlink(db_file.name)
        except:
            pass


if __name__ == "__main__":
    demo_enhanced_license_features()
