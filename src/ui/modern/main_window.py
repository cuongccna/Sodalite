"""
FinanTidy - Modern Main Window with CustomTkinter
Professional dark theme dashboard with database integration and multi-language support
"""

import customtkinter as ctk
from tkinter import messagebox
import datetime
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Import language manager
try:
    from core.language_manager import get_language_manager, t
    _lang_manager = get_language_manager()
    _t = t
except ImportError:
    # Fallback if language manager not available
    _lang_manager = None
    _t = lambda key, default=None: default or key

# Import database services
try:
    from ...database.database_manager import get_db_manager
    from ...database.business_services import get_analytics_service
except ImportError:
    try:
        from src.database.database_manager import get_db_manager
        from src.database.business_services import get_analytics_service
    except ImportError:
        # Mock for testing
        def get_db_manager():
            return None
        def get_analytics_service(company_id):
            return None

class ModernMainWindow(ctk.CTk):
    """Modern Main Window with Database Integration and Multi-language Support"""
    
    def __init__(self, session_data=None):
        super().__init__()
        
        # Initialize language support
        self.lang_manager = _lang_manager
        self.t = _t
        
        # Load language settings
        self.load_language_settings()
        
        # Session data from login
        self.session_data = session_data or {
            "user_id": 1,
            "username": "Demo User", 
            "full_name": self.t("dashboard.demo_user", "Demo User"),
            "company_id": 1,
            "company_name": self.t("dashboard.demo_company", "Demo Company"),
            "role": "admin",
            "license": {"type": "free"}
        }
        
        # Database manager
        try:
            self.db_manager = get_db_manager()
            self.analytics_service = get_analytics_service(self.session_data['company_id'])
        except Exception as e:
            print(f"Database service error: {e}")
            self.db_manager = None
            self.analytics_service = None
        
        # Window configuration
        self.title(f"FinanTidy - {self.session_data['company_name']}")
        self.geometry("1500x900")
        self.state('zoomed')  # Maximize window on Windows
        
        # Load dashboard statistics
        self.dashboard_stats = self.load_dashboard_statistics()
        
        # Create main UI
        self.create_main_ui()
        
        # Set protocol for window close
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def load_language_settings(self):
        """Load language settings from file"""
        try:
            import json
            settings_file = "finantidy_settings.json"
            if os.path.exists(settings_file):
                with open(settings_file, 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                    language = settings.get('language', 'vi')
                    if self.lang_manager:
                        self.lang_manager.set_language(language)
        except Exception as e:
            print(f"Error loading language settings: {e}")
    
    def load_dashboard_statistics(self):
        """Load dashboard statistics from database"""
        try:
            if self.db_manager:
                return self.db_manager.get_company_statistics(self.session_data['company_id'])
            else:
                # Mock data for testing
                return {
                    'invoices': {'total': 25, 'paid': 18, 'pending': 5, 'overdue': 2},
                    'financial': {'total_revenue': 150200000, 'pending_amount': 32000000},
                    'providers': {'total': 15},
                    'transactions': {'monthly': 28}
                }
        except Exception as e:
            print(f"Error loading dashboard statistics: {e}")
            return {
                'invoices': {'total': 0, 'paid': 0, 'pending': 0, 'overdue': 0},
                'financial': {'total_revenue': 0, 'pending_amount': 0},
                'providers': {'total': 0},
                'transactions': {'monthly': 0}
            }
    
    def create_main_ui(self):
        """Create modern dashboard interface"""
        
        # Header frame
        header_frame = ctk.CTkFrame(self, height=80, corner_radius=0)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Header content
        self.create_header(header_frame)
        
        # Main content area
        content_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Create sidebar and main content
        self.create_content_area(content_frame)
    
    def create_header(self, header_frame):
        """Create header with company info and user menu"""
        
        # Left side - Company info
        left_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        left_frame.pack(side="left", fill="y", padx=20, pady=15)
        
        # Company icon and name
        company_container = ctk.CTkFrame(left_frame, fg_color="transparent")
        company_container.pack(side="left", fill="y")
        
        company_icon = ctk.CTkLabel(
            company_container,
            text="🏢",
            font=ctk.CTkFont(size=32)
        )
        company_icon.pack(side="left", padx=(0, 10))
        
        # Company info
        company_info = ctk.CTkFrame(company_container, fg_color="transparent")
        company_info.pack(side="left", fill="y")
        
        company_title = ctk.CTkLabel(
            company_info,
            text=self.session_data['company_name'],
            font=ctk.CTkFont(size=18, weight="bold")
        )
        company_title.pack(anchor="w")
        
        company_subtitle = ctk.CTkLabel(
            company_info,
            text=f"{self.t('app.subtitle', 'Financial Management System')} • {self.session_data['role'].title()}",
            font=ctk.CTkFont(size=12),
            text_color="gray70"
        )
        company_subtitle.pack(anchor="w")
        
        # Center - Current time
        center_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        center_frame.pack(expand=True, fill="both")
        
        current_time = datetime.datetime.now().strftime("%A, %B %d, %Y - %H:%M")
        time_label = ctk.CTkLabel(
            center_frame,
            text=current_time,
            font=ctk.CTkFont(size=14),
            text_color="gray60"
        )
        time_label.pack(expand=True)
        
        # Right side - User info and controls
        right_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        right_frame.pack(side="right", fill="y", padx=20, pady=15)
        
        # User info
        user_container = ctk.CTkFrame(right_frame, fg_color="transparent")
        user_container.pack(side="right", fill="y")
        
        user_icon = ctk.CTkLabel(
            user_container,
            text="👤",
            font=ctk.CTkFont(size=24)
        )
        user_icon.pack(side="left", padx=(0, 8))
        
        user_info = ctk.CTkFrame(user_container, fg_color="transparent")
        user_info.pack(side="left", fill="y", padx=(0, 15))
        
        username_label = ctk.CTkLabel(
            user_info,
            text=self.session_data.get("full_name", "Demo User"),
            font=ctk.CTkFont(size=14, weight="bold")
        )
        username_label.pack(anchor="w")
        
        role_label = ctk.CTkLabel(
            user_info,
            text=f"Role: {self.session_data.get('role', 'User').title()}",
            font=ctk.CTkFont(size=11),
            text_color="gray70"
        )
        role_label.pack(anchor="w")
        
        # Logout button  
        logout_button = ctk.CTkButton(
            right_frame,
            text=self.t("buttons.logout", "🚪 Logout"),
            width=120,  # Increased width
            height=40,  # Increased height
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#dc2626",
            hover_color="#b91c1c",
            command=self.logout
        )
        logout_button.pack(side="right", padx=(0, 10))
        
        # Settings button
        settings_button = ctk.CTkButton(
            right_frame,
            text=self.t("buttons.settings", "⚙️ Settings"),  # Added text
            width=120,  # Increased width
            height=40,  # Increased height
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.show_settings
        )
        settings_button.pack(side="right", padx=(0, 10))
    
    def create_content_area(self, content_frame):
        """Create sidebar and main dashboard area"""
        
        # Sidebar
        sidebar_frame = ctk.CTkFrame(content_frame, width=280, corner_radius=0)
        sidebar_frame.pack(side="left", fill="y", padx=(0, 0), pady=0)
        sidebar_frame.pack_propagate(False)
        
        self.create_sidebar(sidebar_frame)
        
        # Main dashboard area
        self.dashboard_frame = ctk.CTkFrame(content_frame, corner_radius=0)
        self.dashboard_frame.pack(side="right", fill="both", expand=True, padx=0, pady=0)
        
        # Create dashboard content
        self.create_dashboard_content()
    
    def create_sidebar(self, sidebar_frame):
        """Create navigation sidebar"""
        
        # Sidebar title
        nav_title = ctk.CTkLabel(
            sidebar_frame,
            text=self.t("navigation.title", "NAVIGATION"),
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="gray60"
        )
        nav_title.pack(pady=(25, 15), padx=25, anchor="w")
        
        # Navigation buttons
        nav_buttons = [
            ("📊", self.t("navigation.dashboard", "Dashboard"), self.show_dashboard, True),
            ("📄", self.t("navigation.invoices", "Invoices"), self.show_invoices, False),
            ("🏪", self.t("navigation.providers", "Providers"), self.show_providers, False),
            ("📈", self.t("navigation.analytics", "Analytics"), self.show_analytics, False),
            ("💰", self.t("navigation.transactions", "Transactions"), self.show_transactions, False),
            ("📋", self.t("navigation.reports", "Reports"), self.show_reports, False)
        ]
        
        self.nav_buttons = {}
        for icon, text, command, is_active in nav_buttons:
            button = ctk.CTkButton(
                sidebar_frame,
                text=f"{icon}  {text}",
                height=45,
                font=ctk.CTkFont(size=16, weight="bold" if is_active else "normal"),
                anchor="w",
                fg_color="#1f538d" if is_active else "transparent",
                hover_color="#2563eb",
                command=command
            )
            button.pack(pady=3, padx=20, fill="x")
            self.nav_buttons[text] = button
        
        # Separator
        separator = ctk.CTkFrame(sidebar_frame, height=2, fg_color="gray30")
        separator.pack(pady=20, padx=20, fill="x")
        
        # Quick Stats section - Using scrollable frame with proper sizing
        stats_container = ctk.CTkScrollableFrame(
            sidebar_frame, 
            width=250,
            height=180,  # Reduced height to prevent overlap
            corner_radius=10
        )
        stats_container.pack(pady=10, padx=20, fill="x")
        
        stats_title = ctk.CTkLabel(
            stats_container,
            text=self.t("dashboard.quick_overview", "QUICK OVERVIEW"),
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="gray60"
        )
        stats_title.pack(pady=(5, 10), anchor="w")
        
        # Quick stats with real data and translations
        stats = self.dashboard_stats
        quick_stats = [
            ("💰", self.t("dashboard.stats.revenue", "Total Revenue"), f"₫{stats['financial']['total_revenue']:,.0f}", "#10b981"),
            ("📄", self.t("dashboard.stats.invoices", "Total Invoices"), str(stats['invoices']['total']), "#3b82f6"),
            ("🏪", self.t("dashboard.stats.providers", "Providers"), str(stats['providers']['total']), "#f59e0b"),
            ("⚠️", self.t("dashboard.stats.overdue", "Overdue"), str(stats['invoices']['overdue']), "#ef4444")
        ]
        
        for icon, title, value, color in quick_stats:
            self.create_quick_stat_card(stats_container, icon, title, value, color)
        
        # Footer info - place at bottom with proper spacing
        footer_frame = ctk.CTkFrame(sidebar_frame, fg_color="transparent")
        footer_frame.pack(side="bottom", fill="x", pady=(5, 15), padx=20)
        
        version_label = ctk.CTkLabel(
            footer_frame,
            text=self.t("app.version", "FinanTidy v2.0 Professional\nwith Viettel eInvoice"),
            font=ctk.CTkFont(size=9),
            text_color="gray50",
            justify="center"
        )
        version_label.pack(pady=5)
    
    def create_quick_stat_card(self, parent, icon, title, value, color):
        """Create quick stat card in sidebar"""
        
        card = ctk.CTkFrame(parent, height=60, corner_radius=8)  # Reduced height
        card.pack(pady=2, padx=5, fill="x")  # Reduced padding
        card.pack_propagate(False)
        
        # Content frame
        content_frame = ctk.CTkFrame(card, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=10, pady=8)  # Reduced padding
        
        # Left side - Icon
        icon_label = ctk.CTkLabel(
            content_frame,
            text=icon,
            font=ctk.CTkFont(size=24),
            width=35
        )
        icon_label.pack(side="left", anchor="center")
        
        # Right side - Info
        info_frame = ctk.CTkFrame(content_frame, fg_color="transparent")
        info_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))
        
        # Value
        value_label = ctk.CTkLabel(
            info_frame,
            text=value,
            font=ctk.CTkFont(size=16, weight="bold"),
            anchor="w"
        )
        value_label.pack(fill="x")
        
        # Title
        title_label = ctk.CTkLabel(
            info_frame,
            text=title,
            font=ctk.CTkFont(size=11),
            text_color="gray70",
            anchor="w"
        )
        title_label.pack(fill="x")
    
    def create_dashboard_content(self):
        """Create main dashboard content"""
        
        # Dashboard container
        dashboard_container = ctk.CTkScrollableFrame(self.dashboard_frame)
        dashboard_container.pack(fill="both", expand=True, padx=25, pady=25)
        
        # Welcome header with translations
        welcome_frame = ctk.CTkFrame(dashboard_container, fg_color="transparent")
        welcome_frame.pack(fill="x", pady=(0, 25))
        
        welcome_text = self.t("dashboard.welcome", "Welcome back, {name}!").format(
            name=self.session_data.get('username', 'User')
        )
        welcome_title = ctk.CTkLabel(
            welcome_frame,
            text=f"{welcome_text} 👋",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        welcome_title.pack(anchor="w")
        
        welcome_subtitle = ctk.CTkLabel(
            welcome_frame,
            text=self.t("dashboard.welcome_subtitle", "Here's what's happening with your finances today"),
            font=ctk.CTkFont(size=16),
            text_color="gray70"
        )
        welcome_subtitle.pack(anchor="w", pady=(5, 0))
        
        # Stats cards row
        stats_frame = ctk.CTkFrame(dashboard_container, fg_color="transparent")
        stats_frame.pack(fill="x", pady=(0, 25))
        
        # Configure grid
        stats_frame.grid_columnconfigure(0, weight=1)
        stats_frame.grid_columnconfigure(1, weight=1)
        stats_frame.grid_columnconfigure(2, weight=1)
        stats_frame.grid_columnconfigure(3, weight=1)
        
        # Main stats cards
        main_stats = [
            ("💰", "Total Revenue", "₫150,200,000", "+12.5%", "#10b981"),
            ("📈", "Monthly Growth", "₫25,800,000", "+8.2%", "#3b82f6"),
            ("📄", "Total Invoices", "245", "+5 this week", "#f59e0b"),
            ("🏪", "Active Providers", "15", "2 new", "#8b5cf6")
        ]
        
        for i, (icon, title, value, change, color) in enumerate(main_stats):
            card = self.create_main_stat_card(stats_frame, icon, title, value, change, color)
            card.grid(row=0, column=i, padx=(0, 15) if i < 3 else 0, sticky="ew")
        
        # Content sections row
        content_sections = ctk.CTkFrame(dashboard_container, fg_color="transparent")
        content_sections.pack(fill="both", expand=True, pady=(0, 25))
        
        # Configure grid for content sections
        content_sections.grid_columnconfigure(0, weight=2)
        content_sections.grid_columnconfigure(1, weight=1)
        content_sections.grid_rowconfigure(0, weight=1)
        
        # Recent activity section
        recent_activity = self.create_recent_activity_section(content_sections)
        recent_activity.grid(row=0, column=0, sticky="nsew", padx=(0, 15))
        
        # Quick actions section
        quick_actions = self.create_quick_actions_section(content_sections)
        quick_actions.grid(row=0, column=1, sticky="nsew")
    
    def create_main_stat_card(self, parent, icon, title, value, change, color):
        """Create main statistics card"""
        
        card = ctk.CTkFrame(parent, corner_radius=15, height=120)
        card.pack_propagate(False)
        
        # Content container
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=15)
        
        # Header with icon
        header = ctk.CTkFrame(content, fg_color="transparent")
        header.pack(fill="x")
        
        icon_container = ctk.CTkFrame(header, width=50, height=50, corner_radius=25, fg_color=color)
        icon_container.pack(side="left")
        icon_container.pack_propagate(False)
        
        icon_label = ctk.CTkLabel(
            icon_container,
            text=icon,
            font=ctk.CTkFont(size=24)
        )
        icon_label.pack(expand=True)
        
        # Value
        value_label = ctk.CTkLabel(
            content,
            text=value,
            font=ctk.CTkFont(size=24, weight="bold")
        )
        value_label.pack(anchor="w", pady=(10, 0))
        
        # Title and change
        footer = ctk.CTkFrame(content, fg_color="transparent")
        footer.pack(fill="x", pady=(5, 0))
        
        title_label = ctk.CTkLabel(
            footer,
            text=title,
            font=ctk.CTkFont(size=14),
            text_color="gray70"
        )
        title_label.pack(side="left")
        
        change_label = ctk.CTkLabel(
            footer,
            text=change,
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#10b981"
        )
        change_label.pack(side="right")
        
        return card
    
    def create_recent_activity_section(self, parent):
        """Create recent activity section"""
        
        section = ctk.CTkFrame(parent, corner_radius=15)
        
        # Header
        header = ctk.CTkFrame(section, fg_color="transparent")
        header.pack(fill="x", padx=25, pady=(25, 15))
        
        title = ctk.CTkLabel(
            header,
            text=f"📋 {self.t('dashboard.recent_activity', 'Recent Activity')}",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack(side="left")
        
        view_all_button = ctk.CTkButton(
            header,
            text=self.t("dashboard.view_all", "View All"),
            width=80,
            height=30,
            font=ctk.CTkFont(size=12),
            fg_color="transparent",
            hover_color="gray20",
            border_width=1
        )
        view_all_button.pack(side="right")
        
        # Activity list
        activity_frame = ctk.CTkFrame(section, fg_color="transparent")
        activity_frame.pack(fill="both", expand=True, padx=25, pady=(0, 25))
        
        activities = [
            ("📄", "New invoice #INV-2025-001", "ABC Company Ltd. - ₫8,500,000", "2 hours ago", "#3b82f6"),
            ("💰", "Payment received", "XYZ Corp payment processed", "4 hours ago", "#10b981"),
            ("🏪", "Provider added", "Tech Solutions Ltd. registered", "6 hours ago", "#f59e0b"),
            ("📊", "Report generated", "Monthly financial summary", "1 day ago", "#8b5cf6"),
            ("⚙️", "System backup", "Automatic backup completed", "1 day ago", "#6b7280")
        ]
        
        for icon, title, description, time, color in activities:
            activity_item = self.create_activity_item(activity_frame, icon, title, description, time, color)
            activity_item.pack(fill="x", pady=3)
        
        return section
    
    def create_activity_item(self, parent, icon, title, description, time, color):
        """Create activity item"""
        
        item = ctk.CTkFrame(parent, height=70, corner_radius=10, fg_color="gray10")
        item.pack_propagate(False)
        
        content = ctk.CTkFrame(item, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=15, pady=10)
        
        # Icon
        icon_container = ctk.CTkFrame(content, width=40, height=40, corner_radius=20, fg_color=color)
        icon_container.pack(side="left")
        icon_container.pack_propagate(False)
        
        icon_label = ctk.CTkLabel(
            icon_container,
            text=icon,
            font=ctk.CTkFont(size=18)
        )
        icon_label.pack(expand=True)
        
        # Info
        info_frame = ctk.CTkFrame(content, fg_color="transparent")
        info_frame.pack(side="left", fill="both", expand=True, padx=(15, 0))
        
        title_label = ctk.CTkLabel(
            info_frame,
            text=title,
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        )
        title_label.pack(fill="x")
        
        desc_label = ctk.CTkLabel(
            info_frame,
            text=description,
            font=ctk.CTkFont(size=12),
            text_color="gray70",
            anchor="w"
        )
        desc_label.pack(fill="x")
        
        # Time
        time_label = ctk.CTkLabel(
            content,
            text=time,
            font=ctk.CTkFont(size=10),
            text_color="gray60"
        )
        time_label.pack(side="right", anchor="ne")
        
        return item
    
    def create_quick_actions_section(self, parent):
        """Create quick actions section"""
        
        section = ctk.CTkFrame(parent, corner_radius=15)
        
        # Header
        header = ctk.CTkFrame(section, fg_color="transparent")
        header.pack(fill="x", padx=25, pady=(25, 15))
        
        title = ctk.CTkLabel(
            header,
            text=f"⚡ {self.t('dashboard.quick_actions', 'Quick Actions')}",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        title.pack()
        
        # Actions
        actions_frame = ctk.CTkFrame(section, fg_color="transparent")
        actions_frame.pack(fill="both", expand=True, padx=25, pady=(0, 25))
        
        # Action buttons with translations
        actions = [
            ("📄", self.t("actions.create_invoice", "Create Invoice"), self.create_invoice),
            ("🏪", self.t("actions.add_provider", "Add Provider"), self.add_provider),
            ("💰", self.t("actions.record_payment", "Record Payment"), self.record_payment),
            ("📊", self.t("actions.generate_report", "Generate Report"), self.generate_report),
            ("📋", self.t("actions.viettel_einvoice", "Viettel eInvoice"), self.open_viettel_config),
            ("⚙️", self.t("actions.system_settings", "System Settings"), self.show_settings),
            ("📈", self.t("actions.view_analytics", "View Analytics"), self.show_analytics)
        ]
        
        for icon, text, command in actions:
            button = ctk.CTkButton(
                actions_frame,
                text=f"{icon}  {text}",
                height=45,
                font=ctk.CTkFont(size=14, weight="bold"),
                anchor="w",
                command=command
            )
            button.pack(fill="x", pady=5)
        
        return section
    
    # Navigation methods
    def show_dashboard(self):
        self.set_active_nav("Dashboard")
        # Clear and recreate dashboard content
        for widget in self.dashboard_frame.winfo_children():
            widget.destroy()
        self.create_dashboard_content()
        print("Dashboard selected")
    
    def show_invoices(self):
        self.set_active_nav("Invoices")
        # Show placeholder content for invoices
        self.show_module_placeholder("📄 Invoices Management", 
                                   "Invoice management module is being prepared.\nFeatures: Create, edit, send invoices, track payments.")
    
    def show_providers(self):
        self.set_active_nav("Providers")
        # Show placeholder content for providers
        self.show_module_placeholder("🏪 Providers Management", 
                                   "Provider management module is being prepared.\nFeatures: Add providers, manage contracts, track payments.")
    
    def show_analytics(self):
        self.set_active_nav("Analytics")
        # Show placeholder content for analytics
        self.show_module_placeholder("📊 Analytics Dashboard", 
                                   "Analytics module is being prepared.\nFeatures: Financial reports, charts, business insights.")
    
    def show_transactions(self):
        self.set_active_nav("Transactions")
        # Show placeholder content for transactions
        self.show_module_placeholder("💳 Transactions Management", 
                                   "Transaction module is being prepared.\nFeatures: Record transactions, categorize expenses, track income.")
    
    def show_reports(self):
        self.set_active_nav("Reports")
        # Show placeholder content for reports
        self.show_module_placeholder("📈 Reports & Analysis", 
                                   "Reports module is being prepared.\nFeatures: Generate reports, export data, financial analysis.")
    
    def show_module_placeholder(self, title, description):
        """Show placeholder content for modules under development"""
        # Clear dashboard frame and show placeholder
        for widget in self.dashboard_frame.winfo_children():
            widget.destroy()
        
        # Create placeholder content
        placeholder_frame = ctk.CTkFrame(self.dashboard_frame)
        placeholder_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title_label = ctk.CTkLabel(
            placeholder_frame,
            text=title,
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.pack(pady=(50, 20))
        
        # Description
        desc_label = ctk.CTkLabel(
            placeholder_frame,
            text=description,
            font=ctk.CTkFont(size=16),
            text_color="gray70"
        )
        desc_label.pack(pady=(0, 30))
        
        # Coming soon badge
        badge = ctk.CTkFrame(placeholder_frame, fg_color="#f59e0b", corner_radius=20)
        badge.pack(pady=20)
        
        badge_label = ctk.CTkLabel(
            badge,
            text="🚧 Coming Soon",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="white"
        )
        badge_label.pack(padx=20, pady=10)
    
    def set_active_nav(self, active_item):
        """Set active navigation item"""
        for item, button in self.nav_buttons.items():
            if item == active_item:
                button.configure(fg_color="#1f538d", font=ctk.CTkFont(size=16, weight="bold"))
            else:
                button.configure(fg_color="transparent", font=ctk.CTkFont(size=16, weight="normal"))
    
    # Action methods with translations
    def create_invoice(self):
        messagebox.showinfo(
            self.t("actions.create_invoice", "Create Invoice"), 
            self.t("messages.coming_soon", "Invoice creation module will be available soon!")
        )
    
    def add_provider(self):
        messagebox.showinfo(
            self.t("actions.add_provider", "Add Provider"), 
            self.t("messages.coming_soon", "Provider management module will be available soon!")
        )
    
    def record_payment(self):
        messagebox.showinfo(
            self.t("actions.record_payment", "Record Payment"), 
            self.t("messages.coming_soon", "Payment recording module will be available soon!")
        )
    
    def generate_report(self):
        messagebox.showinfo(
            self.t("actions.generate_report", "Generate Report"), 
            self.t("messages.coming_soon", "Report generation module will be available soon!")
        )
    
    def show_settings(self):
        # Open settings configuration window with language support
        try:
            from .settings_window import SettingsWindow
            settings_window = SettingsWindow(self, self.session_data)
            settings_window.focus()
        except Exception as e:
            messagebox.showerror(self.t("messages.error", "Error"), 
                               f"Failed to open Settings module:\n{str(e)}")
    
    def open_viettel_config(self):
        """Open Viettel eInvoice configuration directly"""
        try:
            from .viettel_config_window import ViettelConfigWindow
            viettel_window = ViettelConfigWindow(self)
            viettel_window.focus()
        except Exception as e:
            messagebox.showerror(
                self.t("messages.error", "Error"), 
                f"Failed to open Viettel eInvoice configuration:\n{str(e)}"
            )
    
    def logout(self):
        """Handle logout with database cleanup"""
        logout_msg = self.t("messages.logout_confirm", 
                           "Are you sure you want to logout?\n\nUser: {user}\nCompany: {company}").format(
                               user=self.session_data['full_name'],
                               company=self.session_data['company_name']
                           )
        result = messagebox.askyesno(self.t("buttons.logout", "Logout"), logout_msg)
        if result:
            # Cleanup database connections if needed
            try:
                if self.db_manager:
                    # Log logout activity
                    pass  # Could add audit logging here
            except Exception as e:
                print(f"Logout cleanup error: {e}")
            
            self.destroy()
            # Restart login window
            from .login_window import ModernLoginWindow
            login_window = ModernLoginWindow()
            login_window.mainloop()
    
    def on_closing(self):
        """Handle window closing"""
        result = messagebox.askyesno("Exit", "Are you sure you want to exit FinanTidy?")
        if result:
            self.destroy()

def main():
    """Main function for testing"""
    session_data = {
        "user_id": 1,
        "username": "demo", 
        "full_name": "Demo User",
        "company_id": 1,
        "company_name": "Demo Company",
        "role": "admin",
        "license": {"type": "free"}
    }
    app = ModernMainWindow(session_data)
    app.mainloop()

if __name__ == "__main__":
    main()
