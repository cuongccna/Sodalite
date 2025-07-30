"""
FinanTidy - Language Manager
Handles multi-language support (Vietnamese/English)
"""

import json
import os
from typing import Dict, Any, Optional

class LanguageManager:
    """Manages application language and translations"""
    
    def __init__(self, language_dir: str = None):
        """Initialize language manager"""
        self.language_dir = language_dir or os.path.join(os.path.dirname(__file__), 'languages')
        self.current_language = 'vi'  # Default to Vietnamese
        self.translations = {}
        
        # Ensure language directory exists
        os.makedirs(self.language_dir, exist_ok=True)
        
        # Load translations
        self.load_translations()
    
    def load_translations(self):
        """Load all translation files"""
        # Load Vietnamese translations
        vi_file = os.path.join(self.language_dir, 'vi.json')
        if os.path.exists(vi_file):
            with open(vi_file, 'r', encoding='utf-8') as f:
                self.translations['vi'] = json.load(f)
        else:
            self.translations['vi'] = self.get_default_vietnamese()
            self.save_translations('vi')
        
        # Load English translations
        en_file = os.path.join(self.language_dir, 'en.json')
        if os.path.exists(en_file):
            with open(en_file, 'r', encoding='utf-8') as f:
                self.translations['en'] = json.load(f)
        else:
            self.translations['en'] = self.get_default_english()
            self.save_translations('en')
    
    def save_translations(self, language: str):
        """Save translations to file"""
        if language in self.translations:
            file_path = os.path.join(self.language_dir, f'{language}.json')
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.translations[language], f, indent=2, ensure_ascii=False)
    
    def set_language(self, language: str):
        """Set current language"""
        if language in self.translations:
            self.current_language = language
            return True
        return False
    
    def get_language(self) -> str:
        """Get current language"""
        return self.current_language
    
    def get_current_language(self) -> str:
        """Get current language (alias for get_language)"""
        return self.current_language
    
    def get_available_languages(self) -> Dict[str, str]:
        """Get available languages"""
        return {
            'vi': 'Tiếng Việt',
            'en': 'English'
        }
    
    def t(self, key: str, default: str = None) -> str:
        """
        Translate a key to current language
        
        Args:
            key: Translation key (can use dot notation like 'login.username')
            default: Default text if translation not found
            
        Returns:
            Translated text
        """
        try:
            # Handle dot notation
            keys = key.split('.')
            text = self.translations[self.current_language]
            
            for k in keys:
                text = text[k]
            
            return text
        except (KeyError, TypeError):
            # Fallback to default or key itself
            return default or key
    
    def get_default_vietnamese(self) -> Dict[str, Any]:
        """Get default Vietnamese translations"""
        return {
            "app": {
                "title": "FinanTidy",
                "name": "FinanTidy",
                "welcome": "Chào mừng đến với FinanTidy",
                "subtitle": "Hệ thống quản lý tài chính hiện đại với tích hợp hóa đơn điện tử Viettel",
                "version": "FinanTidy v2.0 - Phiên bản chuyên nghiệp với tích hợp hóa đơn điện tử Viettel"
            },
            "common": {
                "ok": "Đồng ý",
                "cancel": "Hủy",
                "yes": "Có",
                "no": "Không",
                "save": "Lưu",
                "close": "Đóng",
                "apply": "Áp dụng",
                "reset": "Đặt lại",
                "confirm": "Xác nhận",
                "warning": "Cảnh báo",
                "error": "Lỗi",
                "success": "Thành công",
                "info": "Thông tin"
            },
            "login": {
                "title": "Đăng nhập FinanTidy",
                "form_title": "Đăng nhập vào tài khoản",
                "username_label": "Tên đăng nhập",
                "username": "Tên đăng nhập",
                "username_placeholder": "Nhập tên đăng nhập của bạn",
                "password_label": "Mật khẩu",
                "password": "Mật khẩu",
                "password_placeholder": "Nhập mật khẩu của bạn",
                "remember_me": "Ghi nhớ đăng nhập",
                "forgot_password": "Quên mật khẩu?",
                "login_button": "Đăng nhập",
                "cancel_button": "❌ HỦY BỎ",
                "demo_title": "🔑 Thông tin đăng nhập mặc định",
                "demo_info": "Tên đăng nhập: admin  •  Mật khẩu: admin",
                "error_title": "Đăng nhập thất bại",
                "error_message": "Tên đăng nhập hoặc mật khẩu không đúng!",
                "default_credentials": "Thông tin đăng nhập mặc định:",
                "login_error": "Lỗi đăng nhập",
                "login_failed": "Đăng nhập thất bại",
                "invalid_credentials": "Tên đăng nhập hoặc mật khẩu không đúng!",
                "fill_all_fields": "Vui lòng nhập đầy đủ thông tin đăng nhập",
                "signing_in": "Đang đăng nhập..."
            },
            "navigation": {
                "dashboard": "Tổng quan",
                "invoices": "Hóa đơn",
                "providers": "Nhà cung cấp",
                "analytics": "Phân tích",
                "transactions": "Giao dịch",
                "reports": "Báo cáo"
            },
            "dashboard": {
                "welcome": "Chào mừng trở lại, {name}!",
                "welcome_subtitle": "Đây là tình hình tài chính của bạn hôm nay",
                "recent_activity": "Hoạt động Gần đây",
                "quick_actions": "Thao tác Nhanh",
                "quick_overview": "TỔNG QUAN NHANH",
                "view_all": "Xem tất cả",
                "total_invoices": "Tổng hóa đơn",
                "providers": "Nhà cung cấp",
                "demo_user": "Người dùng Demo",
                "demo_company": "Công ty Demo",
                "stats": {
                    "revenue": "Tổng doanh thu",
                    "pending": "Chờ thanh toán",
                    "invoices": "Tổng hóa đơn",
                    "providers": "Nhà cung cấp",
                    "overdue": "Quá hạn"
                }
            },
            "actions": {
                "create_invoice": "📄 Tạo hóa đơn",
                "add_provider": "🏪 Thêm nhà cung cấp",
                "record_payment": "💰 Ghi nhận thanh toán",
                "generate_report": "📈 Tạo báo cáo",
                "viettel_einvoice": "📧 Viettel eInvoice",
                "system_settings": "⚙️ Cài đặt hệ thống",
                "view_analytics": "📊 Xem phân tích"
            },
            "settings": {
                "title": "Cài đặt Hệ thống",
                "subtitle": "Cấu hình tùy chọn ứng dụng FinanTidy của bạn",
                "language": "Ngôn ngữ",
                "language_desc": "Chọn ngôn ngữ hiển thị giao diện",
                "appearance": "Giao diện",
                "notifications": "Thông báo",
                "save": "Lưu cài đặt",
                "reset": "Đặt lại",
                "cancel": "Hủy bỏ",
                "save_success": "Cài đặt đã được lưu thành công!",
                "categories": "DANH MỤC CÀI ĐẶT",
                "company": "Công ty",
                "display": "Hiển thị",
                "backup": "Sao lưu",
                "security": "Bảo mật",
                "invoice": "Hóa đơn",
                "viettel_einvoice": "Hóa đơn điện tử Viettel",
                "language": {
                    "title": "Cài đặt ngôn ngữ",
                    "description": "Chọn ngôn ngữ ưa thích cho giao diện ứng dụng",
                    "restart_note": "Lưu ý: Một số yếu tố giao diện có thể cần khởi động lại ứng dụng để cập nhật hoàn toàn."
                },
                "company": {
                    "title": "Thông tin công ty",
                    "description": "Cấu hình thông tin công ty cho hóa đơn và tài liệu",
                    "name": "Tên công ty",
                    "address": "Địa chỉ",
                    "phone": "Số điện thoại",
                    "email": "Email"
                },
                "display": {
                    "title": "Cài đặt hiển thị"
                },
                "notifications": {
                    "title": "Cài đặt thông báo"
                },
                "backup": {
                    "title": "Cài đặt sao lưu"
                },
                "security": {
                    "title": "Cài đặt bảo mật"
                },
                "invoice": {
                    "title": "Cài đặt hóa đơn"
                },
                "viettel_einvoice": {
                    "title": "Cài đặt hóa đơn điện tử Viettel",
                    "description": "Cấu hình tích hợp API Viettel eInvoice để xử lý hóa đơn điện tử",
                    "connection_status": "Trạng thái kết nối",
                    "not_configured": "Chưa được cấu hình",
                    "configuration": "Cấu hình",
                    "configure": "Cấu hình API",
                    "test_connection": "Kiểm tra kết nối",
                    "import_config": "Nhập cấu hình",
                    "info": "Thông tin",
                    "info_content": "Tích hợp Viettel eInvoice cho phép bạn:\n• Tự động tạo hóa đơn điện tử\n• Gửi hóa đơn tới cơ quan thuế\n• Theo dõi trạng thái và xác thực hóa đơn\n• Tuân thủ quy định hóa đơn điện tử Việt Nam\n\nLiên hệ Viettel để có thông tin đăng nhập API và chi tiết cấu hình.",
                    "config_title": "Cấu hình Viettel",
                    "config_message": "Cửa sổ cấu hình Viettel eInvoice sẽ sớm có sẵn!",
                    "test_title": "Kiểm tra kết nối",
                    "test_message": "Chức năng kiểm tra kết nối sẽ có sẵn sau khi cấu hình.",
                    "import_title": "Nhập cấu hình Viettel",
                    "import_success_title": "Nhập thành công",
                    "import_success_message": "Cấu hình đã được nhập từ: {}"
                },
                "reset_confirm_title": "Đặt lại cài đặt",
                "reset_confirm_message": "Điều này sẽ đặt lại tất cả cài đặt về giá trị mặc định.\nBạn có chắc chắn muốn tiếp tục không?",
                "reset_success_title": "Đặt lại",
                "reset_success_message": "Cài đặt đã được đặt lại về mặc định thành công!"
            },
            "modules": {
                "invoices": {
                    "title": "📄 Quản lý Hóa đơn",
                    "description": "Module quản lý hóa đơn đang được chuẩn bị.\nTính năng: Tạo, sửa, gửi hóa đơn, theo dõi thanh toán."
                },
                "providers": {
                    "title": "🏪 Quản lý Nhà cung cấp",
                    "description": "Module quản lý nhà cung cấp đang được chuẩn bị.\nTính năng: Thêm nhà cung cấp, quản lý hợp đồng, theo dõi thanh toán."
                },
                "analytics": {
                    "title": "📊 Bảng điều khiển Phân tích",
                    "description": "Module phân tích đang được chuẩn bị.\nTính năng: Báo cáo tài chính, biểu đồ, thông tin kinh doanh."
                },
                "transactions": {
                    "title": "💳 Quản lý Giao dịch",
                    "description": "Module giao dịch đang được chuẩn bị.\nTính năng: Ghi nhận giao dịch, phân loại chi phí, theo dõi thu nhập."
                },
                "reports": {
                    "title": "📈 Báo cáo & Phân tích",
                    "description": "Module báo cáo đang được chuẩn bị.\nTính năng: Tạo báo cáo, xuất dữ liệu, phân tích tài chính."
                },
                "coming_soon": "🚧 Sắp ra mắt"
            },
            "buttons": {
                "ok": "Đồng ý",
                "cancel": "Hủy bỏ",
                "save": "Lưu",
                "close": "Đóng",
                "settings": "⚙️ Cài đặt",
                "logout": "🔴 Đăng xuất"
            },
            "messages": {
                "success": "Thành công",
                "error": "Lỗi",
                "warning": "Cảnh báo",
                "info": "Thông tin",
                "coming_soon": "Module này sẽ sớm được cung cấp!",
                "logout_confirm": "Bạn có chắc chắn muốn đăng xuất?\n\nNgười dùng: {user}\nCông ty: {company}"
            }
        }
    
    def get_default_english(self) -> Dict[str, Any]:
        """Get default English translations"""
        return {
            "app": {
                "title": "FinanTidy",
                "name": "FinanTidy",
                "welcome": "Welcome to FinanTidy",
                "subtitle": "Modern financial management system with Viettel eInvoice integration",
                "version": "FinanTidy v2.0 - Professional Edition with Viettel eInvoice Integration"
            },
            "common": {
                "ok": "OK",
                "cancel": "Cancel",
                "yes": "Yes",
                "no": "No",
                "save": "Save",
                "close": "Close",
                "apply": "Apply",
                "reset": "Reset",
                "confirm": "Confirm",
                "warning": "Warning",
                "error": "Error",
                "success": "Success",
                "info": "Information"
            },
            "login": {
                "title": "FinanTidy Login",
                "form_title": "Sign in to your account",
                "username_label": "Username",
                "username": "Username",
                "username_placeholder": "Enter your username",
                "password_label": "Password",
                "password": "Password",
                "password_placeholder": "Enter your password",
                "remember_me": "Remember me",
                "forgot_password": "Forgot password?",
                "login_button": "Sign In",
                "cancel_button": "❌ CANCEL",
                "demo_title": "🔑 Default Login Credentials",
                "demo_info": "Username: admin  •  Password: admin",
                "error_title": "Login Failed",
                "error_message": "Invalid username or password!",
                "default_credentials": "Default credentials:",
                "login_error": "Login Error",
                "login_failed": "Login Failed",
            },
            "login": {
                "title": "FinanTidy Login",
                "username": "Username",
                "username_placeholder": "Enter your username",
                "password": "Password",
                "password_placeholder": "Enter your password",
                "remember_me": "Remember me",
                "forgot_password": "Forgot Password?",
                "login_button": "🔐 SIGN IN",
                "cancel_button": "❌ CANCEL",
                "cancel_button": "❌ CANCEL",
                "demo_title": "🔑 Default Login Credentials",
                "demo_info": "Username: admin  •  Password: admin",
                "login_error": "Login Error",
                "login_failed": "Login Failed",
                "invalid_credentials": "Invalid username or password!",
                "fill_all_fields": "Please enter both username and password",
                "signing_in": "Signing In..."
            },
            "navigation": {
                "dashboard": "Dashboard",
                "invoices": "Invoices",
                "providers": "Providers",
                "analytics": "Analytics",
                "transactions": "Transactions",
                "reports": "Reports"
            },
            "dashboard": {
                "welcome": "Welcome back, {name}!",
                "welcome_subtitle": "Here's what's happening with your finances today",
                "recent_activity": "Recent Activity",
                "quick_actions": "Quick Actions",
                "quick_overview": "QUICK OVERVIEW",
                "view_all": "View All",
                "total_invoices": "Total Invoices",
                "providers": "Providers",
                "demo_user": "Demo User",
                "demo_company": "Demo Company",
                "stats": {
                    "revenue": "Total Revenue",
                    "pending": "Pending",
                    "invoices": "Total Invoices",
                    "providers": "Providers",
                    "overdue": "Overdue"
                }
            },
            "actions": {
                "create_invoice": "📄 Create Invoice",
                "add_provider": "🏪 Add Provider",
                "record_payment": "💰 Record Payment",
                "generate_report": "📈 Generate Report",
                "viettel_einvoice": "📧 Viettel eInvoice",
                "system_settings": "⚙️ System Settings",
                "view_analytics": "📊 View Analytics"
            },
            "settings": {
                "title": "System Settings",
                "subtitle": "Configure your FinanTidy application preferences",
                "language": "Language",
                "language_desc": "Select interface display language",
                "appearance": "Appearance",
                "notifications": "Notifications",
                "save": "Save Settings",
                "reset": "Reset",
                "cancel": "Cancel",
                "save_success": "Settings saved successfully!",
                "categories": "SETTINGS CATEGORIES",
                "company": "Company",
                "display": "Display",
                "backup": "Backup",
                "security": "Security",
                "invoice": "Invoice",
                "viettel_einvoice": "Viettel eInvoice",
                "language": {
                    "title": "Language Settings",
                    "description": "Choose your preferred language for the application interface",
                    "restart_note": "Note: Some interface elements may require restarting the application to fully update."
                },
                "company": {
                    "title": "Company Information",
                    "description": "Configure your company details for invoices and documents",
                    "name": "Company Name",
                    "address": "Address",
                    "phone": "Phone",
                    "email": "Email"
                },
                "display": {
                    "title": "Display Settings"
                },
                "notifications": {
                    "title": "Notification Settings"
                },
                "backup": {
                    "title": "Backup Settings"
                },
                "security": {
                    "title": "Security Settings"
                },
                "invoice": {
                    "title": "Invoice Settings"
                },
                "viettel_einvoice": {
                    "title": "Viettel eInvoice Settings",
                    "description": "Configure Viettel eInvoice API integration for electronic invoice processing",
                    "connection_status": "Connection Status",
                    "not_configured": "Not Configured",
                    "configuration": "Configuration",
                    "configure": "Configure API",
                    "test_connection": "Test Connection",
                    "import_config": "Import Config",
                    "info": "Information",
                    "info_content": "Viettel eInvoice integration allows you to:\n• Automatically create electronic invoices\n• Submit invoices to tax authorities\n• Track invoice status and validation\n• Comply with Vietnamese e-invoice regulations\n\nContact Viettel for API credentials and configuration details.",
                    "config_title": "Viettel Configuration",
                    "config_message": "Viettel eInvoice configuration window will be available soon!",
                    "test_title": "Test Connection",
                    "test_message": "Connection test functionality will be available after configuration.",
                    "import_title": "Import Viettel Configuration",
                    "import_success_title": "Import Success",
                    "import_success_message": "Configuration imported from: {}"
                },
                "reset_confirm_title": "Reset Settings",
                "reset_confirm_message": "This will reset all settings to their default values.\nAre you sure you want to continue?",
                "reset_success_title": "Reset",
                "reset_success_message": "Settings reset to defaults successfully!"
            },
            "modules": {
                "invoices": {
                    "title": "📄 Invoices Management",
                    "description": "Invoice management module is being prepared.\nFeatures: Create, edit, send invoices, track payments."
                },
                "providers": {
                    "title": "🏪 Providers Management",
                    "description": "Provider management module is being prepared.\nFeatures: Add providers, manage contracts, track payments."
                },
                "analytics": {
                    "title": "📊 Analytics Dashboard",
                    "description": "Analytics module is being prepared.\nFeatures: Financial reports, charts, business insights."
                },
                "transactions": {
                    "title": "💳 Transactions Management",
                    "description": "Transaction module is being prepared.\nFeatures: Record transactions, categorize expenses, track income."
                },
                "reports": {
                    "title": "📈 Reports & Analysis",
                    "description": "Reports module is being prepared.\nFeatures: Generate reports, export data, financial analysis."
                },
                "coming_soon": "🚧 Coming Soon"
            },
            "buttons": {
                "ok": "OK",
                "cancel": "Cancel",
                "save": "Save",
                "close": "Close",
                "settings": "⚙️ Settings",
                "logout": "🔴 Logout"
            },
            "messages": {
                "success": "Success",
                "error": "Error",
                "warning": "Warning",
                "info": "Information",
                "coming_soon": "This module will be available soon!",
                "logout_confirm": "Are you sure you want to logout?\n\nUser: {user}\nCompany: {company}"
            }
        }

# Global language manager instance
_language_manager = None

def get_language_manager() -> LanguageManager:
    """Get global language manager instance"""
    global _language_manager
    if _language_manager is None:
        lang_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'languages')
        _language_manager = LanguageManager(lang_dir)
    return _language_manager

def t(key: str, default: str = None) -> str:
    """Shortcut function for translation"""
    return get_language_manager().t(key, default)
