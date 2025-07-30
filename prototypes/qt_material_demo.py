"""
FinanTidy - Qt Material Theme Demo
Modern Material Design with PySide6
"""

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

try:
    from qt_material import apply_stylesheet
    MATERIAL_AVAILABLE = True
except ImportError:
    MATERIAL_AVAILABLE = False
    print("Qt Material not installed. Install with: pip install qt-material")

class MaterialLoginWindow(QWidget):
    """Material Design Login Window"""
    
    user_authenticated = Signal(dict)
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        """Setup Material UI"""
        self.setWindowTitle("FinanTidy - Material Login")
        self.setFixedSize(450, 600)
        
        # Center window
        self.center_window()
        
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(40, 60, 40, 60)
        main_layout.setSpacing(30)
        
        # Logo section
        logo_layout = QVBoxLayout()
        logo_layout.setAlignment(Qt.AlignCenter)
        
        # App icon
        icon_label = QLabel("💰")
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet("""
            QLabel {
                font-size: 64px;
                background-color: rgba(33, 150, 243, 0.1);
                border-radius: 35px;
                padding: 20px;
                margin: 20px;
            }
        """)
        icon_label.setFixedSize(120, 120)
        logo_layout.addWidget(icon_label)
        
        # Title
        title = QLabel("FinanTidy")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                color: #1976D2;
                margin: 10px;
            }
        """)
        logo_layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Professional Financial Management")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #666;
                margin-bottom: 20px;
            }
        """)
        logo_layout.addWidget(subtitle)
        
        main_layout.addLayout(logo_layout)
        
        # Form section
        form_widget = QWidget()
        form_widget.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 0.95);
                border-radius: 15px;
                padding: 30px;
            }
        """)
        form_layout = QVBoxLayout(form_widget)
        form_layout.setSpacing(25)
        
        # Username field
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username or Email")
        self.username_input.setText("demo")
        self.username_input.setStyleSheet("""
            QLineEdit {
                padding: 15px;
                font-size: 16px;
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #2196F3;
            }
        """)
        form_layout.addWidget(self.username_input)
        
        # Password field
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setText("demo")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("""
            QLineEdit {
                padding: 15px;
                font-size: 16px;
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #2196F3;
            }
        """)
        form_layout.addWidget(self.password_input)
        
        # Login button
        self.login_button = QPushButton("SIGN IN")
        self.login_button.clicked.connect(self.login)
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
                border-radius: 8px;
                text-transform: uppercase;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #0D47A1;
            }
        """)
        form_layout.addWidget(self.login_button)
        
        main_layout.addWidget(form_widget)
        
        # Footer
        footer_layout = QHBoxLayout()
        footer_layout.setAlignment(Qt.AlignCenter)
        
        forgot_button = QPushButton("Forgot Password?")
        forgot_button.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                color: #2196F3;
                font-size: 14px;
                text-decoration: underline;
            }
            QPushButton:hover {
                color: #1976D2;
            }
        """)
        footer_layout.addWidget(forgot_button)
        
        main_layout.addLayout(footer_layout)
        
        # Connect Enter key
        self.username_input.returnPressed.connect(self.login)
        self.password_input.returnPressed.connect(self.login)
    
    def center_window(self):
        """Center window on screen"""
        screen = QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
    
    def login(self):
        """Handle login"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter both username and password!")
            return
        
        if username == "demo" and password == "demo":
            user_data = {"username": username, "id": 1}
            QMessageBox.information(self, "Success", f"Welcome {username}!")
            self.user_authenticated.emit(user_data)
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials!")

class MaterialMainWindow(QMainWindow):
    """Material Design Main Window"""
    
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        """Setup main window UI"""
        self.setWindowTitle("FinanTidy - Material Dashboard")
        self.setGeometry(100, 100, 1200, 800)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)
        
        # Main content area
        content_area = self.create_content_area()
        main_layout.addWidget(content_area)
    
    def create_sidebar(self):
        """Create material sidebar"""
        sidebar = QWidget()
        sidebar.setFixedWidth(280)
        sidebar.setStyleSheet("""
            QWidget {
                background-color: #1976D2;
                color: white;
            }
        """)
        
        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Header
        header = QWidget()
        header.setStyleSheet("background-color: #0D47A1; padding: 20px;")
        header_layout = QVBoxLayout(header)
        
        company_label = QLabel("🏢 Demo Company")
        company_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        header_layout.addWidget(company_label)
        
        user_label = QLabel("👤 Demo User")
        user_label.setStyleSheet("font-size: 14px; color: #BBDEFB;")
        header_layout.addWidget(user_label)
        
        layout.addWidget(header)
        
        # Navigation
        nav_items = [
            ("📊", "Dashboard"),
            ("📄", "Invoices"),
            ("🏪", "Providers"),
            ("📈", "Analytics"),
            ("⚙️", "Settings")
        ]
        
        for icon, text in nav_items:
            btn = QPushButton(f"{icon}  {text}")
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding: 15px 20px;
                    border: none;
                    font-size: 16px;
                    color: white;
                    background-color: transparent;
                }
                QPushButton:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                }
                QPushButton:pressed {
                    background-color: rgba(255, 255, 255, 0.2);
                }
            """)
            layout.addWidget(btn)
        
        layout.addStretch()
        
        # Logout button
        logout_btn = QPushButton("🚪 Logout")
        logout_btn.setStyleSheet("""
            QPushButton {
                text-align: left;
                padding: 15px 20px;
                border: none;
                font-size: 16px;
                color: #FFCDD2;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: rgba(244, 67, 54, 0.1);
                color: #F44336;
            }
        """)
        logout_btn.clicked.connect(self.logout)
        layout.addWidget(logout_btn)
        
        return sidebar
    
    def create_content_area(self):
        """Create main content area"""
        content = QWidget()
        content.setStyleSheet("background-color: #FAFAFA;")
        
        layout = QVBoxLayout(content)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        
        # Header
        header_layout = QHBoxLayout()
        
        title = QLabel("Dashboard")
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #333;")
        header_layout.addWidget(title)
        
        header_layout.addStretch()
        
        refresh_btn = QPushButton("🔄 Refresh")
        refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        header_layout.addWidget(refresh_btn)
        
        layout.addLayout(header_layout)
        
        # Stats cards
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(20)
        
        stats_data = [
            ("💰", "Revenue", "₫120,500,000", "#4CAF50"),
            ("📄", "Invoices", "245", "#2196F3"),
            ("🏪", "Providers", "18", "#FF9800"),
            ("📊", "Reports", "12", "#9C27B0")
        ]
        
        for icon, title, value, color in stats_data:
            card = self.create_stat_card(icon, title, value, color)
            stats_layout.addWidget(card)
        
        layout.addLayout(stats_layout)
        
        # Main content
        content_widget = QWidget()
        content_widget.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        
        content_layout = QVBoxLayout(content_widget)
        
        content_title = QLabel("Recent Activity")
        content_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #333; margin-bottom: 15px;")
        content_layout.addWidget(content_title)
        
        # Activity list
        activities = [
            "📄 New invoice from ABC Company - ₫5,200,000",
            "💰 Payment received from XYZ Corp - ₫8,500,000",
            "🏪 New provider added: Tech Solutions Ltd",
            "📊 Monthly report generated",
            "⚙️ System backup completed"
        ]
        
        for activity in activities:
            activity_widget = QWidget()
            activity_widget.setStyleSheet("""
                QWidget {
                    background-color: #F5F5F5;
                    border-radius: 5px;
                    padding: 10px;
                    margin: 5px 0;
                }
                QWidget:hover {
                    background-color: #E0E0E0;
                }
            """)
            
            activity_layout = QHBoxLayout(activity_widget)
            activity_label = QLabel(activity)
            activity_label.setStyleSheet("color: #333; font-size: 14px;")
            activity_layout.addWidget(activity_label)
            
            content_layout.addWidget(activity_widget)
        
        layout.addWidget(content_widget)
        
        return content
    
    def create_stat_card(self, icon, title, value, color):
        """Create statistics card"""
        card = QWidget()
        card.setStyleSheet(f"""
            QWidget {{
                background-color: white;
                border-radius: 10px;
                border-left: 5px solid {color};
                padding: 20px;
            }}
        """)
        
        layout = QVBoxLayout(card)
        layout.setAlignment(Qt.AlignCenter)
        
        # Icon
        icon_label = QLabel(icon)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setStyleSheet(f"font-size: 36px; color: {color}; margin-bottom: 10px;")
        layout.addWidget(icon_label)
        
        # Value
        value_label = QLabel(value)
        value_label.setAlignment(Qt.AlignCenter)
        value_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333; margin-bottom: 5px;")
        layout.addWidget(value_label)
        
        # Title
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 14px; color: #666;")
        layout.addWidget(title_label)
        
        return card
    
    def logout(self):
        """Handle logout"""
        reply = QMessageBox.question(
            self, 
            "Logout", 
            "Are you sure you want to logout?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.close()

def main():
    """Main application"""
    app = QApplication(sys.argv)
    
    # Apply material theme if available
    if MATERIAL_AVAILABLE:
        apply_stylesheet(app, theme='dark_blue.xml')
    
    # Create login window
    login_window = MaterialLoginWindow()
    
    def on_login(user_data):
        """Handle successful login"""
        login_window.close()
        main_window = MaterialMainWindow()
        main_window.show()
    
    login_window.user_authenticated.connect(on_login)
    login_window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
