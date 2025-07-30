"""
Main Window
The primary application interface
"""

from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                              QMenuBar, QStatusBar, QTabWidget, QLabel,
                              QToolBar, QMessageBox, QSplitter, QTableWidget,
                              QTableWidgetItem, QHeaderView, QPushButton,
                              QFrame, QGridLayout, QProgressBar, QComboBox)
from PySide6.QtCore import Qt, QTimer, Signal, QThread
from PySide6.QtGui import QIcon, QFont, QPixmap, QAction, QPalette

from database.manager import DatabaseManager
from core.license_manager import LicenseManager
from providers import ProviderFactory, ProviderType, list_available_providers


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
        
        # Initialize provider system
        self.available_providers = list_available_providers()
        self.active_providers = []
        
        # Initialize data refresh timer
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.auto_refresh_data)
        self.refresh_timer.start(300000)  # Refresh every 5 minutes
        
        # Sample data for dashboard (will be replaced with real data)
        self.dashboard_data = {
            'invoices_this_month': 0,
            'total_amount_this_month': 0,
            'vat_amount_this_month': 0,
            'recent_invoices': [],
            'monthly_trends': [],
            'provider_status': {}
        }
        
        self.setup_ui()
        self.setup_menubar()
        self.setup_toolbar()
        self.setup_statusbar()
        
        # Load company data
        self.load_company_data()
        
        # Initialize dashboard data
        self.load_dashboard_data()
        self.load_invoices_data()
    
    def setup_ui(self):
        """Setup main UI với modern design system"""
        self.setWindowTitle(f"FinanTidy - {self.user['username']}")
        self.setMinimumSize(1400, 900)
        
        # Modern app-wide stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8fafc;
                font-family: 'Inter', 'Segoe UI', 'SF Pro Display', system-ui, sans-serif;
            }
            QWidget {
                font-family: 'Inter', 'Segoe UI', 'SF Pro Display', system-ui, sans-serif;
                color: #1e293b;
            }
            QTabWidget::pane {
                border: 1px solid #e2e8f0;
                border-radius: 16px;
                background-color: white;
                padding: 0px;
            }
            QTabBar::tab {
                background-color: #f1f5f9;
                border: 1px solid #e2e8f0;
                padding: 14px 28px;
                margin-right: 4px;
                margin-bottom: 2px;
                border-radius: 12px 12px 0 0;
                color: #64748b;
                font-weight: 600;
                font-size: 14px;
                min-width: 100px;
            }
            QTabBar::tab:selected {
                background-color: #3b82f6;
                color: white;
                border-bottom: 2px solid #3b82f6;
                font-weight: 700;
            }
            QTabBar::tab:hover:!selected {
                background-color: #e2e8f0;
                color: #475569;
            }
        """)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout với modern spacing
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(20)
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
        """Create modern sidebar với clean design"""
        left_widget = QWidget()
        left_widget.setFixedWidth(320)
        left_widget.setStyleSheet("""
            QWidget {
                background-color: white;
                border-radius: 16px;
                border: 1px solid #e2e8f0;
            }
        """)
        
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(24, 24, 24, 24)
        left_layout.setSpacing(24)
        
        # Company info header
        self.create_company_header(left_layout)
        
        # Quick stats
        self.create_quick_stats(left_layout)
        
        # Navigation menu
        self.create_navigation_menu(left_layout)
        
        left_layout.addStretch()
        
        left_widget.setLayout(left_layout)
        splitter.addWidget(left_widget)
    
    def create_navigation_menu(self, layout):
        """Tạo modern navigation menu"""
        nav_widget = QWidget()
        nav_layout = QVBoxLayout()
        nav_layout.setSpacing(8)
        
        # Navigation title
        nav_title = QLabel("NAVIGATION")
        nav_title.setStyleSheet("""
            color: #64748b;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1px;
            padding: 0px 12px 8px 12px;
            text-transform: uppercase;
        """)
        nav_layout.addWidget(nav_title)
        
        # Menu items với modern design
        menu_items = [
            ("🏠", "Dashboard", True),
            ("📄", "Invoices", False),
            ("🔌", "Providers", False),
            ("�", "Analytics", False),
            ("⚙️", "Settings", False)
        ]
        
        for icon, text, is_active in menu_items:
            nav_item = self.create_nav_item(icon, text, is_active)
            nav_layout.addWidget(nav_item)
        
        nav_widget.setLayout(nav_layout)
        layout.addWidget(nav_widget)
    
    def create_nav_item(self, icon, text, is_active=False):
        """Tạo modern nav item"""
        nav_item = QPushButton(f"{icon}  {text}")
        nav_item.setStyleSheet(f"""
            QPushButton {{
                text-align: left;
                padding: 12px 16px;
                border: none;
                border-radius: 12px;
                color: {'#3b82f6' if is_active else '#64748b'};
                background-color: {'#eff6ff' if is_active else 'transparent'};
                font-size: 14px;
                font-weight: {'600' if is_active else '500'};
            }}
            QPushButton:hover {{
                background-color: {'#dbeafe' if is_active else '#f1f5f9'};
                color: {'#2563eb' if is_active else '#475569'};
            }}
            QPushButton:pressed {{
                background-color: #bfdbfe;
                color: #1d4ed8;
            }}
        """)
        return nav_item
    
    def create_company_header(self, layout):
        """Create modern company header với clean styling"""
        header_widget = QWidget()
        header_widget.setStyleSheet("""
            QWidget {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 24px;
                border-radius: 16px;
                border: none;
            }
        """)
        
        header_layout = QVBoxLayout()
        header_layout.setSpacing(12)
        
        # Company icon
        company_icon = QLabel("🏢")
        company_icon.setAlignment(Qt.AlignCenter)
        company_icon.setStyleSheet("""
            font-size: 32px; 
            background: rgba(255, 255, 255, 0.2);
            border-radius: 16px;
            padding: 12px;
            margin-bottom: 8px;
        """)
        header_layout.addWidget(company_icon)
        
        # Company name
        self.company_name_label = QLabel("Demo Company")
        self.company_name_label.setAlignment(Qt.AlignCenter)
        self.company_name_label.setFont(QFont("Inter", 16, QFont.Bold))
        self.company_name_label.setStyleSheet("""
            color: white;
            background-color: transparent;
            margin: 0px;
            padding: 0px;
        """)
        
        # Tax code
        self.tax_code_label = QLabel(f"MST: {self.company_tax_code}")
        self.tax_code_label.setAlignment(Qt.AlignCenter)
        self.tax_code_label.setStyleSheet("""
            color: rgba(255, 255, 255, 0.8);
            font-size: 13px;
            font-weight: 500;
            background-color: transparent;
            margin: 0px;
            padding: 0px;
        """)
        
        header_layout.addWidget(self.company_name_label)
        header_layout.addWidget(self.tax_code_label)
        
        header_widget.setLayout(header_layout)
        layout.addWidget(header_widget)
    
    def create_quick_stats(self, layout):
        """Create modern statistics cards"""
        stats_widget = QWidget()
        stats_widget.setStyleSheet("""
            QWidget {
                background-color: #f8fafc;
                padding: 20px;
                border-radius: 16px;
                border: 1px solid #e2e8f0;
            }
        """)
        
        stats_layout = QVBoxLayout()
        stats_layout.setSpacing(16)
        
        # Stats title
        title_layout = QHBoxLayout()
        title_text = QLabel("Monthly Overview")
        title_text.setFont(QFont("Inter", 14, QFont.Bold))
        title_text.setStyleSheet("color: #1e293b; margin: 0px;")
        
        title_layout.addWidget(title_text)
        title_layout.addStretch()
        stats_layout.addLayout(title_layout)
        
        # Stats grid
        stats_container = QVBoxLayout()
        stats_container.setSpacing(12)
        
        # Stats items với modern design
        stats_items = [
            ("📄", "Invoices", "0", "#3b82f6"),
            ("💰", "Revenue", "0 VND", "#10b981"),
            ("🧾", "VAT", "0 VND", "#f59e0b")
        ]
        
        for icon, label, value, color in stats_items:
            item_widget = self.create_stat_item(icon, label, value, color)
            stats_container.addWidget(item_widget)
        
        stats_layout.addLayout(stats_container)
        stats_widget.setLayout(stats_layout)
        layout.addWidget(stats_widget)
    
    def create_stat_item(self, icon, label, value, color):
        """Create modern stat card"""
        item_widget = QWidget()
        item_widget.setStyleSheet(f"""
            QWidget {{
                background-color: white;
                border-radius: 12px;
                padding: 16px;
                border: 1px solid #e2e8f0;
            }}
            QWidget:hover {{
                border-color: {color};
                background-color: #fafbfc;
            }}
        """)
        
        item_layout = QHBoxLayout()
        item_layout.setContentsMargins(0, 0, 0, 0)
        item_layout.setSpacing(12)
        
        # Icon container
        icon_container = QLabel(icon)
        icon_container.setStyleSheet(f"""
            font-size: 20px;
            background-color: {color}20;
            border-radius: 10px;
            padding: 8px;
            max-width: 40px;
            max-height: 40px;
        """)
        icon_container.setFixedSize(40, 40)
        icon_container.setAlignment(Qt.AlignCenter)
        
        # Content layout
        content_layout = QVBoxLayout()
        content_layout.setSpacing(2)
        content_layout.setContentsMargins(0, 0, 0, 0)
        
        value_label = QLabel(value)
        value_label.setFont(QFont("Inter", 16, QFont.Bold))
        value_label.setStyleSheet(f"color: {color}; margin: 0px;")
        
        label_label = QLabel(label)
        label_label.setStyleSheet("color: #64748b; font-size: 12px; font-weight: 500; margin: 0px;")
        
        content_layout.addWidget(value_label)
        content_layout.addWidget(label_label)
        
        item_layout.addWidget(icon_container)
        item_layout.addLayout(content_layout)
        item_layout.addStretch()
        
        item_widget.setLayout(item_layout)
        return item_widget
    
    def create_right_panel(self, splitter):
        """Create right content panel with real dashboard"""
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(20, 20, 20, 20)
        
        # Welcome header
        self.create_welcome_header(right_layout)
        
        # Create tabbed interface
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #dee2e6;
                border-radius: 8px;
                background-color: white;
            }
            QTabBar::tab {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                padding: 10px 20px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: #3498db;
                color: white;
            }
        """)
        
        # Dashboard tab
        self.create_dashboard_tab()
        
        # Invoices tab
        self.create_invoices_tab()
        
        # Providers tab
        self.create_providers_tab()
        
        # Analytics tab
        self.create_analytics_tab()
        
        right_layout.addWidget(self.tab_widget)
        
        right_widget.setLayout(right_layout)
        splitter.addWidget(right_widget)
    
    def create_invoices_tab(self):
        """Create invoices management tab"""
        invoices_widget = QWidget()
        invoices_layout = QVBoxLayout()
        invoices_layout.setContentsMargins(20, 20, 20, 20)
        
        # Header with controls
        header_layout = QHBoxLayout()
        
        invoices_title = QLabel("📧 Quản lý Hóa đơn")
        invoices_title.setStyleSheet("font-weight: bold; font-size: 16px;")
        
        # Filter controls
        filter_label = QLabel("Lọc theo:")
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Tất cả", "Tháng này", "Quý này", "Năm này"])
        
        add_invoice_btn = QPushButton("➕ Thêm hóa đơn")
        add_invoice_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        add_invoice_btn.clicked.connect(self.add_invoice)
        
        header_layout.addWidget(invoices_title)
        header_layout.addStretch()
        header_layout.addWidget(filter_label)
        header_layout.addWidget(self.filter_combo)
        header_layout.addWidget(add_invoice_btn)
        
        # Invoices table
        self.invoices_table = QTableWidget()
        self.invoices_table.setColumnCount(6)
        self.invoices_table.setHorizontalHeaderLabels([
            "Số HĐ", "Nhà cung cấp", "Ngày phát hành", "Subtotal", "VAT", "Tổng tiền"
        ])
        self.invoices_table.horizontalHeader().setStretchLastSection(True)
        self.invoices_table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #dee2e6;
                border-radius: 8px;
                background-color: white;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #f8f9fa;
            }
            QHeaderView::section {
                background-color: #f8f9fa;
                padding: 10px;
                border: none;
                font-weight: bold;
            }
        """)
        
        invoices_layout.addLayout(header_layout)
        invoices_layout.addWidget(self.invoices_table)
        
        invoices_widget.setLayout(invoices_layout)
        self.tab_widget.addTab(invoices_widget, "📧 Hóa đơn")
    
    def create_providers_tab(self):
        """Create providers management tab"""
        providers_widget = QWidget()
        providers_layout = QVBoxLayout()
        providers_layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        providers_title = QLabel("🔌 Quản lý Providers")
        providers_title.setStyleSheet("font-weight: bold; font-size: 16px; margin-bottom: 20px;")
        providers_layout.addWidget(providers_title)
        
        # Provider cards
        providers_grid = QGridLayout()
        providers_grid.setSpacing(15)
        
        for i, provider in enumerate(self.available_providers):
            card = self.create_provider_card(provider)
            row = i // 2
            col = i % 2
            providers_grid.addWidget(card, row, col)
        
        providers_container = QWidget()
        providers_container.setLayout(providers_grid)
        providers_layout.addWidget(providers_container)
        
        providers_layout.addStretch()
        providers_widget.setLayout(providers_layout)
        self.tab_widget.addTab(providers_widget, "🔌 Providers")
    
    def create_provider_card(self, provider):
        """Create individual provider card"""
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 20px;
            }
            QFrame:hover {
                border-color: #3498db;
            }
        """)
        
        layout = QVBoxLayout()
        
        # Provider header
        header_layout = QHBoxLayout()
        
        # Icon and name
        name_label = QLabel(f"🔌 {provider['type'].upper()}")
        name_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        
        # Status
        status_color = "#27ae60" if provider['supports_real_time'] else "#f39c12"
        status_text = "Hoạt động" if provider['supports_real_time'] else "Thủ công"
        status_label = QLabel(status_text)
        status_label.setStyleSheet(f"color: {status_color}; font-size: 12px; font-weight: bold;")
        
        header_layout.addWidget(name_label)
        header_layout.addStretch()
        header_layout.addWidget(status_label)
        
        # Description
        desc_text = f"Supports: {', '.join(provider['required_credentials']) or 'No credentials needed'}"
        desc_label = QLabel(desc_text)
        desc_label.setStyleSheet("color: #6c757d; font-size: 12px;")
        desc_label.setWordWrap(True)
        
        # Action buttons
        buttons_layout = QHBoxLayout()
        
        config_btn = QPushButton("🔧 Configure")
        config_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px 12px;
                border-radius: 4px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        config_btn.clicked.connect(lambda: self.configure_provider(provider['type']))
        
        test_btn = QPushButton("🧪 Test")
        test_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 8px 12px;
                border-radius: 4px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        test_btn.clicked.connect(lambda: self.test_provider(provider['type']))
        
        buttons_layout.addWidget(config_btn)
        buttons_layout.addWidget(test_btn)
        
        layout.addLayout(header_layout)
        layout.addWidget(desc_label)
        layout.addLayout(buttons_layout)
        
        card.setLayout(layout)
        return card
    
    def setup_menubar(self):
        """Setup menu bar"""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("Tệp")
        
        # Company menu
        company_menu = menubar.addMenu("Công ty")
        
        # Tools menu
        tools_menu = menubar.addMenu("Công cụ")
        
        # Add provider management
        provider_action = QAction("Quản lý Provider", self)
        provider_action.triggered.connect(self.show_provider_management)
        tools_menu.addAction(provider_action)
        
        tools_menu.addSeparator()
        
        # Add sync action
        sync_action = QAction("Đồng bộ hóa đơn", self)
        sync_action.triggered.connect(self.sync_invoices)
        tools_menu.addAction(sync_action)
        
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
        self.load_dashboard_data()
        self.update_dashboard_stats()
        self.load_recent_invoices()
        self.update_provider_status()
    
    def auto_refresh_data(self):
        """Auto refresh data every 5 minutes"""
        self.refresh_data()
    
    def create_welcome_header(self, layout):
        """Create welcome header section"""
        header_widget = QWidget()
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 20)
        
        # Welcome message
        welcome_label = QLabel(f"Xin chào {self.user['full_name']}!")
        welcome_font = QFont()
        welcome_font.setPointSize(18)
        welcome_font.setBold(True)
        welcome_label.setFont(welcome_font)
        welcome_label.setStyleSheet("color: #2c3e50;")
        
        # License info with upgrade option
        license_type = self.license_manager.get_license_type()
        license_info = QWidget()
        license_layout = QVBoxLayout()
        license_layout.setContentsMargins(0, 0, 0, 0)
        
        license_label = QLabel(f"Gói hiện tại: {license_type.upper()}")
        license_label.setStyleSheet("color: #7f8c8d; font-size: 14px;")
        
        if license_type == 'free':
            upgrade_btn = QPushButton("Nâng cấp Pro")
            upgrade_btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 5px 15px;
                    border-radius: 4px;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)
            upgrade_btn.clicked.connect(self.show_upgrade_dialog)
            
            license_layout.addWidget(license_label)
            license_layout.addWidget(upgrade_btn)
        else:
            license_layout.addWidget(license_label)
        
        license_info.setLayout(license_layout)
        
        header_layout.addWidget(welcome_label)
        header_layout.addStretch()
        header_layout.addWidget(license_info)
        
        header_widget.setLayout(header_layout)
        layout.addWidget(header_widget)
    
    def create_dashboard_tab(self):
        """Create main dashboard tab"""
        dashboard_widget = QWidget()
        dashboard_layout = QVBoxLayout()
        dashboard_layout.setContentsMargins(20, 20, 20, 20)
        
        # Stats cards row
        self.create_stats_cards(dashboard_layout)
        
        # Charts and recent activity
        content_splitter = QSplitter(Qt.Horizontal)
        
        # Left: Quick actions and recent invoices
        self.create_quick_actions_panel(content_splitter)
        
        # Right: Charts and analytics preview
        self.create_charts_panel(content_splitter)
        
        content_splitter.setSizes([400, 500])
        dashboard_layout.addWidget(content_splitter)
        
        dashboard_widget.setLayout(dashboard_layout)
        self.tab_widget.addTab(dashboard_widget, "📊 Dashboard")
    
    def create_stats_cards(self, layout):
        """Create stats cards row"""
        stats_frame = QFrame()
        stats_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        
        stats_layout = QHBoxLayout()
        
        # Stats data
        stats_data = [
            ("Hóa đơn tháng này", str(self.dashboard_data['invoices_this_month']), "#3498db", "📧"),
            ("Tổng chi phí", f"{self.dashboard_data['total_amount_this_month']:,.0f} VNĐ", "#e74c3c", "💰"),
            ("VAT", f"{self.dashboard_data['vat_amount_this_month']:,.0f} VNĐ", "#f39c12", "📋"),
            ("Providers", f"{len(self.available_providers)} kích hoạt", "#27ae60", "🔌")
        ]
        
        for title, value, color, icon in stats_data:
            card = self.create_stat_card(title, value, color, icon)
            stats_layout.addWidget(card)
        
        stats_frame.setLayout(stats_layout)
        layout.addWidget(stats_frame)
    
    def create_stat_card(self, title, value, color, icon):
        """Create individual stat card"""
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background-color: white;
                border: 1px solid #dee2e6;
                border-left: 4px solid {color};
                border-radius: 8px;
                padding: 15px;
                margin: 5px;
            }}
        """)
        
        card_layout = QVBoxLayout()
        
        # Header with icon
        header_layout = QHBoxLayout()
        icon_label = QLabel(icon)
        icon_label.setStyleSheet("font-size: 20px;")
        
        title_label = QLabel(title)
        title_label.setStyleSheet("color: #6c757d; font-size: 12px; font-weight: bold;")
        
        header_layout.addWidget(icon_label)
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        # Value
        value_label = QLabel(value)
        value_label.setStyleSheet(f"color: {color}; font-size: 18px; font-weight: bold; margin-top: 10px;")
        
        card_layout.addLayout(header_layout)
        card_layout.addWidget(value_label)
        card_layout.addStretch()
        
        card.setLayout(card_layout)
        return card
    
    def create_quick_actions_panel(self, splitter):
        """Create quick actions and recent invoices panel"""
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        
        # Quick actions
        actions_frame = QFrame()
        actions_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 15px;
            }
        """)
        
        actions_layout = QVBoxLayout()
        
        actions_title = QLabel("⚡ Thao tác nhanh")
        actions_title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 10px;")
        actions_layout.addWidget(actions_title)
        
        # Action buttons
        action_buttons = [
            ("🔄 Đồng bộ hóa đơn", self.sync_invoices),
            ("📊 Xem báo cáo", self.show_reports),
            ("🔧 Cấu hình Provider", self.show_provider_management),
            ("📈 Xuất dữ liệu", self.export_data)
        ]
        
        for text, callback in action_buttons:
            btn = QPushButton(text)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #f8f9fa;
                    border: 1px solid #dee2e6;
                    border-radius: 4px;
                    padding: 8px 12px;
                    text-align: left;
                    font-size: 12px;
                    margin-bottom: 5px;
                }
                QPushButton:hover {
                    background-color: #e9ecef;
                }
            """)
            btn.clicked.connect(callback)
            actions_layout.addWidget(btn)
        
        actions_layout.addStretch()
        actions_frame.setLayout(actions_layout)
        
        # Recent invoices
        recent_frame = QFrame()
        recent_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 15px;
            }
        """)
        
        recent_layout = QVBoxLayout()
        
        recent_title = QLabel("📋 Hóa đơn gần đây")
        recent_title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 10px;")
        recent_layout.addWidget(recent_title)
        
        # Recent invoices table
        self.recent_invoices_table = QTableWidget()
        self.recent_invoices_table.setColumnCount(3)
        self.recent_invoices_table.setHorizontalHeaderLabels(["Số HĐ", "Nhà cung cấp", "Số tiền"])
        self.recent_invoices_table.horizontalHeader().setStretchLastSection(True)
        self.recent_invoices_table.setMaximumHeight(200)
        self.recent_invoices_table.setStyleSheet("""
            QTableWidget {
                border: none;
                font-size: 12px;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #dee2e6;
            }
        """)
        
        recent_layout.addWidget(self.recent_invoices_table)
        recent_frame.setLayout(recent_layout)
        
        left_layout.addWidget(actions_frame)
        left_layout.addWidget(recent_frame)
        
        left_widget.setLayout(left_layout)
        splitter.addWidget(left_widget)
    
    def create_charts_panel(self, splitter):
        """Create charts and analytics panel"""
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        
        # Monthly trend chart placeholder
        chart_frame = QFrame()
        chart_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 15px;
            }
        """)
        
        chart_layout = QVBoxLayout()
        
        chart_title = QLabel("📈 Xu hướng chi phí 6 tháng qua")
        chart_title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 10px;")
        chart_layout.addWidget(chart_title)
        
        # Placeholder for chart
        chart_placeholder = QLabel("📊 Biểu đồ sẽ được tích hợp trong tuần 5-6\n\nSử dụng matplotlib hoặc QtCharts\nđể hiển thị xu hướng chi phí theo thời gian")
        chart_placeholder.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 2px dashed #dee2e6;
                border-radius: 8px;
                padding: 40px;
                text-align: center;
                color: #6c757d;
                font-size: 12px;
            }
        """)
        chart_placeholder.setAlignment(Qt.AlignCenter)
        chart_layout.addWidget(chart_placeholder)
        
        chart_frame.setLayout(chart_layout)
        
        # Provider status
        provider_frame = QFrame()
        provider_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 15px;
            }
        """)
        
        provider_layout = QVBoxLayout()
        
        provider_title = QLabel("🔌 Trạng thái Provider")
        provider_title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 10px;")
        provider_layout.addWidget(provider_title)
        
        # Provider status list
        self.provider_status_widget = QWidget()
        self.provider_status_layout = QVBoxLayout()
        self.provider_status_widget.setLayout(self.provider_status_layout)
        
        provider_layout.addWidget(self.provider_status_widget)
        provider_layout.addStretch()
        
        provider_frame.setLayout(provider_layout)
        
        right_layout.addWidget(chart_frame, 2)
        right_layout.addWidget(provider_frame, 1)
        
        right_widget.setLayout(right_layout)
        splitter.addWidget(right_widget)
    
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
    
    def show_provider_management(self):
        """Show provider management dialog"""
        provider_info = []
        for provider in self.available_providers:
            provider_info.append(
                f"📦 {provider['type'].upper()}\n"
                f"   🔑 Credentials: {', '.join(provider['required_credentials']) or 'None'}\n"
                f"   🌐 Real-time: {'Yes' if provider['supports_real_time'] else 'No'}"
            )
        
        message = (
            f"🔌 Available Providers ({len(self.available_providers)}):\n\n" +
            "\n\n".join(provider_info) +
            "\n\n💡 Provider configuration sẽ được triển khai trong tuần 4-5."
        )
        
        QMessageBox.information(
            self,
            "Quản lý Provider",
            message
        )
    
    def create_analytics_tab(self):
        """Create analytics and reports tab"""
        analytics_widget = QWidget()
        analytics_layout = QVBoxLayout()
        analytics_layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        analytics_title = QLabel("📊 Phân tích và Báo cáo")
        analytics_title.setStyleSheet("font-weight: bold; font-size: 16px; margin-bottom: 20px;")
        analytics_layout.addWidget(analytics_title)
        
        # License usage statistics
        usage_frame = QFrame()
        usage_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 20px;
            }
        """)
        
        usage_layout = QVBoxLayout()
        
        usage_title = QLabel("📈 Sử dụng gói license")
        usage_title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 15px;")
        usage_layout.addWidget(usage_title)
        
        # License usage statistics (demo data)
        stats = {'companies_count': 3, 'monthly_invoices': 27}
        license_type = 'free'
        limits = {'max_companies': 3, 'monthly_invoices': 50}
        
        # Companies usage
        companies_label = QLabel(f"Số công ty: {stats['companies_count']}/{limits['max_companies']}")
        companies_progress = QProgressBar()
        companies_progress.setMaximum(limits['max_companies'])
        companies_progress.setValue(stats['companies_count'])
        companies_progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                background-color: #ecf0f1;
            }
            QProgressBar::chunk {
                background-color: #3498db;
                border-radius: 3px;
            }
        """)
        
        # Invoices usage
        invoices_label = QLabel(f"Hóa đơn tháng này: {stats['monthly_invoices']}/{limits['monthly_invoices']}")
        invoices_progress = QProgressBar()
        invoices_progress.setMaximum(limits['monthly_invoices'])
        invoices_progress.setValue(min(stats['monthly_invoices'], limits['monthly_invoices']))
        invoices_progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                background-color: #ecf0f1;
            }
            QProgressBar::chunk {
                background-color: #27ae60;
                border-radius: 3px;
            }
        """)
        
        usage_layout.addWidget(companies_label)
        usage_layout.addWidget(companies_progress)
        usage_layout.addWidget(invoices_label)
        usage_layout.addWidget(invoices_progress)
        
        # Available features (simplified)
        features_label = QLabel("✨ Tính năng hiện tại:")
        features_label.setStyleSheet("font-weight: bold; margin-top: 15px; margin-bottom: 10px;")
        usage_layout.addWidget(features_label)
        
        if license_type == 'free':
            features_text = [
                "• Quản lý cơ bản:",
                "  - Tối đa 3 công ty",
                "  - 50 hóa đơn/tháng",
                "  - Báo cáo cơ bản",
                "  - Manual provider"
            ]
        else:
            features_text = [
                "• Tính năng Pro:",
                "  - Không giới hạn công ty",
                "  - Không giới hạn hóa đơn",
                "  - Báo cáo nâng cao",
                "  - Tất cả providers"
            ]
        
        features_display = QLabel("\n".join(features_text))
        features_display.setStyleSheet("color: #2c3e50; font-size: 12px; padding: 10px; background-color: #f8f9fa; border-radius: 4px;")
        features_display.setWordWrap(True)
        usage_layout.addWidget(features_display)
        
        # Upgrade recommendations (simplified)
        if license_type == 'free' and (stats['companies_count'] >= 2 or stats['monthly_invoices'] >= 40):
            upgrade_label = QLabel("💡 Khuyến nghị nâng cấp:")
            upgrade_label.setStyleSheet("font-weight: bold; color: #e67e22; margin-top: 15px; margin-bottom: 10px;")
            usage_layout.addWidget(upgrade_label)
            
            recommendations = [
                "Bạn đang sử dụng gần hết hạn mức gói Free",
                "Nâng cấp lên Pro để không giới hạn"
            ]
            
            for rec in recommendations:
                rec_label = QLabel(f"• {rec}")
                rec_label.setStyleSheet("color: #e67e22; font-size: 12px; margin-left: 10px;")
                rec_label.setWordWrap(True)
                usage_layout.addWidget(rec_label)
        
        usage_frame.setLayout(usage_layout)
        analytics_layout.addWidget(usage_frame)
        
        # Reports section
        reports_frame = QFrame()
        reports_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        
        reports_layout = QVBoxLayout()
        
        reports_title = QLabel("📋 Tạo báo cáo")
        reports_title.setStyleSheet("font-weight: bold; font-size: 14px; margin-bottom: 15px;")
        reports_layout.addWidget(reports_title)
        
        # Report buttons grid
        buttons_layout = QGridLayout()
        
        report_buttons = [
            ("📊 Báo cáo tháng", "Tạo báo cáo chi phí tháng hiện tại"),
            ("📈 Báo cáo quý", "Tạo báo cáo chi phí theo quý"),
            ("💰 Báo cáo VAT", "Tạo báo cáo thuế VAT"),
            ("🏢 Báo cáo nhà cung cấp", "Phân tích chi phí theo nhà cung cấp")
        ]
        
        for i, (title, description) in enumerate(report_buttons):
            btn = QPushButton(title)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 10px 15px;
                    border-radius: 6px;
                    font-weight: bold;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
            """)
            btn.clicked.connect(lambda checked, desc=description: self.generate_report(desc))
            
            row = i // 2
            col = i % 2
            buttons_layout.addWidget(btn, row, col)
        
        reports_layout.addLayout(buttons_layout)
        reports_frame.setLayout(reports_layout)
        analytics_layout.addWidget(reports_frame)
        
        analytics_layout.addStretch()
        analytics_widget.setLayout(analytics_layout)
        self.tab_widget.addTab(analytics_widget, "📊 Phân tích")
    
    def sync_invoices(self):
        """Sync invoices from providers"""
        QMessageBox.information(
            self,
            "Đồng bộ hóa đơn",
            "🔄 Chức năng đồng bộ hóa đơn tự động\n\n"
            "Sẽ kết nối với:\n"
            "• Viettel eInvoice API\n"
            "• MobiFone API (sắp có)\n"
            "• VNPT API (sắp có)\n\n"
            "Triển khai trong tuần 4-5."
        )
    
    def load_dashboard_data(self):
        """Load dashboard data"""
        # Load sample data for demonstration
        self.load_recent_invoices()
        self.update_dashboard_stats()
        self.update_provider_status()
    
    def update_dashboard_stats(self):
        """Update dashboard statistics"""
        # Update stats cards with sample data
        stats_data = [
            ("📧 Hóa đơn tháng này", "27", "#3498db"),
            ("💰 Tổng chi", "156.8M VNĐ", "#27ae60"),
            ("🧾 VAT", "15.7M VNĐ", "#f39c12"),
            ("🏢 Công ty", "3", "#9b59b6"),
            ("🔌 Providers", f"{len(self.available_providers)}", "#e74c3c"),
            ("📊 Báo cáo", "12", "#34495e")
        ]
        
        # Find and update stats cards
        for i, (label, value, color) in enumerate(stats_data):
            # This will update the display when we call refresh_data
            pass
    
    def load_recent_invoices(self):
        """Load recent invoices into the table"""
        # Sample data for demonstration
        sample_invoices = [
            ["HD001-2025", "Công ty TNHH ABC", "24,500,000 VNĐ"],
            ["HD002-2025", "Nhà cung cấp XYZ Ltd", "18,750,000 VNĐ"],
            ["HD003-2025", "Dịch vụ Marketing DEF", "12,300,000 VNĐ"],
            ["HD004-2025", "Văn phòng phẩm GHI", "3,200,000 VNĐ"],
            ["HD005-2025", "Công ty Logistics JKL", "45,800,000 VNĐ"]
        ]
        
        self.recent_invoices_table.setRowCount(len(sample_invoices))
        for row, invoice in enumerate(sample_invoices):
            for col, data in enumerate(invoice):
                item = QTableWidgetItem(data)
                item.setTextAlignment(Qt.AlignCenter)
                self.recent_invoices_table.setItem(row, col, item)
        
        # Auto-resize columns
        self.recent_invoices_table.resizeColumnsToContents()
    
    def load_invoices_data(self):
        """Load sample invoices data into invoices table"""
        sample_invoices = [
            ["HD001-2025", "Công ty TNHH ABC Technology", "15/07/2025", "22,000,000", "2,200,000", "24,200,000"],
            ["HD002-2025", "Nhà cung cấp XYZ Materials", "16/07/2025", "17,000,000", "1,700,000", "18,700,000"],
            ["HD003-2025", "Dịch vụ Marketing DEF", "18/07/2025", "11,000,000", "1,100,000", "12,100,000"],
            ["HD004-2025", "Văn phòng phẩm GHI Store", "20/07/2025", "2,900,000", "290,000", "3,190,000"],
            ["HD005-2025", "Công ty Logistics JKL", "22/07/2025", "41,600,000", "4,160,000", "45,760,000"],
            ["HD006-2025", "Dịch vụ IT Support MNO", "23/07/2025", "8,500,000", "850,000", "9,350,000"],
            ["HD007-2025", "Thuê văn phòng PQR", "25/07/2025", "15,000,000", "1,500,000", "16,500,000"],
            ["HD008-2025", "Quảng cáo Google Ads", "26/07/2025", "6,400,000", "640,000", "7,040,000"],
            ["HD009-2025", "Hosting & Domain STU", "27/07/2025", "1,800,000", "180,000", "1,980,000"],
            ["HD010-2025", "Bảo hiểm VWX Insurance", "28/07/2025", "12,700,000", "1,270,000", "13,970,000"]
        ]
        
        if hasattr(self, 'invoices_table'):
            self.invoices_table.setRowCount(len(sample_invoices))
            for row, invoice in enumerate(sample_invoices):
                for col, data in enumerate(invoice):
                    item = QTableWidgetItem(str(data))
                    if col >= 3:  # Money columns
                        item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                        if col >= 3 and col <= 5:  # Format money
                            try:
                                amount = int(data.replace(',', ''))
                                formatted = f"{amount:,} VNĐ"
                                item.setText(formatted)
                            except:
                                item.setText(f"{data} VNĐ")
                    else:
                        item.setTextAlignment(Qt.AlignCenter)
                    self.invoices_table.setItem(row, col, item)
            
            # Auto-resize columns
            self.invoices_table.resizeColumnsToContents()
    
    def update_provider_status(self):
        """Update provider status in the dashboard"""
        # Clear existing status
        for i in reversed(range(self.provider_status_layout.count())):
            child = self.provider_status_layout.itemAt(i).widget()
            if child:
                child.setParent(None)
        
        # Add provider status items
        for provider in self.available_providers:
            status_widget = QWidget()
            status_layout = QHBoxLayout()
            status_layout.setContentsMargins(5, 5, 5, 5)
            
            # Provider icon and name
            name_label = QLabel(f"🔌 {provider['type'].upper()}")
            name_label.setStyleSheet("font-weight: bold; font-size: 12px;")
            
            # Status indicator
            status_color = "#27ae60" if provider['supports_real_time'] else "#f39c12"
            status_text = "Hoạt động" if provider['supports_real_time'] else "Thủ công"
            status_label = QLabel(status_text)
            status_label.setStyleSheet(f"color: {status_color}; font-size: 11px;")
            
            status_layout.addWidget(name_label)
            status_layout.addStretch()
            status_layout.addWidget(status_label)
            
            status_widget.setLayout(status_layout)
            self.provider_status_layout.addWidget(status_widget)
    
    def show_upgrade_dialog(self):
        """Show license upgrade dialog"""
        current_type = self.license_manager.get_license_type()
        
        if current_type == 'free':
            next_tier = 'pro'
            price = "299,000 VNĐ/tháng"
            benefits = [
                "• Không giới hạn số công ty",
                "• Không giới hạn hóa đơn/tháng", 
                "• Xuất Excel/PDF",
                "• Báo cáo nâng cao",
                "• Hỗ trợ email"
            ]
        elif current_type == 'pro':
            next_tier = 'agency'
            price = "999,000 VNĐ/tháng"
            benefits = [
                "• Tất cả tính năng Pro",
                "• Quản lý đa công ty",
                "• API access",
                "• Custom reports",
                "• Hỗ trợ ưu tiên"
            ]
        else:
            QMessageBox.information(
                self,
                "Nâng cấp gói",
                "Bạn đang sử dụng gói cao nhất!"
            )
            return
        
        message = (
            f"🚀 Nâng cấp lên gói {next_tier.upper()}\n\n"
            f"💰 Giá: {price}\n\n"
            f"✨ Lợi ích:\n" + "\n".join(benefits) +
            "\n\n📞 Liên hệ: sales@sodalite.vn"
        )
        
        QMessageBox.information(
            self,
            f"Nâng cấp lên {next_tier.upper()}",
            message
        )
    
    def configure_provider(self, provider_type):
        """Configure a specific provider"""
        QMessageBox.information(
            self,
            f"Cấu hình {provider_type}",
            f"🔧 Cấu hình provider {provider_type}\n\n"
            "Sẽ cho phép nhập:\n"
            "• API credentials\n"
            "• Connection settings\n"
            "• Sync preferences\n\n"
            "Triển khai trong tuần 4-5."
        )
    
    def test_provider(self, provider_type):
        """Test provider connection"""
        QMessageBox.information(
            self,
            f"Test {provider_type}",
            f"🧪 Kiểm tra kết nối {provider_type}\n\n"
            "Sẽ test:\n"
            "• API connectivity\n"
            "• Authentication\n"
            "• Data access\n\n"
            "Triển khai trong tuần 4-5."
        )
    
    def add_invoice(self):
        """Add new invoice manually"""
        QMessageBox.information(
            self,
            "Thêm hóa đơn",
            "📝 Thêm hóa đơn thủ công\n\n"
            "Form sẽ bao gồm:\n"
            "• Thông tin nhà cung cấp\n"
            "• Chi tiết hóa đơn\n"
            "• Số tiền và VAT\n"
            "• File đính kèm\n\n"
            "Triển khai trong tuần 5-6."
        )
    
    def show_reports(self):
        """Show reports dialog"""
        QMessageBox.information(
            self,
            "Báo cáo",
            "📊 Hệ thống báo cáo\n\n"
            "Các loại báo cáo:\n"
            "• Báo cáo chi phí theo tháng/quý\n"
            "• Báo cáo VAT\n"
            "• Phân tích nhà cung cấp\n"
            "• Xu hướng chi tiêu\n\n"
            "Triển khai trong tuần 6-7."
        )
    
    def export_data(self):
        """Export data to various formats"""
        license_type = self.license_manager.get_license_type()
        available_formats = self.license_manager.get_export_formats(license_type)
        
        if not available_formats:
            QMessageBox.warning(
                self,
                "Xuất dữ liệu",
                "Gói hiện tại không hỗ trợ xuất dữ liệu.\n\n"
                "Vui lòng nâng cấp lên gói Pro để sử dụng tính năng này."
            )
            return
        
        formats_text = ", ".join(available_formats)
        QMessageBox.information(
            self,
            "Xuất dữ liệu",
            f"📤 Xuất dữ liệu\n\n"
            f"Định dạng hỗ trợ: {formats_text}\n\n"
            "Sẽ cho phép xuất:\n"
            "• Danh sách hóa đơn\n"
            "• Báo cáo tổng hợp\n"
            "• Dữ liệu thô\n\n"
            "Triển khai trong tuần 5-6."
        )
    
    def generate_report(self, report_type):
        """Generate specific report type"""
        QMessageBox.information(
            self,
            "Tạo báo cáo",
            f"📋 Tạo báo cáo: {report_type}\n\n"
            "Báo cáo sẽ bao gồm:\n"
            "• Biểu đồ và thống kê\n"
            "• Bảng dữ liệu chi tiết\n"
            "• Xuất PDF/Excel\n\n"
            "Triển khai trong tuần 6-7."
        )
