#!/usr/bin/env python3
"""
Test Login UI - Kiểm tra giao diện đăng nhập
"""

import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from PySide6.QtWidgets import QApplication
from src.ui.login_window import LoginWindow
from src.database.manager import DatabaseManager

def test_login_ui():
    """Test the login UI"""
    print("🚀 Khởi tạo test giao diện đăng nhập...")
    
    app = QApplication(sys.argv)
    
    # Initialize database manager
    db_manager = DatabaseManager("test_financials.db")
    
    # Create and show login window
    login_window = LoginWindow(db_manager)
    
    print("✅ Hiển thị giao diện đăng nhập...")
    print("📝 Thông tin đăng nhập:")
    print("   Username: demo")
    print("   Password: demo")
    print("💡 Kiểm tra xem bạn có thể thấy và nhập vào các trường username/password không")
    
    login_window.show()
    
    # Run the application
    sys.exit(app.exec())

if __name__ == "__main__":
    test_login_ui()
