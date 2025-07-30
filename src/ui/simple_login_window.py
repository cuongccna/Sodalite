"""
FinanTidy - Simple Login Window
Giao diện đăng nhập đơn giản, rõ ràng với textbox có thể nhìn thấy
"""

from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QFormLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QCheckBox, QMessageBox, QFrame,
    QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Signal, Qt, QSize
from PySide6.QtGui import QFont, QIcon, QPalette, QPixmap

from database.manager import DatabaseManager


class SimpleLoginWindow(QDialog):
    """Giao diện đăng nhập đơn giản với textbox rõ ràng"""
    
    user_authenticated = Signal(dict)
    
    def __init__(self, db_manager: DatabaseManager):
        super().__init__()
        self.db_manager = db_manager
        self.setup_ui()
        self.setup_styling()
    
    def setup_ui(self):
        """Thiết lập giao diện người dùng"""
        # Cấu hình cửa sổ
        self.setWindowTitle("FinanTidy - Đăng nhập")
        self.setFixedSize(420, 480)
        self.setModal(True)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        
        # Layout chính
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(30, 30, 30, 30)
        self.main_layout.setSpacing(25)
        
        # Tạo các phần giao diện
        self.create_header()
        self.create_login_form()
        self.create_buttons()
        
    def create_header(self):
        """Tạo phần header với logo và tiêu đề"""
        header_layout = QVBoxLayout()
        header_layout.setSpacing(8)
        
        # Logo
        self.logo_label = QLabel("💼")
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setObjectName("logo")
        
        # Tiêu đề ứng dụng
        self.title_label = QLabel("FinanTidy")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setObjectName("title")
        
        # Mô tả
        self.subtitle_label = QLabel("Quản lý tài chính thông minh")
        self.subtitle_label.setAlignment(Qt.AlignCenter)
        self.subtitle_label.setObjectName("subtitle")
        
        header_layout.addWidget(self.logo_label)
        header_layout.addWidget(self.title_label)
        header_layout.addWidget(self.subtitle_label)
        
        self.main_layout.addLayout(header_layout)
    
    def create_login_form(self):
        """Tạo form đăng nhập đơn giản và rõ ràng"""
        # Container cho form
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
        
        # Trường tên đăng nhập
        username_label = QLabel("Tên đăng nhập:")
        username_label.setObjectName("fieldLabel")
        self.username_input = QLineEdit()
        self.username_input.setObjectName("textInput")
        self.username_input.setText("demo")
        self.username_input.setPlaceholderText("Nhập tên đăng nhập của bạn")
        self.username_input.setMinimumHeight(42)
        
        # Trường mật khẩu
        password_label = QLabel("Mật khẩu:")
        password_label.setObjectName("fieldLabel")
        self.password_input = QLineEdit()
        self.password_input.setObjectName("textInput")
        self.password_input.setText("demo")
        self.password_input.setPlaceholderText("Nhập mật khẩu của bạn")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(42)
        
        # Checkbox hiển thị mật khẩu
        self.show_password_checkbox = QCheckBox("Hiển thị mật khẩu")
        self.show_password_checkbox.setObjectName("checkbox")
        self.show_password_checkbox.toggled.connect(self.toggle_password_visibility)
        
        # Thêm vào layout
        form_layout.addWidget(username_label)
        form_layout.addWidget(self.username_input)
        form_layout.addSpacing(5)
        form_layout.addWidget(password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addSpacing(5)
        form_layout.addWidget(self.show_password_checkbox)
        
        self.main_layout.addWidget(form_frame)
    
    def create_buttons(self):
        """Tạo các nút hành động"""
        button_layout = QVBoxLayout()
        button_layout.setSpacing(12)
        
        # Nút đăng nhập
        self.login_button = QPushButton("Đăng nhập")
        self.login_button.setObjectName("loginButton")
        self.login_button.setMinimumHeight(45)
        self.login_button.setCursor(Qt.PointingHandCursor)
        self.login_button.clicked.connect(self.login)
        
        # Nút đăng ký
        register_button = QPushButton("Đăng ký tài khoản mới")
        register_button.setObjectName("registerButton")
        register_button.setMinimumHeight(40)
        register_button.setCursor(Qt.PointingHandCursor)
        register_button.clicked.connect(self.show_register_dialog)
        
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(register_button)
        
        # Thêm spacer để đẩy nút xuống dưới
        self.main_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.main_layout.addLayout(button_layout)
        
        # Kết nối phím Enter
        self.username_input.returnPressed.connect(self.login)
        self.password_input.returnPressed.connect(self.login)
    
    def setup_styling(self):
        """Thiết lập style đơn giản và rõ ràng"""
        self.setStyleSheet("""
            /* Nền chính của dialog */
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
            
            /* Tiêu đề chính */
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
            
            /* Ô nhập liệu - QUAN TRỌNG: Màu nền trắng, viền rõ ràng */
            QLineEdit#textInput {
                font-size: 14px;
                padding: 12px 16px;
                border: 2px solid #cbd5e1;
                border-radius: 8px;
                background-color: #ffffff;  /* Nền trắng rõ ràng */
                color: #1f2937;            /* Chữ đen rõ ràng */
                selection-background-color: #3b82f6;
                selection-color: white;
            }
            
            QLineEdit#textInput:focus {
                border-color: #3b82f6;
                background-color: #ffffff;  /* Giữ nền trắng khi focus */
                outline: none;
            }
            
            QLineEdit#textInput:hover {
                border-color: #94a3b8;
                background-color: #ffffff;  /* Giữ nền trắng khi hover */
            }
            
            /* Placeholder text rõ ràng */
            QLineEdit#textInput::placeholder {
                color: #94a3b8;
                font-style: italic;
                font-weight: normal;
            }
            
            /* Checkbox */
            QCheckBox#checkbox {
                font-size: 13px;
                color: #6b7280;
                padding: 3px 0;
                spacing: 6px;
            }
            
            QCheckBox#checkbox::indicator {
                width: 16px;
                height: 16px;
                border: 2px solid #cbd5e1;
                border-radius: 3px;
                background-color: white;
            }
            
            QCheckBox#checkbox::indicator:checked {
                background-color: #3b82f6;
                border-color: #3b82f6;
            }
            
            QCheckBox#checkbox::indicator:hover {
                border-color: #94a3b8;
            }
            
            /* Nút đăng nhập chính */
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
            
            QPushButton#loginButton:pressed {
                background-color: #1d4ed8;
            }
            
            /* Nút đăng ký phụ */
            QPushButton#registerButton {
                background-color: transparent;
                color: #6b7280;
                font-size: 13px;
                font-weight: 500;
                border: 2px solid #d1d5db;
                border-radius: 8px;
                padding: 10px 20px;
            }
            
            QPushButton#registerButton:hover {
                background-color: #f9fafb;
                color: #374151;
                border-color: #9ca3af;
            }
            
            QPushButton#registerButton:pressed {
                background-color: #f3f4f6;
            }
        """)
    
    def toggle_password_visibility(self, checked):
        """Chuyển đổi hiển thị mật khẩu"""
        if checked:
            self.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
    
    def login(self):
        """Xử lý đăng nhập"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        # Kiểm tra input
        if not username or not password:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin đăng nhập.")
            return
        
        # Thử đăng nhập
        try:
            user_data = self.db_manager.authenticate_user(username, password)
            
            if user_data:
                QMessageBox.information(self, "Thành công", f"Chào mừng {user_data.get('username', username)}!")
                self.user_authenticated.emit(user_data)
                self.accept()
            else:
                # Demo mode - cho phép đăng nhập với bất kỳ thông tin nào
                demo_user = {
                    'id': 1,
                    'username': username,
                    'role': 'user',
                    'company_id': 1
                }
                QMessageBox.information(self, "Demo Mode", f"Đăng nhập thành công (Demo)\nChào mừng {username}!")
                self.user_authenticated.emit(demo_user)
                self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi kết nối: {str(e)}")
    
    def show_register_dialog(self):
        """Hiển thị dialog đăng ký"""
        QMessageBox.information(self, "Đăng ký", "Tính năng đăng ký sẽ được phát triển trong phiên bản tiếp theo.")
