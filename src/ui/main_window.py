"""
Main Window
The primary application interface
"""

from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                              QMenuBar, QStatusBar, QTabWidget, QLabel,
                              QToolBar, QAction, QMessageBox, QSplitter)
from PySide6.QtCore import Qt, QTimer, Signal
from PySide6.QtGui import QIcon, QFont, QPixmap

from database.manager import DatabaseManager
from core.license_manager import LicenseManager


class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self, user, company_tax_code, db_manager, license_manager):
        super().__init__()
        
        self.user = user
        self.company_tax_code = company_tax_code
        self.db_manager = db_manager
        self.license_manager = license_manager
        
        # Load user license
        self.license_manager.load_user_license(self.user['id'])
        
        self.setup_ui()
        self.setup_menubar()
        self.setup_toolbar()
        self.setup_statusbar()
        
        # Load company data
        self.load_company_data()
    
    def setup_ui(self):
        """Setup main UI"""
        self.setWindowTitle(f"FinanTidy - {self.user['full_name']}")
        self.setMinimumSize(1200, 800)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        central_widget.setLayout(main_layout)
        
        # Create main content area
        self.create_main_content(main_layout)
    
    def create_main_content(self, layout):
        """Create main content area"""
        # Main splitter
        splitter = QSplitter(Qt.Horizontal)
        
        # Left panel (navigation/summary)
        self.create_left_panel(splitter)
        
        # Right panel (main content)
        self.create_right_panel(splitter)
        
        # Set splitter proportions
        splitter.setSizes([300, 900])
        
        layout.addWidget(splitter)
    
    def create_left_panel(self, splitter):
        """Create left navigation panel"""
        left_widget = QWidget()
        left_widget.setMaximumWidth(300)
        left_widget.setStyleSheet("""
            QWidget {
                background-color: #34495e;
                color: white;
            }
        """)
        
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 0, 0)
        
        # Company info header
        self.create_company_header(left_layout)
        
        # Quick stats
        self.create_quick_stats(left_layout)
        
        # Navigation menu (placeholder)
        nav_label = QLabel("Dashboard")
        nav_label.setStyleSheet("""
            QLabel {
                background-color: #3498db;
                padding: 15px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        left_layout.addWidget(nav_label)
        
        left_layout.addStretch()
        
        left_widget.setLayout(left_layout)
        splitter.addWidget(left_widget)
    
    def create_company_header(self, layout):
        """Create company info header"""
        header_widget = QWidget()
        header_widget.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                padding: 20px;
            }
        """)
        
        header_layout = QVBoxLayout()
        
        # Company name
        self.company_name_label = QLabel("Đang tải...")
        company_font = QFont()
        company_font.setPointSize(14)
        company_font.setBold(True)
        self.company_name_label.setFont(company_font)
        self.company_name_label.setStyleSheet("color: white;")
        
        # Tax code
        self.tax_code_label = QLabel(f"MST: {self.company_tax_code}")
        self.tax_code_label.setStyleSheet("color: #bdc3c7; font-size: 12px;")
        
        header_layout.addWidget(self.company_name_label)
        header_layout.addWidget(self.tax_code_label)
        
        header_widget.setLayout(header_layout)
        layout.addWidget(header_widget)
    
    def create_quick_stats(self, layout):
        """Create quick statistics panel"""
        stats_widget = QWidget()
        stats_widget.setStyleSheet("""
            QWidget {
                background-color: #34495e;
                padding: 20px;
            }
        """)
        
        stats_layout = QVBoxLayout()
        
        # Title
        title_label = QLabel("Tổng quan tháng này")
        title_font = QFont()
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: #ecf0f1; margin-bottom: 15px;")
        
        stats_layout.addWidget(title_label)
        
        # Stats items (placeholder)
        stats_items = [
            ("Hóa đơn", "0"),
            ("Tổng chi", "0 VNĐ"),
            ("VAT", "0 VNĐ")
        ]
        
        for label, value in stats_items:
            item_widget = self.create_stat_item(label, value)
            stats_layout.addWidget(item_widget)
        
        stats_widget.setLayout(stats_layout)
        layout.addWidget(stats_widget)
    
    def create_stat_item(self, label, value):
        """Create individual stat item"""
        item_widget = QWidget()
        item_layout = QVBoxLayout()
        item_layout.setContentsMargins(0, 5, 0, 5)
        
        value_label = QLabel(value)
        value_font = QFont()
        value_font.setPointSize(16)
        value_font.setBold(True)
        value_label.setFont(value_font)
        value_label.setStyleSheet("color: #3498db;")
        
        label_label = QLabel(label)
        label_label.setStyleSheet("color: #bdc3c7; font-size: 12px;")
        
        item_layout.addWidget(value_label)
        item_layout.addWidget(label_label)
        
        item_widget.setLayout(item_layout)
        return item_widget
    
    def create_right_panel(self, splitter):
        """Create right content panel"""
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(20, 20, 20, 20)
        
        # Welcome message
        welcome_label = QLabel(f"Xin chào {self.user['full_name']}!")
        welcome_font = QFont()
        welcome_font.setPointSize(18)
        welcome_font.setBold(True)
        welcome_label.setFont(welcome_font)
        welcome_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        
        # License info
        license_type = self.license_manager.get_license_type()
        license_label = QLabel(f"Gói hiện tại: {license_type.upper()}")
        license_label.setStyleSheet("color: #7f8c8d; font-size: 14px; margin-bottom: 30px;")
        
        # Placeholder content
        content_label = QLabel(
            "Dashboard sẽ được triển khai trong tuần 4-5.\n\n"
            "Hiện tại bạn đã đăng nhập thành công vào hệ thống!\n\n"
            "Các tính năng sẽ được phát triển theo lộ trình 8 tuần như đã lên kế hoạch."
        )
        content_label.setWordWrap(True)
        content_label.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 30px;
                font-size: 14px;
                color: #495057;
            }
        """)
        
        right_layout.addWidget(welcome_label)
        right_layout.addWidget(license_label)
        right_layout.addWidget(content_label)
        right_layout.addStretch()
        
        right_widget.setLayout(right_layout)
        splitter.addWidget(right_widget)
    
    def setup_menubar(self):
        """Setup menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("Tệp")
        
        # Company menu
        company_menu = menubar.addMenu("Công ty")
        
        # Tools menu
        tools_menu = menubar.addMenu("Công cụ")
        
        # Help menu
        help_menu = menubar.addMenu("Trợ giúp")
        
        # Add about action
        about_action = QAction("Về FinanTidy", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
    
    def setup_toolbar(self):
        """Setup toolbar"""
        toolbar = QToolBar("Main Toolbar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        # Add some placeholder actions
        refresh_action = QAction("Làm mới", self)
        refresh_action.triggered.connect(self.refresh_data)
        toolbar.addAction(refresh_action)
        
        toolbar.addSeparator()
        
        settings_action = QAction("Cài đặt", self)
        settings_action.triggered.connect(self.show_settings)
        toolbar.addAction(settings_action)
    
    def setup_statusbar(self):
        """Setup status bar"""
        statusbar = self.statusBar()
        
        # Connection status
        self.connection_label = QLabel("Đã kết nối")
        self.connection_label.setStyleSheet("color: green;")
        statusbar.addPermanentWidget(self.connection_label)
        
        # License status
        license_type = self.license_manager.get_license_type()
        self.license_status_label = QLabel(f"Gói {license_type.upper()}")
        statusbar.addPermanentWidget(self.license_status_label)
    
    def load_company_data(self):
        """Load company data"""
        try:
            # This is a placeholder - actual implementation in later weeks
            self.company_name_label.setText("Công ty Demo")
            
        except Exception as e:
            QMessageBox.warning(
                self,
                "Lỗi tải dữ liệu",
                f"Không thể tải dữ liệu công ty: {str(e)}"
            )
    
    def refresh_data(self):
        """Refresh all data"""
        self.statusBar().showMessage("Đang làm mới dữ liệu...", 2000)
        # Placeholder for actual refresh implementation
    
    def show_settings(self):
        """Show settings dialog"""
        QMessageBox.information(
            self,
            "Cài đặt",
            "Cửa sổ cài đặt sẽ được triển khai trong tuần 7."
        )
    
    def show_about(self):
        """Show about dialog"""
        QMessageBox.about(
            self,
            "Về FinanTidy",
            "FinanTidy v1.0.0\n"
            "Project Sodalite\n\n"
            "Quản lý hóa đơn và tài chính thông minh\n"
            "Dành cho doanh nghiệp siêu nhỏ Việt Nam\n\n"
            "© 2025 Sodalite Development"
        )
