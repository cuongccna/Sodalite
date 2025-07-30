#!/usr/bin/env python3
"""
Test Login Window để kiểm tra form hiển thị
"""

import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from PySide6.QtWidgets import QApplication
from ui.login_window import LoginWindow
from database.manager import DatabaseManager

def test_login_window():
    """Test login window display"""
    print("🔍 Testing Login Window...")
    
    app = QApplication(sys.argv)
    
    try:
        # Initialize database
        db_manager = DatabaseManager()
        db_manager.initialize_master_db()
        
        # Create login window
        login_window = LoginWindow(db_manager)
        login_window.show()
        
        print("✅ Login window created and shown")
        print("📋 You should now see:")
        print("   • Clear 'Tên đăng nhập' field")
        print("   • Clear 'Mật khẩu' field") 
        print("   • Login credentials: demo/demo")
        
        # Run the application
        sys.exit(app.exec())
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_login_window()
