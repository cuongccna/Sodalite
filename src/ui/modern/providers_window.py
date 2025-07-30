"""
FinanTidy - Providers Management Module
Modern CustomTkinter interface for provider/supplier management
"""

import customtkinter as ctk
from tkinter import messagebox, filedialog
import datetime
import json
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from src.database.business_services import get_provider_service

# Set appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ProvidersWindow(ctk.CTkToplevel):
    """Modern Providers Management Window"""
    
    def __init__(self, parent, session_data=None):
        super().__init__(parent)
        
        # Window configuration
        self.title("FinanTidy - Providers Management")
        self.geometry("1300x700")
        self.transient(parent)
        
        # Session data
        self.session_data = session_data or {}
        self.company_id = self.session_data.get('company_id', 1)
        
        # Initialize database service
        try:
            self.provider_service = get_provider_service(self.company_id)
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {e}")
            self.destroy()
            return
        
        # Load providers data
        self.providers_data = self.load_providers_data()
        
        # Selected provider
        self.selected_provider = None
        
        # Create UI
        self.create_providers_ui()
        
        # Center window
        self.center_window()
    
    def center_window(self):
        """Center window on screen"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (1300 // 2)
        y = (self.winfo_screenheight() // 2) - (700 // 2)
        self.geometry(f"1300x700+{x}+{y}")
    
    def load_providers_data(self):
        """Load providers data from database"""
        try:
            # Get providers with pagination
            result = self.provider_service.get_providers(
                page=1, 
                page_size=100,  # Load more providers for the list
                search_term=""
            )
            return result.get('providers', [])
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to load providers: {e}")
            return []
    
    def refresh_providers_data(self):
        """Refresh providers data from database"""
        self.providers_data = self.load_providers_data()
        self.populate_providers_list()
    
    def create_providers_ui(self):
        """Create providers management interface"""
        
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
        
        # Left panel - Providers list
        self.create_providers_list(content_frame)
        
        # Right panel - Provider details
        self.create_provider_details(content_frame)
    
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
            text="🏪 Providers Management",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(anchor="w")
        
        active_count = len([p for p in self.providers_data if p["status"] == "Active"])
        stats_label = ctk.CTkLabel(
            left_frame,
            text=f"Total: {len(self.providers_data)} providers • Active: {active_count} • Value: ₫{sum(p['total_amount'] for p in self.providers_data):,}",
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        stats_label.pack(anchor="w")
        
        # Right side - Action buttons
        right_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        right_frame.pack(side="right", fill="y", padx=25, pady=20)
        
        # New provider button
        new_button = ctk.CTkButton(
            right_frame,
            text="+ New Provider",
            height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.create_new_provider
        )
        new_button.pack(side="right", padx=(10, 0))
        
        # Import button
        import_button = ctk.CTkButton(
            right_frame,
            text="📥 Import",
            height=40,
            width=100,
            font=ctk.CTkFont(size=14),
            fg_color="#8b5cf6",
            hover_color="#7c3aed",
            command=self.import_providers
        )
        import_button.pack(side="right", padx=(10, 0))
        
        # Export button
        export_button = ctk.CTkButton(
            right_frame,
            text="📊 Export",
            height=40,
            width=100,
            font=ctk.CTkFont(size=14),
            fg_color="#10b981",
            hover_color="#059669",
            command=self.export_providers
        )
        export_button.pack(side="right")
    
    def create_providers_list(self, parent):
        """Create providers list panel"""
        
        # Left panel container
        list_container = ctk.CTkFrame(parent, corner_radius=15)
        list_container.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        # List header
        list_header = ctk.CTkFrame(list_container, height=50, corner_radius=0)
        list_header.pack(fill="x", padx=20, pady=(20, 10))
        list_header.pack_propagate(False)
        
        header_title = ctk.CTkLabel(
            list_header,
            text="Providers List",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        header_title.pack(side="left", pady=15)
        
        # Filter frame
        filter_frame = ctk.CTkFrame(list_header, fg_color="transparent")
        filter_frame.pack(side="right", fill="y", pady=10)
        
        # Type filter
        self.type_filter = ctk.CTkOptionMenu(
            filter_frame,
            values=["All Types", "Technology", "Marketing", "Supplies", "Legal"],
            width=120,
            height=30,
            command=self.filter_providers
        )
        self.type_filter.pack(side="right", padx=(10, 0))
        
        # Search entry
        self.search_entry = ctk.CTkEntry(
            filter_frame,
            placeholder_text="Search providers...",
            width=180,
            height=30
        )
        self.search_entry.pack(side="right")
        self.search_entry.bind("<KeyRelease>", self.filter_providers)
        
        # Scrollable frame for providers
        self.providers_scroll = ctk.CTkScrollableFrame(list_container)
        self.providers_scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Populate providers list
        self.refresh_providers_list()
    
    def create_provider_details(self, parent):
        """Create provider details panel"""
        
        # Right panel container
        self.details_container = ctk.CTkFrame(parent, corner_radius=15)
        self.details_container.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        # Details header
        details_header = ctk.CTkFrame(self.details_container, height=50, corner_radius=0)
        details_header.pack(fill="x", padx=20, pady=(20, 10))
        details_header.pack_propagate(False)
        
        self.details_title = ctk.CTkLabel(
            details_header,
            text="Provider Details",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        self.details_title.pack(side="left", pady=15)
        
        # Action buttons for selected provider
        self.action_frame = ctk.CTkFrame(details_header, fg_color="transparent")
        self.action_frame.pack(side="right", fill="y", pady=10)
        
        # Scrollable frame for details
        self.details_scroll = ctk.CTkScrollableFrame(self.details_container)
        self.details_scroll.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Show default message
        self.show_no_selection_message()
    
    def refresh_providers_list(self, filtered_data=None):
        """Refresh the providers list"""
        
        # Clear existing items
        for widget in self.providers_scroll.winfo_children():
            widget.destroy()
        
        # Use filtered data or all data
        data_to_show = filtered_data if filtered_data is not None else self.providers_data
        
        # Create provider cards
        for provider in data_to_show:
            self.create_provider_card(self.providers_scroll, provider)
    
    def create_provider_card(self, parent, provider):
        """Create individual provider card"""
        
        # Card container
        card = ctk.CTkFrame(parent, height=110, corner_radius=12)
        card.pack(fill="x", pady=5)
        card.pack_propagate(False)
        
        # Make card clickable
        card.bind("<Button-1>", lambda e: self.select_provider(provider))
        
        # Card content
        content_frame = ctk.CTkFrame(card, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=15, pady=10)
        
        # Top row - Name and status
        top_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        top_frame.pack(fill="x")
        
        # Provider name
        name_label = ctk.CTkLabel(
            top_frame,
            text=provider.get("provider_name", "Unknown Provider"),
            font=ctk.CTkFont(size=16, weight="bold")
        )
        name_label.pack(side="left")
        
        # Status badge
        status_colors = {
            "Active": "#10b981",
            "Inactive": "#6b7280"
        }
        
        status_badge = ctk.CTkLabel(
            top_frame,
            text=provider["status"],
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="white",
            corner_radius=6,
            fg_color=status_colors.get(provider["status"], "#6b7280"),
            width=60,
            height=20
        )
        status_badge.pack(side="right")
        
        # Middle row - Type and contact
        middle_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        middle_frame.pack(fill="x", pady=(5, 0))
        
        type_label = ctk.CTkLabel(
            middle_frame,
            text=f"📂 {provider.get('provider_type', 'Unknown')} • 👤 {provider.get('contact_person', 'N/A')}",
            font=ctk.CTkFont(size=12),
            text_color="gray70"
        )
        type_label.pack(side="left")
        
        # Rating stars
        rating = "⭐" * provider["rating"] + "☆" * (5 - provider["rating"])
        rating_label = ctk.CTkLabel(
            middle_frame,
            text=rating,
            font=ctk.CTkFont(size=12)
        )
        rating_label.pack(side="right")
        
        # Bottom row - Stats
        bottom_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        bottom_frame.pack(fill="x", pady=(5, 0))
        
        stats_label = ctk.CTkLabel(
            bottom_frame,
            text=f"📄 {provider['total_invoices']} invoices • ₫{provider['total_amount']:,} • Last: {provider['last_transaction']}",
            font=ctk.CTkFont(size=11),
            text_color="gray60"
        )
        stats_label.pack(side="left")
    
    def select_provider(self, provider):
        """Select and display provider details"""
        self.selected_provider = provider
        self.show_provider_details(provider)
    
    def show_provider_details(self, provider):
        """Display detailed provider information"""
        
        # Clear existing details
        for widget in self.details_scroll.winfo_children():
            widget.destroy()
        
        # Update title
        self.details_title.configure(text=f"Provider: {provider.get('provider_name', 'Unknown Provider')}")
        
        # Clear and recreate action buttons
        for widget in self.action_frame.winfo_children():
            widget.destroy()
        
        # Edit button
        edit_button = ctk.CTkButton(
            self.action_frame,
            text="✏️ Edit",
            width=80,
            height=30,
            font=ctk.CTkFont(size=12),
            command=lambda: self.edit_provider(provider)
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
            command=lambda: self.delete_provider(provider)
        )
        delete_button.pack(side="right", padx=(5, 0))
        
        # Contact button
        contact_button = ctk.CTkButton(
            self.action_frame,
            text="📧 Contact",
            width=80,
            height=30,
            font=ctk.CTkFont(size=12),
            fg_color="#10b981",
            hover_color="#059669",
            command=lambda: self.contact_provider(provider)
        )
        contact_button.pack(side="right")
        
        # Provider details content
        self.create_provider_details_content(self.details_scroll, provider)
    
    def create_provider_details_content(self, parent, provider):
        """Create detailed provider content"""
        
        # Basic information section
        basic_section = ctk.CTkFrame(parent, corner_radius=12)
        basic_section.pack(fill="x", pady=(0, 15))
        
        basic_title = ctk.CTkLabel(
            basic_section,
            text="📋 Basic Information",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        basic_title.pack(anchor="w", padx=20, pady=(15, 10))
        
        # Basic info fields
        basic_info = [
            ("Provider ID:", provider["id"]),
            ("Company Name:", provider.get("provider_name", "N/A")),
            ("Business Type:", provider.get("provider_type", "N/A")),
            ("Contact Person:", provider["contact_person"]),
            ("Email:", provider["email"]),
            ("Phone:", provider["phone"]),
            ("Tax ID:", provider["tax_id"]),
            ("Status:", provider["status"])
        ]
        
        for i, (label, value) in enumerate(basic_info):
            info_frame = ctk.CTkFrame(basic_section, fg_color="transparent")
            info_frame.pack(fill="x", padx=20, pady=2)
            
            label_widget = ctk.CTkLabel(
                info_frame,
                text=label,
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color="gray70",
                width=120,
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
        
        # Address section
        address_section = ctk.CTkFrame(parent, corner_radius=12)
        address_section.pack(fill="x", pady=(0, 15))
        
        address_title = ctk.CTkLabel(
            address_section,
            text="📍 Address Information",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        address_title.pack(anchor="w", padx=20, pady=(15, 10))
        
        address_text = ctk.CTkLabel(
            address_section,
            text=provider["address"],
            font=ctk.CTkFont(size=14),
            anchor="w",
            justify="left"
        )
        address_text.pack(anchor="w", padx=20, pady=(0, 15))
        
        # Services section
        services_section = ctk.CTkFrame(parent, corner_radius=12)
        services_section.pack(fill="x", pady=(0, 15))
        
        services_title = ctk.CTkLabel(
            services_section,
            text="🛠️ Services Provided",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        services_title.pack(anchor="w", padx=20, pady=(15, 10))
        
        # Services tags
        services_frame = ctk.CTkFrame(services_section, fg_color="transparent")
        services_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        for service in provider["services"]:
            service_tag = ctk.CTkLabel(
                services_frame,
                text=service,
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color="white",
                corner_radius=8,
                fg_color="#1f538d",
                height=25
            )
            service_tag.pack(side="left", padx=(0, 10), pady=2)
        
        # Statistics section
        stats_section = ctk.CTkFrame(parent, corner_radius=12)
        stats_section.pack(fill="x", pady=(0, 15))
        
        stats_title = ctk.CTkLabel(
            stats_section,
            text="📊 Statistics",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        stats_title.pack(anchor="w", padx=20, pady=(15, 10))
        
        # Stats grid
        stats_grid = ctk.CTkFrame(stats_section, fg_color="transparent")
        stats_grid.pack(fill="x", padx=20, pady=(0, 15))
        
        # Rating
        rating_frame = ctk.CTkFrame(stats_grid, corner_radius=8, height=60)
        rating_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        rating_frame.pack_propagate(False)
        
        rating_stars = "⭐" * provider["rating"] + "☆" * (5 - provider["rating"])
        ctk.CTkLabel(rating_frame, text="Rating", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray70").pack(pady=(8, 0))
        ctk.CTkLabel(rating_frame, text=rating_stars, font=ctk.CTkFont(size=14)).pack()
        
        # Total invoices
        invoices_frame = ctk.CTkFrame(stats_grid, corner_radius=8, height=60)
        invoices_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        invoices_frame.pack_propagate(False)
        
        ctk.CTkLabel(invoices_frame, text="Total Invoices", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray70").pack(pady=(8, 0))
        ctk.CTkLabel(invoices_frame, text=str(provider["total_invoices"]), font=ctk.CTkFont(size=16, weight="bold")).pack()
        
        # Total amount
        amount_frame = ctk.CTkFrame(stats_grid, corner_radius=8, height=60)
        amount_frame.pack(side="left", fill="both", expand=True)
        amount_frame.pack_propagate(False)
        
        ctk.CTkLabel(amount_frame, text="Total Amount", font=ctk.CTkFont(size=11, weight="bold"), text_color="gray70").pack(pady=(8, 0))
        ctk.CTkLabel(amount_frame, text=f"₫{provider['total_amount']:,}", font=ctk.CTkFont(size=14, weight="bold")).pack()
        
        # Notes section
        notes_section = ctk.CTkFrame(parent, corner_radius=12)
        notes_section.pack(fill="x")
        
        notes_title = ctk.CTkLabel(
            notes_section,
            text="📝 Notes",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        notes_title.pack(anchor="w", padx=20, pady=(15, 10))
        
        notes_text = ctk.CTkLabel(
            notes_section,
            text=provider["notes"],
            font=ctk.CTkFont(size=14),
            anchor="w",
            justify="left",
            wraplength=400
        )
        notes_text.pack(anchor="w", padx=20, pady=(0, 15))
    
    def show_no_selection_message(self):
        """Show message when no provider is selected"""
        
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
            text="🏪",
            font=ctk.CTkFont(size=64)
        )
        icon_label.pack(expand=True, pady=(50, 10))
        
        message_label = ctk.CTkLabel(
            message_frame,
            text="Select a provider to view details",
            font=ctk.CTkFont(size=18),
            text_color="gray60"
        )
        message_label.pack(expand=True)
    
    def filter_providers(self, value=None):
        """Filter providers based on search query and type"""
        query = self.search_entry.get().lower()
        type_filter = self.type_filter.get()
        
        filtered_data = []
        
        for provider in self.providers_data:
            # Text search
            text_match = (
                query in provider.get("provider_name", "").lower() or
                query in provider.get("contact_person", "").lower() or
                query in provider.get("email", "").lower() or
                query in provider.get("provider_type", "").lower()
            )
            
            # Type filter
            type_match = type_filter == "All Types" or provider.get("provider_type") == type_filter
            
            if text_match and type_match:
                filtered_data.append(provider)
        
        self.refresh_providers_list(filtered_data)
    
    # Action methods
    def create_new_provider(self):
        """Create new provider"""
        # Open provider form dialog
        dialog = ProviderFormDialog(self, "Create New Provider")
        if dialog.result:
            try:
                # Create provider using database service
                new_provider = self.provider_service.create_provider(dialog.result)
                messagebox.showinfo("Success", f"Provider '{new_provider['provider_name']}' created successfully!")
                self.refresh_providers_data()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create provider: {e}")
    
    def edit_provider(self, provider):
        """Edit selected provider"""
        # Open provider form dialog with current data
        dialog = ProviderFormDialog(self, "Edit Provider", provider)
        if dialog.result:
            try:
                # Update provider using database service
                updated_provider = self.provider_service.update_provider(provider['id'], dialog.result)
                messagebox.showinfo("Success", f"Provider '{updated_provider['provider_name']}' updated successfully!")
                self.refresh_providers_data()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update provider: {e}")
    
    def delete_provider(self, provider):
        """Delete selected provider"""
        result = messagebox.askyesno(
            "Delete Provider",
            f"Are you sure you want to delete provider '{provider['provider_name']}'?\n\nThis action cannot be undone."
        )
        if result:
            try:
                # Delete provider using database service
                self.provider_service.delete_provider(provider['id'])
                messagebox.showinfo("Success", "Provider deleted successfully!")
                self.refresh_providers_data()
                self.show_no_selection_message()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete provider: {e}")
    
    def contact_provider(self, provider):
        """Contact selected provider"""
        import webbrowser
        email = provider.get('email', '')
        if email:
            webbrowser.open(f"mailto:{email}")
        else:
            messagebox.showwarning("No Email", "No email address available for this provider.")
    
    def export_providers(self):
        """Export providers to file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.providers_data, f, indent=2, ensure_ascii=False)
                messagebox.showinfo("Export Success", f"Providers exported to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export providers:\n{str(e)}")
    
    def import_providers(self):
        """Import providers from file"""
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            messagebox.showinfo("Import", "Provider import functionality will be implemented next!")


class ProviderFormDialog(ctk.CTkToplevel):
    """Provider form dialog for create/edit operations"""
    
    def __init__(self, parent, title, provider_data=None):
        super().__init__(parent)
        
        self.title(title)
        self.geometry("600x700")
        self.transient(parent)
        self.grab_set()  # Make dialog modal
        
        # Initialize result
        self.result = None
        self.provider_data = provider_data or {}
        
        # Create form
        self.create_form()
        
        # Center dialog
        self.center_dialog()
    
    def center_dialog(self):
        """Center dialog on parent window"""
        self.update_idletasks()
        parent_x = self.master.winfo_x()
        parent_y = self.master.winfo_y()
        parent_width = self.master.winfo_width()
        parent_height = self.master.winfo_height()
        
        x = parent_x + (parent_width // 2) - (600 // 2)
        y = parent_y + (parent_height // 2) - (700 // 2)
        self.geometry(f"600x700+{x}+{y}")
    
    def create_form(self):
        """Create provider form"""
        # Main frame
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = ctk.CTkLabel(main_frame, text=self.title(), font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=(0, 20))
        
        # Scrollable frame for form fields
        scrollable_frame = ctk.CTkScrollableFrame(main_frame)
        scrollable_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        # Form fields
        self.entries = {}
        
        # Provider Name
        self.create_field(scrollable_frame, "Provider Name*", "provider_name", required=True)
        
        # Provider Code
        self.create_field(scrollable_frame, "Provider Code*", "provider_code", required=True)
        
        # Provider Type
        type_frame = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
        type_frame.pack(fill="x", pady=5)
        
        ctk.CTkLabel(type_frame, text="Provider Type*", font=ctk.CTkFont(weight="bold")).pack(anchor="w")
        self.entries["provider_type"] = ctk.CTkOptionMenu(
            type_frame, 
            values=["service_provider", "supplier", "consultant", "contractor"],
            width=200
        )
        self.entries["provider_type"].pack(anchor="w", pady=(5, 0))
        
        # Contact Person
        self.create_field(scrollable_frame, "Contact Person", "contact_person")
        
        # Email
        self.create_field(scrollable_frame, "Email", "email")
        
        # Phone
        self.create_field(scrollable_frame, "Phone", "phone")
        
        # Website
        self.create_field(scrollable_frame, "Website", "website")
        
        # Address
        self.create_field(scrollable_frame, "Address", "address", height=80)
        
        # Tax ID
        self.create_field(scrollable_frame, "Tax ID", "tax_id")
        
        # Payment Terms
        self.create_field(scrollable_frame, "Payment Terms (days)", "payment_terms", field_type="number")
        
        # Credit Limit
        self.create_field(scrollable_frame, "Credit Limit", "credit_limit", field_type="number")
        
        # Services (comma-separated)
        self.create_field(scrollable_frame, "Services (comma-separated)", "services_text", height=60)
        
        # Notes
        self.create_field(scrollable_frame, "Notes", "notes", height=100)
        
        # Populate form if editing
        if self.provider_data:
            self.populate_form()
        
        # Buttons
        button_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        button_frame.pack(fill="x", pady=(0, 0))
        
        cancel_btn = ctk.CTkButton(button_frame, text="Cancel", command=self.cancel, fg_color="gray")
        cancel_btn.pack(side="right", padx=(10, 0))
        
        save_btn = ctk.CTkButton(button_frame, text="Save", command=self.save)
        save_btn.pack(side="right")
    
    def create_field(self, parent, label, key, required=False, field_type="text", height=None):
        """Create a form field"""
        field_frame = ctk.CTkFrame(parent, fg_color="transparent")
        field_frame.pack(fill="x", pady=5)
        
        label_text = label + (" *" if required and not label.endswith("*") else "")
        ctk.CTkLabel(field_frame, text=label_text, font=ctk.CTkFont(weight="bold")).pack(anchor="w")
        
        if height and height > 40:
            # Text area
            self.entries[key] = ctk.CTkTextbox(field_frame, height=height)
        else:
            # Single line entry
            self.entries[key] = ctk.CTkEntry(field_frame, width=400)
        
        self.entries[key].pack(anchor="w", pady=(5, 0))
    
    def populate_form(self):
        """Populate form with existing provider data"""
        for key, widget in self.entries.items():
            if key == "services_text":
                # Convert services list to comma-separated string
                services = self.provider_data.get('services', [])
                if isinstance(services, list):
                    value = ', '.join(services)
                else:
                    value = str(services) if services else ''
            else:
                value = self.provider_data.get(key, '')
            
            if isinstance(widget, ctk.CTkTextbox):
                widget.delete("1.0", "end")
                widget.insert("1.0", str(value))
            elif isinstance(widget, ctk.CTkOptionMenu):
                if value in widget.cget("values"):
                    widget.set(value)
            else:
                widget.delete(0, "end")
                widget.insert(0, str(value))
    
    def save(self):
        """Save provider data"""
        # Validate required fields
        required_fields = ["provider_name", "provider_code", "provider_type"]
        for field in required_fields:
            if field in self.entries:
                if isinstance(self.entries[field], ctk.CTkOptionMenu):
                    value = self.entries[field].get()
                elif isinstance(self.entries[field], ctk.CTkTextbox):
                    value = self.entries[field].get("1.0", "end").strip()
                else:
                    value = self.entries[field].get().strip()
                
                if not value:
                    messagebox.showerror("Validation Error", f"{field.replace('_', ' ').title()} is required!")
                    return
        
        # Collect form data
        data = {}
        for key, widget in self.entries.items():
            if isinstance(widget, ctk.CTkTextbox):
                value = widget.get("1.0", "end").strip()
            elif isinstance(widget, ctk.CTkOptionMenu):
                value = widget.get()
            else:
                value = widget.get().strip()
            
            # Special handling for services
            if key == "services_text":
                if value:
                    data["services"] = [s.strip() for s in value.split(",") if s.strip()]
                else:
                    data["services"] = []
            # Special handling for numeric fields
            elif key in ["payment_terms", "credit_limit"]:
                try:
                    data[key] = int(value) if value else 0
                except ValueError:
                    data[key] = 0
            else:
                data[key] = value
        
        # Set default values
        if not data.get("rating"):
            data["rating"] = 0.0
        if not data.get("is_preferred"):
            data["is_preferred"] = False
        
        self.result = data
        self.destroy()
    
    def cancel(self):
        """Cancel form"""
        self.result = None
        self.destroy()


def main():
    """Test function"""
    root = ctk.CTk()
    root.withdraw()  # Hide root window
    
    providers_window = ProvidersWindow(root)
    providers_window.mainloop()

if __name__ == "__main__":
    main()
