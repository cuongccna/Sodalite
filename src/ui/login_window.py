"""
Login Window
Handles user authentication
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
                              QLabel, QLineEdit, QPushButton, QCheckBox, 
                              QMessageBox, QFrame)
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QFont, QPixmap, QPalette

from database.manager import DatabaseManager


class LoginWindow(QDialog):
    """Login dialog for user authentication"""
    
    user_authenticated = Signal(dict)  # Emitted when user successfully logs in
    
    def __init__(self, db_manager: DatabaseManager):
        super().__init__()
        self.db_manager = db_manager
        self.setup_ui()
        
        # Auto-fill admin credentials for development
        self.username_input.setText("admin")
        self.password_input.setText("admin123")
    
    def setup_ui(self):
        """Setup the login UI"""
        self.setWindowTitle("FinanTidy - Đăng nhập")
        self.setFixedSize(400, 300)
        self.setModal(True)
        
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(40, 30, 40, 30)
        
        # Logo and title
        self.create_header(layout)
        
        # Login form
        self.create_form(layout)
        
        # Action buttons
        self.create_buttons(layout)
        
        self.setLayout(layout)
    
    def create_header(self, layout):
        """Create header with logo and title"""
        header_layout = QVBoxLayout()
        header_layout.setAlignment(Qt.AlignCenter)
        
        # App title
        title_label = QLabel("FinanTidy")
        title_font = QFont()
        title_font.setPointSize(24)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 5px;")
        
        # Subtitle
        subtitle_label = QLabel("Quản lý tài chính thông minh")
        subtitle_font = QFont()
        subtitle_font.setPointSize(10)
        subtitle_label.setFont(subtitle_font)
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: #7f8c8d; margin-bottom: 20px;")
        
        header_layout.addWidget(title_label)
        header_layout.addWidget(subtitle_label)
        
        layout.addLayout(header_layout)
    
    def create_form(self, layout):
        """Create login form"""
        form_frame = QFrame()
        form_frame.setFrameStyle(QFrame.Box)
        form_frame.setLineWidth(1)
        form_frame.setStyleSheet("""
            QFrame {
                border: 1px solid #bdc3c7;
                border-radius: 8px;
                background-color: #ffffff;
                padding: 20px;
            }
        """)
        
        form_layout = QFormLayout()
        form_layout.setSpacing(15)
        
        # Username input
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Tên đăng nhập")
        self.username_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #bdc3c7;
                border-radius: 4px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border-color: #3498db;
            }
        """)
        
        # Password input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Mật khẩu")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet(self.username_input.styleSheet())
        
        # Remember me checkbox
        self.remember_checkbox = QCheckBox("Ghi nhớ đăng nhập")
        self.remember_checkbox.setStyleSheet("color: #34495e;")
        
        form_layout.addRow("Tên đăng nhập:", self.username_input)
        form_layout.addRow("Mật khẩu:", self.password_input)
        form_layout.addRow("", self.remember_checkbox)
        
        form_frame.setLayout(form_layout)
        layout.addWidget(form_frame)
        
        # Connect Enter key to login
        self.username_input.returnPressed.connect(self.login)
        self.password_input.returnPressed.connect(self.login)
    
    def create_buttons(self, layout):
        """Create action buttons"""
        button_layout = QHBoxLayout()
        
        # Login button
        self.login_button = QPushButton("Đăng nhập")
        self.login_button.setFixedHeight(40)
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)
        self.login_button.clicked.connect(self.login)
        
        # Register button (for future implementation)
        self.register_button = QPushButton("Đăng ký")
        self.register_button.setFixedHeight(40)
        self.register_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #3498db;
                border: 1px solid #3498db;
                border-radius: 6px;
                font-size: 14px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #3498db;
                color: white;
            }
        """)
        self.register_button.clicked.connect(self.show_register_dialog)
        
        button_layout.addWidget(self.register_button)
        button_layout.addWidget(self.login_button)
        
        layout.addLayout(button_layout)
    
    def login(self):
        """Handle login attempt"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(
                self,
                "Thông tin không đầy đủ",
                "Vui lòng nhập tên đăng nhập và mật khẩu."
            )
            return
        
        # Disable login button during authentication
        self.login_button.setEnabled(False)
        self.login_button.setText("Đang đăng nhập...")
        
        try:
            # Authenticate user
            user_data = self.db_manager.authenticate_user(username, password)
            
            if user_data:
                # Successful login
                self.user_authenticated.emit(user_data)
            else:
                # Failed login
                QMessageBox.critical(
                    self,
                    "Đăng nhập thất bại",
                    "Tên đăng nhập hoặc mật khẩu không đúng."
                )
                self.password_input.clear()
                self.password_input.setFocus()
        
        except Exception as e:
            QMessageBox.critical(
                self,
                "Lỗi đăng nhập",
                f"Có lỗi xảy ra khi đăng nhập: {str(e)}"
            )
        
        finally:
            # Re-enable login button
            self.login_button.setEnabled(True)
            self.login_button.setText("Đăng nhập")
    
    def show_register_dialog(self):
        """Show registration dialog (placeholder)"""
        QMessageBox.information(
            self,
            "Đăng ký",
            "Tính năng đăng ký sẽ được triển khai trong phiên bản tới.\n\n"
            "Hiện tại, vui lòng sử dụng tài khoản admin/admin123 để trải nghiệm."
        )
