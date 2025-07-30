#!/usr/bin/env python3
"""
Test script cho giao diện đăng nhập mới theo mẫu đơn giản
"""

import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class SimpleLoginTest(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FinanTidy - Test Login (Simple)")
        self.setFixedSize(400, 300)
        
        # Style theo mẫu
        self.setStyleSheet("""
            QWidget {
                background-color: #f7f7f7;
                font-family: Arial;
                font-size: 14px;
            }
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 6px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 2px solid #0078d7;
            }
            QPushButton {
                padding: 12px;
                background-color: #0078d7;
                color: white;
                border: none;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)

        # Layout chính
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(15)

        # Tiêu đề
        title = QLabel("Welcome Back 👋")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Email input
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setText("demo")
        layout.addWidget(self.email_input)

        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mật khẩu")
        self.password_input.setText("demo")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Login button
        self.login_button = QPushButton("Đăng nhập")
        self.login_button.clicked.connect(self.test_login)
        layout.addWidget(self.login_button)

        # Wrapper layout
        wrapper = QVBoxLayout(self)
        wrapper.addStretch()
        wrapper.addLayout(layout)
        wrapper.addStretch()

        self.setLayout(wrapper)
        
        # Connect Enter key
        self.email_input.returnPressed.connect(self.test_login)
        self.password_input.returnPressed.connect(self.test_login)

    def test_login(self):
        """Test login function"""
        email = self.email_input.text().strip()
        password = self.password_input.text()
        
        if not email or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return
        
        QMessageBox.information(self, "Test thành công!", 
                               f"✅ Giao diện đơn giản hoạt động tốt!\n\n"
                               f"Email: {email}\n"
                               f"Password: {'*' * len(password)}\n\n"
                               f"Thiết kế sạch sẽ và dễ sử dụng!")
        self.close()


def main():
    """Test giao diện đơn giản"""
    print("🧪 Test giao diện đăng nhập theo mẫu đơn giản")
    print("=" * 50)
    print("✨ Kiểm tra:")
    print("• Thiết kế đơn giản, sạch sẽ")
    print("• Textbox nền trắng, viền rõ ràng") 
    print("• Focus state màu xanh")
    print("• Button hover effect")
    print("• Layout căn giữa đẹp mắt")
    
    app = QApplication([])
    
    login_window = SimpleLoginTest()
    login_window.show()
    
    return app.exec()


if __name__ == "__main__":
    main()
