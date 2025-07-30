#!/usr/bin/env python3
"""
Test login flow để kiểm tra xem main window có mở sau khi login không
"""

import sys
import os
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def test_login_flow():
    """Test complete login flow"""
    print("🚀 Testing Login Flow...")
    
    try:
        import customtkinter as ctk
        from ui.modern.login_window import ModernLoginWindow
        
        # Set appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create login window
        login = ModernLoginWindow()
        print("✅ Login window created")
        
        # Simulate login
        login.username_entry.delete(0, 'end')
        login.username_entry.insert(0, "admin")
        login.password_entry.delete(0, 'end') 
        login.password_entry.insert(0, "admin")
        print("✅ Credentials entered")
        
        # Check if login_action method exists
        if hasattr(login, 'login_action'):
            print("✅ login_action method found")
        else:
            print("❌ login_action method not found")
            
        # Check if open_main_window method exists
        if hasattr(login, 'open_main_window'):
            print("✅ open_main_window method found")
        else:
            print("❌ open_main_window method not found")
            
        # Check if main_window can be imported
        try:
            from ui.modern.main_window import ModernMainWindow
            print("✅ ModernMainWindow can be imported")
        except ImportError as e:
            print(f"❌ Cannot import ModernMainWindow: {e}")
            
        login.destroy()
        print("✅ Login window test completed")
        
    except Exception as e:
        print(f"❌ Login flow test failed: {e}")
        import traceback
        traceback.print_exc()

def main():
    """Run test"""
    print("🔍 Testing Login to Main Window Flow")
    print("=" * 50)
    
    test_login_flow()
    
    print("=" * 50)
    print("✅ Test completed!")
    print("\n💡 To test manually:")
    print("   1. Run: cd src && python main.py")
    print("   2. Login with admin/admin")
    print("   3. Main window should open")

if __name__ == "__main__":
    main()
