"""
PySide6 Advanced Layout Examples - Grid & Form Layout
Ví dụ nâng cao về Grid Layout và Form Layout
"""

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QMainWindow, QTabWidget,
    QGridLayout, QFormLayout, QLineEdit, QTextEdit,
    QComboBox, QCheckBox, QSpinBox
)
from PySide6.QtCore import Qt


class AdvancedLayoutExamples(QMainWindow):
    """Ví dụ về Grid Layout và Form Layout"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 Layout Examples - Nâng cao")
        self.setGeometry(100, 100, 900, 700)
        
        # Tab widget
        tab_widget = QTabWidget()
        
        # Tab 1: Grid Layout
        tab_widget.addTab(self.create_grid_example(), "QGridLayout")
        
        # Tab 2: Form Layout
        tab_widget.addTab(self.create_form_example(), "QFormLayout")
        
        # Tab 3: Complex Layout
        tab_widget.addTab(self.create_complex_example(), "Complex Layout")
        
        self.setCentralWidget(tab_widget)
    
    def create_grid_example(self):
        """Ví dụ QGridLayout - bố trí theo lưới"""
        widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("QGridLayout - Bố trí theo lưới (hàng, cột)")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #0078d7; margin: 10px;")
        main_layout.addWidget(title)
        
        # Mô tả
        desc = QLabel("Cú pháp: addWidget(widget, row, column, rowspan, colspan)")
        desc.setStyleSheet("font-size: 12px; color: #666; margin: 5px;")
        main_layout.addWidget(desc)
        
        # Tạo Grid Layout
        grid = QGridLayout()
        grid.setSpacing(10)
        
        # Ví dụ 1: Các ô đơn lẻ
        for row in range(3):
            for col in range(3):
                btn = QPushButton(f"({row},{col})")
                btn.setStyleSheet("""
                    QPushButton {
                        padding: 15px;
                        background-color: #e8f5e8;
                        color: #2e7d32;
                        border: 2px solid #4caf50;
                        border-radius: 8px;
                        font-size: 12px;
                        font-weight: bold;
                        min-height: 40px;
                    }
                    QPushButton:hover {
                        background-color: #c8e6c9;
                        color: #1b5e20;
                    }
                """)
                grid.addWidget(btn, row, col)
        
        # Ví dụ 2: Span nhiều ô
        # Nút span 2 cột (colspan = 2)
        wide_btn = QPushButton("Span 2 cột (3,0) colspan=2")
        wide_btn.setStyleSheet("""
            QPushButton {
                padding: 15px;
                background-color: #fff3e0;
                color: #f57c00;
                border: 2px solid #ff9800;
                border-radius: 8px;
                font-size: 12px;
                font-weight: bold;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #ffe0b2;
                color: #e65100;
            }
        """)
        grid.addWidget(wide_btn, 3, 0, 1, 2)  # row=3, col=0, rowspan=1, colspan=2
        
        # Nút span 2 hàng (rowspan = 2)
        tall_btn = QPushButton("Span 2 hàng\n(3,2)\nrowspan=2")
        tall_btn.setStyleSheet("""
            QPushButton {
                padding: 15px;
                background-color: #f3e5f5;
                color: #7b1fa2;
                border: 2px solid #9c27b0;
                border-radius: 8px;
                font-size: 12px;
                font-weight: bold;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #e1bee7;
                color: #4a148c;
            }
        """)
        grid.addWidget(tall_btn, 3, 2, 2, 1)  # row=3, col=2, rowspan=2, colspan=1
        
        # Nút ở hàng 4
        single_btn = QPushButton("(4,0)")
        single_btn.setStyleSheet("""
            QPushButton {
                padding: 15px;
                background-color: #e3f2fd;
                color: #1565c0;
                border: 2px solid #2196f3;
                border-radius: 8px;
                font-size: 12px;
                font-weight: bold;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #bbdefb;
                color: #0d47a1;
            }
        """)
        grid.addWidget(single_btn, 4, 0)
        
        # Thêm grid vào main layout
        grid_widget = QWidget()
        grid_widget.setLayout(grid)
        main_layout.addWidget(grid_widget)
        main_layout.addStretch()
        
        widget.setLayout(main_layout)
        return widget
    
    def create_form_example(self):
        """Ví dụ QFormLayout - dạng biểu mẫu"""
        widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("QFormLayout - Dạng biểu mẫu (Label + Widget)")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #0078d7; margin: 10px;")
        main_layout.addWidget(title)
        
        # Mô tả
        desc = QLabel("Cú pháp: addRow(label_text, widget) hoặc addRow(label_widget, widget)")
        desc.setStyleSheet("font-size: 12px; color: #666; margin: 5px;")
        main_layout.addWidget(desc)
        
        # Tạo Form Layout
        form = QFormLayout()
        form.setSpacing(15)
        
        # CSS cho các widget
        input_style = """
            QLineEdit, QComboBox, QSpinBox {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 6px;
                font-size: 14px;
                background-color: white;
            }
            QLineEdit:focus, QComboBox:focus, QSpinBox:focus {
                border-color: #0078d7;
            }
        """
        
        text_style = """
            QTextEdit {
                border: 2px solid #ddd;
                border-radius: 6px;
                font-size: 14px;
                background-color: white;
            }
            QTextEdit:focus {
                border-color: #0078d7;
            }
        """
        
        # Các trường form
        name_input = QLineEdit()
        name_input.setPlaceholderText("Nhập họ tên đầy đủ")
        name_input.setStyleSheet(input_style)
        form.addRow("Họ tên:", name_input)
        
        email_input = QLineEdit()
        email_input.setPlaceholderText("example@email.com")
        email_input.setStyleSheet(input_style)
        form.addRow("Email:", email_input)
        
        age_input = QSpinBox()
        age_input.setRange(18, 100)
        age_input.setValue(25)
        age_input.setStyleSheet(input_style)
        form.addRow("Tuổi:", age_input)
        
        city_combo = QComboBox()
        city_combo.addItems(["Hà Nội", "TP.HCM", "Đà Nẵng", "Cần Thơ", "Hải Phòng"])
        city_combo.setStyleSheet(input_style)
        form.addRow("Thành phố:", city_combo)
        
        note_text = QTextEdit()
        note_text.setPlaceholderText("Ghi chú thêm...")
        note_text.setMaximumHeight(80)
        note_text.setStyleSheet(text_style)
        form.addRow("Ghi chú:", note_text)
        
        # Checkbox
        agree_check = QCheckBox("Tôi đồng ý với điều khoản sử dụng")
        agree_check.setStyleSheet("font-size: 14px; color: #333;")
        form.addRow("", agree_check)
        
        # Submit button
        submit_btn = QPushButton("Gửi thông tin")
        submit_btn.setStyleSheet("""
            QPushButton {
                padding: 12px 20px;
                background-color: #4caf50;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
                max-width: 150px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        form.addRow("", submit_btn)
        
        # Thêm form vào widget
        form_widget = QWidget()
        form_widget.setLayout(form)
        form_widget.setStyleSheet("background-color: #f9f9f9; padding: 20px; border-radius: 10px;")
        
        main_layout.addWidget(form_widget)
        main_layout.addStretch()
        
        widget.setLayout(main_layout)
        return widget
    
    def create_complex_example(self):
        """Ví dụ layout phức tạp - kết hợp nhiều loại layout"""
        widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Title
        title = QLabel("Complex Layout - Kết hợp nhiều loại layout")
        title.setStyleSheet("font-size: 16px; font-weight: bold; color: #0078d7; margin: 10px;")
        main_layout.addWidget(title)
        
        # Top section - HBox với 3 nút
        top_layout = QHBoxLayout()
        for i in range(1, 4):
            btn = QPushButton(f"Top {i}")
            btn.setStyleSheet("""
                QPushButton {
                    padding: 10px;
                    background-color: #e1f5fe;
                    color: #1565c0;
                    border: 2px solid #0078d7;
                    border-radius: 6px;
                    font-size: 14px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #bbdefb;
                    color: #0d47a1;
                }
            """)
            top_layout.addWidget(btn)
        
        main_layout.addLayout(top_layout)
        
        # Middle section - Grid 2x2
        middle_layout = QGridLayout()
        grid_colors = ["#ffebee", "#f3e5f5", "#e8f5e8", "#fff3e0"]
        border_colors = ["#f44336", "#9c27b0", "#4caf50", "#ff9800"]
        
        for i in range(2):
            for j in range(2):
                idx = i * 2 + j
                btn = QPushButton(f"Grid ({i},{j})")
                btn.setStyleSheet(f"""
                    QPushButton {{
                        padding: 20px;
                        background-color: {grid_colors[idx]};
                        border: 2px solid {border_colors[idx]};
                        border-radius: 8px;
                        font-size: 14px;
                        min-height: 60px;
                    }}
                    QPushButton:hover {{
                        opacity: 0.8;
                    }}
                """)
                middle_layout.addWidget(btn, i, j)
        
        middle_widget = QWidget()
        middle_widget.setLayout(middle_layout)
        main_layout.addWidget(middle_widget)
        
        # Bottom section - Form với VBox wrapper
        bottom_wrapper = QVBoxLayout()
        bottom_wrapper.addStretch()
        
        # Mini form
        form_layout = QFormLayout()
        
        quick_input = QLineEdit()
        quick_input.setPlaceholderText("Quick input...")
        quick_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 6px;
                background-color: white;
            }
            QLineEdit:focus {
                border-color: #0078d7;
            }
        """)
        
        quick_btn = QPushButton("Submit")
        quick_btn.setStyleSheet("""
            QPushButton {
                padding: 8px 15px;
                background-color: #4caf50;
                color: white;
                border: none;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        
        form_layout.addRow("Quick:", quick_input)
        form_layout.addRow("", quick_btn)
        
        bottom_wrapper.addLayout(form_layout)
        bottom_wrapper.addStretch()
        
        main_layout.addLayout(bottom_wrapper)
        
        widget.setLayout(main_layout)
        return widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Tạo cửa sổ ví dụ
    window = AdvancedLayoutExamples()
    window.show()
    
    sys.exit(app.exec())
