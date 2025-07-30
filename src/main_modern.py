"""
FinanTidy - Main Application Entry Point
Project Sodalite - Modern UI Version

Author: Development Team
Date: July 2025
"""

import sys
import os
from pathlib import Path

# Add src directory to path for imports
src_path = Path(__file__).parent
sys.path.insert(0, str(src_path))

# Try modern UI first, fallback to legacy
try:
    import customtkinter as ctk
    from ui.modern.login_window import ModernLoginWindow
    USE_MODERN_UI = True
    print("🎨 Using Modern CustomTkinter UI")
except ImportError:
    from PySide6.QtWidgets import QApplication
    from PySide6.QtCore import QTranslator, QLocale
    from core.app import FinanTidyApp
    USE_MODERN_UI = False
    print("⚠️  Using Legacy PySide6 UI (CustomTkinter not available)")

def main():
    """Main application entry point"""
    
    if USE_MODERN_UI:
        # Modern CustomTkinter UI
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create modern login window
        login_window = ModernLoginWindow()
        login_window.mainloop()
        
    else:
        # Legacy PySide6 UI
        # Create QApplication instance
        app = QApplication(sys.argv)
        
        # Set application properties
        app.setApplicationName("FinanTidy")
        app.setApplicationVersion("1.0.0")
        app.setOrganizationName("Sodalite Development")
        app.setOrganizationDomain("finantiday.com")
        
        # Initialize translator for internationalization
        translator = QTranslator()
        locale = QLocale.system().name()
        
        # Load Vietnamese translation if available
        if locale.startswith('vi'):
            translator.load(f"translations/finantiday_{locale}.qm")
            app.installTranslator(translator)
        
        # Create and show main application
        main_app = FinanTidyApp()
        main_app.show()
        
        # Start event loop
        sys.exit(app.exec())


if __name__ == "__main__":
    main()
