"""
Welcome Window
Introduces new users to FinanTidy's key features
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                              QPushButton, QFrame, QScrollArea, QWidget)
from PySide6.QtCore import Signal, Qt, QTimer
from PySide6.QtGui import QFont, QPixmap, QPainter, QColor


class WelcomeWindow(QDialog):
    """Welcome screen for first-time users"""
    
    welcome_completed = Signal()  # Emitted when user completes welcome flow
    
    def __init__(self):
        super().__init__()
        self.current_page = 0
        self.total_pages = 4
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the welcome UI"""
        self.setWindowTitle("Chào mừng đến với FinanTidy")
        self.setFixedSize(600, 500)
        self.setModal(True)
        
        # Main layout
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Header
        self.create_header(layout)
        
        # Content area
        self.create_content_area(layout)
        
        # Navigation
        self.create_navigation(layout)
        
        self.setLayout(layout)
        
        # Load first page
        self.show_page(0)
    
    def create_header(self, layout):
        """Create header with progress indicator"""
        header_frame = QFrame()
        header_frame.setFixedHeight(80)
        header_frame.setStyleSheet("""
            QFrame {
                background-color: #3498db;
                border: none;
            }
        """)
        
        header_layout = QVBoxLayout()
        header_layout.setContentsMargins(30, 20, 30, 20)
        
        # Title
        self.title_label = QLabel("Chào mừng đến với FinanTidy")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.title_label.setStyleSheet("color: white;")
        
        # Progress indicator
        self.progress_label = QLabel("Bước 1 / 4")
        self.progress_label.setStyleSheet("color: #ecf0f1; font-size: 12px;")
        
        header_layout.addWidget(self.title_label)
        header_layout.addWidget(self.progress_label)
        
        header_frame.setLayout(header_layout)
        layout.addWidget(header_frame)
    
    def create_content_area(self, layout):
        """Create scrollable content area"""
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setStyleSheet("border: none; background-color: white;")
        
        # Content widget
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(40, 30, 40, 30)
        self.content_layout.setSpacing(20)
        self.content_widget.setLayout(self.content_layout)
        
        scroll_area.setWidget(self.content_widget)
        layout.addWidget(scroll_area)
    
    def create_navigation(self, layout):
        """Create navigation buttons"""
        nav_frame = QFrame()
        nav_frame.setFixedHeight(70)
        nav_frame.setStyleSheet("""
            QFrame {
                background-color: #ecf0f1;
                border-top: 1px solid #bdc3c7;
            }
        """)
        
        nav_layout = QHBoxLayout()
        nav_layout.setContentsMargins(30, 15, 30, 15)
        
        # Back button
        self.back_button = QPushButton("Quay lại")
        self.back_button.setFixedHeight(40)
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #7f8c8d;
                border: 1px solid #bdc3c7;
                border-radius: 6px;
                font-size: 14px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #bdc3c7;
                color: #2c3e50;
            }
        """)
        self.back_button.clicked.connect(self.previous_page)
        
        # Skip button
        self.skip_button = QPushButton("Bỏ qua")
        self.skip_button.setFixedHeight(40)
        self.skip_button.setStyleSheet(self.back_button.styleSheet())
        self.skip_button.clicked.connect(self.skip_welcome)
        
        nav_layout.addWidget(self.back_button)
        nav_layout.addStretch()
        nav_layout.addWidget(self.skip_button)
        
        # Next/Finish button
        self.next_button = QPushButton("Tiếp theo")
        self.next_button.setFixedHeight(40)
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 30px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        self.next_button.clicked.connect(self.next_page)
        
        nav_layout.addWidget(self.next_button)
        
        nav_frame.setLayout(nav_layout)
        layout.addWidget(nav_frame)
    
    def clear_content(self):
        """Clear current content"""
        while self.content_layout.count():
            child = self.content_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def show_page(self, page_index):
        """Show specific page content"""
        self.current_page = page_index
        self.clear_content()
        
        # Update header
        self.progress_label.setText(f"Bước {page_index + 1} / {self.total_pages}")
        
        # Update navigation buttons
        self.back_button.setVisible(page_index > 0)
        if page_index == self.total_pages - 1:
            self.next_button.setText("Bắt đầu")
        else:
            self.next_button.setText("Tiếp theo")
        
        # Show page content
        if page_index == 0:
            self.show_intro_page()
        elif page_index == 1:
            self.show_security_page()
        elif page_index == 2:
            self.show_ai_page()
        elif page_index == 3:
            self.show_value_page()
    
    def show_intro_page(self):
        """Show introduction page"""
        # Welcome message
        welcome_label = QLabel("Chào mừng bạn đến với FinanTidy!")
        welcome_font = QFont()
        welcome_font.setPointSize(16)
        welcome_font.setBold(True)
        welcome_label.setFont(welcome_font)
        welcome_label.setStyleSheet("color: #2c3e50; margin-bottom: 10px;")
        
        # Description
        desc_label = QLabel(
            "FinanTidy là giải pháp quản lý hóa đơn và tài chính được thiết kế đặc biệt "
            "cho các doanh nghiệp siêu nhỏ, startups và văn phòng dịch vụ kế toán tại Việt Nam.\n\n"
            "Chúng tôi hiểu rằng bạn cần một công cụ đơn giản, an toàn và hiệu quả để quản lý "
            "tài chính mà không cần phải là chuyên gia kế toán."
        )
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("color: #34495e; font-size: 14px; line-height: 1.6;")
        
        self.content_layout.addWidget(welcome_label)
        self.content_layout.addWidget(desc_label)
        self.content_layout.addStretch()
    
    def show_security_page(self):
        """Show security feature page"""
        title = QLabel("🔒 An toàn & Tốc độ")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("color: #27ae60; margin-bottom: 15px;")
        
        features = [
            "Dữ liệu được lưu trữ hoàn toàn trên máy tính của bạn",
            "Không cần kết nối internet để sử dụng",
            "Tốc độ xử lý nhanh, không bị chậm do mạng",
            "Quyền riêng tư tuyệt đối - không ai có thể truy cập dữ liệu của bạn"
        ]
        
        for feature in features:
            feature_label = QLabel(f"✓ {feature}")
            feature_label.setWordWrap(True)
            feature_label.setStyleSheet("""
                color: #2c3e50; 
                font-size: 14px; 
                padding: 8px 0; 
                border-bottom: 1px solid #ecf0f1;
            """)
            self.content_layout.addWidget(feature_label)
        
        self.content_layout.addStretch()
    
    def show_ai_page(self):
        """Show AI features page"""
        title = QLabel("🤖 Trợ lý AI Thông minh")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("color: #8e44ad; margin-bottom: 15px;")
        
        features = [
            "Tự động phân loại chi phí dựa trên tên nhà cung cấp",
            "Cảnh báo thông minh về các bất thường trong tài chính",
            "Dự báo dòng tiền để giúp bạn lập kế hoạch tốt hơn",
            "Gợi ý tối ưu hóa chi phí dựa trên dữ liệu lịch sử"
        ]
        
        for feature in features:
            feature_label = QLabel(f"✨ {feature}")
            feature_label.setWordWrap(True)
            feature_label.setStyleSheet("""
                color: #2c3e50; 
                font-size: 14px; 
                padding: 8px 0; 
                border-bottom: 1px solid #ecf0f1;
            """)
            self.content_layout.addWidget(feature_label)
        
        self.content_layout.addStretch()
    
    def show_value_page(self):
        """Show value proposition page"""
        title = QLabel("💎 Giá trị Minh bạch")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setStyleSheet("color: #e67e22; margin-bottom: 15px;")
        
        packages = [
            ("Miễn phí", "100 hóa đơn/tháng, 1 công ty, xuất CSV"),
            ("Pro", "1,000 hóa đơn/tháng, 3 công ty, AI + Excel/PDF"),
            ("Agency", "Không giới hạn, nhiều người dùng, tính năng đại lý")
        ]
        
        for package_name, description in packages:
            package_frame = QFrame()
            package_frame.setStyleSheet("""
                QFrame {
                    border: 1px solid #bdc3c7;
                    border-radius: 8px;
                    background-color: #f8f9fa;
                    padding: 15px;
                    margin: 5px 0;
                }
            """)
            
            package_layout = QVBoxLayout()
            
            name_label = QLabel(package_name)
            name_font = QFont()
            name_font.setBold(True)
            name_label.setFont(name_font)
            name_label.setStyleSheet("color: #2c3e50; font-size: 14px;")
            
            desc_label = QLabel(description)
            desc_label.setStyleSheet("color: #7f8c8d; font-size: 12px;")
            desc_label.setWordWrap(True)
            
            package_layout.addWidget(name_label)
            package_layout.addWidget(desc_label)
            package_frame.setLayout(package_layout)
            
            self.content_layout.addWidget(package_frame)
        
        self.content_layout.addStretch()
    
    def next_page(self):
        """Go to next page or finish"""
        if self.current_page < self.total_pages - 1:
            self.show_page(self.current_page + 1)
        else:
            self.finish_welcome()
    
    def previous_page(self):
        """Go to previous page"""
        if self.current_page > 0:
            self.show_page(self.current_page - 1)
    
    def skip_welcome(self):
        """Skip welcome flow"""
        self.finish_welcome()
    
    def finish_welcome(self):
        """Complete welcome flow"""
        self.welcome_completed.emit()
        self.accept()
