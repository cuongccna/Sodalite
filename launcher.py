#!/usr/bin/env python3
"""
Simple launcher để test login -> main window flow
"""

import sys
import os
import time
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def run_app():
    """Run FinanTidy application"""
    try:
        import customtkinter as ctk
        from ui.modern.login_window import ModernLoginWindow
        
        # Configure CTk
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        print("🚀 FinanTidy đang khởi động...")
        print("📱 Cửa sổ đăng nhập sẽ xuất hiện trong giây lát...")
        
        # Small delay to show message
        time.sleep(1)
        
        # Create and run login window
        app = ModernLoginWindow()
        app.mainloop()
        
        print("✅ Ứng dụng đã đóng")
        
    except ImportError as e:
        print(f"❌ Lỗi import: {e}")
        print("💡 Đảm bảo CustomTkinter đã được cài đặt")
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("=" * 60)
    print("🏦 FinanTidy - Professional Financial Management System")
    print("=" * 60)
    
    run_app()
    
    print("\n👋 Cảm ơn bạn đã sử dụng FinanTidy!")
