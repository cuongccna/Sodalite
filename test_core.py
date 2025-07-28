"""
FinanTidy CLI Test Suite
Test core functionality without GUI dependencies
"""

import os
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_database_operations():
    """Test database functionality"""
    print("🗃️  Testing Database Operations...")
    
    try:
        from database.manager import DatabaseManager
        from database.models import User, Company
        
        # Initialize database manager
        data_dir = Path.home() / "FinanTidy" / "test_data"
        db_manager = DatabaseManager(str(data_dir))
        db_manager.initialize_master_db()
        
        print("  ✅ Database initialized successfully")
        
        # Test user authentication
        user = db_manager.authenticate_user("admin", "admin123")
        if user:
            print(f"  ✅ User authenticated: {user['username']}")
        else:
            print("  ❌ User authentication failed")
            return False
        
        # Test company retrieval
        companies = db_manager.get_user_companies(user['id'])
        print(f"  ✅ Found {len(companies)} companies for user")
        
        for company in companies:
            print(f"    - {company['company_name']} (MST: {company['tax_code']})")
        
        if len(companies) == 0:
            print("  ⚠️  No companies found - this is expected on fresh install")
        
        db_manager.close_all_connections()
        return True
        
    except Exception as e:
        print(f"  ❌ Database test failed: {e}")
        return False


def test_license_manager():
    """Test license management"""
    print("\n🔐 Testing License Manager...")
    
    try:
        from core.license_manager import LicenseManager
        from database.manager import DatabaseManager
        
        # Initialize with database using SAME data dir as other tests
        data_dir = Path.home() / "FinanTidy" / "dev_data"  # Use dev_data, not test_data
        db_manager = DatabaseManager(str(data_dir))
        db_manager.initialize_master_db()  # Initialize master DB first
        license_manager = LicenseManager(db_manager)
        
        # Load admin user license (should be Agency from setup)
        success = license_manager.load_user_license(1)  # Admin user ID
        if success:
            print("  ✅ License loaded successfully")
        else:
            print("  ❌ License loading failed")
            return False
        
        # Test license features
        license_type = license_manager.get_license_type()
        print(f"  ✅ License type: {license_type}")
        
        # Test feature checks
        features_to_test = [
            'ai_suggestions',
            'advanced_reports',
            'multi_user',
            'bulk_operations'
        ]
        
        for feature in features_to_test:
            enabled = license_manager.is_feature_enabled(feature)
            status = "✅" if enabled else "⚠️"
            print(f"  {status} Feature '{feature}': {'Enabled' if enabled else 'Disabled'}")
        
        # Test limits
        max_companies = license_manager.get_max_companies()
        max_invoices = license_manager.get_max_invoices_per_month()
        
        print(f"  📊 Limits - Companies: {max_companies}, Invoices/month: {max_invoices}")
        
        db_manager.close_all_connections()
        return True
        
    except Exception as e:
        print(f"  ❌ License manager test failed: {e}")
        return False


def test_configuration():
    """Test configuration loading"""
    print("\n⚙️  Testing Configuration...")
    
    try:
        import json
        from pathlib import Path
        
        config_path = Path(__file__).parent / "config" / "default_config.json"
        
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print("  ✅ Configuration loaded successfully")
            print(f"  📱 App: {config['app']['name']} v{config['app']['version']}")
            print(f"  🗃️  Database: {config['database']['master_db_name']}")
            print(f"  🎨 UI: Theme={config['ui']['theme']}, Language={config['ui']['language']}")
            return True
        else:
            print(f"  ❌ Configuration file not found: {config_path}")
            return False
            
    except Exception as e:
        print(f"  ❌ Configuration test failed: {e}")
        return False


def test_imports():
    """Test all critical imports"""
    print("\n📦 Testing Package Imports...")
    
    imports_to_test = [
        ('SQLAlchemy', 'sqlalchemy'),
        ('Pandas', 'pandas'),
        ('Requests', 'requests'),
        ('Cryptography', 'cryptography'),
        ('Loguru', 'loguru'),
        ('Python-dotenv', 'dotenv'),
        ('Pydantic', 'pydantic'),
    ]
    
    success_count = 0
    
    for name, module in imports_to_test:
        try:
            __import__(module)
            print(f"  ✅ {name}")
            success_count += 1
        except ImportError as e:
            print(f"  ❌ {name}: {e}")
    
    print(f"\n  📊 Import Success Rate: {success_count}/{len(imports_to_test)} ({success_count/len(imports_to_test)*100:.1f}%)")
    return success_count == len(imports_to_test)


def run_all_tests():
    """Run comprehensive test suite"""
    print("🚀 FinanTidy Core Functionality Test Suite")
    print("=" * 50)
    
    tests = [
        ("Package Imports", test_imports),
        ("Configuration", test_configuration),
        ("Database Operations", test_database_operations),
        ("License Manager", test_license_manager),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"\n❌ {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} {test_name}")
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("🎉 All tests passed! Core functionality is working properly.")
        print("💡 Ready to proceed with GUI troubleshooting or continue with business logic development.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
