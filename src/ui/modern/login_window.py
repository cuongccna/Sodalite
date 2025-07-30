"""
FinanTidy - Modern Login Window with CustomTkinter
Professional dark theme interface with database authentication and multi-language support
"""

import customtkinter as ctk
from tkinter import messagebox
import sys
import os
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")  # "dark" or "light"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

# Import language manager
try:
    from core.language_manager import get_language_manager, t
    _lang_manager = get_language_manager()
    _t = t
except ImportError:
    # Fallback if language manager not available
    _lang_manager = None
    _t = lambda key, default=None: default or key

# Import database manager
try:
    from ...database.database_manager import get_db_manager
except ImportError:
    try:
        from src.database.database_manager import get_db_manager
    except ImportError:
        # Mock for testing
        def get_db_manager():
            class MockManager:
                def authenticate_user(self, username, password):
                    if username == "admin" and password == "admin":
                        return {
                            'user': {'id': 1, 'username': 'admin', 'full_name': 'Administrator'},
                            'companies': [{'id': 1, 'name': 'Demo Company', 'role': 'owner'}],
                            'license': {'type': 'free', 'max_companies': 1}
                        }
                    return None
            return MockManager()

class ModernLoginWindow(ctk.CTk):
    """Modern Login Window with Database Authentication and Multi-language Support"""
    
    def __init__(self):
        super().__init__()
        
        # Initialize language support
        self.lang_manager = _lang_manager
        self.t = _t
        
        # Load language settings
        self.load_language_settings()
        
        # Database manager
        try:
            self.db_manager = get_db_manager()
        except Exception as e:
            print(f"Database initialization error: {e}")
            self.db_manager = get_db_manager()  # Will use mock
        
        # Window configuration
        self.title(self.t("login.title", "FinanTidy - Professional Login"))
        self.geometry("550x750")  # Increased height for better spacing
        self.resizable(False, False)
        
        # Center window
        self.center_window()
        
        # Set protocol for window close
        self.protocol("WM_DELETE_WINDOW", self.cancel_action)
        
        # Create UI
        self.create_login_ui()
        
        # Load language settings
        self.load_language_settings()
    
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
    
    def center_window(self):
        """Center window on screen"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (550 // 2)
        y = (self.winfo_screenheight() // 2) - (750 // 2)  # Updated for new height
        self.geometry(f"550x750+{x}+{y}")
    
    def create_login_ui(self):
        """Create modern login interface"""
        
        # Main container frame
        main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=30, pady=40)
        
        # Top spacer
        top_spacer = ctk.CTkFrame(main_frame, height=50, fg_color="transparent")
        top_spacer.pack(fill="x")
        
        # Logo/Icon section with background
        logo_container = ctk.CTkFrame(main_frame, corner_radius=20, height=140)
        logo_container.pack(pady=(0, 30), padx=20, fill="x")
        logo_container.pack_propagate(False)
        
        # App icon
        icon_label = ctk.CTkLabel(
            logo_container, 
            text="💰", 
            font=ctk.CTkFont(size=70, weight="bold")
        )
        icon_label.pack(expand=True)
        
        # Title section
        title_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        title_frame.pack(pady=(0, 10), fill="x")
        
        title_label = ctk.CTkLabel(
            title_frame,
            text=_t("app.welcome", "Welcome to FinanTidy"),
            font=ctk.CTkFont(size=32, weight="bold")
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = ctk.CTkLabel(
            title_frame,
            text=_t("app.subtitle", "Professional Financial Management System"),
            font=ctk.CTkFont(size=16),
            text_color="gray70"
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Login form frame
        form_frame = ctk.CTkFrame(main_frame, corner_radius=20)
        form_frame.pack(pady=(30, 20), padx=20, fill="x")
        
        # Form title
        form_title = ctk.CTkLabel(
            form_frame,
            text=_t("login.form_title", "Sign In to Your Account"),
            font=ctk.CTkFont(size=20, weight="bold")
        )
        form_title.pack(pady=(30, 25))
        
        # Username field
        username_label = ctk.CTkLabel(
            form_frame, 
            text=_t("login.username", "Username or Email"),
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        )
        username_label.pack(pady=(10, 5), padx=30, fill="x")
        
        self.username_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text=_t("login.username_placeholder", "Enter your username or email"),
            height=50,
            width=400,  # Fixed width
            font=ctk.CTkFont(size=16),
            corner_radius=12
        )
        self.username_entry.pack(pady=(0, 20), padx=30, fill="x")
        self.username_entry.insert(0, "admin")  # Default admin username
        
        # Password field
        password_label = ctk.CTkLabel(
            form_frame, 
            text=_t("login.password", "Password"),
            font=ctk.CTkFont(size=14, weight="bold"),
            anchor="w"
        )
        password_label.pack(pady=(0, 5), padx=30, fill="x")
        
        self.password_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text=_t("login.password_placeholder", "Enter your password"),
            show="*",
            height=50,
            width=400,  # Fixed width
            font=ctk.CTkFont(size=16),
            corner_radius=12
        )
        self.password_entry.pack(pady=(0, 25), padx=30, fill="x")
        self.password_entry.insert(0, "admin")  # Default admin password
        
        # Remember me checkbox
        remember_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
        remember_frame.pack(pady=(0, 25), padx=30, fill="x")
        
        self.remember_var = ctk.BooleanVar()
        remember_checkbox = ctk.CTkCheckBox(
            remember_frame,
            text=_t("login.remember_me", "Remember me"),
            variable=self.remember_var,
            font=ctk.CTkFont(size=14)
        )
        remember_checkbox.pack(side="left")
        
        # Forgot password link
        forgot_button = ctk.CTkButton(
            remember_frame,
            text=_t("login.forgot_password", "Forgot Password?"),
            font=ctk.CTkFont(size=12),
            fg_color="transparent",
            text_color="gray70",
            hover_color="gray20",
            height=25,
            width=120,
            command=self.forgot_password
        )
        forgot_button.pack(side="right")
        
        # Login button
        self.login_button = ctk.CTkButton(
            form_frame,
            text=_t('login.login_button', '🔐 ĐĂNG NHẬP'),
            height=55,
            font=ctk.CTkFont(size=18, weight="bold"),
            corner_radius=15,
            fg_color="#1f538d",
            hover_color="#2563eb",
            command=self.login_action
        )
        self.login_button.pack(pady=(0, 15), padx=30, fill="x")
        
        # Cancel/Exit button  
        self.cancel_button = ctk.CTkButton(
            form_frame,
            text=_t('login.cancel_button', '❌ HỦY BỎ'),
            height=45,
            font=ctk.CTkFont(size=16, weight="bold"),
            corner_radius=15,
            fg_color="#ef4444",
            hover_color="#dc2626",
            command=self.cancel_action
        )
        self.cancel_button.pack(pady=(0, 20), padx=30, fill="x")
        
        # Footer section
        footer_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        footer_frame.pack(pady=(20, 30), fill="x")
        
        # Demo credentials info with better styling
        demo_frame = ctk.CTkFrame(footer_frame, corner_radius=12, fg_color="gray20")
        demo_frame.pack(pady=(0, 15), padx=20, fill="x")
        
        demo_title = ctk.CTkLabel(
            demo_frame,
            text=_t("login.demo_title", "🔑 Default Login Credentials"),
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#60a5fa"
        )
        demo_title.pack(pady=(15, 5))
        
        demo_info = ctk.CTkLabel(
            demo_frame,
            text=_t("login.demo_info", "Username: admin  •  Password: admin"),
            font=ctk.CTkFont(size=13),
            text_color="gray70"
        )
        demo_info.pack(pady=(0, 15))
        
        # Version info
        version_info = ctk.CTkLabel(
            footer_frame,
            text=_t("app.version", "FinanTidy v2.0 - Professional Edition with Viettel eInvoice Integration"),
            font=ctk.CTkFont(size=11),
            text_color="gray50"
        )
        version_info.pack(pady=(5, 0))
        
        # Bind Enter key
        self.bind('<Return>', lambda event: self.login_action())
        self.username_entry.bind('<Return>', lambda event: self.password_entry.focus())
        self.password_entry.bind('<Return>', lambda event: self.login_action())
        
        # Focus on username field
        self.username_entry.focus()
    
    def login_action(self):
        """Handle login action"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Login Error", "Please enter both username and password!")
            return
        
        # Show loading state
        self.login_button.configure(text="Signing In...", state="disabled")
        self.cancel_button.configure(state="disabled")
        self.update()
        
        try:
            # Try database authentication
            user_data = self.db_manager.authenticate_user(username, password)
            
            if user_data:
                # Extract user info safely
                user_info = user_data.get('user', {})
                companies = user_data.get('companies', [])
                
                if not companies:
                    companies = [{'id': 1, 'name': 'Demo Company', 'role': 'admin'}]
                
                # Use first company for demo
                selected_company = companies[0]
                
                # Prepare user session data with defaults
                session_data = {
                    'user_id': user_info.get('id', 1),
                    'username': user_info.get('username', username), 
                    'full_name': user_info.get('full_name', 'Demo User'),
                    'company_id': selected_company.get('id', 1),
                    'company_name': selected_company.get('name', 'Demo Company'),
                    'role': selected_company.get('role', 'admin'),
                    'license': user_data.get('license', {'type': 'demo'})
                }
                
                # Store session data for launcher
                self.session_data = session_data
                
                # Open main window
                self.open_main_window(session_data)
                return
            else:
                messagebox.showerror(_t("login.error_title", "Login Failed"), 
                                   _t("login.error_message", "Invalid username or password!") + "\n\n" +
                                   _t("login.default_credentials", "Default credentials:") + "\n" +
                                   _t("login.username_label", "Username") + ": admin\n" +
                                   _t("login.password_label", "Password") + ": admin")
                
        except Exception as e:
            # Fallback to demo mode on database error
            print(f"Database error (using demo mode): {e}")
            session_data = {
                'user_id': 1,
                'username': username,
                'full_name': 'Demo User',
                'company_id': 1,
                'company_name': 'Demo Company',
                'role': 'admin',
                'license': {'type': 'demo'}
            }
            
            # Store session data for launcher
            self.session_data = session_data
            
            # Open main window
            self.open_main_window(session_data)
            return
        
        finally:
            # Reset button state only if window still exists
            try:
                if self.winfo_exists():
                    self.login_button.configure(text=_t('login.login_button', '🔐 ĐĂNG NHẬP'), state="normal")
                    self.cancel_button.configure(state="normal")
            except:
                pass
    
    def forgot_password(self):
        """Handle forgot password"""
        messagebox.showinfo("Password Recovery", 
                          "Password recovery feature will be available in the next version.\n\n"
                          "For demo access, use:\n"
                          "Username: admin\n"
                          "Password: admin")
    
    def cancel_action(self):
        """Handle cancel action"""
        self.quit()
        self.destroy()
    
    def open_main_window(self, session_data):
        """Open main application window with session data"""
        print("🔧 DEBUG: Opening main window...")
        try:
            # Import main window
            from .main_window import ModernMainWindow
            print("🔧 DEBUG: Main window imported")
            
            # Hide login window
            self.withdraw()
            print("🔧 DEBUG: Login window hidden")
            
            # Create and show main window
            main_window = ModernMainWindow(session_data)
            print("🔧 DEBUG: Main window created")
            
            # Make sure main window is on top and focused
            main_window.lift()
            main_window.focus_force()
            print("🔧 DEBUG: Main window focused")
            
            # Set up close handler to show login again
            def on_main_close():
                print("🔧 DEBUG: Main window closing...")
                main_window.destroy()
                self.deiconify()  # Show login window again
                self.username_entry.delete(0, 'end')
                self.password_entry.delete(0, 'end')
                self.username_entry.focus()
                print("🔧 DEBUG: Login window restored")
            
            main_window.protocol("WM_DELETE_WINDOW", on_main_close)
            print("🔧 DEBUG: Close handler set")
            
            # Start main window
            print("🔧 DEBUG: Starting main window mainloop...")
            main_window.mainloop()
            print("🔧 DEBUG: Main window mainloop ended")
            
        except ImportError as e:
            print(f"🔧 DEBUG: Import error - {e}")
            messagebox.showerror("Import Error", f"Failed to import main window:\n{str(e)}")
            # Reset login button state
            self.login_button.configure(text=_t('login.login_button', '🔐 ĐĂNG NHẬP'), state="normal")
            self.cancel_button.configure(state="normal")
        except Exception as e:
            print(f"🔧 DEBUG: General error - {e}")
            import traceback
            traceback.print_exc()
            messagebox.showerror("Critical Error", f"Unable to start the main application:\n{str(e)}")
            # Reset login button state  
            self.login_button.configure(text=_t('login.login_button', '🔐 ĐĂNG NHẬP'), state="normal")
            self.cancel_button.configure(state="normal")

def main():
    """Main function for testing"""
    # Create and run the application
    app = ModernLoginWindow()
    app.mainloop()

if __name__ == "__main__":
    main()
