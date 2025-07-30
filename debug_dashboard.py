#!/usr/bin/env python3
"""
Debug script để kiểm tra tại sao dữ liệu demo không hiển thị
"""

import sys
import os
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

def test_dashboard_data():
    """Test dashboard data loading"""
    print("🔍 Debug Dashboard Data Loading...")
    
    try:
        # Test imports
        from PySide6.QtWidgets import QApplication
        from PySide6.QtCore import Qt
        print("✅ Qt imports successful")
        
        # Test our modules
        from database.manager import DatabaseManager
        from core.license_manager import LicenseManager
        print("✅ Core modules import successful")
        
        # Create minimal app for Qt widgets
        app = QApplication(sys.argv)
        
        # Test database
        db_manager = DatabaseManager()
        db_manager.initialize_master_db()  # Initialize first!
        print("✅ Database manager created and initialized")
        
        # Test license manager
        license_manager = LicenseManager(db_manager)
        print("✅ License manager created")
        
        # Test main window import
        from ui.main_window import MainWindow
        print("✅ MainWindow import successful")
        
        # Create test user data
        test_user = {
            'id': 1,
            'full_name': 'Demo User',
            'username': 'demo'
        }
        
        # Create main window
        print("🏗️ Creating MainWindow...")
        main_window = MainWindow(
            user=test_user,
            company_tax_code="0123456789",
            db_manager=db_manager,
            license_manager=license_manager
        )
        
        print("✅ MainWindow created successfully")
        
        # Check if data loading methods exist
        if hasattr(main_window, 'load_dashboard_data'):
            print("✅ load_dashboard_data method exists")
            main_window.load_dashboard_data()
            print("✅ load_dashboard_data executed")
        else:
            print("❌ load_dashboard_data method missing")
            
        if hasattr(main_window, 'load_invoices_data'):
            print("✅ load_invoices_data method exists")
            main_window.load_invoices_data()
            print("✅ load_invoices_data executed")
        else:
            print("❌ load_invoices_data method missing")
        
        # Check if UI components exist
        if hasattr(main_window, 'recent_invoices_table'):
            row_count = main_window.recent_invoices_table.rowCount()
            print(f"✅ Recent invoices table has {row_count} rows")
        else:
            print("❌ recent_invoices_table not found")
            
        if hasattr(main_window, 'invoices_table'):
            row_count = main_window.invoices_table.rowCount()
            print(f"✅ Main invoices table has {row_count} rows")
        else:
            print("❌ invoices_table not found")
        
        # Show the window to test
        main_window.show()
        print("✅ MainWindow shown")
        
        print("\n🎯 Dashboard should now display with sample data!")
        print("   Check the application window for:")
        print("   • 6 statistics cards with real numbers")
        print("   • Recent invoices table with 5 rows")
        print("   • Invoices tab with 10 sample invoices")
        print("   • Vietnamese interface throughout")
        
        # Don't exit immediately, let user see the window
        import time
        time.sleep(2)
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_dashboard_data()
