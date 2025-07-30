#!/usr/bin/env python3
"""
Demo script để test login flow hoàn chỉnh
"""

import sys
import os
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def demo_login():
    """Demo login process"""
    print("🚀 Starting FinanTidy Demo...")
    
    try:
        import customtkinter as ctk
        from ui.modern.login_window import ModernLoginWindow
        
        # Set appearance
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        print("✅ Creating login window...")
        login = ModernLoginWindow()
        
        print("✅ Login window ready!")
        print("📝 Instructions:")
        print("   - Username: admin")
        print("   - Password: admin")
        print("   - Click 'ĐĂNG NHẬP' button")
        print("   - Main window should open")
        print("   - Close main window to return to login")
        
        # Start login window
        login.mainloop()
        
        print("✅ Application closed successfully")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    demo_login()
