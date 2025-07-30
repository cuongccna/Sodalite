"""
Test thiết kế mới của Login Window
Kiểm tra việc áp dụng QFormLayout theo mẫu pythonguis.com
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from PySide6.QtWidgets import QApplication, QMessageBox

# Import login window with proper path handling
try:
    from src.ui.login_window import LoginWindow
except ImportError:
    # Try alternative import for testing
    sys.path.insert(0, str(project_root / "src"))
    from ui.login_window import LoginWindow


class MockDatabaseManager:
    """Mock database manager for testing"""
    
    def authenticate_user(self, username, password):
        """Mock authentication - accepts demo/demo"""
        if username == "demo" and password == "demo":
            return {
                "id": 1,
                "username": username,
                "full_name": "Demo User",
                "email": "demo@finantidy.com"
            }
        return None


def test_login_window():
    """Test the new login window design"""
    app = QApplication(sys.argv)
    
    # Create mock database
    db_manager = MockDatabaseManager()
    
    # Create login window
    login_window = LoginWindow(db_manager)
    
    def handle_successful_login(user_data):
        """Handle successful login"""
        QMessageBox.information(
            None,
            "🎉 Test thành công!",
            f"Đăng nhập thành công với thông tin:\n\n"
            f"👤 Username: {user_data['username']}\n"
            f"📧 Email: {user_data['email']}\n"
            f"🆔 ID: {user_data['id']}\n\n"
            f"✅ QFormLayout đã hoạt động đúng cách!"
        )
        app.quit()
    
    # Connect success signal
    login_window.user_authenticated.connect(handle_successful_login)
    
    # Show login window
    login_window.show()
    
    print("🚀 Đang khởi chạy Login Window với thiết kế mới...")
    print("📝 Thông tin đăng nhập test:")
    print("   • Username: demo")
    print("   • Password: demo")
    print("💡 Kiểm tra các tính năng:")
    print("   ✓ QFormLayout.addRow() layout")
    print("   ✓ Proper field alignment")
    print("   ✓ Show/hide password")
    print("   ✓ Enter key navigation")
    print("   ✓ Validation & error handling")
    
    # Run application
    sys.exit(app.exec())


if __name__ == "__main__":
    test_login_window()
