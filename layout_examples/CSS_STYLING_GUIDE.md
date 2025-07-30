# 🎨 PySide6 Styling Best Practices - Hướng dẫn CSS

## ❌ Lỗi thường gặp: Màu chữ và màu nền xung đột

### Vấn đề ban đầu
```python
# ❌ WRONG - Chỉ có background-color, không có color
btn.setStyleSheet("""
    QPushButton {
        background-color: #e1f5fe;  # Màu nền sáng
        border: 2px solid #0078d7;
    }
""")
# Kết quả: Text có thể không nhìn thấy hoặc khó đọc
```

### ✅ Giải pháp đúng
```python
# ✅ CORRECT - Có cả background-color và color
btn.setStyleSheet("""
    QPushButton {
        background-color: #e1f5fe;  # Màu nền sáng
        color: #1565c0;             # Màu chữ tối (contrast tốt)
        border: 2px solid #0078d7;
        font-weight: bold;          # Tăng độ đậm để dễ đọc
    }
    QPushButton:hover {
        background-color: #bbdefb;  # Màu nền hover
        color: #0d47a1;             # Màu chữ hover (tối hơn)
    }
""")
```

---

## 🎯 Color Contrast Guidelines

### 1. Nguyên tắc cơ bản
- **Màu nền sáng** → **Màu chữ tối**
- **Màu nền tối** → **Màu chữ sáng**
- **Luôn test contrast ratio** ≥ 4.5:1 (WCAG AA standard)

### 2. Bảng màu chuẩn cho các theme

| Background Color | Text Color | Border Color | Hover BG | Hover Text |
|------------------|------------|--------------|----------|------------|
| `#e1f5fe` (Blue light) | `#1565c0` (Blue dark) | `#0078d7` | `#bbdefb` | `#0d47a1` |
| `#f3e5f5` (Purple light) | `#7b1fa2` (Purple dark) | `#9c27b0` | `#e1bee7` | `#4a148c` |
| `#e8f5e8` (Green light) | `#2e7d32` (Green dark) | `#4caf50` | `#c8e6c9` | `#1b5e20` |
| `#fff3e0` (Orange light) | `#f57c00` (Orange dark) | `#ff9800` | `#ffe0b2` | `#e65100` |
| `#ffebee` (Red light) | `#d32f2f` (Red dark) | `#f44336` | `#ffcdd2` | `#b71c1c` |

---

## 🔧 Complete Button Template

```python
def create_styled_button(text, color_theme="blue"):
    """Tạo button với styling hoàn chỉnh"""
    
    themes = {
        "blue": {
            "bg": "#e1f5fe",
            "color": "#1565c0", 
            "border": "#0078d7",
            "hover_bg": "#bbdefb",
            "hover_color": "#0d47a1"
        },
        "purple": {
            "bg": "#f3e5f5",
            "color": "#7b1fa2",
            "border": "#9c27b0", 
            "hover_bg": "#e1bee7",
            "hover_color": "#4a148c"
        },
        "green": {
            "bg": "#e8f5e8",
            "color": "#2e7d32",
            "border": "#4caf50",
            "hover_bg": "#c8e6c9", 
            "hover_color": "#1b5e20"
        }
    }
    
    theme = themes.get(color_theme, themes["blue"])
    
    btn = QPushButton(text)
    btn.setStyleSheet(f"""
        QPushButton {{
            padding: 12px 20px;
            background-color: {theme['bg']};
            color: {theme['color']};
            border: 2px solid {theme['border']};
            border-radius: 8px;
            font-size: 14px;
            font-weight: bold;
            min-width: 100px;
        }}
        QPushButton:hover {{
            background-color: {theme['hover_bg']};
            color: {theme['hover_color']};
        }}
        QPushButton:pressed {{
            background-color: {theme['border']};
            color: white;
        }}
        QPushButton:disabled {{
            background-color: #f5f5f5;
            color: #9e9e9e;
            border-color: #e0e0e0;
        }}
    """)
    
    return btn

# Sử dụng
blue_btn = create_styled_button("Blue Button", "blue")
purple_btn = create_styled_button("Purple Button", "purple") 
green_btn = create_styled_button("Green Button", "green")
```

---

## 📋 CSS Properties Checklist

### Bắt buộc cho Button
- ✅ `background-color` - Màu nền
- ✅ `color` - Màu chữ  
- ✅ `border` - Đường viền
- ✅ `padding` - Khoảng cách trong
- ✅ `border-radius` - Bo góc

### Tăng trải nghiệm
- ✅ `font-weight: bold` - Chữ đậm
- ✅ `font-size` - Kích thước chữ
- ✅ `:hover` state - Hiệu ứng hover
- ✅ `:pressed` state - Hiệu ứng nhấn
- ✅ `:disabled` state - Trạng thái vô hiệu hóa

### Responsive Design
- ✅ `min-width` / `max-width` - Chiều rộng
- ✅ `min-height` - Chiều cao tối thiểu
- ✅ `margin` - Khoảng cách ngoài

---

## 🎨 Color Palette Generator

Để tạo color palette nhất quán:

1. **Chọn màu chính** (Primary Color)
2. **Tạo màu sáng** (+40% lightness) cho background
3. **Tạo màu tối** (-20% lightness) cho text
4. **Tạo màu hover** (giữa background và primary)

### Tools hữu ích:
- [Coolors.co](https://coolors.co) - Color palette generator
- [Contrast Checker](https://webaim.org/resources/contrastchecker/) - Test contrast
- [Material Design Colors](https://material.io/design/color/) - Google's color system

---

## 🚀 Kết luận

**Nguyên tắc vàng**: Luôn cặp `background-color` với `color` phù hợp!

```python
# Template cơ bản luôn đúng
widget.setStyleSheet("""
    QWidget {
        background-color: [MÀU NỀN];
        color: [MÀU CHỮ TƯƠNG PHẢN];
        border: 1px solid [MÀU VIỀN];
        font-weight: bold;
    }
    QWidget:hover {
        background-color: [MÀU NỀN HOVER];
        color: [MÀU CHỮ HOVER];
    }
""")
```
