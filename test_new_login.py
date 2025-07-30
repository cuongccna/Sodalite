#!/usr/bin/env python3
"""
Test script cho giao diện đăng nhập mới
Kiểm tra việc hiển thị textbox và placeholder rõ ràng
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from PySide6.QtWidgets import QApplication
from src.ui.login_window import LoginWindow


class MockDatabaseManager:
    """Mock database manager cho test"""
    def authenticate_user(self, username, password):
        print(f"Thử đăng nhập với: {username}/{password}")
        if username == "demo" and password == "demo":
            return {"username": username, "id": 1, "role": "user"}
        return None


def main():
    """Test giao diện đăng nhập mới"""
    print("🧪 Test giao diện đăng nhập FinanTidy")
    print("=" * 50)
    
    app = QApplication([])
    
    # Tạo mock database manager
    db_manager = MockDatabaseManager()
    
    # Tạo cửa sổ đăng nhập
    login_window = LoginWindow(db_manager)
    
    def on_login_success(user_data):
        print(f"✅ Đăng nhập thành công: {user_data}")
        print("Dashboard sẽ được mở ở đây...")
        app.quit()
    
    # Kết nối signal
    login_window.user_authenticated.connect(on_login_success)
    
    # Hiển thị cửa sổ
    login_window.show()
    
    print("✨ Kiểm tra:")
    print("• Textbox có nền trắng rõ ràng")
    print("• Placeholder text có thể đọc được") 
    print("• Viền textbox rõ ràng khi focus")
    print("• Có thể nhập text bình thường")
    print("• Đăng nhập với demo/demo")
    
    return app.exec()


if __name__ == "__main__":
    main()
