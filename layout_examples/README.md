# PySide6 Layout Learning Guide

## 📚 Tổng hợp kiến thức Layout trong PySide6

### 1. Các loại Layout chính

| Layout | Mô tả | Khi nào sử dụng |
|--------|-------|------------------|
| `QVBoxLayout` | Bố trí theo chiều dọc | Danh sách, menu, form đơn giản |
| `QHBoxLayout` | Bố trí theo chiều ngang | Toolbar, button group |
| `QGridLayout` | Bố trí theo lưới (hàng/cột) | Calculator, table layout |
| `QFormLayout` | Dạng biểu mẫu (label + widget) | Form đăng ký, cài đặt |
| `QStackedLayout` | Stack nhiều widget | Tab content, wizard pages |

### 2. Phân tích Login Form hiện tại

```python
# Từ login_window.py
# Wrapper layout (outer)
wrapper = QVBoxLayout(self)
wrapper.addStretch()        # Đẩy xuống
wrapper.addLayout(layout)   # Form content ở giữa
wrapper.addStretch()        # Đẩy lên

# Inner layout (form content)
layout = QVBoxLayout()
layout.setAlignment(Qt.AlignCenter)
layout.setSpacing(15)
layout.addWidget(title)          # Title
layout.addWidget(username_input) # Input 1
layout.addWidget(password_input) # Input 2  
layout.addWidget(login_button)   # Button
```

**💡 Kỹ thuật này tạo hiệu ứng căn giữa hoàn hảo!**

### 3. Các method quan trọng

#### Layout Management
- `addWidget(widget)` - Thêm widget vào layout
- `addLayout(layout)` - Thêm layout con vào layout cha
- `addStretch()` - Thêm khoảng trống co giãn
- `setSpacing(pixels)` - Khoảng cách giữa các widget
- `setContentsMargins(left, top, right, bottom)` - Margin của layout

#### Grid Layout đặc biệt
- `addWidget(widget, row, col)` - Thêm vào ô (row, col)
- `addWidget(widget, row, col, rowspan, colspan)` - Span nhiều ô

#### Alignment
- `setAlignment(Qt.AlignCenter)` - Căn giữa
- `addWidget(widget, alignment=Qt.AlignRight)` - Căn phải widget

### 4. Best Practices từ Login Form

1. **Nested Layout Pattern**:
   ```python
   # Outer wrapper cho căn giữa
   wrapper = QVBoxLayout(self)
   wrapper.addStretch()
   
   # Inner layout cho content
   content_layout = QVBoxLayout()
   # ... thêm widgets
   
   wrapper.addLayout(content_layout)
   wrapper.addStretch()
   ```

2. **Styling với CSS**:
   ```python
   widget.setStyleSheet("""
       QLineEdit {
           padding: 10px;
           border: 1px solid #ccc;
           border-radius: 6px;
       }
       QLineEdit:focus {
           border: 2px solid #0078d7;
       }
   """)
   ```

3. **Responsive Spacing**:
   ```python
   layout.setSpacing(15)  # Consistent spacing
   layout.setAlignment(Qt.AlignCenter)  # Center alignment
   ```

### 5. Các file ví dụ

1. **01_basic_layouts.py** - VBox, HBox, Nested Layout
2. **02_advanced_layouts.py** - Grid, Form, Complex Layout  
3. **03_stacked_stretch.py** - StackedLayout, Stretch, Real App

### 6. Chạy thử các ví dụ

```bash
# Chạy từng file ví dụ
python layout_examples/01_basic_layouts.py
python layout_examples/02_advanced_layouts.py  
python layout_examples/03_stacked_stretch.py

# Hoặc chạy login form hiện tại
python src/ui/login_window.py
```

### 7. Code Template mẫu

```python
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt

app = QApplication([])

# Tạo window
window = QWidget()
window.setWindowTitle("My App")
window.setFixedSize(400, 300)

# Tạo layout chính (wrapper)
main_layout = QVBoxLayout()
main_layout.addStretch()  # Top stretch

# Tạo content layout  
content_layout = QVBoxLayout()
content_layout.setAlignment(Qt.AlignCenter)
content_layout.setSpacing(10)

# Thêm widgets vào content
content_layout.addWidget(QPushButton("Button 1"))
content_layout.addWidget(QPushButton("Button 2"))

# Lắp ráp layout
main_layout.addLayout(content_layout)
main_layout.addStretch()  # Bottom stretch

# Apply layout và show
window.setLayout(main_layout)
window.show()

app.exec()
```

---

## 🎯 Kết luận

Login form hiện tại của bạn đã sử dụng rất tốt:
- ✅ **Nested Layout** (wrapper + inner)
- ✅ **Stretch** để căn giữa  
- ✅ **Alignment** và **Spacing** hợp lý
- ✅ **CSS Styling** đẹp mắt

Đây là một mẫu thiết kế chuẩn mực có thể áp dụng cho nhiều component khác!
