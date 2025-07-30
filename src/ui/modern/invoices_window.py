"""
FinanTidy - Invoices Management Module
Modern CustomTkinter interface with database integration and Viettel eInvoice support
"""

import customtkinter as ctk
from tkinter import messagebox, filedialog
import datetime
from pathlib import Path
import json
import os
import sys

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Import database services
try:
    from ...database.business_services import get_invoice_service, get_provider_service
except ImportError:
    try:
        from src.database.business_services import get_invoice_service, get_provider_service
    except ImportError:
        # Mock for testing
        def get_invoice_service(company_id):
            return None
        def get_provider_service(company_id):
            return None

# Import Viettel eInvoice integration
try:
    from src.integrations.viettel_einvoice import ViettelEInvoiceService, ViettelEInvoiceConfig
    from src.ui.modern.viettel_config_window import ViettelConfigWindow
    VIETTEL_AVAILABLE = True
except ImportError as e:
    print(f"Viettel eInvoice integration not available: {e}")
    VIETTEL_AVAILABLE = False

class InvoicesWindow(ctk.CTkToplevel):
    """Modern Invoices Management Window with Database Integration"""
    
    def __init__(self, parent):
        super().__init__(parent)
        
        # Window configuration
        self.title("FinanTidy - Invoices Management")
        self.geometry("1400x800")
        self.transient(parent)
        
        # Get session data from parent
        self.session_data = getattr(parent, 'session_data', {
            'company_id': 1, 'user_id': 1, 'company_name': 'Demo Company'
        })
        
        # Database services
        try:
            self.invoice_service = get_invoice_service(self.session_data['company_id'])
            self.provider_service = get_provider_service(self.session_data['company_id'])
        except Exception as e:
            print(f"Database service error: {e}")
            self.invoice_service = None
            self.provider_service = None
        
        # Load invoice data
        self.invoices_data = self.load_invoices_data()
        
        # Selected invoice
        self.selected_invoice = None
        
        # Create UI
        self.create_invoices_ui()
        
        # Center window
        self.center_window()
    
    def center_window(self):
        """Center window on screen"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (1400 // 2)
        y = (self.winfo_screenheight() // 2) - (800 // 2)
        self.geometry(f"1400x800+{x}+{y}")
    
    def load_invoices_data(self):
        """Load invoice data from database"""
        try:
            if self.invoice_service:
                invoices, total_count = self.invoice_service.get_all_invoices(limit=100)
                return invoices
            else:
                # Fallback to sample data
                return self.load_sample_data()
        except Exception as e:
            print(f"Error loading invoices: {e}")
            return self.load_sample_data()
    
    def load_sample_data(self):
        """Load sample invoice data for testing"""
        return [
            {
                "id": 1,
                "invoice_number": "INV-2025-001",
                "invoice_date": "2025-01-28",
                "due_date": "2025-02-28",
                "description": "Marketing services - January 2025",
                "total_amount": 8500000,
                "paid_amount": 0,
                "remaining_amount": 8500000,
                "status": "sent",
                "is_overdue": False,
                "provider_name": "ABC Company Ltd.",
                "currency": "VND"
            },
            {
                "id": 2,
                "invoice_number": "INV-2025-002",
                "invoice_date": "2025-01-25",
                "due_date": "2025-02-25",
                "description": "Software development services",
                "total_amount": 12300000,
                "paid_amount": 12300000,
                "remaining_amount": 0,
                "status": "paid",
                "is_overdue": False,
                "provider_name": "XYZ Corporation",
                "currency": "VND"
            },
            {
                "id": 3,
                "invoice_number": "INV-2025-003",
                "invoice_date": "2024-12-15",
                "due_date": "2025-01-15",
                "description": "Office supplies and equipment",
                "total_amount": 3200000,
                "paid_amount": 0,
                "remaining_amount": 3200000,
                "status": "sent",
                "is_overdue": True,
                "provider_name": "Office Supply Co.",
                "currency": "VND"
            },
            {
                "id": 4,
                "invoice_number": "INV-2025-004",
                "invoice_date": "2025-01-30",
                "due_date": "2025-03-01",
                "description": "Legal consultation services",
                "total_amount": 7500000,
                "paid_amount": 0,
                "remaining_amount": 7500000,
                "status": "draft",
                "is_overdue": False,
                "provider_name": "Legal Advisory Ltd.",
                "currency": "VND"
            }
        ]
    
    def create_invoices_ui(self):
        """Create invoices management interface"""
        
        # Main container
        main_container = ctk.CTkFrame(self, corner_radius=0)
        main_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_container)
        
        # Content area
        content_frame = ctk.CTkFrame(main_container, corner_radius=0, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, pady=(20, 0))
        
        # Configure grid
        content_frame.grid_columnconfigure(0, weight=1)
        content_frame.grid_columnconfigure(1, weight=1)
        content_frame.grid_rowconfigure(0, weight=1)
        
        # Left panel - Invoices list
        self.create_invoices_list(content_frame)
        
        # Right panel - Invoice details
        self.create_invoice_details(content_frame)
    
    def create_header(self, parent):
        """Create header with title and actions"""
        
        header_frame = ctk.CTkFrame(parent, height=80, corner_radius=15)
        header_frame.pack(fill="x", pady=(0, 20))
        header_frame.pack_propagate(False)
        
        # Left side - Title and stats
        left_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        left_frame.pack(side="left", fill="y", padx=25, pady=20)
        
        title_label = ctk.CTkLabel(
            left_frame,
            text="📄 Invoices Management",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(anchor="w")
        
        stats_label = ctk.CTkLabel(
            left_frame,
            text=f"Total: {len(self.invoices_data)} invoices • Value: ₫{sum(inv['amount'] for inv in self.invoices_data):,}",
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        stats_label.pack(anchor="w")
        
        # Right side - Action buttons
        right_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        right_frame.pack(side="right", fill="y", padx=25, pady=20)
        
        # New invoice button
        new_button = ctk.CTkButton(
            right_frame,
            text="+ New Invoice",
            height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.create_new_invoice
        )
        new_button.pack(side="right", padx=(10, 0))
        
        # Viettel eInvoice config button (if available)
        if VIETTEL_AVAILABLE:
            viettel_config_button = ctk.CTkButton(
                right_frame,
                text="⚙️ eInvoice Config",
                height=40,
                width=140,
                font=ctk.CTkFont(size=14),
                fg_color="#8b5cf6",
                hover_color="#7c3aed",
                command=self.open_viettel_config
            )
            viettel_config_button.pack(side="right", padx=(10, 0))
        
        # Export button
        export_button = ctk.CTkButton(
            right_frame,
            text="📊 Export",
            height=40,
            width=100,
            font=ctk.CTkFont(size=14),
            fg_color="#10b981",
            hover_color="#059669",
            command=self.export_invoices
        )
        export_button.pack(side="right", padx=(10, 0))
        
        # Filter button
        filter_button = ctk.CTkButton(
            right_frame,
            text="🔍 Filter",
            height=40,
            width=100,
            font=ctk.CTkFont(size=14),
            fg_color="#f59e0b",
            hover_color="#d97706",
            command=self.show_filter
        )
        filter_button.pack(side="right")
    
    def create_invoices_list(self, parent):
        """Create invoices list panel"""
        
        # Left panel container
        list_container = ctk.CTkFrame(parent, corner_radius=15)
        list_container.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        # List header
        list_header = ctk.CTkFrame(list_container, height=50, corner_radius=0)
        list_header.pack(fill="x", padx=20, pady=(20, 10))
        list_header.pack_propagate(False)
        
        header_title = ctk.CTkLabel(
            list_header,
            text="Invoices List",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        header_title.pack(side="left", pady=15)
        
        # Search frame
        search_frame = ctk.CTkFrame(list_header, fg_color="transparent")
        search_frame.pack(side="right", fill="y", pady=10)
        
        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Search invoices...",
            width=200,
            height=30
        )
        self.search_entry.pack(side="right")
        self.search_entry.bind("<KeyRelease>", self.filter_invoices)
        
        # Scrollable frame for invoices
        self.invoices_scroll = ctk.CTkScrollableFrame(list_container)
        self.invoices_scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Populate invoices list
        self.refresh_invoices_list()
    
    def create_invoice_details(self, parent):
        """Create invoice details panel"""
        
        # Right panel container
        self.details_container = ctk.CTkFrame(parent, corner_radius=15)
        self.details_container.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        # Details header
        details_header = ctk.CTkFrame(self.details_container, height=50, corner_radius=0)
        details_header.pack(fill="x", padx=20, pady=(20, 10))
        details_header.pack_propagate(False)
        
        self.details_title = ctk.CTkLabel(
            details_header,
            text="Invoice Details",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.details_title.pack(side="left", pady=15)
        
        # Action buttons for selected invoice
        self.action_frame = ctk.CTkFrame(details_header, fg_color="transparent")
        self.action_frame.pack(side="right", fill="y", pady=10)
        
        # Scrollable frame for details
        self.details_scroll = ctk.CTkScrollableFrame(self.details_container)
        self.details_scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Show default message
        self.show_no_selection_message()
    
    def refresh_invoices_list(self, filtered_data=None):
        """Refresh the invoices list"""
        
        # Clear existing items
        for widget in self.invoices_scroll.winfo_children():
            widget.destroy()
        
        # Use filtered data or all data
        data_to_show = filtered_data if filtered_data is not None else self.invoices_data
        
        # Create invoice cards
        for invoice in data_to_show:
            self.create_invoice_card(self.invoices_scroll, invoice)
    
    def create_invoice_card(self, parent, invoice):
        """Create individual invoice card"""
        
        # Card container
        card = ctk.CTkFrame(parent, height=100, corner_radius=12)
        card.pack(fill="x", pady=5)
        card.pack_propagate(False)
        
        # Make card clickable
        card.bind("<Button-1>", lambda e: self.select_invoice(invoice))
        
        # Card content
        content_frame = ctk.CTkFrame(card, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=15, pady=10)
        
        # Left side - Main info
        left_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        left_frame.pack(side="left", fill="both", expand=True)
        
        # Invoice ID
        id_label = ctk.CTkLabel(
            left_frame,
            text=invoice["id"],
            font=ctk.CTkFont(size=16, weight="bold")
        )
        id_label.pack(anchor="w")
        
        # Customer
        customer_label = ctk.CTkLabel(
            left_frame,
            text=invoice["customer"],
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        customer_label.pack(anchor="w")
        
        # Amount and date
        info_label = ctk.CTkLabel(
            left_frame,
            text=f"₫{invoice['amount']:,} • {invoice['date']}",
            font=ctk.CTkFont(size=12),
            text_color="gray60"
        )
        info_label.pack(anchor="w", pady=(5, 0))
        
        # Right side - Status
        right_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        right_frame.pack(side="right", fill="y")
        
        # Status badge
        status_colors = {
            "Paid": "#10b981",
            "Pending": "#f59e0b", 
            "Overdue": "#ef4444",
            "Draft": "#6b7280"
        }
        
        status_badge = ctk.CTkLabel(
            right_frame,
            text=invoice["status"],
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="white",
            corner_radius=8,
            fg_color=status_colors.get(invoice["status"], "#6b7280"),
            width=80,
            height=25
        )
        status_badge.pack(pady=(10, 0))
        
        # Amount
        amount_label = ctk.CTkLabel(
            right_frame,
            text=f"₫{invoice['amount']:,}",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        amount_label.pack(pady=(5, 0))
    
    def select_invoice(self, invoice):
        """Select and display invoice details"""
        self.selected_invoice = invoice
        self.show_invoice_details(invoice)
    
    def show_invoice_details(self, invoice):
        """Display detailed invoice information"""
        
        # Clear existing details
        for widget in self.details_scroll.winfo_children():
            widget.destroy()
        
        # Update title
        self.details_title.configure(text=f"Invoice: {invoice['id']}")
        
        # Clear and recreate action buttons
        for widget in self.action_frame.winfo_children():
            widget.destroy()
        
        # Create eInvoice button (if Viettel integration available)
        if VIETTEL_AVAILABLE:
            einvoice_button = ctk.CTkButton(
                self.action_frame,
                text="📧 eInvoice",
                width=90,
                height=30,
                font=ctk.CTkFont(size=12),
                fg_color="#8b5cf6",
                hover_color="#7c3aed",
                command=lambda: self.create_einvoice(invoice)
            )
            einvoice_button.pack(side="right", padx=(5, 0))
        
        # Edit button
        edit_button = ctk.CTkButton(
            self.action_frame,
            text="✏️ Edit",
            width=80,
            height=30,
            font=ctk.CTkFont(size=12),
            command=lambda: self.edit_invoice(invoice)
        )
        edit_button.pack(side="right", padx=(5, 0))
        
        # Delete button
        delete_button = ctk.CTkButton(
            self.action_frame,
            text="🗑️ Delete",
            width=80,
            height=30,
            font=ctk.CTkFont(size=12),
            fg_color="#ef4444",
            hover_color="#dc2626",
            command=lambda: self.delete_invoice(invoice)
        )
        delete_button.pack(side="right", padx=(5, 0))
        
        # Print button
        print_button = ctk.CTkButton(
            self.action_frame,
            text="🖨️ Print",
            width=80,
            height=30,
            font=ctk.CTkFont(size=12),
            fg_color="#10b981",
            hover_color="#059669",
            command=lambda: self.print_invoice(invoice)
        )
        print_button.pack(side="right")
        
        # Invoice details content
        self.create_invoice_details_content(self.details_scroll, invoice)
    
    def create_invoice_details_content(self, parent, invoice):
        """Create detailed invoice content"""
        
        # Basic information section
        basic_section = ctk.CTkFrame(parent, corner_radius=12)
        basic_section.pack(fill="x", pady=(0, 15))
        
        basic_title = ctk.CTkLabel(
            basic_section,
            text="📋 Basic Information",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        basic_title.pack(anchor="w", padx=20, pady=(15, 10))
        
        # Basic info grid
        basic_grid = ctk.CTkFrame(basic_section, fg_color="transparent")
        basic_grid.pack(fill="x", padx=20, pady=(0, 15))
        
        basic_info = [
            ("Invoice ID:", invoice["id"]),
            ("Customer:", invoice["customer"]),
            ("Amount:", f"₫{invoice['amount']:,}"),
            ("Currency:", invoice["currency"]),
            ("Date:", invoice["date"]),
            ("Due Date:", invoice["due_date"]),
            ("Status:", invoice["status"])
        ]
        
        for i, (label, value) in enumerate(basic_info):
            row = i // 2
            col = i % 2
            
            info_frame = ctk.CTkFrame(basic_grid, fg_color="transparent")
            info_frame.grid(row=row, column=col, sticky="w", padx=(0, 20), pady=2)
            
            label_widget = ctk.CTkLabel(
                info_frame,
                text=label,
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color="gray70",
                width=100,
                anchor="w"
            )
            label_widget.pack(side="left")
            
            value_widget = ctk.CTkLabel(
                info_frame,
                text=value,
                font=ctk.CTkFont(size=12),
                anchor="w"
            )
            value_widget.pack(side="left", padx=(10, 0))
        
        # Description section
        desc_section = ctk.CTkFrame(parent, corner_radius=12)
        desc_section.pack(fill="x", pady=(0, 15))
        
        desc_title = ctk.CTkLabel(
            desc_section,
            text="📝 Description",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        desc_title.pack(anchor="w", padx=20, pady=(15, 10))
        
        desc_text = ctk.CTkLabel(
            desc_section,
            text=invoice["description"],
            font=ctk.CTkFont(size=14),
            anchor="w",
            justify="left"
        )
        desc_text.pack(anchor="w", padx=20, pady=(0, 15))
        
        # Items section
        items_section = ctk.CTkFrame(parent, corner_radius=12)
        items_section.pack(fill="both", expand=True)
        
        items_title = ctk.CTkLabel(
            items_section,
            text="📦 Invoice Items",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        items_title.pack(anchor="w", padx=20, pady=(15, 10))
        
        # Items table header
        header_frame = ctk.CTkFrame(items_section, height=40, corner_radius=8, fg_color="#2b2b2b")
        header_frame.pack(fill="x", padx=20, pady=(0, 10))
        header_frame.pack_propagate(False)
        
        headers = ["Description", "Qty", "Price", "Total"]
        header_widths = [300, 80, 120, 120]
        
        for i, (header, width) in enumerate(zip(headers, header_widths)):
            header_label = ctk.CTkLabel(
                header_frame,
                text=header,
                font=ctk.CTkFont(size=12, weight="bold"),
                width=width
            )
            header_label.pack(side="left", padx=(20 if i == 0 else 10, 0), pady=12)
        
        # Items list
        for item in invoice["items"]:
            item_frame = ctk.CTkFrame(items_section, height=35, corner_radius=8, fg_color="#1a1a1a")
            item_frame.pack(fill="x", padx=20, pady=2)
            item_frame.pack_propagate(False)
            
            # Item data
            item_data = [
                item["description"],
                str(item["quantity"]),
                f"₫{item['price']:,}",
                f"₫{item['quantity'] * item['price']:,}"
            ]
            
            for i, (data, width) in enumerate(zip(item_data, header_widths)):
                item_label = ctk.CTkLabel(
                    item_frame,
                    text=data,
                    font=ctk.CTkFont(size=12),
                    width=width,
                    anchor="w" if i == 0 else "center"
                )
                item_label.pack(side="left", padx=(20 if i == 0 else 10, 0), pady=8)
        
        # Total section
        total_frame = ctk.CTkFrame(items_section, height=40, corner_radius=8, fg_color="#1f538d")
        total_frame.pack(fill="x", padx=20, pady=(10, 15))
        total_frame.pack_propagate(False)
        
        total_label = ctk.CTkLabel(
            total_frame,
            text="TOTAL AMOUNT:",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="white"
        )
        total_label.pack(side="left", padx=20, pady=12)
        
        total_amount = ctk.CTkLabel(
            total_frame,
            text=f"₫{invoice['amount']:,}",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="white"
        )
        total_amount.pack(side="right", padx=20, pady=12)
    
    def show_no_selection_message(self):
        """Show message when no invoice is selected"""
        
        # Clear existing details
        for widget in self.details_scroll.winfo_children():
            widget.destroy()
        
        # Clear action buttons
        for widget in self.action_frame.winfo_children():
            widget.destroy()
        
        # No selection message
        message_frame = ctk.CTkFrame(self.details_scroll, fg_color="transparent")
        message_frame.pack(expand=True, fill="both")
        
        icon_label = ctk.CTkLabel(
            message_frame,
            text="📄",
            font=ctk.CTkFont(size=64)
        )
        icon_label.pack(expand=True, pady=(50, 10))
        
        message_label = ctk.CTkLabel(
            message_frame,
            text="Select an invoice to view details",
            font=ctk.CTkFont(size=18),
            text_color="gray60"
        )
        message_label.pack(expand=True)
    
    def filter_invoices(self, event=None):
        """Filter invoices based on search query"""
        query = self.search_entry.get().lower()
        
        if not query:
            self.refresh_invoices_list()
            return
        
        filtered_data = [
            invoice for invoice in self.invoices_data
            if (query in invoice["id"].lower() or 
                query in invoice["customer"].lower() or
                query in invoice["status"].lower() or
                query in invoice["description"].lower())
        ]
        
        self.refresh_invoices_list(filtered_data)
    
    # Action methods
    def create_new_invoice(self):
        """Create new invoice"""
        messagebox.showinfo("New Invoice", "New invoice creation form will be implemented next!")
    
    def edit_invoice(self, invoice):
        """Edit selected invoice"""
        messagebox.showinfo("Edit Invoice", f"Edit form for invoice {invoice['id']} will be implemented next!")
    
    def delete_invoice(self, invoice):
        """Delete selected invoice"""
        result = messagebox.askyesno(
            "Delete Invoice", 
            f"Are you sure you want to delete invoice {invoice['id']}?\n\nThis action cannot be undone."
        )
        if result:
            self.invoices_data.remove(invoice)
            self.refresh_invoices_list()
            self.show_no_selection_message()
            messagebox.showinfo("Success", "Invoice deleted successfully!")
    
    def print_invoice(self, invoice):
        """Print selected invoice"""
        messagebox.showinfo("Print Invoice", f"Printing invoice {invoice['id']}...\n\nPDF generation will be implemented next!")
    
    def export_invoices(self):
        """Export invoices to file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.invoices_data, f, indent=2, ensure_ascii=False)
                messagebox.showinfo("Export Success", f"Invoices exported to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export invoices:\n{str(e)}")
    
    def show_filter(self):
        """Show filter options"""
        messagebox.showinfo("Filter", "Advanced filter options will be implemented next!")
    
    # Viettel eInvoice Integration Methods
    def open_viettel_config(self):
        """Open Viettel eInvoice configuration window"""
        if not VIETTEL_AVAILABLE:
            messagebox.showerror(
                "Integration Not Available",
                "Viettel eInvoice integration is not available.\n\n"
                "Please ensure all required dependencies are installed."
            )
            return
        
        try:
            config_window = ViettelConfigWindow(self, self.session_data)
            config_window.focus()
        except Exception as e:
            messagebox.showerror(
                "Configuration Error",
                f"Failed to open Viettel configuration:\n{str(e)}"
            )
    
    def create_einvoice(self, invoice):
        """Create electronic invoice via Viettel API"""
        if not VIETTEL_AVAILABLE:
            messagebox.showerror(
                "Integration Not Available",
                "Viettel eInvoice integration is not available."
            )
            return
        
        try:
            # Load Viettel configuration
            config_file = os.path.join(os.path.expanduser('~'), 'FinanTidy', 'viettel_config.json')
            config = ViettelEInvoiceConfig.load_config(config_file)
            
            # Validate configuration
            if not self._validate_viettel_config(config):
                result = messagebox.askyesno(
                    "Configuration Required",
                    "Viettel eInvoice is not configured properly.\n\n"
                    "Would you like to configure it now?"
                )
                if result:
                    self.open_viettel_config()
                return
            
            # Convert invoice data to Viettel format
            viettel_data = self._convert_invoice_to_viettel(invoice)
            
            # Show confirmation dialog
            result = messagebox.askyesno(
                "Create Electronic Invoice",
                f"Create electronic invoice for:\n"
                f"Invoice: {invoice.get('invoice_number', 'N/A')}\n"
                f"Amount: ₫{invoice.get('total_amount', 0):,.0f}\n\n"
                f"This will submit the invoice to Viettel eInvoice system.\n"
                f"Continue?"
            )
            
            if not result:
                return
            
            # Create progress dialog
            progress_dialog = self._create_progress_dialog("Creating electronic invoice...")
            
            try:
                # Initialize Viettel service
                service = ViettelEInvoiceService(config)
                
                # Create invoice
                progress_dialog.update_status("Authenticating with Viettel...")
                auth_result = service.authenticate()
                
                if not auth_result:
                    raise Exception("Authentication failed")
                
                progress_dialog.update_status("Creating electronic invoice...")
                result = service.create_invoice(viettel_data)
                
                progress_dialog.destroy()
                
                if result['success']:
                    # Show success message
                    invoice_no = result.get('invoice_no', 'N/A')
                    transaction_id = result.get('transaction_id', 'N/A')
                    
                    messagebox.showinfo(
                        "Electronic Invoice Created",
                        f"✅ Electronic invoice created successfully!\n\n"
                        f"Invoice Number: {invoice_no}\n"
                        f"Transaction ID: {transaction_id}\n\n"
                        f"You can download the PDF file from the system."
                    )
                    
                    # Ask if user wants to download PDF
                    download_result = messagebox.askyesno(
                        "Download PDF",
                        "Would you like to download the PDF file now?"
                    )
                    
                    if download_result:
                        self._download_einvoice_pdf(service, transaction_id, invoice_no)
                
                else:
                    messagebox.showerror(
                        "Electronic Invoice Error",
                        f"Failed to create electronic invoice:\n{result.get('error', 'Unknown error')}"
                    )
                    
            except Exception as e:
                progress_dialog.destroy()
                messagebox.showerror(
                    "Electronic Invoice Error",
                    f"Error creating electronic invoice:\n{str(e)}"
                )
                
        except Exception as e:
            messagebox.showerror(
                "eInvoice Error",
                f"Error processing electronic invoice:\n{str(e)}"
            )
    
    def _validate_viettel_config(self, config):
        """Validate Viettel configuration"""
        required_fields = [
            'base_url', 'username', 'password', 
            'supplier_tax_code', 'template_code', 'invoice_series'
        ]
        
        for field in required_fields:
            if not config.get(field):
                return False
        
        return True
    
    def _convert_invoice_to_viettel(self, invoice):
        """Convert FinanTidy invoice to Viettel format"""
        # Basic invoice data conversion
        viettel_data = {
            'invoice_date': invoice.get('invoice_date', datetime.datetime.now().strftime('%Y-%m-%d')),
            'currency': 'VND',
            'description': invoice.get('description', ''),
            'buyer_name': invoice.get('customer_name', ''),
            'buyer_tax_code': invoice.get('customer_tax_code', ''),
            'buyer_address': invoice.get('customer_address', ''),
            'buyer_email': invoice.get('customer_email', ''),
            'items': []
        }
        
        # Convert items
        for item in invoice.get('items', []):
            viettel_item = {
                'item_name': item.get('item_name', ''),
                'quantity': item.get('quantity', 1),
                'unit_price': item.get('unit_price', 0),
                'tax_rate': item.get('tax_rate', 10),  # Default 10% VAT
                'discount_rate': item.get('discount_rate', 0),
                'description': item.get('description', '')
            }
            viettel_data['items'].append(viettel_item)
        
        return viettel_data
    
    def _create_progress_dialog(self, message):
        """Create progress dialog for long operations"""
        progress_window = ctk.CTkToplevel(self)
        progress_window.title("Processing...")
        progress_window.geometry("400x150")
        progress_window.transient(self)
        progress_window.grab_set()
        
        # Center on parent
        parent_x = self.winfo_x()
        parent_y = self.winfo_y()
        parent_width = self.winfo_width()
        parent_height = self.winfo_height()
        
        x = parent_x + (parent_width // 2) - (400 // 2)
        y = parent_y + (parent_height // 2) - (150 // 2)
        progress_window.geometry(f"400x150+{x}+{y}")
        
        # Progress content
        content_frame = ctk.CTkFrame(progress_window)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Status label
        status_label = ctk.CTkLabel(
            content_frame,
            text=message,
            font=ctk.CTkFont(size=14)
        )
        status_label.pack(pady=(20, 10))
        
        # Progress bar
        progress_bar = ctk.CTkProgressBar(content_frame, width=300)
        progress_bar.pack(pady=10)
        progress_bar.set(0.5)  # Indeterminate
        
        # Update method
        def update_status(new_message):
            status_label.configure(text=new_message)
            progress_window.update()
        
        progress_window.update_status = update_status
        progress_window.update()
        
        return progress_window
    
    def _download_einvoice_pdf(self, service, transaction_id, invoice_no):
        """Download electronic invoice PDF"""
        try:
            # Create download dialog
            download_dialog = self._create_progress_dialog("Downloading PDF file...")
            
            # Download file
            download_dialog.update_status("Requesting PDF from Viettel...")
            file_result = service.get_invoice_file(transaction_id, 'pdf')
            
            download_dialog.destroy()
            
            if file_result['success']:
                # Save file dialog
                file_path = filedialog.asksaveasfilename(
                    title="Save Electronic Invoice PDF",
                    defaultextension=".pdf",
                    initialvalue=f"einvoice_{invoice_no}.pdf",
                    filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
                )
                
                if file_path:
                    # Decode and save file
                    import base64
                    file_data = base64.b64decode(file_result['file_data'])
                    
                    with open(file_path, 'wb') as f:
                        f.write(file_data)
                    
                    messagebox.showinfo(
                        "Download Complete",
                        f"Electronic invoice PDF saved to:\n{file_path}"
                    )
            else:
                messagebox.showerror(
                    "Download Error",
                    f"Failed to download PDF:\n{file_result.get('error', 'Unknown error')}"
                )
                
        except Exception as e:
            messagebox.showerror(
                "Download Error",
                f"Error downloading PDF:\n{str(e)}"
            )


def main():
    """Test function"""
    root = ctk.CTk()
    root.withdraw()  # Hide root window
    
    invoices_window = InvoicesWindow(root)
    invoices_window.mainloop()

if __name__ == "__main__":
    main()
