"""
FinanTidy - Viettel eInvoice Configuration Window
Modern UI for configuring Viettel electronic invoice integration
"""

import customtkinter as ctk
from tkinter import messagebox, filedialog
import json
import os
import sys
from typing import Dict, Any

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.integrations.viettel_einvoice import ViettelEInvoiceService, ViettelEInvoiceConfig

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ViettelConfigWindow(ctk.CTkToplevel):
    """Viettel eInvoice Configuration Window"""
    
    def __init__(self, parent, session_data=None):
        super().__init__(parent)
        
        # Window configuration
        self.title("FinanTidy - Viettel eInvoice Configuration")
        self.geometry("800x600")
        self.transient(parent)
        
        # Session data
        self.session_data = session_data or {}
        self.company_id = self.session_data.get('company_id', 1)
        
        # Configuration file path
        self.config_file = os.path.join(os.path.expanduser('~'), 'FinanTidy', 'viettel_config.json')
        
        # Load existing configuration
        self.config = self.load_configuration()
        
        # Create UI
        self.create_ui()
        
        # Center window
        self.center_window()
    
    def center_window(self):
        """Center window on parent"""
        self.update_idletasks()
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()
        
        x = parent_x + (parent_width // 2) - (800 // 2)
        y = parent_y + (parent_height // 2) - (600 // 2)
        self.geometry(f"800x600+{x}+{y}")
    
    def load_configuration(self) -> Dict[str, Any]:
        """Load Viettel configuration"""
        try:
            return ViettelEInvoiceConfig.load_config(self.config_file)
        except Exception as e:
            print(f"Error loading config: {e}")
            return ViettelEInvoiceConfig.load_config()
    
    def create_ui(self):
        """Create configuration interface"""
        # Main container
        main_container = ctk.CTkFrame(self, corner_radius=0)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_container)
        
        # Configuration form
        self.create_config_form(main_container)
        
        # Action buttons
        self.create_action_buttons(main_container)
    
    def create_header(self, parent):
        """Create header section"""
        header_frame = ctk.CTkFrame(parent, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 20))
        
        # Title
        title_label = ctk.CTkLabel(
            header_frame,
            text="Viettel eInvoice Configuration",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(side="left")
        
        # Status indicator
        self.status_label = ctk.CTkLabel(
            header_frame,
            text="Not Connected",
            font=ctk.CTkFont(size=14),
            text_color="red"
        )
        self.status_label.pack(side="right")
    
    def create_config_form(self, parent):
        """Create configuration form"""
        # Scrollable frame
        scroll_frame = ctk.CTkScrollableFrame(parent, height=400)
        scroll_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        # Form fields
        self.entries = {}
        
        # API Configuration section
        self.create_section(scroll_frame, "API Configuration")
        
        self.create_field(scroll_frame, "Base URL", "base_url", 
                         placeholder="https://sinvoice.viettel.vn", required=True)
        
        self.create_field(scroll_frame, "Username", "username",
                         placeholder="0100109106-001", required=True)
        
        self.create_field(scroll_frame, "Password", "password", 
                         show="*", required=True)
        
        # Authentication method
        auth_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        auth_frame.pack(fill="x", pady=5)
        
        ctk.CTkLabel(auth_frame, text="Authentication Method *", 
                    font=ctk.CTkFont(weight="bold")).pack(anchor="w")
        
        self.entries["auth_method"] = ctk.CTkOptionMenu(
            auth_frame, 
            values=["token", "basic"],
            width=200
        )
        self.entries["auth_method"].pack(anchor="w", pady=(5, 0))
        
        # Company Information section
        self.create_section(scroll_frame, "Company Information")
        
        self.create_field(scroll_frame, "Tax Code", "supplier_tax_code",
                         placeholder="0100109106", required=True)
        
        self.create_field(scroll_frame, "Company Name", "company_name",
                         placeholder="Your Company Name")
        
        self.create_field(scroll_frame, "Address", "company_address", height=80)
        
        self.create_field(scroll_frame, "Phone", "company_phone")
        
        self.create_field(scroll_frame, "Email", "company_email")
        
        # Invoice Template section
        self.create_section(scroll_frame, "Invoice Template")
        
        self.create_field(scroll_frame, "Template Code", "template_code",
                         placeholder="01GTKT0/001", required=True)
        
        self.create_field(scroll_frame, "Invoice Series", "invoice_series",
                         placeholder="C22T", required=True)
        
        # Bank Information section
        self.create_section(scroll_frame, "Bank Information")
        
        self.create_field(scroll_frame, "Bank Name", "bank_name")
        
        self.create_field(scroll_frame, "Bank Account", "bank_account")
        
        # Populate form with existing data
        self.populate_form()
    
    def create_section(self, parent, title: str):
        """Create a section header"""
        section_frame = ctk.CTkFrame(parent, fg_color="transparent")
        section_frame.pack(fill="x", pady=(20, 10))
        
        section_label = ctk.CTkLabel(
            section_frame,
            text=title,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        section_label.pack(anchor="w")
        
        # Separator line
        separator = ctk.CTkFrame(section_frame, height=2)
        separator.pack(fill="x", pady=(5, 0))
    
    def create_field(self, parent, label: str, key: str, 
                    placeholder: str = "", required: bool = False, 
                    show: str = None, height: int = None):
        """Create a form field"""
        field_frame = ctk.CTkFrame(parent, fg_color="transparent")
        field_frame.pack(fill="x", pady=5)
        
        label_text = label + (" *" if required else "")
        ctk.CTkLabel(field_frame, text=label_text, 
                    font=ctk.CTkFont(weight="bold")).pack(anchor="w")
        
        if height and height > 40:
            # Text area
            self.entries[key] = ctk.CTkTextbox(field_frame, height=height)
        else:
            # Single line entry
            self.entries[key] = ctk.CTkEntry(
                field_frame, 
                width=500, 
                placeholder_text=placeholder,
                show=show
            )
        
        self.entries[key].pack(anchor="w", pady=(5, 0))
    
    def populate_form(self):
        """Populate form with existing configuration"""
        for key, widget in self.entries.items():
            value = self.config.get(key, "")
            
            if isinstance(widget, ctk.CTkTextbox):
                widget.delete("1.0", "end")
                widget.insert("1.0", str(value))
            elif isinstance(widget, ctk.CTkOptionMenu):
                if value in widget.cget("values"):
                    widget.set(value)
            else:
                widget.delete(0, "end")
                widget.insert(0, str(value))
    
    def create_action_buttons(self, parent):
        """Create action buttons"""
        button_frame = ctk.CTkFrame(parent, fg_color="transparent")
        button_frame.pack(fill="x", pady=(10, 0))
        
        # Test connection button
        test_btn = ctk.CTkButton(
            button_frame,
            text="Test Connection",
            command=self.test_connection,
            width=150
        )
        test_btn.pack(side="left", padx=(0, 10))
        
        # Save configuration button
        save_btn = ctk.CTkButton(
            button_frame,
            text="Save Configuration",
            command=self.save_configuration,
            width=150
        )
        save_btn.pack(side="left", padx=(0, 10))
        
        # Load from file button
        load_btn = ctk.CTkButton(
            button_frame,
            text="Load from File",
            command=self.load_from_file,
            width=150,
            fg_color="gray"
        )
        load_btn.pack(side="left", padx=(0, 10))
        
        # Export configuration button
        export_btn = ctk.CTkButton(
            button_frame,
            text="Export Config",
            command=self.export_configuration,
            width=150,
            fg_color="gray"
        )
        export_btn.pack(side="left")
        
        # Close button
        close_btn = ctk.CTkButton(
            button_frame,
            text="Close",
            command=self.destroy,
            width=100,
            fg_color="red"
        )
        close_btn.pack(side="right")
    
    def collect_form_data(self) -> Dict[str, Any]:
        """Collect data from form"""
        data = {}
        
        for key, widget in self.entries.items():
            if isinstance(widget, ctk.CTkTextbox):
                data[key] = widget.get("1.0", "end").strip()
            elif isinstance(widget, ctk.CTkOptionMenu):
                data[key] = widget.get()
            else:
                data[key] = widget.get().strip()
        
        return data
    
    def validate_form(self, data: Dict[str, Any]) -> bool:
        """Validate form data"""
        required_fields = [
            "base_url", "username", "password", 
            "supplier_tax_code", "template_code", "invoice_series"
        ]
        
        for field in required_fields:
            if not data.get(field):
                messagebox.showerror(
                    "Validation Error",
                    f"Field '{field.replace('_', ' ').title()}' is required!"
                )
                return False
        
        return True
    
    def test_connection(self):
        """Test connection to Viettel API"""
        data = self.collect_form_data()
        
        if not self.validate_form(data):
            return
        
        try:
            # Show loading
            self.status_label.configure(text="Testing...", text_color="orange")
            self.update()
            
            # Test authentication
            service = ViettelEInvoiceService(data)
            success = service.authenticate()
            
            if success:
                self.status_label.configure(text="Connected", text_color="green")
                messagebox.showinfo(
                    "Connection Test",
                    "Successfully connected to Viettel eInvoice API!\n\n"
                    "Your configuration is valid and ready to use."
                )
            else:
                self.status_label.configure(text="Connection Failed", text_color="red")
                messagebox.showerror(
                    "Connection Test",
                    "Failed to connect to Viettel eInvoice API.\n\n"
                    "Please check your credentials and configuration."
                )
                
        except Exception as e:
            self.status_label.configure(text="Error", text_color="red")
            messagebox.showerror(
                "Connection Error",
                f"Error testing connection:\n{str(e)}"
            )
    
    def save_configuration(self):
        """Save configuration to file"""
        data = self.collect_form_data()
        
        if not self.validate_form(data):
            return
        
        try:
            # Ensure config directory exists
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            
            # Save configuration
            ViettelEInvoiceConfig.save_config(data, self.config_file)
            
            # Update current config
            self.config = data
            
            messagebox.showinfo(
                "Configuration Saved",
                f"Configuration saved successfully!\n\nFile: {self.config_file}"
            )
            
        except Exception as e:
            messagebox.showerror(
                "Save Error",
                f"Failed to save configuration:\n{str(e)}"
            )
    
    def load_from_file(self):
        """Load configuration from file"""
        file_path = filedialog.askopenfilename(
            title="Load Viettel Configuration",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                self.config = ViettelEInvoiceConfig.load_config(file_path)
                self.populate_form()
                
                messagebox.showinfo(
                    "Configuration Loaded",
                    f"Configuration loaded from:\n{file_path}"
                )
                
            except Exception as e:
                messagebox.showerror(
                    "Load Error",
                    f"Failed to load configuration:\n{str(e)}"
                )
    
    def export_configuration(self):
        """Export configuration to file"""
        data = self.collect_form_data()
        
        file_path = filedialog.asksaveasfilename(
            title="Export Viettel Configuration",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                ViettelEInvoiceConfig.save_config(data, file_path)
                
                messagebox.showinfo(
                    "Configuration Exported",
                    f"Configuration exported to:\n{file_path}"
                )
                
            except Exception as e:
                messagebox.showerror(
                    "Export Error",
                    f"Failed to export configuration:\n{str(e)}"
                )


def main():
    """Test function"""
    root = ctk.CTk()
    root.withdraw()  # Hide root window
    
    config_window = ViettelConfigWindow(root)
    config_window.mainloop()

if __name__ == "__main__":
    main()
