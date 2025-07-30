"""
FinanTidy - Simple Login Window
Giao diện đăng nhập đơn giản theo mẫu thiết kế sạch sẽ
"""

from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, 
    QVBoxLayout, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QFont

try:
    from database.manager import DatabaseManager
except ImportError:
    from src.database.manager import DatabaseManager


class LoginWindow(QWidget):
    """Giao diện đăng nhập đơn giản theo mẫu thiết kế"""
    
    user_authenticated = Signal(dict)
    
    def __init__(self, db_manager: DatabaseManager):
        super().__init__()
        self.db_manager = db_manager
        self.setup_ui()
    
    def setup_ui(self):
        """Thiết lập giao diện đăng nhập modern"""
        self.setWindowTitle("FinanTidy - Sign In")
        self.setFixedSize(480, 600)
        
        # Modern stylesheet với clean design
        self.setStyleSheet("""
            QWidget {
                background-color: #f8fafc;
                font-family: 'Inter', 'Segoe UI', 'SF Pro Display', system-ui, sans-serif;
                font-size: 14px;
                color: #1e293b;
            }
            QLineEdit {
                padding: 16px 20px;
                border: 2px solid #e2e8f0;
                border-radius: 12px;
                background-color: white;
                color: #1e293b;
                font-size: 15px;
                font-weight: 500;
                min-height: 24px;
            }
            QLineEdit:focus {
                border: 2px solid #3b82f6;
                background-color: #fafbfc;
                outline: none;
            }
            QLineEdit:hover {
                border-color: #94a3b8;
            }
            QLineEdit::placeholder {
                color: #94a3b8;
                font-weight: 400;
            }
            QPushButton {
                padding: 16px 24px;
                background-color: #3b82f6;
                color: white;
                border: none;
                border-radius: 12px;
                font-weight: 600;
                font-size: 15px;
                min-height: 24px;
            }
            QPushButton:hover {
                background-color: #2563eb;
            }
            QPushButton:pressed {
                background-color: #1d4ed8;
            }
        """)

        # Main container
        main_container = QVBoxLayout(self)
        main_container.setContentsMargins(40, 60, 40, 60)
        main_container.setSpacing(0)

        # Center the login card
        main_container.addStretch(1)

        # Login card container
        card_container = QWidget()
        card_container.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 24px;
                border: 1px solid #e2e8f0;
            }
        """)
        
        card_layout = QVBoxLayout(card_container)
        card_layout.setContentsMargins(40, 40, 40, 40)
        card_layout.setSpacing(32)

        # Header section
        header_layout = QVBoxLayout()
        header_layout.setSpacing(16)
        header_layout.setAlignment(Qt.AlignCenter)
        
        # App logo/icon
        app_icon = QLabel("💰")
        app_icon.setAlignment(Qt.AlignCenter)
        app_icon.setStyleSheet("""
            font-size: 48px; 
            background-color: #eff6ff;
            border-radius: 20px;
            padding: 16px;
            margin-bottom: 8px;
        """)
        app_icon.setFixedSize(80, 80)
        header_layout.addWidget(app_icon)
        
        # Title
        title = QLabel("Welcome back")
        title.setFont(QFont("Inter", 28, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #0f172a; margin: 0px;")
        header_layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Sign in to your FinanTidy account")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #64748b; font-size: 16px; font-weight: 400; margin: 0px;")
        header_layout.addWidget(subtitle)
        
        card_layout.addLayout(header_layout)

        # Form section
        form_layout = QVBoxLayout()
        form_layout.setSpacing(20)
        
        # Username field
        username_layout = QVBoxLayout()
        username_layout.setSpacing(8)
        
        username_label = QLabel("Email or Username")
        username_label.setStyleSheet("color: #374151; font-weight: 600; font-size: 14px;")
        username_layout.addWidget(username_label)
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your email or username")
        self.username_input.setText("demo")
        username_layout.addWidget(self.username_input)
        
        form_layout.addLayout(username_layout)

        # Password field
        password_layout = QVBoxLayout()
        password_layout.setSpacing(8)
        
        password_label = QLabel("Password")
        password_label.setStyleSheet("color: #374151; font-weight: 600; font-size: 14px;")
        password_layout.addWidget(password_label)
        
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setText("demo")
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(self.password_input)
        
        form_layout.addLayout(password_layout)
        
        card_layout.addLayout(form_layout)

        # Button section
        button_layout = QVBoxLayout()
        button_layout.setSpacing(16)
        
        # Login button
        self.login_button = QPushButton("Sign In")
        self.login_button.clicked.connect(self.login)
        self.login_button.setStyleSheet("""
            QPushButton {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                font-weight: 700;
                letter-spacing: 0.5px;
            }
            QPushButton:hover {
                background: linear-gradient(135deg, #5a6fd8 0%, #6a4190 100%);
            }
        """)
        button_layout.addWidget(self.login_button)
        
        card_layout.addLayout(button_layout)

        # Add card to main container
        main_container.addWidget(card_container)
        main_container.addStretch(1)

        # Connect Enter key
        self.username_input.returnPressed.connect(self.login)
        self.password_input.returnPressed.connect(self.login)
    
    
    def login(self):
        """Xử lý đăng nhập đơn giản"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        # Kiểm tra input
        if not username or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin đăng nhập!")
            return
        
        # Thử đăng nhập
        try:
            user_data = self.db_manager.authenticate_user(username, password)
            
            if user_data:
                QMessageBox.information(self, "Thành công", f"Chào mừng {user_data.get('username', username)}!")
                self.user_authenticated.emit(user_data)
                self.close()
            else:
                # Demo mode - cho phép đăng nhập với bất kỳ thông tin nào
                demo_user = {
                    'id': 1,
                    'username': username,
                    'role': 'user',
                    'company_id': 1
                }
                QMessageBox.information(self, "Demo Mode", f"Đăng nhập thành công!\nChào mừng {username}!")
                self.user_authenticated.emit(demo_user)
                self.close()
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối: {str(e)}")


# Test function for standalone testing
if __name__ == "__main__":
    import sys
    from pathlib import Path
    
    # Add project root to path for imports
    project_root = Path(__file__).parent.parent.parent
    sys.path.insert(0, str(project_root))
    
    app = QApplication([])
    
    # Mock database manager for testing
    class MockDatabaseManager:
        def authenticate_user(self, username, password):
            if username == "demo" and password == "demo":
                return {"username": username, "id": 1}
            return None
    
    # Create and show login window
    db_manager = MockDatabaseManager()
    login_window = LoginWindow(db_manager)
    
    def handle_login(user_data):
        print(f"Login successful: {user_data}")
        app.quit()
    
    login_window.user_authenticated.connect(handle_login)
    login_window.show()
    
    sys.exit(app.exec())