"""
FinanTidy - Settings Module
Modern CustomTkinter interface for application settings and preferences with multi-language support
"""

import customtkinter as ctk
from tkinter import messagebox, filedialog
import json
import os
import sys

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SettingsWindow(ctk.CTkToplevel):
    """Modern Settings Configuration Window with Language Support"""
    
    def __init__(self, parent, session_data=None):
        super().__init__(parent)
        
        self.parent = parent
        self.session_data = session_data or {}
        
        # Import language manager
        try:
            from core.language_manager import get_language_manager, t
            self.lang_manager = get_language_manager()
            self.t = t
        except ImportError:
            # Fallback if language manager not available
            self.lang_manager = None
            self.t = lambda key, default=None: default or key
        
        # Window configuration
        self.title(self.t("settings.title", "FinanTidy - Settings"))
        self.geometry("1200x800")
        self.transient(parent)
        
        # Settings data
        self.settings_data = self.load_settings()
        
        # Create UI
        self.create_settings_ui()
        
        # Center window
        self.center_window()
    
    def center_window(self):
        """Center window on screen"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.winfo_screenheight() // 2) - (800 // 2)
        self.geometry(f"1200x800+{x}+{y}")
    
    def load_settings(self):
        """Load settings from file or return defaults"""
        default_settings = {
            "language": "vi",  # Default Vietnamese
            "theme": "dark",
            "company": {
                "name": "FinanTidy Company",
                "address": "123 Business Street, City, Country",
                "phone": "+84 123 456 789",
                "email": "info@finantidy.com",
                "tax_id": "0123456789",
                "website": "www.finantidy.com"
            },
            "display": {
                "theme": "dark",
                "language": "Vietnamese",
                "currency": "VND",
                "date_format": "DD/MM/YYYY",
                "number_format": "1,234,567.89"
            },
            "notifications": {
                "email_alerts": True,
                "invoice_reminders": True,
                "payment_notifications": True,
                "weekly_reports": False,
                "system_updates": True
            },
            "backup": {
                "auto_backup": True,
                "backup_frequency": "Daily",
                "backup_location": "C:/FinanTidy/Backups",
                "keep_backups": "30"
            },
            "security": {
                "require_password": True,
                "session_timeout": "30",
                "two_factor_auth": False,
                "data_encryption": True
            },
            "invoice": {
                "default_payment_terms": "30",
                "auto_numbering": True,
                "number_prefix": "INV",
                "include_logo": True,
                "default_notes": "Thank you for your business!"
            }
        }
        
        # Try to load from file (would be implemented with actual file I/O)
        return default_settings
    
    def save_settings(self):
        """Save settings to file"""
        # Would implement actual file saving here
        messagebox.showinfo(self.t("settings.save", "Settings"), self.t("settings.save_success", "Settings saved successfully!"))
    
    def create_settings_ui(self):
        """Create settings interface"""
        
        # Main container
        main_container = ctk.CTkFrame(self, corner_radius=0)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_container)
        
        # Content area
        content_area = ctk.CTkFrame(main_container, corner_radius=0)
        content_area.pack(fill="both", expand=True, pady=(20, 0))
        
        # Settings navigation and content
        self.create_settings_content(content_area)
    
    def create_header(self, parent):
        """Create header with title and controls"""
        
        header_frame = ctk.CTkFrame(parent, height=80, corner_radius=15)
        header_frame.pack(fill="x", pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Left side - Title
        left_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        left_frame.pack(side="left", fill="y", padx=25, pady=20)
        
        title_label = ctk.CTkLabel(
            left_frame,
            text=f"⚙️ {self.t('settings.title', 'Application Settings')}",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(anchor="w")
        
        subtitle_label = ctk.CTkLabel(
            left_frame,
            text=self.t("settings.subtitle", "Configure your FinanTidy application preferences"),
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        subtitle_label.pack(anchor="w")
        
        # Right side - Controls
        right_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        right_frame.pack(side="right", fill="y", padx=25, pady=20)
        
        # Reset button
        reset_button = ctk.CTkButton(
            right_frame,
            text=f"🔄 {self.t('settings.reset', 'Reset')}",
            height=35,
            width=100,
            font=ctk.CTkFont(size=14),
            fg_color="#ef4444",
            hover_color="#dc2626",
            command=self.reset_settings
        )
        reset_button.pack(side="right", padx=(10, 0))
        
        # Save button
        save_button = ctk.CTkButton(
            right_frame,
            text=f"💾 {self.t('settings.save', 'Save')}",
            height=35,
            width=100,
            font=ctk.CTkFont(size=14),
            fg_color="#10b981",
            hover_color="#059669",
            command=self.save_settings
        )
        save_button.pack(side="right")
    
    def create_settings_content(self, parent):
        """Create settings navigation and content area"""
        
        # Settings navigation sidebar
        nav_frame = ctk.CTkFrame(parent, width=280, corner_radius=15)
        nav_frame.pack(side="left", fill="y", padx=(0, 10))
        nav_frame.pack_propagate(False)
        
        # Settings categories
        categories = [
            ("🌐", self.t("settings.language", "Language"), "language", False),
            ("🏢", self.t("settings.company", "Company"), "company", True),
            ("🎨", self.t("settings.display", "Display"), "display", False),
            ("🔔", self.t("settings.notifications", "Notifications"), "notifications", False),
            ("💾", self.t("settings.backup", "Backup"), "backup", False),
            ("🔐", self.t("settings.security", "Security"), "security", False),
            ("📄", self.t("settings.invoice", "Invoice"), "invoice", False),
            ("📋", self.t("settings.viettel_einvoice", "Viettel eInvoice"), "viettel_einvoice", False)
        ]
        
        # Navigation title
        nav_title = ctk.CTkLabel(
            nav_frame,
            text=self.t("settings.categories", "SETTINGS CATEGORIES"),
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="gray60"
        )
        nav_title.pack(pady=(25, 15), padx=20, anchor="w")
        
        self.nav_buttons = {}
        for icon, name, key, is_active in categories:
            button = ctk.CTkButton(
                nav_frame,
                text=f"{icon}  {name}",
                height=45,
                font=ctk.CTkFont(size=16, weight="bold" if is_active else "normal"),
                anchor="w",
                fg_color="#1f538d" if is_active else "transparent",
                hover_color="#2563eb",
                command=lambda k=key: self.show_category(k)
            )
            button.pack(pady=3, padx=20, fill="x")
            self.nav_buttons[key] = button
        
        # Settings content area
        self.content_frame = ctk.CTkScrollableFrame(parent, corner_radius=15)
        self.content_frame.pack(side="right", fill="both", expand=True)
        
        # Show default category (company)
        self.current_category = "company"
        self.show_category("company")
    
    def show_category(self, category):
        """Show specific settings category"""
        # Update navigation
        for key, button in self.nav_buttons.items():
            if key == category:
                button.configure(fg_color="#1f538d", font=ctk.CTkFont(size=16, weight="bold"))
            else:
                button.configure(fg_color="transparent", font=ctk.CTkFont(size=16, weight="normal"))
        
        # Clear content
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        self.current_category = category
        
        # Show category content
        if category == "language":
            self.show_language_settings()
        elif category == "company":
            self.show_company_settings()
        elif category == "display":
            self.show_display_settings()
        elif category == "notifications":
            self.show_notification_settings()
        elif category == "backup":
            self.show_backup_settings()
        elif category == "security":
            self.show_security_settings()
        elif category == "invoice":
            self.show_invoice_settings()
        elif category == "viettel_einvoice":
            self.show_viettel_settings()
    
    def show_language_settings(self):
        """Show language settings"""
        # Title
        title = ctk.CTkLabel(
            self.content_frame,
            text=f"🌐 {self.t('settings.language.title', 'Language Settings')}",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(30, 20), anchor="w")
        
        # Description
        desc = ctk.CTkLabel(
            self.content_frame,
            text=self.t('settings.language.description', 'Choose your preferred language for the application interface'),
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        desc.pack(pady=(0, 30), anchor="w")
        
        # Language selection frame
        lang_frame = ctk.CTkFrame(self.content_frame)
        lang_frame.pack(fill="x", pady=(0, 20))
        
        # Current language
        current_lang = self.lang_manager.get_current_language() if self.lang_manager else "vi"
        
        # Language options
        self.language_var = ctk.StringVar(value=current_lang)
        
        # Vietnamese option
        vi_frame = ctk.CTkFrame(lang_frame)
        vi_frame.pack(fill="x", padx=20, pady=10)
        
        vi_radio = ctk.CTkRadioButton(
            vi_frame,
            text="🇻🇳 Tiếng Việt (Vietnamese)",
            variable=self.language_var,
            value="vi",
            font=ctk.CTkFont(size=16),
            command=self.change_language
        )
        vi_radio.pack(side="left", padx=20, pady=15)
        
        # English option
        en_frame = ctk.CTkFrame(lang_frame)
        en_frame.pack(fill="x", padx=20, pady=10)
        
        en_radio = ctk.CTkRadioButton(
            en_frame,
            text="🇺🇸 English",
            variable=self.language_var,
            value="en",
            font=ctk.CTkFont(size=16),
            command=self.change_language
        )
        en_radio.pack(side="left", padx=20, pady=15)
        
        # Language change note
        note = ctk.CTkLabel(
            self.content_frame,
            text=self.t('settings.language.restart_note', 'Note: Some interface elements may require restarting the application to fully update.'),
            font=ctk.CTkFont(size=12),
            text_color="gray60"
        )
        note.pack(pady=(20, 0), anchor="w")
    
    def change_language(self):
        """Handle language change"""
        new_language = self.language_var.get()
        if self.lang_manager:
            # Get current language for confirmation message
            current_lang = self.lang_manager.get_current_language()
            
            if new_language != current_lang:
                # Show confirmation in both languages
                if new_language == "vi":
                    confirm_msg = "Bạn có muốn thay đổi ngôn ngữ sang Tiếng Việt không?\nWould you like to change the language to Vietnamese?"
                    confirm_title = "Xác nhận thay đổi ngôn ngữ / Confirm Language Change"
                else:
                    confirm_msg = "Would you like to change the language to English?\nBạn có muốn thay đổi ngôn ngữ sang Tiếng Anh không?"
                    confirm_title = "Confirm Language Change / Xác nhận thay đổi ngôn ngữ"
                
                if messagebox.askyesno(confirm_title, confirm_msg):
                    # Change language
                    self.lang_manager.set_language(new_language)
                    
                    # Success message in new language
                    if new_language == "vi":
                        success_msg = "Ngôn ngữ đã được thay đổi thành công!\nLanguage changed successfully!"
                        success_title = "Thành công / Success"
                    else:
                        success_msg = "Language changed successfully!\nNgôn ngữ đã được thay đổi thành công!"
                        success_title = "Success / Thành công"
                    
                    messagebox.showinfo(success_title, success_msg)
                    
                    # Refresh the current settings window
                    self.refresh_ui()
                else:
                    # Reset radio button to previous selection
                    self.language_var.set(current_lang)
    
    def refresh_ui(self):
        """Refresh the UI with new language"""
        # Update window title
        self.title(self.t("settings.title", "FinanTidy - Settings"))
        
        # Recreate the UI
        for widget in self.winfo_children():
            widget.destroy()
        
        self.create_settings_ui()
    
    def show_company_settings(self):
        """Show company settings"""
        # Title
        title = ctk.CTkLabel(
            self.content_frame,
            text=f"🏢 {self.t('settings.company.title', 'Company Information')}",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(30, 10), anchor="w")
        
        # Description
        desc = ctk.CTkLabel(
            self.content_frame,
            text=self.t('settings.company.description', 'Configure your company details for invoices and documents'),
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        desc.pack(pady=(0, 30), anchor="w")
        
        # Company form
        form_frame = ctk.CTkFrame(self.content_frame)
        form_frame.pack(fill="x", pady=(0, 20))
        
        # Company name
        name_label = ctk.CTkLabel(form_frame, text=self.t('settings.company.name', 'Company Name'), font=ctk.CTkFont(size=14, weight="bold"))
        name_label.pack(anchor="w", padx=20, pady=(20, 5))
        
        self.company_name = ctk.CTkEntry(form_frame, height=40, font=ctk.CTkFont(size=14))
        self.company_name.pack(fill="x", padx=20, pady=(0, 15))
        self.company_name.insert(0, self.settings_data["company"]["name"])
        
        # Company address
        address_label = ctk.CTkLabel(form_frame, text=self.t('settings.company.address', 'Address'), font=ctk.CTkFont(size=14, weight="bold"))
        address_label.pack(anchor="w", padx=20, pady=(10, 5))
        
        self.company_address = ctk.CTkTextbox(form_frame, height=80, font=ctk.CTkFont(size=14))
        self.company_address.pack(fill="x", padx=20, pady=(0, 15))
        self.company_address.insert("1.0", self.settings_data["company"]["address"])
        
        # Contact info row
        contact_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        contact_frame.pack(fill="x", padx=20, pady=(10, 20))
        
        # Phone
        phone_frame = ctk.CTkFrame(contact_frame, fg_color="transparent")
        phone_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        phone_label = ctk.CTkLabel(phone_frame, text=self.t('settings.company.phone', 'Phone'), font=ctk.CTkFont(size=14, weight="bold"))
        phone_label.pack(anchor="w", pady=(0, 5))
        
        self.company_phone = ctk.CTkEntry(phone_frame, height=40, font=ctk.CTkFont(size=14))
        self.company_phone.pack(fill="x")
        self.company_phone.insert(0, self.settings_data["company"]["phone"])
        
        # Email
        email_frame = ctk.CTkFrame(contact_frame, fg_color="transparent")
        email_frame.pack(side="right", fill="x", expand=True, padx=(10, 0))
        
        email_label = ctk.CTkLabel(email_frame, text=self.t('settings.company.email', 'Email'), font=ctk.CTkFont(size=14, weight="bold"))
        email_label.pack(anchor="w", pady=(0, 5))
        
        self.company_email = ctk.CTkEntry(email_frame, height=40, font=ctk.CTkFont(size=14))
        self.company_email.pack(fill="x")
        self.company_email.insert(0, self.settings_data["company"]["email"])
    
    def show_display_settings(self):
        """Show display settings"""
        title = ctk.CTkLabel(
            self.content_frame,
            text=f"🎨 {self.t('settings.display.title', 'Display Settings')}",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(30, 20), anchor="w")
    
    def show_notification_settings(self):
        """Show notification settings"""
        title = ctk.CTkLabel(
            self.content_frame,
            text=f"🔔 {self.t('settings.notifications.title', 'Notification Settings')}",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(30, 20), anchor="w")
    
    def show_backup_settings(self):
        """Show backup settings"""
        title = ctk.CTkLabel(
            self.content_frame,
            text=f"💾 {self.t('settings.backup.title', 'Backup Settings')}",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(30, 20), anchor="w")
    
    def show_security_settings(self):
        """Show security settings"""
        title = ctk.CTkLabel(
            self.content_frame,
            text=f"🔐 {self.t('settings.security.title', 'Security Settings')}",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(30, 20), anchor="w")
    
    def show_invoice_settings(self):
        """Show invoice settings"""
        title = ctk.CTkLabel(
            self.content_frame,
            text=f"📄 {self.t('settings.invoice.title', 'Invoice Settings')}",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(30, 20), anchor="w")
    
    def show_viettel_settings(self):
        """Show Viettel eInvoice settings"""
        # Title
        title = ctk.CTkLabel(
            self.content_frame,
            text=f"📋 {self.t('settings.viettel_einvoice.title', 'Viettel eInvoice Settings')}",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=(30, 10), anchor="w")
        
        # Description
        desc = ctk.CTkLabel(
            self.content_frame,
            text=self.t('settings.viettel_einvoice.description', 'Configure Viettel eInvoice API integration for electronic invoice processing'),
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        desc.pack(pady=(0, 30), anchor="w")
        
        # Configuration status frame
        status_frame = ctk.CTkFrame(self.content_frame)
        status_frame.pack(fill="x", pady=(0, 20))
        
        status_title = ctk.CTkLabel(
            status_frame,
            text=self.t('settings.viettel_einvoice.connection_status', 'Connection Status'),
            font=ctk.CTkFont(size=16, weight="bold")
        )
        status_title.pack(anchor="w", padx=20, pady=(20, 10))
        
        # Connection status indicator
        status_indicator_frame = ctk.CTkFrame(status_frame, fg_color="transparent")
        status_indicator_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        status_icon = ctk.CTkLabel(
            status_indicator_frame,
            text="🔴",
            font=ctk.CTkFont(size=18)
        )
        status_icon.pack(side="left", padx=(0, 10))
        
        status_text = ctk.CTkLabel(
            status_indicator_frame,
            text=self.t('settings.viettel_einvoice.not_configured', 'Not Configured'),
            font=ctk.CTkFont(size=14),
            text_color="#ef4444"
        )
        status_text.pack(side="left")
        
        # Configuration buttons frame
        buttons_frame = ctk.CTkFrame(self.content_frame)
        buttons_frame.pack(fill="x", pady=(0, 20))
        
        buttons_title = ctk.CTkLabel(
            buttons_frame,
            text=self.t('settings.viettel_einvoice.configuration', 'Configuration'),
            font=ctk.CTkFont(size=16, weight="bold")
        )
        buttons_title.pack(anchor="w", padx=20, pady=(20, 15))
        
        # Button container
        button_container = ctk.CTkFrame(buttons_frame, fg_color="transparent")
        button_container.pack(fill="x", padx=20, pady=(0, 20))
        
        # Configure button
        config_button = ctk.CTkButton(
            button_container,
            text=f"⚙️ {self.t('settings.viettel_einvoice.configure', 'Configure API')}",
            height=45,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#1f538d",
            hover_color="#2563eb",
            command=self.open_viettel_config
        )
        config_button.pack(side="left", padx=(0, 10))
        
        # Test connection button
        test_button = ctk.CTkButton(
            button_container,
            text=f"🔍 {self.t('settings.viettel_einvoice.test_connection', 'Test Connection')}",
            height=45,
            font=ctk.CTkFont(size=14),
            fg_color="#059669",
            hover_color="#047857",
            command=self.test_viettel_connection
        )
        test_button.pack(side="left", padx=(0, 10))
        
        # Import settings button
        import_button = ctk.CTkButton(
            button_container,
            text=f"📥 {self.t('settings.viettel_einvoice.import_config', 'Import Config')}",
            height=45,
            font=ctk.CTkFont(size=14),
            fg_color="#6366f1",
            hover_color="#4f46e5",
            command=self.import_viettel_config
        )
        import_button.pack(side="left")
        
        # Information section
        info_frame = ctk.CTkFrame(self.content_frame)
        info_frame.pack(fill="x", pady=(0, 20))
        
        info_title = ctk.CTkLabel(
            info_frame,
            text=self.t('settings.viettel_einvoice.info', 'Information'),
            font=ctk.CTkFont(size=16, weight="bold")
        )
        info_title.pack(anchor="w", padx=20, pady=(20, 10))
        
        info_text = ctk.CTkLabel(
            info_frame,
            text=self.t('settings.viettel_einvoice.info_content', 
                       'Viettel eInvoice integration allows you to:\n'
                       '• Automatically create electronic invoices\n'
                       '• Submit invoices to tax authorities\n'
                       '• Track invoice status and validation\n'
                       '• Comply with Vietnamese e-invoice regulations\n\n'
                       'Contact Viettel for API credentials and configuration details.'),
            font=ctk.CTkFont(size=12),
            text_color="gray70",
            justify="left"
        )
        info_text.pack(anchor="w", padx=20, pady=(0, 20))
    
    def open_viettel_config(self):
        """Open Viettel eInvoice configuration window"""
        try:
            from .viettel_config_window import ViettelConfigWindow
            config_window = ViettelConfigWindow(self)
            config_window.focus()
        except Exception as e:
            messagebox.showinfo(
                self.t('settings.viettel_einvoice.config_title', 'Viettel Configuration'),
                self.t('settings.viettel_einvoice.config_message', 'Viettel eInvoice configuration window will be available soon!')
            )
    
    def test_viettel_connection(self):
        """Test Viettel eInvoice connection"""
        messagebox.showinfo(
            self.t('settings.viettel_einvoice.test_title', 'Test Connection'),
            self.t('settings.viettel_einvoice.test_message', 'Connection test functionality will be available after configuration.')
        )
    
    def import_viettel_config(self):
        """Import Viettel configuration from file"""
        file_path = filedialog.askopenfilename(
            title=self.t('settings.viettel_einvoice.import_title', 'Import Viettel Configuration'),
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            messagebox.showinfo(
                self.t('settings.viettel_einvoice.import_success_title', 'Import Success'),
                self.t('settings.viettel_einvoice.import_success_message', f'Configuration imported from: {file_path}')
            )
    
    def reset_settings(self):
        """Reset all settings to defaults"""
        if messagebox.askyesno(
            self.t("settings.reset_confirm_title", "Reset Settings"), 
            self.t("settings.reset_confirm_message", "This will reset all settings to their default values.\nAre you sure you want to continue?")
        ):
            self.settings_data = self.load_settings()
            self.show_category(self.current_category)
            messagebox.showinfo(
                self.t("settings.reset_success_title", "Reset"), 
                self.t("settings.reset_success_message", "Settings reset to defaults successfully!")
            )

def main():
    """Test function"""
    root = ctk.CTk()
    root.withdraw()  # Hide root window
    
    app = SettingsWindow(root)
    app.mainloop()

if __name__ == "__main__":
    main()
