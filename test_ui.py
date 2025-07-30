#!/usr/bin/env python3
"""
Quick test script to verify UI components work correctly
"""

import sys
import os
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def test_login_window():
    """Test login window"""
    print("🔍 Testing Login Window...")
    try:
        import customtkinter as ctk
        from ui.modern.login_window import ModernLoginWindow
        
        # Create login window
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        login = ModernLoginWindow()
        print("✅ Login window created successfully")
        
        # Check if login button exists
        if hasattr(login, 'login_button'):
            button_text = login.login_button.cget("text")
            print(f"✅ Login button found with text: '{button_text}'")
        else:
            print("❌ Login button not found")
            
        login.destroy()
        
    except Exception as e:
        print(f"❌ Login window test failed: {e}")

def test_settings_window():
    """Test settings window"""
    print("🔍 Testing Settings Window...")
    try:
        import customtkinter as ctk
        from ui.modern.settings_window import SettingsWindow
        
        # Create root window
        root = ctk.CTk()
        root.withdraw()
        
        # Create settings window
        settings = SettingsWindow(root)
        print("✅ Settings window created successfully")
        
        # Check navigation buttons
        if hasattr(settings, 'nav_buttons'):
            categories = list(settings.nav_buttons.keys())
            print(f"✅ Settings categories found: {categories}")
            
            if 'viettel_einvoice' in categories:
                print("✅ Viettel eInvoice category found")
            else:
                print("❌ Viettel eInvoice category not found")
        else:
            print("❌ Navigation buttons not found")
            
        settings.destroy()
        root.destroy()
        
    except Exception as e:
        print(f"❌ Settings window test failed: {e}")

def test_language_manager():
    """Test language manager"""
    print("🔍 Testing Language Manager...")
    try:
        from core.language_manager import get_language_manager, t
        
        lang_manager = get_language_manager()
        print("✅ Language manager loaded")
        
        # Test Vietnamese translations
        login_button_vi = t('login.login_button', 'Default')
        viettel_title_vi = t('settings.viettel_einvoice.title', 'Default')
        
        print(f"✅ Vietnamese login button: '{login_button_vi}'")
        print(f"✅ Vietnamese Viettel title: '{viettel_title_vi}'")
        
        # Switch to English
        lang_manager.set_language('en')
        
        login_button_en = t('login.login_button', 'Default')
        viettel_title_en = t('settings.viettel_einvoice.title', 'Default')
        
        print(f"✅ English login button: '{login_button_en}'")
        print(f"✅ English Viettel title: '{viettel_title_en}'")
        
        # Switch back to Vietnamese
        lang_manager.set_language('vi')
        
    except Exception as e:
        print(f"❌ Language manager test failed: {e}")

def main():
    """Run all tests"""
    print("🚀 Starting UI Component Tests")
    print("=" * 50)
    
    test_language_manager()
    print()
    
    test_login_window()
    print()
    
    test_settings_window()
    print()
    
    print("=" * 50)
    print("✅ All tests completed!")

if __name__ == "__main__":
    main()
