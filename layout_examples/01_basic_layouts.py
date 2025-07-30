"""
PySide6 Layout Examples - Các ví dụ về Layout cơ bản
Học thiết kế layout từ cơ bản đến nâng cao
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QMainWindow, QTabWidget
)
from PySide6.QtCore import Qt


class BasicLayoutExamples(QMainWindow):
    """Ví dụ về các loại layout cơ bản"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Layout Examples - Cơ bản")
        self.setGeometry(100, 100, 800, 600)
        
        # Tạo tab widget để hiển thị các ví dụ khác nhau
        tab_widget = QTabWidget()
        
        # Tab 1: VBox Layout
        tab_widget.addTab(self.create_vbox_example(), "QVBoxLayout")
        
        # Tab 2: HBox Layout  
        tab_widget.addTab(self.create_hbox_example(), "QHBoxLayout")
        
        # Tab 3: Nested Layout
        tab_widget.addTab(self.create_nested_example(), "Nested Layout")
        
        self.setCentralWidget(tab_widget)
    
    def create_vbox_example(self):
        """Ví dụ QVBoxLayout - bố trí theo chiều dọc"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Thêm label mô tả
        title = QLabel("QVBoxLayout - Bố trí theo chiều dọc")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #0078d7; margin: 10px;")
        layout.addWidget(title)
        
        # Thêm các nút theo chiều dọc
        for i in range(1, 6):
            btn = QPushButton(f"Nút {i}")
            btn.setStyleSheet("""
                QPushButton {
                    padding: 10px;
                    margin: 5px;
                    background-color: #e1f5fe;
                    color: #1565c0;
                    border: 2px solid #0078d7;
                    border-radius: 8px;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #bbdefb;
                    color: #0d47a1;
                }
            """)
            layout.addWidget(btn)
        
        # Thêm stretch để đẩy nội dung lên trên
        layout.addStretch()
        
        widget.setLayout(layout)
        return widget
    
    def create_hbox_example(self):
        """Ví dụ QHBoxLayout - bố trí theo chiều ngang"""
        widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("QHBoxLayout - Bố trí theo chiều ngang")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #0078d7; margin: 10px;")
        main_layout.addWidget(title)
        
        # Tạo HBox layout
        hbox_layout = QHBoxLayout()
        
        # Thêm các nút theo chiều ngang
        for i in range(1, 5):
            btn = QPushButton(f"Nút {i}")
            btn.setStyleSheet("""
                QPushButton {
                    padding: 15px;
                    margin: 5px;
                    background-color: #f3e5f5;
                    color: #7b1fa2;
                    border: 2px solid #9c27b0;
                    border-radius: 8px;
                    font-size: 14px;
                    font-weight: bold;
                    min-width: 100px;
                }
                QPushButton:hover {
                    background-color: #e1bee7;
                    color: #4a148c;
                }
            """)
            hbox_layout.addWidget(btn)
        
        main_layout.addLayout(hbox_layout)
        main_layout.addStretch()
        
        widget.setLayout(main_layout)
        return widget
    
    def create_nested_example(self):
        """Ví dụ Nested Layout - lồng layout (như trong login form)"""
        widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("Nested Layout - Lồng layout (như Login Form)")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #0078d7; margin: 10px;")
        main_layout.addWidget(title)
        
        # Mô tả cách hoạt động
        description = QLabel("Giống như login form: wrapper layout + inner layout + stretch")
        description.setStyleSheet("font-size: 12px; color: #666; margin: 5px;")
        main_layout.addWidget(description)
        
        # Tạo wrapper layout (giống login form)
        wrapper = QVBoxLayout()
        wrapper.addStretch()  # Đẩy xuống giữa
        
        # Inner layout (chứa form content)
        inner_layout = QVBoxLayout()
        inner_layout.setSpacing(10)
        inner_layout.setAlignment(Qt.AlignCenter)
        
        # Form title
        form_title = QLabel("🎯 Form Example")
        form_title.setStyleSheet("""
            font-size: 18px; 
            font-weight: bold; 
            color: #333;
            padding: 10px;
            background-color: #f0f8ff;
            border-radius: 8px;
            text-align: center;
        """)
        form_title.setAlignment(Qt.AlignCenter)
        inner_layout.addWidget(form_title)
        
        # Các nút trong form
        for i in range(1, 4):
            btn = QPushButton(f"Form Button {i}")
            btn.setStyleSheet("""
                QPushButton {
                    padding: 12px;
                    margin: 3px;
                    background-color: #fff3e0;
                    color: #f57c00;
                    border: 2px solid #ff9800;
                    border-radius: 6px;
                    font-size: 14px;
                    font-weight: bold;
                    max-width: 200px;
                }
                QPushButton:hover {
                    background-color: #ffe0b2;
                    color: #e65100;
                }
            """)
            inner_layout.addWidget(btn)
        
        wrapper.addLayout(inner_layout)
        wrapper.addStretch()  # Đẩy lên giữa
        
        main_layout.addLayout(wrapper)
        
        widget.setLayout(main_layout)
        return widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Tạo cửa sổ ví dụ
    window = BasicLayoutExamples()
    window.show()
    
    sys.exit(app.exec())
