"""
Full Integration Test - Login Window + Database + Dashboard
Test hoàn chỉnh việc tích hợp giao diện mới với hệ thống
"""

import sys
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "src"))

from PySide6.QtWidgets import QApplication, QMessageBox
from database.manager import DatabaseManager
from ui.login_window import LoginWindow
from ui.dashboard_window import DashboardWindow


class FinanTidyTestApp:
    """Full application test với login + dashboard integration"""
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.db_manager = None
        self.login_window = None
        self.dashboard_window = None
        
    def initialize_database(self):
        """Initialize database connection"""
        try:
            self.db_manager = DatabaseManager()
            print("✅ Database initialized successfully")
            return True
        except Exception as e:
            QMessageBox.critical(
                None,
                "Database Error", 
                f"Failed to initialize database:\n{str(e)}"
            )
            return False
    
    def show_login(self):
        """Show login window with new QFormLayout design"""
        self.login_window = LoginWindow(self.db_manager)
        self.login_window.user_authenticated.connect(self.handle_login_success)
        self.login_window.show()
        
        print("🚀 Login Window displayed with QFormLayout design")
        print("📝 Test credentials: demo/demo")
    
    def handle_login_success(self, user_data):
        """Handle successful login and show dashboard"""
        print(f"✅ Login successful for user: {user_data['username']}")
        
        try:
            # Show dashboard
            self.dashboard_window = DashboardWindow(self.db_manager, user_data)
            self.dashboard_window.show()
            
            # Close login window
            if self.login_window:
                self.login_window.close()
            
            print("🎉 Dashboard opened successfully!")
            print("📊 Week 4 features available:")
            print("   • 6 Statistics Cards")
            print("   • 4 Data Analysis Tabs") 
            print("   • Sample data (156.8M VNĐ)")
            print("   • Charts and visualizations")
            
        except Exception as e:
            QMessageBox.critical(
                None,
                "Dashboard Error",
                f"Failed to open dashboard:\n{str(e)}"
            )
    
    def run(self):
        """Run the complete application test"""
        print("🔬 Starting FinanTidy Full Integration Test...")
        print("=" * 50)
        
        # Step 1: Initialize database
        if not self.initialize_database():
            return 1
        
        # Step 2: Show login window
        self.show_login()
        
        # Step 3: Run application
        print("⏳ Waiting for user interaction...")
        return self.app.exec()


def main():
    """Run full integration test"""
    print("🧪 FinanTidy Integration Test")
    print("Testing: QFormLayout Login + Week 4 Dashboard")
    print("=" * 50)
    
    # Create and run test app
    test_app = FinanTidyTestApp()
    exit_code = test_app.run()
    
    print("\n" + "=" * 50)
    print("🏁 Test completed with exit code:", exit_code)
    
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
