#!/usr/bin/env python3
"""
Debug script để kiểm tra từng bước của login flow
"""

import sys
import os
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def debug_login_components():
    """Debug các component của login"""
    print("🔍 Debugging Login Components...")
    
    try:
        # Test imports
        print("1️⃣ Testing imports...")
        
        import customtkinter as ctk
        print("   ✅ CustomTkinter imported")
        
        from ui.modern.login_window import ModernLoginWindow
        print("   ✅ ModernLoginWindow imported")
        
        from ui.modern.main_window import ModernMainWindow
        print("   ✅ ModernMainWindow imported")
        
        from core.language_manager import get_language_manager, t
        print("   ✅ Language manager imported")
        
        # Test login window creation
        print("\n2️⃣ Testing login window creation...")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        login = ModernLoginWindow()
        print("   ✅ Login window created")
        
        # Test session data creation
        print("\n3️⃣ Testing session data...")
        session_data = {
            'user_id': 1,
            'username': 'admin',
            'full_name': 'Demo User',
            'company_id': 1,
            'company_name': 'Demo Company',
            'role': 'admin',
            'license': {'type': 'demo'}
        }
        print("   ✅ Session data created")
        
        # Test main window creation
        print("\n4️⃣ Testing main window creation...")
        try:
            main_window = ModernMainWindow(session_data)
            print("   ✅ Main window created successfully")
            main_window.destroy()
        except Exception as e:
            print(f"   ❌ Main window creation failed: {e}")
            import traceback
            traceback.print_exc()
        
        # Test open_main_window method
        print("\n5️⃣ Testing open_main_window method...")
        if hasattr(login, 'open_main_window'):
            print("   ✅ open_main_window method exists")
            
            # Check method code (just signature)
            import inspect
            signature = inspect.signature(login.open_main_window)
            print(f"   📝 Method signature: {signature}")
        else:
            print("   ❌ open_main_window method not found")
        
        login.destroy()
        print("\n✅ All tests completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Debug failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🔧 FinanTidy Login Flow Debug")
    print("=" * 50)
    
    debug_login_components()
    
    print("\n" + "=" * 50)
    print("💡 If all tests pass, the login flow should work correctly")
