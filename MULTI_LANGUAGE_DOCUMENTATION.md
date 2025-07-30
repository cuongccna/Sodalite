# FinanTidy - Multi-Language Support (Anh-Việt) ✅

## 🌐 Tổng quan hệ thống đa ngôn ngữ

FinanTidy hiện đã hỗ trợ **2 ngôn ngữ**:
- 🇻🇳 **Tiếng Việt** (Mặc định)
- 🇺🇸 **English** (Quốc tế)

## 🏗️ Kiến trúc hệ thống

### 1. **Language Manager** (`src/core/language_manager.py`)
- **Class**: `LanguageManager` - Quản lý translations và ngôn ngữ hiện tại
- **Function**: `t(key, default)` - Function dịch thuật chính
- **Storage**: JSON files trong `data/languages/`
- **Auto-loading**: Tự động load settings từ `finantidy_settings.json`

### 2. **Translation Files**
```
data/languages/
├── vi.json     # Tiếng Việt (default)
└── en.json     # English
```

### 3. **Settings Integration**
- **Settings Window**: Giao diện chọn ngôn ngữ trong Settings
- **Auto-save**: Tự động lưu lựa chọn ngôn ngữ
- **Real-time**: Một số thay đổi áp dụng ngay lập tức

## 🎯 Cách sử dụng

### Cho người dùng cuối:
1. **Mở Settings**: Click vào ⚙️ Settings button
2. **Chọn Language**: Click vào 🌐 Language category
3. **Chọn ngôn ngữ**: 
   - 🇻🇳 Tiếng Việt (mặc định)
   - 🇺🇸 English 
4. **Xác nhận**: Dialog xác nhận bằng cả 2 ngôn ngữ
5. **Áp dụng**: Một số thay đổi ngay lập tức, restart để áp dụng hoàn toàn

### Cho developer:
```python
# Import language manager
from core.language_manager import get_language_manager, t

# Sử dụng translation
self.t("login.username", "Username")  # Key với fallback
self.t("navigation.dashboard")        # Key không fallback

# Thay đổi ngôn ngữ
lang_manager = get_language_manager()
lang_manager.set_language('en')       # 'vi' hoặc 'en'
```

## 📋 Translations được implement

### ✅ Login Window:
- Title, labels, buttons, messages
- Error dialogs và confirmations
- Demo credentials info

### ✅ Main Window:
- Navigation menu (Dashboard, Invoices, etc.)
- Header buttons (Settings, Logout)
- Company subtitle
- Welcome messages

### ✅ Settings Window:
- Language selection interface
- Confirmation dialogs
- Section titles và descriptions

### ✅ Modules Placeholders:
- Module titles và descriptions
- "Coming Soon" badges
- Consistent translations

## 🔧 Technical Details

### Language Keys Structure:
```json
{
  "app": {
    "title": "FinanTidy",
    "subtitle": "Hệ thống Quản lý Tài chính"
  },
  "login": {
    "title": "Đăng nhập FinanTidy",
    "username": "Tên đăng nhập",
    "login_button": "🔐 ĐĂNG NHẬP"
  },
  "navigation": {
    "dashboard": "Tổng quan",
    "invoices": "Hóa đơn"
  }
}
```

### Settings Storage:
```json
{
  "language": "vi",
  "theme": "dark",
  "company": {...}
}
```

### Import Pattern:
```python
# Add to every UI file
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from core.language_manager import get_language_manager, t
    _lang_manager = get_language_manager()
    _t = t
except ImportError:
    _lang_manager = None
    _t = lambda key, default=None: default or key
```

## 🚀 Features hoạt động

### ✅ Language Selection:
- Visual radio buttons với flags
- Real-time preview
- Bilingual confirmation dialogs
- Auto-save preferences

### ✅ Translation Coverage:
- **UI Elements**: Buttons, labels, titles
- **Messages**: Errors, confirmations, info
- **Navigation**: Menu items, placeholders
- **Settings**: All settings categories

### ✅ Fallback Support:
- Default values nếu translation missing
- Graceful degradation nếu language manager fail
- English fallback cho missing Vietnamese keys

## 📱 User Experience

### Language Change Flow:
1. **Current Language Display**: Hiển thị ngôn ngữ hiện tại
2. **Bilingual Options**: Mô tả bằng cả 2 ngôn ngữ
3. **Confirmation Dialog**: Xác nhận bằng cả 2 ngôn ngữ
4. **Immediate Changes**: Title, buttons update ngay
5. **Restart Notice**: Thông báo restart để áp dụng hoàn toàn

### Default Behavior:
- **Vietnamese First**: Mặc định Tiếng Việt
- **Settings Persistence**: Lưu lựa chọn tự động
- **Auto-load**: Load language settings khi khởi động

## 🔮 Mở rộng trong tương lai

### Planned Enhancements:
1. **More Languages**: Thêm ngôn ngữ khác (中文, 한국어, etc.)
2. **Date/Time Localization**: Format ngày tháng theo locale
3. **Number Formatting**: Format số tiền theo locale
4. **RTL Support**: Hỗ trợ ngôn ngữ Right-to-Left
5. **Pluralization**: Xử lý số ít/số nhiều

### Easy Translation Addition:
```python
# Thêm ngôn ngữ mới
def get_default_chinese(self):
    return {
        "app": {"title": "财务管理"},
        "login": {"username": "用户名"}
    }

# Update available languages
def get_available_languages(self):
    return {
        'vi': 'Tiếng Việt',
        'en': 'English', 
        'zh': '中文'
    }
```

## 📊 Performance & Storage

### Translation Files:
- **Size**: ~5-10KB per language
- **Loading**: Lazy load only needed languages
- **Caching**: In-memory caching sau khi load
- **Updates**: Hot-reload không cần restart

### Settings Persistence:
- **File**: `finantidy_settings.json` (UTF-8)
- **Auto-save**: Mỗi khi thay đổi language
- **Backup**: Có thể backup/restore settings

**🎉 FinanTidy giờ đây hoàn toàn đa ngôn ngữ Anh-Việt với trải nghiệm người dùng tuyệt vời!**
