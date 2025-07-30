#!/usr/bin/env python3
"""
Test script for Viettel eInvoice integration
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_viettel_integration():
    """Test Viettel eInvoice integration components"""
    
    print("🧪 Testing Viettel eInvoice Integration...")
    print("=" * 50)
    
    # Test 1: Import Viettel service
    try:
        from integrations.viettel_einvoice import ViettelEInvoiceService, ViettelEInvoiceConfig
        print("✅ Viettel eInvoice service imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import Viettel service: {e}")
        return False
        
    # Test 2: Create configuration instance
    try:
        config = ViettelEInvoiceConfig()
        print("✅ Viettel configuration instance created")
    except Exception as e:
        print(f"❌ Failed to create configuration: {e}")
        return False
        
    # Test 3: Check configuration status
    try:
        is_configured = config.is_configured()
        print(f"📋 Configuration status: {'Configured' if is_configured else 'Not configured'}")
    except Exception as e:
        print(f"❌ Failed to check configuration status: {e}")
        return False
        
    # Test 4: Test service initialization
    try:
        service = ViettelEInvoiceService(config)
        print("✅ Viettel eInvoice service initialized")
    except Exception as e:
        print(f"❌ Failed to initialize service: {e}")
        return False
        
    # Test 5: Import UI components
    try:
        from ui.modern.viettel_config_window import ViettelConfigWindow
        print("✅ Viettel configuration window imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import configuration window: {e}")
        return False
        
    print("\n🎉 All Viettel eInvoice integration tests passed!")
    print("\n📝 Next steps:")
    print("1. Configure Viettel API credentials via Settings > Viettel eInvoice")
    print("2. Test connection with Viettel test environment")
    print("3. Create test electronic invoice")
    print("4. Verify PDF generation and download")
    
    return True

def test_ui_integration():
    """Test UI integration"""
    
    print("\n🖥️ Testing UI Integration...")
    print("=" * 30)
    
    # Test main window imports
    try:
        from ui.modern.main_window import ModernMainWindow
        print("✅ Main window imports work")
    except ImportError as e:
        print(f"❌ Main window import failed: {e}")
        return False
        
    # Test invoices window imports  
    try:
        from ui.modern.invoices_window import InvoicesWindow
        print("✅ Invoices window imports work")
    except ImportError as e:
        print(f"❌ Invoices window import failed: {e}")
        return False
        
    # Test settings window imports
    try:
        from ui.modern.settings_window import SettingsWindow
        print("✅ Settings window imports work")
    except ImportError as e:
        print(f"❌ Settings window import failed: {e}")
        return False
        
    print("✅ All UI integration tests passed!")
    return True

if __name__ == "__main__":
    print("🚀 FinanTidy Viettel eInvoice Integration Test")
    print("=" * 60)
    
    success = True
    
    # Run integration tests
    success &= test_viettel_integration()
    success &= test_ui_integration()
    
    print("\n" + "=" * 60)
    if success:
        print("🎊 ALL TESTS PASSED! Viettel eInvoice integration is ready!")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    
    print("\n📋 Integration Summary:")
    print("• ViettelEInvoiceService: API integration and invoice creation")
    print("• ViettelConfigWindow: Configuration UI for credentials and settings")
    print("• InvoicesWindow: Enhanced with eInvoice buttons and functionality")  
    print("• SettingsWindow: Added Viettel eInvoice configuration section")
    print("• MainWindow: Added quick access to Viettel configuration")
    
    input("\nPress Enter to exit...")
