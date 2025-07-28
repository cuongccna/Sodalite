"""
Core Application Class
Handles main application lifecycle and coordination
"""

from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QTimer, Signal

from database.manager import DatabaseManager
from core.license_manager import LicenseManager
from ui.login_window import LoginWindow
from ui.welcome_window import WelcomeWindow
from ui.main_window import MainWindow


class FinanTidyApp(QMainWindow):
    """Main application class coordinating all components"""
    
    # Signals
    user_authenticated = Signal(dict)  # Emitted when user successfully logs in
    company_selected = Signal(str)     # Emitted when company is selected
    
    def __init__(self):
        super().__init__()
        
        # Initialize core components
        self.db_manager = DatabaseManager()
        self.license_manager = LicenseManager()
        
        # Application state
        self.current_user = None
        self.current_company = None
        self.main_window = None
        
        # Initialize database
        self._initialize_database()
        
        # Show login window
        self._show_login()
    
    def _initialize_database(self):
        """Initialize master database and check integrity"""
        try:
            self.db_manager.initialize_master_db()
        except Exception as e:
            QMessageBox.critical(
                self,
                "Database Error",
                f"Failed to initialize database: {str(e)}"
            )
            self.close()
    
    def _show_login(self):
        """Show login window"""
        self.login_window = LoginWindow(self.db_manager)
        self.login_window.user_authenticated.connect(self._on_user_authenticated)
        self.login_window.show()
        
        # Hide main window during login
        self.hide()
    
    def _on_user_authenticated(self, user_data):
        """Handle successful user authentication"""
        self.current_user = user_data
        self.login_window.close()
        
        # Check if this is first time user
        if user_data.get('first_login', False):
            self._show_welcome()
        else:
            self._show_company_selection()
    
    def _show_welcome(self):
        """Show welcome screen for first-time users"""
        self.welcome_window = WelcomeWindow()
        self.welcome_window.welcome_completed.connect(self._show_company_selection)
        self.welcome_window.show()
    
    def _show_company_selection(self):
        """Show company selection or go directly to main window"""
        # Get user's companies
        companies = self.db_manager.get_user_companies(self.current_user['id'])
        
        if len(companies) == 0:
            # No companies, show company setup
            self._show_company_setup()
        elif len(companies) == 1:
            # Only one company, select it automatically
            self.current_company = companies[0]['tax_code']
            self._show_main_window()
        else:
            # Multiple companies, show selection dialog
            self._show_company_selection_dialog(companies)
    
    def _show_company_setup(self):
        """Show company setup dialog for new users"""
        # TODO: Implement company setup dialog
        pass
    
    def _show_company_selection_dialog(self, companies):
        """Show dialog to select from multiple companies"""
        # TODO: Implement company selection dialog
        pass
    
    def _show_main_window(self):
        """Show main application window"""
        if self.main_window:
            self.main_window.close()
        
        self.main_window = MainWindow(
            user=self.current_user,
            company_tax_code=self.current_company,
            db_manager=self.db_manager,
            license_manager=self.license_manager
        )
        
        self.main_window.show()
        self.show()  # Show the main app window
    
    def closeEvent(self, event):
        """Handle application close event"""
        # Close all child windows
        if hasattr(self, 'login_window'):
            self.login_window.close()
        if hasattr(self, 'welcome_window'):
            self.welcome_window.close()
        if self.main_window:
            self.main_window.close()
        
        # Close database connections
        self.db_manager.close_all_connections()
        
        event.accept()
