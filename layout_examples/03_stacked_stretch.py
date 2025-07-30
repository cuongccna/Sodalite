"""
PySide6 StackedLayout & Stretch Examples
Ví dụ về StackedLayout và cách sử dụng Stretch, Alignment
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QMainWindow, QTabWidget,
    QStackedLayout, QStackedWidget, QComboBox
)
from PySide6.QtCore import Qt


class StackedLayoutExamples(QMainWindow):
    """Ví dụ về StackedLayout và Stretch/Alignment"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Layout Examples - StackedLayout & Stretch")
        self.setGeometry(100, 100, 800, 600)
        
        # Tab widget
        tab_widget = QTabWidget()
        
        # Tab 1: StackedLayout
        tab_widget.addTab(self.create_stacked_example(), "QStackedLayout")
        
        # Tab 2: Stretch & Alignment
        tab_widget.addTab(self.create_stretch_example(), "Stretch & Alignment")
        
        # Tab 3: Real App Example
        tab_widget.addTab(self.create_real_app_example(), "Real App Layout")
        
        self.setCentralWidget(tab_widget)
    
    def create_stacked_example(self):
        """Ví dụ QStackedLayout - stack nhiều widget"""
        widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("QStackedLayout - Stack nhiều widget (hiển thị 1 lúc 1 cái)")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #0078d7; margin: 10px;")
        main_layout.addWidget(title)
        
        # Combo để chọn page
        page_combo = QComboBox()
        page_combo.addItems(["Trang chủ", "Hồ sơ", "Cài đặt", "Giới thiệu"])
        page_combo.setStyleSheet("""
            QComboBox {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 6px;
                font-size: 14px;
                background-color: white;
                min-width: 200px;
            }
            QComboBox:focus {
                border-color: #0078d7;
            }
        """)
        main_layout.addWidget(page_combo)
        
        # Tạo Stacked Widget
        stacked_widget = QStackedWidget()
        
        # Page 1: Trang chủ
        home_page = QWidget()
        home_layout = QVBoxLayout()
        home_layout.addWidget(QLabel("🏠 TRANG CHỦ"))
        home_layout.addWidget(QLabel("Chào mừng bạn đến với ứng dụng!"))
        home_layout.addWidget(QPushButton("Bắt đầu sử dụng"))
        home_layout.addStretch()
        home_page.setLayout(home_layout)
        home_page.setStyleSheet("background-color: #e3f2fd; padding: 20px; border-radius: 8px;")
        
        # Page 2: Hồ sơ
        profile_page = QWidget()
        profile_layout = QVBoxLayout()
        profile_layout.addWidget(QLabel("👤 HỒ SƠ"))
        profile_layout.addWidget(QLabel("Tên: Nguyễn Văn A"))
        profile_layout.addWidget(QLabel("Email: nguyenvana@email.com"))
        profile_layout.addWidget(QPushButton("Chỉnh sửa hồ sơ"))
        profile_layout.addStretch()
        profile_page.setLayout(profile_layout)
        profile_page.setStyleSheet("background-color: #f3e5f5; padding: 20px; border-radius: 8px;")
        
        # Page 3: Cài đặt
        settings_page = QWidget()
        settings_layout = QVBoxLayout()
        settings_layout.addWidget(QLabel("⚙️ CÀI ĐẶT"))
        settings_layout.addWidget(QLabel("Chế độ tối: Tắt"))
        settings_layout.addWidget(QLabel("Ngôn ngữ: Tiếng Việt"))
        settings_layout.addWidget(QPushButton("Lưu cài đặt"))
        settings_layout.addStretch()
        settings_page.setLayout(settings_layout)
        settings_page.setStyleSheet("background-color: #e8f5e8; padding: 20px; border-radius: 8px;")
        
        # Page 4: Giới thiệu
        about_page = QWidget()
        about_layout = QVBoxLayout()
        about_layout.addWidget(QLabel("ℹ️ GIỚI THIỆU"))
        about_layout.addWidget(QLabel("Phiên bản: 1.0.0"))
        about_layout.addWidget(QLabel("Phát triển bởi: Your Team"))
        about_layout.addWidget(QPushButton("Xem chi tiết"))
        about_layout.addStretch()
        about_page.setLayout(about_layout)
        about_page.setStyleSheet("background-color: #fff3e0; padding: 20px; border-radius: 8px;")
        
        # Thêm các page vào stacked widget
        stacked_widget.addWidget(home_page)      # index 0
        stacked_widget.addWidget(profile_page)   # index 1
        stacked_widget.addWidget(settings_page)  # index 2
        stacked_widget.addWidget(about_page)     # index 3
        
        # Kết nối combo với stacked widget
        page_combo.currentIndexChanged.connect(stacked_widget.setCurrentIndex)
        
        main_layout.addWidget(stacked_widget)
        
        widget.setLayout(main_layout)
        return widget
    
    def create_stretch_example(self):
        """Ví dụ về Stretch và Alignment"""
        widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("Stretch & Alignment - Căn chỉnh và co giãn")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #0078d7; margin: 10px;")
        main_layout.addWidget(title)
        
        # Ví dụ 1: addStretch()
        section1 = QWidget()
        section1_layout = QVBoxLayout()
        
        section1_title = QLabel("1. addStretch() - Đẩy widget về đầu/cuối")
        section1_title.setStyleSheet("font-weight: bold; color: #333; margin: 5px;")
        section1_layout.addWidget(section1_title)
        
        btn1 = QPushButton("Nút đầu")
        btn1.setStyleSheet("padding: 8px; background-color: #e1f5fe; color: #1565c0; border: 1px solid #0078d7; border-radius: 4px; font-weight: bold;")
        section1_layout.addWidget(btn1)
        
        section1_layout.addStretch()  # Đẩy nút xuống dưới lên trên
        
        btn2 = QPushButton("Nút cuối")
        btn2.setStyleSheet("padding: 8px; background-color: #f3e5f5; color: #7b1fa2; border: 1px solid #9c27b0; border-radius: 4px; font-weight: bold;")
        section1_layout.addWidget(btn2)
        
        section1.setLayout(section1_layout)
        section1.setStyleSheet("border: 2px solid #ddd; border-radius: 8px; margin: 5px;")
        section1.setMaximumHeight(150)
        main_layout.addWidget(section1)
        
        # Ví dụ 2: Alignment
        section2 = QWidget()
        section2_layout = QVBoxLayout()
        
        section2_title = QLabel("2. Alignment - Căn chỉnh widget")
        section2_title.setStyleSheet("font-weight: bold; color: #333; margin: 5px;")
        section2_layout.addWidget(section2_title)
        
        # HBox với các alignment khác nhau
        align_layout = QHBoxLayout()
        
        left_btn = QPushButton("Left")
        left_btn.setStyleSheet("padding: 8px; background-color: #ffebee; color: #d32f2f; border: 1px solid #f44336; border-radius: 4px; font-weight: bold;")
        align_layout.addWidget(left_btn, alignment=Qt.AlignLeft)
        
        center_btn = QPushButton("Center")
        center_btn.setStyleSheet("padding: 8px; background-color: #e8f5e8; color: #2e7d32; border: 1px solid #4caf50; border-radius: 4px; font-weight: bold;")
        align_layout.addWidget(center_btn, alignment=Qt.AlignCenter)
        
        right_btn = QPushButton("Right")
        right_btn.setStyleSheet("padding: 8px; background-color: #fff3e0; color: #f57c00; border: 1px solid #ff9800; border-radius: 4px; font-weight: bold;")
        align_layout.addWidget(right_btn, alignment=Qt.AlignRight)
        
        section2_layout.addLayout(align_layout)
        
        section2.setLayout(section2_layout)
        section2.setStyleSheet("border: 2px solid #ddd; border-radius: 8px; margin: 5px;")
        section2.setMaximumHeight(100)
        main_layout.addWidget(section2)
        
        # Ví dụ 3: Kết hợp Stretch + Alignment (như login form)
        section3 = QWidget()
        section3_layout = QVBoxLayout()
        
        section3_title = QLabel("3. Kết hợp Stretch + Alignment (như Login Form)")
        section3_title.setStyleSheet("font-weight: bold; color: #333; margin: 5px;")
        section3_layout.addWidget(section3_title)
        
        # Wrapper layout với stretch (giống login form)
        wrapper = QVBoxLayout()
        wrapper.addStretch()  # Đẩy xuống
        
        # Inner content
        inner_layout = QVBoxLayout()
        inner_layout.setAlignment(Qt.AlignCenter)
        inner_layout.setSpacing(8)
        
        mini_title = QLabel("🔑 Mini Login")
        mini_title.setStyleSheet("font-size: 14px; font-weight: bold; text-align: center;")
        mini_title.setAlignment(Qt.AlignCenter)
        inner_layout.addWidget(mini_title)
        
        mini_input = QPushButton("Username Input")
        mini_input.setStyleSheet("padding: 6px; background-color: white; color: #333; border: 1px solid #ccc; border-radius: 4px; max-width: 150px;")
        inner_layout.addWidget(mini_input)
        
        mini_login = QPushButton("Login")
        mini_login.setStyleSheet("padding: 6px; background-color: #0078d7; color: white; border: none; border-radius: 4px; max-width: 150px;")
        inner_layout.addWidget(mini_login)
        
        wrapper.addLayout(inner_layout)
        wrapper.addStretch()  # Đẩy lên
        
        section3_layout.addLayout(wrapper)
        
        section3.setLayout(section3_layout)
        section3.setStyleSheet("border: 2px solid #ddd; border-radius: 8px; margin: 5px; background-color: #f9f9f9;")
        section3.setMaximumHeight(200)
        main_layout.addWidget(section3)
        
        main_layout.addStretch()
        
        widget.setLayout(main_layout)
        return widget
    
    def create_real_app_example(self):
        """Ví dụ layout thực tế của một ứng dụng"""
        widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Header
        header = QWidget()
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(15, 10, 15, 10)
        
        app_title = QLabel("📱 My App")
        app_title.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        header_layout.addWidget(app_title)
        
        header_layout.addStretch()
        
        user_btn = QPushButton("👤 User")
        user_btn.setStyleSheet("""
            QPushButton {
                padding: 6px 12px;
                background-color: rgba(255,255,255,0.2);
                color: white;
                border: 1px solid rgba(255,255,255,0.3);
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: rgba(255,255,255,0.3);
            }
        """)
        header_layout.addWidget(user_btn)
        
        header.setLayout(header_layout)
        header.setStyleSheet("background-color: #0078d7; border-bottom: 1px solid #005a9e;")
        header.setFixedHeight(50)
        main_layout.addWidget(header)
        
        # Content area
        content_layout = QHBoxLayout()
        
        # Sidebar
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(10, 15, 10, 15)
        
        nav_buttons = ["🏠 Home", "📊 Dashboard", "📁 Files", "⚙️ Settings"]
        for nav_text in nav_buttons:
            nav_btn = QPushButton(nav_text)
            nav_btn.setStyleSheet("""
                QPushButton {
                    padding: 12px;
                    text-align: left;
                    background-color: transparent;
                    border: none;
                    border-radius: 6px;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #f0f0f0;
                }
            """)
            sidebar_layout.addWidget(nav_btn)
        
        sidebar_layout.addStretch()
        
        sidebar.setLayout(sidebar_layout)
        sidebar.setStyleSheet("background-color: #f8f9fa; border-right: 1px solid #e9ecef;")
        sidebar.setFixedWidth(180)
        content_layout.addWidget(sidebar)
        
        # Main content
        main_content = QWidget()
        main_content_layout = QVBoxLayout()
        main_content_layout.setContentsMargins(20, 20, 20, 20)
        
        content_title = QLabel("Welcome to Dashboard")
        content_title.setStyleSheet("font-size: 24px; font-weight: bold; color: #333; margin-bottom: 20px;")
        main_content_layout.addWidget(content_title)
        
        # Card layout
        cards_layout = QHBoxLayout()
        
        card_data = [
            ("📈 Sales", "1,234", "#e3f2fd"),
            ("👥 Users", "567", "#f3e5f5"),
            ("💰 Revenue", "$12,345", "#e8f5e8")
        ]
        
        for title, value, bg_color in card_data:
            card = QWidget()
            card_layout = QVBoxLayout()
            card_layout.setContentsMargins(20, 15, 20, 15)
            
            card_title = QLabel(title)
            card_title.setStyleSheet("font-size: 14px; color: #666;")
            card_layout.addWidget(card_title)
            
            card_value = QLabel(value)
            card_value.setStyleSheet("font-size: 28px; font-weight: bold; color: #333;")
            card_layout.addWidget(card_value)
            
            card.setLayout(card_layout)
            card.setStyleSheet(f"background-color: {bg_color}; border-radius: 8px; border: 1px solid #ddd;")
            cards_layout.addWidget(card)
        
        main_content_layout.addLayout(cards_layout)
        main_content_layout.addStretch()
        
        main_content.setLayout(main_content_layout)
        content_layout.addWidget(main_content)
        
        main_layout.addLayout(content_layout)
        
        widget.setLayout(main_layout)
        return widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Tạo cửa sổ ví dụ
    window = StackedLayoutExamples()
    window.show()
    
    sys.exit(app.exec())
