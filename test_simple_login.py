#!/usr/bin/env python3
"""
Test script đơn giản cho giao diện đăng nhập mới
Chỉ test UI không cần database
"""

import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel, QCheckBox, QMessageBox, QFrame, QSpacerItem, QSizePolicy
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QFont


class SimpleLoginWindow(QDialog):
    """Giao diện đăng nhập đơn giản test"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_styling()
    
    def setup_ui(self):
        """Thiết lập giao diện người dùng"""
        self.setWindowTitle("FinanTidy - Test Login")
        self.setFixedSize(420, 480)
        self.setModal(True)
        
        # Layout chính
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(25)
        
        # Header
        self.create_header()
        self.create_login_form()
        self.create_buttons()
        
    def create_header(self):
        """Tạo phần header"""
        header_layout = QVBoxLayout()
        header_layout.setSpacing(8)
        
        logo_label = QLabel("💼")
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setObjectName("logo")
        
        title_label = QLabel("FinanTidy")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setObjectName("title")
        
        subtitle_label = QLabel("Quản lý tài chính thông minh")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setObjectName("subtitle")
        
        header_layout.addWidget(logo_label)
        header_layout.addWidget(title_label)
        header_layout.addWidget(subtitle_label)
        
        self.main_layout.addLayout(header_layout)
    
    def create_login_form(self):
        """Tạo form đăng nhập"""
        form_frame = QFrame()
        form_frame.setObjectName("formFrame")
        
        form_layout = QVBoxLayout(form_frame)
        form_layout.setContentsMargins(25, 25, 25, 25)
        form_layout.setSpacing(18)
        
        # Tiêu đề form
        form_title = QLabel("Đăng nhập")
        form_title.setAlignment(Qt.AlignCenter)
        form_title.setObjectName("formTitle")
        form_layout.addWidget(form_title)
        
        # Username
        username_label = QLabel("Tên đăng nhập:")
        username_label.setObjectName("fieldLabel")
        self.username_input = QLineEdit()
        self.username_input.setObjectName("textInput")
        self.username_input.setText("demo")
        self.username_input.setPlaceholderText("Nhập tên đăng nhập của bạn")
        self.username_input.setMinimumHeight(42)
        
        # Password
        password_label = QLabel("Mật khẩu:")
        password_label.setObjectName("fieldLabel")
        self.password_input = QLineEdit()
        self.password_input.setObjectName("textInput")
        self.password_input.setText("demo")
        self.password_input.setPlaceholderText("Nhập mật khẩu của bạn")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(42)
        
        # Show password checkbox
        self.show_password_checkbox = QCheckBox("Hiển thị mật khẩu")
        self.show_password_checkbox.setObjectName("checkbox")
        self.show_password_checkbox.toggled.connect(self.toggle_password_visibility)
        
        form_layout.addWidget(username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addSpacing(5)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addSpacing(5)
        form_layout.addWidget(self.show_password_checkbox)
        
        self.main_layout.addWidget(form_frame)
    
    def create_buttons(self):
        """Tạo nút"""
        button_layout = QVBoxLayout()
        button_layout.setSpacing(12)
        
        self.login_button = QPushButton("Đăng nhập")
        self.login_button.setObjectName("loginButton")
        self.login_button.setMinimumHeight(45)
        self.login_button.setCursor(Qt.PointingHandCursor)
        self.login_button.clicked.connect(self.login)
        
        register_button = QPushButton("Đăng ký tài khoản mới")
        register_button.setObjectName("registerButton")
        register_button.setMinimumHeight(40)
        register_button.setCursor(Qt.PointingHandCursor)
        
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(register_button)
        
        self.main_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.main_layout.addLayout(button_layout)
        
        self.username_input.returnPressed.connect(self.login)
        self.password_input.returnPressed.connect(self.login)
    
    def setup_styling(self):
        """Thiết lập style"""
        self.setStyleSheet("""
            /* Nền chính */
            QDialog {
                background-color: #f8fafc;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            /* Logo */
            QLabel#logo {
                font-size: 36px;
                color: #2563eb;
                padding: 8px;
            }
            
            /* Tiêu đề */
            QLabel#title {
                font-size: 26px;
                font-weight: bold;
                color: #1e293b;
                padding: 4px;
            }
            
            /* Mô tả */
            QLabel#subtitle {
                font-size: 14px;
                color: #64748b;
                padding: 4px;
            }
            
            /* Khung form */
            QFrame#formFrame {
                background-color: white;
                border: 2px solid #e2e8f0;
                border-radius: 12px;
                margin: 5px 0;
            }
            
            /* Tiêu đề form */
            QLabel#formTitle {
                font-size: 16px;
                font-weight: 600;
                color: #374151;
                padding: 8px;
                background-color: #f1f5f9;
                border-radius: 6px;
                margin-bottom: 8px;
            }
            
            /* Nhãn trường */
            QLabel#fieldLabel {
                font-size: 14px;
                font-weight: 500;
                color: #374151;
                padding: 0 2px 3px 2px;
            }
            
            /* Ô nhập liệu - QUAN TRỌNG */
            QLineEdit#textInput {
                font-size: 14px;
                padding: 12px 16px;
                border: 2px solid #cbd5e1;
                border-radius: 8px;
                background-color: #ffffff;  /* Nền trắng */
                color: #1f2937;            /* Chữ đen */
                selection-background-color: #3b82f6;
                selection-color: white;
            }
            
            QLineEdit#textInput:focus {
                border-color: #3b82f6;
                background-color: #ffffff;
                outline: none;
            }
            
            QLineEdit#textInput:hover {
                border-color: #94a3b8;
                background-color: #ffffff;
            }
            
            /* Placeholder rõ ràng */
            QLineEdit#textInput::placeholder {
                color: #94a3b8;
                font-style: italic;
            }
            
            /* Checkbox */
            QCheckBox#checkbox {
                font-size: 13px;
                color: #6b7280;
                padding: 3px 0;
            }
            
            /* Nút đăng nhập */
            QPushButton#loginButton {
                background-color: #3b82f6;
                color: white;
                font-size: 15px;
                font-weight: 600;
                border: none;
                border-radius: 8px;
                padding: 13px 20px;
            }
            
            QPushButton#loginButton:hover {
                background-color: #2563eb;
            }
            
            /* Nút đăng ký */
            QPushButton#registerButton {
                background-color: transparent;
                color: #6b7280;
                font-size: 13px;
                border: 2px solid #d1d5db;
                border-radius: 8px;
                padding: 10px 20px;
            }
            
            QPushButton#registerButton:hover {
                background-color: #f9fafb;
                color: #374151;
            }
        """)
    
    def toggle_password_visibility(self, checked):
        """Toggle password visibility"""
        if checked:
            self.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
    
    def login(self):
        """Test login"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return
        
        QMessageBox.information(self, "Test thành công!", 
                               f"✅ Giao diện hoạt động tốt!\n\n"
                               f"Username: {username}\n"
                               f"Password: {'*' * len(password)}\n\n"
                               f"Textbox có thể nhìn thấy rõ ràng!")
        self.accept()


def main():
    """Test giao diện"""
    print("🧪 Test giao diện đăng nhập mới")
    print("=" * 50)
    print("✨ Kiểm tra:")
    print("• Textbox có nền trắng rõ ràng")
    print("• Placeholder text có thể đọc được") 
    print("• Viền textbox rõ ràng khi focus")
    print("• Có thể nhập text bình thường")
    print("• Test với demo/demo")
    
    app = QApplication([])
    
    login_window = SimpleLoginWindow()
    login_window.show()
    
    return app.exec()


if __name__ == "__main__":
    main()
