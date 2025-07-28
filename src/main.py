"""
FinanTidy - Main Application Entry Point
Project Sodalite

Author: Development Team
Date: July 2025
"""

import sys
import os
from pathlib import Path

# Add src directory to path for imports
src_path = Path(__file__).parent
sys.path.insert(0, str(src_path))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTranslator, QLocale
from core.app import FinanTidyApp


def main():
    """Main application entry point"""
    
    # Create QApplication instance
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("FinanTidy")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Sodalite Development")
    app.setOrganizationDomain("finantiday.com")
    
    # Set application icon (if exists)
    # app.setWindowIcon(QIcon("resources/icons/app_icon.png"))
    
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
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
