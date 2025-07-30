"""
FinanTidy - CustomTkinter Modern UI Demo
Professional dark theme similar to DevExpress
"""

try:
    import customtkinter as ctk
    from PIL import Image
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Please install required packages:")
    print("pip install customtkinter pillow")
    exit(1)

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")  # "dark" or "light"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

class ModernLoginWindow(ctk.CTk):
    """Modern Login Window with CustomTkinter"""
    
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("FinanTidy - Modern Login")
        self.geometry("500x600")
        self.resizable(False, False)
        
        # Center window
        self.center_window()
        
        # Create UI
        self.create_login_ui()
    
    def center_window(self):
        """Center window on screen"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (500 // 2)
        y = (self.winfo_screenheight() // 2) - (600 // 2)
        self.geometry(f"500x600+{x}+{y}")
    
    def create_login_ui(self):
        """Create modern login interface"""
        
        # Main container frame
        main_frame = ctk.CTkFrame(self, corner_radius=0)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Logo/Icon section
        logo_frame = ctk.CTkFrame(main_frame, corner_radius=15)
        logo_frame.pack(pady=(40, 20), padx=40, fill="x")
        
        # App icon
        icon_label = ctk.CTkLabel(
            logo_frame, 
            text="💰", 
            font=ctk.CTkFont(size=60)
        )
        icon_label.pack(pady=20)
        
        # Title
        title_label = ctk.CTkLabel(
            main_frame,
            text="Welcome to FinanTidy",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        title_label.pack(pady=(20, 10))
        
        # Subtitle
        subtitle_label = ctk.CTkLabel(
            main_frame,
            text="Sign in to your account",
            font=ctk.CTkFont(size=16),
            text_color="gray"
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Login form frame
        form_frame = ctk.CTkFrame(main_frame, corner_radius=15)
        form_frame.pack(pady=20, padx=40, fill="x")
        
        # Username field
        username_label = ctk.CTkLabel(
            form_frame, 
            text="Username or Email",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        username_label.pack(pady=(30, 5), padx=30, anchor="w")
        
        self.username_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="Enter your username",
            height=45,
            font=ctk.CTkFont(size=14)
        )
        self.username_entry.pack(pady=(0, 20), padx=30, fill="x")
        self.username_entry.insert(0, "demo")
        
        # Password field
        password_label = ctk.CTkLabel(
            form_frame, 
            text="Password",
            font=ctk.CTkFont(size=14, weight="bold")
        )
        password_label.pack(pady=(0, 5), padx=30, anchor="w")
        
        self.password_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="Enter your password",
            show="*",
            height=45,
            font=ctk.CTkFont(size=14)
        )
        self.password_entry.pack(pady=(0, 30), padx=30, fill="x")
        self.password_entry.insert(0, "demo")
        
        # Login button
        self.login_button = ctk.CTkButton(
            main_frame,
            text="Sign In",
            height=50,
            font=ctk.CTkFont(size=16, weight="bold"),
            command=self.login_action
        )
        self.login_button.pack(pady=20, padx=40, fill="x")
        
        # Remember me checkbox
        self.remember_var = ctk.BooleanVar()
        remember_checkbox = ctk.CTkCheckBox(
            main_frame,
            text="Remember me",
            variable=self.remember_var,
            font=ctk.CTkFont(size=12)
        )
        remember_checkbox.pack(pady=(10, 20))
        
        # Footer links
        footer_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        footer_frame.pack(pady=(20, 30), fill="x")
        
        forgot_button = ctk.CTkButton(
            footer_frame,
            text="Forgot Password?",
            font=ctk.CTkFont(size=12),
            fg_color="transparent",
            text_color="gray",
            hover_color="gray20",
            height=25,
            command=self.forgot_password
        )
        forgot_button.pack()
        
        # Bind Enter key
        self.bind('<Return>', lambda event: self.login_action())
        self.username_entry.bind('<Return>', lambda event: self.password_entry.focus())
        self.password_entry.bind('<Return>', lambda event: self.login_action())
    
    def login_action(self):
        """Handle login action"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password!")
            return
        
        # Demo login
        if username == "demo" and password == "demo":
            messagebox.showinfo("Success", f"Welcome {username}!")
            self.open_main_window()
        else:
            messagebox.showerror("Error", "Invalid credentials!")
    
    def forgot_password(self):
        """Handle forgot password"""
        messagebox.showinfo("Info", "Password recovery feature coming soon!")
    
    def open_main_window(self):
        """Open main application window"""
        self.withdraw()  # Hide login window
        main_window = ModernMainWindow()
        main_window.mainloop()

class ModernMainWindow(ctk.CTk):
    """Modern Main Window with Dashboard"""
    
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("FinanTidy - Dashboard")
        self.geometry("1200x800")
        
        # Create main UI
        self.create_main_ui()
    
    def create_main_ui(self):
        """Create modern dashboard interface"""
        
        # Header frame
        header_frame = ctk.CTkFrame(self, height=70, corner_radius=0)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Header content
        header_content = ctk.CTkFrame(header_frame, fg_color="transparent")
        header_content.pack(fill="both", expand=True, padx=20, pady=15)
        
        # Company info (left)
        company_frame = ctk.CTkFrame(header_content, fg_color="transparent")
        company_frame.pack(side="left", fill="y")
        
        company_label = ctk.CTkLabel(
            company_frame,
            text="🏢 Demo Company",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        company_label.pack(side="left")
        
        # User info (right)
        user_frame = ctk.CTkFrame(header_content, fg_color="transparent")
        user_frame.pack(side="right", fill="y")
        
        user_label = ctk.CTkLabel(
            user_frame,
            text="👤 Demo User",
            font=ctk.CTkFont(size=14)
        )
        user_label.pack(side="right", padx=(0, 10))
        
        logout_button = ctk.CTkButton(
            user_frame,
            text="Logout",
            width=80,
            height=30,
            font=ctk.CTkFont(size=12),
            command=self.logout
        )
        logout_button.pack(side="right")
        
        # Main content area
        content_frame = ctk.CTkFrame(self, corner_radius=0)
        content_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        # Sidebar
        sidebar_frame = ctk.CTkFrame(content_frame, width=250, corner_radius=0)
        sidebar_frame.pack(side="left", fill="y", padx=(0, 0), pady=0)
        sidebar_frame.pack_propagate(False)
        
        # Sidebar navigation
        nav_title = ctk.CTkLabel(
            sidebar_frame,
            text="NAVIGATION",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="gray"
        )
        nav_title.pack(pady=(20, 10), padx=20, anchor="w")
        
        # Navigation buttons
        nav_buttons = [
            ("📊 Dashboard", self.show_dashboard),
            ("📄 Invoices", self.show_invoices),
            ("🏪 Providers", self.show_providers),
            ("📈 Analytics", self.show_analytics),
            ("⚙️ Settings", self.show_settings)
        ]
        
        for text, command in nav_buttons:
            button = ctk.CTkButton(
                sidebar_frame,
                text=text,
                height=40,
                font=ctk.CTkFont(size=14),
                anchor="w",
                command=command
            )
            button.pack(pady=5, padx=20, fill="x")
        
        # Main dashboard area
        self.dashboard_frame = ctk.CTkFrame(content_frame, corner_radius=0)
        self.dashboard_frame.pack(side="right", fill="both", expand=True, padx=0, pady=0)
        
        # Create dashboard content
        self.create_dashboard_content()
    
    def create_dashboard_content(self):
        """Create dashboard content"""
        
        # Dashboard title
        title_frame = ctk.CTkFrame(self.dashboard_frame, fg_color="transparent")
        title_frame.pack(fill="x", padx=20, pady=20)
        
        title_label = ctk.CTkLabel(
            title_frame,
            text="Dashboard",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        title_label.pack(anchor="w")
        
        # Stats cards frame
        stats_frame = ctk.CTkFrame(self.dashboard_frame, fg_color="transparent")
        stats_frame.pack(fill="x", padx=20, pady=(0, 20))
        
        # Stats cards
        stats_data = [
            ("💰", "Total Revenue", "₫120,500,000", "green"),
            ("📄", "Invoices", "245", "blue"),
            ("🏪", "Providers", "18", "orange"),
            ("📊", "This Month", "₫25,800,000", "purple")
        ]
        
        for i, (icon, title, value, color) in enumerate(stats_data):
            card = ctk.CTkFrame(stats_frame, corner_radius=15)
            card.pack(side="left", fill="both", expand=True, padx=(0, 10) if i < 3 else 0)
            
            # Icon
            icon_label = ctk.CTkLabel(
                card,
                text=icon,
                font=ctk.CTkFont(size=30)
            )
            icon_label.pack(pady=(20, 10))
            
            # Title
            title_label = ctk.CTkLabel(
                card,
                text=title,
                font=ctk.CTkFont(size=12),
                text_color="gray"
            )
            title_label.pack()
            
            # Value
            value_label = ctk.CTkLabel(
                card,
                text=value,
                font=ctk.CTkFont(size=20, weight="bold")
            )
            value_label.pack(pady=(5, 20))
        
        # Recent activity frame
        activity_frame = ctk.CTkFrame(self.dashboard_frame, corner_radius=15)
        activity_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        activity_title = ctk.CTkLabel(
            activity_frame,
            text="Recent Activity",
            font=ctk.CTkFont(size=18, weight="bold")
        )
        activity_title.pack(pady=(20, 10), padx=20, anchor="w")
        
        # Activity list
        activities = [
            "📄 New invoice from ABC Company - ₫5,200,000",
            "💰 Payment received from XYZ Corp - ₫8,500,000",
            "🏪 New provider added: Tech Solutions Ltd",
            "📊 Monthly report generated",
            "⚙️ System backup completed"
        ]
        
        for activity in activities:
            activity_item = ctk.CTkFrame(activity_frame, fg_color="transparent")
            activity_item.pack(fill="x", padx=20, pady=5)
            
            activity_label = ctk.CTkLabel(
                activity_item,
                text=activity,
                font=ctk.CTkFont(size=14),
                anchor="w"
            )
            activity_label.pack(fill="x", padx=10, pady=10)
    
    def show_dashboard(self):
        print("Dashboard clicked")
    
    def show_invoices(self):
        print("Invoices clicked")
    
    def show_providers(self):
        print("Providers clicked")
    
    def show_analytics(self):
        print("Analytics clicked")
    
    def show_settings(self):
        print("Settings clicked")
    
    def logout(self):
        """Handle logout"""
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.destroy()
            # Show login window again
            login_window = ModernLoginWindow()
            login_window.mainloop()

if __name__ == "__main__":
    # Create and run the application
    app = ModernLoginWindow()
    app.mainloop()
