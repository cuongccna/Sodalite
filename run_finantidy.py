"""
FinanTidy - Main Application Entry Point
Professional Financial Management System with Database
"""

import sys
import os
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore", category=UserWarning)

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def main():
    """Main application entry point"""
    
    print("=" * 60)
    print("🎯 FinanTidy Professional - Financial Management System")
    print("📅 Version 2.0 - Database Edition")
    print("🏢 Complete Business Financial Solution")
    print("=" * 60)
    print()
    print("🚀 Starting application...")
    
    try:
        # Check database connection
        print("🔧 Checking database connection...")
        from src.database.database_manager import get_db_manager
        db_manager = get_db_manager()
        print("✅ Database connection established")
        
        # Load UI framework
        print("🎨 Loading CustomTkinter framework...")
        import customtkinter as ctk
        from src.ui.modern.login_window import ModernLoginWindow as LoginWindow
        print("✅ Modern UI framework loaded")
        print("✅ All modules ready")
        print()
        
        # Initialize and run login window
        print("🎭 Starting login interface...")
        app = LoginWindow()
        print("✅ Login window ready")
        app.mainloop()
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("\n📋 Please install required dependencies:")
        print("   pip install -r requirements_database.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Application Error: {e}")
        print("\n🔧 Troubleshooting:")
        print("   1. Initialize database: python init_database.py")
        print("   2. Install dependencies: pip install -r requirements_database.txt")
        print("   3. Check file permissions")
        sys.exit(1)

if __name__ == "__main__":
    main()
