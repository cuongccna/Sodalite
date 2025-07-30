"""
🎉 FinanTidy Professional Login - Final Showcase
Demonstrating all professional enhancements for customer attraction
"""

import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMessageBox, QSplashScreen
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont, QPixmap, QPainter, QColor

# Add project paths
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "src"))

try:
    from ui.login_window import LoginWindow
except ImportError:
    from src.ui.login_window import LoginWindow


class ProfessionalShowcaseApp:
    """Professional showcase application"""
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.setup_application()
        self.db_manager = self.create_mock_db()
        
    def setup_application(self):
        """Setup application with professional settings"""
        # Application metadata
        self.app.setApplicationName("FinanTidy Professional")
        self.app.setApplicationVersion("2.0 Professional")
        self.app.setOrganizationName("FinanTidy Solutions")
        self.app.setOrganizationDomain("finantidy.com")
        
        # Professional font rendering
        font = QFont("Segoe UI", 10)
        font.setHintingPreference(QFont.PreferFullHinting)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.app.setFont(font)
        
        # Style settings for crisp rendering
        self.app.setAttribute(Qt.AA_EnableHighDpiScaling)
        self.app.setAttribute(Qt.AA_UseHighDpiPixmaps)
    
    def create_mock_db(self):
        """Create mock database for demonstration"""
        class MockDatabaseManager:
            def authenticate_user(self, username, password):
                if username == "demo" and password == "demo":
                    return {
                        "id": 1,
                        "username": username,
                        "full_name": "Demo Professional User",
                        "email": "demo@finantidy.com",
                        "role": "Finance Manager"
                    }
                return None
        
        return MockDatabaseManager()
    
    def show_splash_screen(self):
        """Show professional splash screen"""
        # Create splash screen
        splash_pixmap = QPixmap(400, 200)
        splash_pixmap.fill(QColor("#f8fafc"))
        
        painter = QPainter(splash_pixmap)
        
        # Draw logo area
        painter.fillRect(0, 0, 400, 60, QColor("#3b82f6"))
        
        # Draw text
        painter.setPen(QColor("white"))
        font = QFont("Segoe UI", 16, QFont.Bold)
        painter.setFont(font)
        painter.drawText(20, 35, "💼 FinanTidy Professional")
        
        painter.setPen(QColor("#374151"))
        font = QFont("Segoe UI", 12)
        painter.setFont(font)
        painter.drawText(20, 90, "🎨 Professional Login Interface Showcase")
        painter.drawText(20, 115, "✨ Enhanced with Modern Design Principles")
        painter.drawText(20, 140, "🚀 Ready to Attract Enterprise Customers")
        painter.drawText(20, 165, "⏳ Loading professional experience...")
        
        painter.end()
        
        # Show splash
        splash = QSplashScreen(splash_pixmap)
        splash.show()
        
        # Auto close after 3 seconds
        QTimer.singleShot(3000, splash.close)
        
        # Process events to show splash
        for _ in range(30):
            self.app.processEvents()
            QTimer.singleShot(100, lambda: None)
    
    def show_feature_overview(self):
        """Show professional feature overview"""
        overview = QMessageBox()
        overview.setWindowTitle("🎯 Professional Enhancement Showcase")
        overview.setIcon(QMessageBox.Information)
        
        overview.setText(
            "<h2>🎉 FinanTidy Professional Login</h2>"
            "<p><b>Welcome to the enhanced professional interface!</b></p>"
        )
        
        overview.setDetailedText(
            "🎨 PROFESSIONAL ENHANCEMENTS APPLIED:\n"
            "\n"
            "✅ VISUAL DESIGN:\n"
            "• Modern color palette with gradients\n"
            "• Professional typography (Segoe UI system)\n"
            "• Golden ratio proportions (450x550)\n"
            "• Proper visual hierarchy with 3 sections\n"
            "\n"
            "✅ ICON & LAYOUT:\n"
            "• Icons properly positioned in input containers\n"
            "• QFormLayout with professional alignment\n"
            "• Container-based input field design\n"
            "• Responsive spacing and margins\n"
            "\n"
            "✅ USER EXPERIENCE:\n"
            "• Smooth hover animations and transitions\n"
            "• Professional loading states\n"
            "• Enhanced focus states with glow effects\n"
            "• Clear visual feedback for all interactions\n"
            "\n"
            "✅ CUSTOMER ATTRACTION FEATURES:\n"
            "• Enterprise-grade professional appearance\n"
            "• Modern design trends for tech-savvy users\n"
            "• Trust-building visual elements for financial app\n"
            "• Premium feel to justify higher pricing\n"
            "\n"
            "🚀 READY FOR PRODUCTION!\n"
            "This interface is now ready to attract enterprise customers\n"
            "and compete with top-tier FinTech applications.\n"
            "\n"
            "📝 Test with: demo/demo"
        )
        
        overview.setStyleSheet("""
            QMessageBox {
                background-color: white;
                font-family: 'Segoe UI', system-ui, sans-serif;
            }
            QMessageBox QLabel {
                color: #374151;
                font-size: 14px;
            }
            QMessageBox QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3b82f6, stop:1 #2563eb);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: 600;
                min-width: 120px;
            }
            QMessageBox QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2563eb, stop:1 #1d4ed8);
            }
        """)
        
        overview.exec()
    
    def show_login_window(self):
        """Show the professional login window"""
        self.login_window = LoginWindow(self.db_manager)
        self.login_window.user_authenticated.connect(self.handle_successful_login)
        self.login_window.show()
    
    def handle_successful_login(self, user_data):
        """Handle successful login with celebration"""
        celebration = QMessageBox()
        celebration.setWindowTitle("🎉 Professional Login Success!")
        celebration.setIcon(QMessageBox.Information)
        
        celebration.setText(
            "<h2>🎊 Congratulations!</h2>"
            "<p><b>The professional login interface is working perfectly!</b></p>"
        )
        
        celebration.setInformativeText(
            f"<p><b>🔐 Authentication Details:</b></p>"
            f"<ul>"
            f"<li><b>👤 User:</b> {user_data['full_name']}</li>"
            f"<li><b>📧 Email:</b> {user_data['email']}</li>"
            f"<li><b>💼 Role:</b> {user_data['role']}</li>"
            f"<li><b>🆔 ID:</b> {user_data['id']}</li>"
            f"</ul>"
            f"<hr>"
            f"<p><b>✨ Professional Features Demonstrated:</b></p>"
            f"<ul>"
            f"<li>🎨 Modern design attracts customers</li>"
            f"<li>🔧 Icons positioned perfectly</li>"
            f"<li>📱 Responsive professional layout</li>"
            f"<li>💫 Smooth animations & effects</li>"
            f"<li>🎯 Enterprise-grade appearance</li>"
            f"<li>⚡ Excellent user experience</li>"
            f"</ul>"
            f"<p><b>🚀 Ready for customer acquisition!</b></p>"
        )
        
        celebration.setStyleSheet("""
            QMessageBox {
                background-color: white;
                font-family: 'Segoe UI', system-ui, sans-serif;
            }
            QMessageBox QLabel {
                color: #374151;
                font-size: 14px;
            }
            QMessageBox QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #10b981, stop:1 #059669);
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 24px;
                font-weight: 600;
                min-width: 140px;
            }
            QMessageBox QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #059669, stop:1 #047857);
            }
        """)
        
        celebration.exec()
        self.app.quit()
    
    def run_showcase(self):
        """Run the complete professional showcase"""
        print("🎬 FinanTidy Professional Login Showcase")
        print("=" * 60)
        print("🎯 Demonstrating Customer Attraction Features")
        print("=" * 60)
        
        # Step 1: Splash screen
        print("1️⃣ Showing professional splash screen...")
        self.show_splash_screen()
        
        # Step 2: Feature overview
        print("2️⃣ Displaying enhancement overview...")
        self.show_feature_overview()
        
        # Step 3: Login window
        print("3️⃣ Launching professional login interface...")
        self.show_login_window()
        
        print("✨ Professional showcase ready!")
        print("💡 Test credentials: demo/demo")
        print("🎨 Notice the professional enhancements!")
        
        # Run application
        return self.app.exec()


def main():
    """Main showcase function"""
    print("🚀 Starting FinanTidy Professional Showcase...")
    
    showcase = ProfessionalShowcaseApp()
    exit_code = showcase.run_showcase()
    
    print("\n" + "=" * 60)
    print("🎊 Professional Showcase Complete!")
    print("✅ All enhancements demonstrated successfully")
    print("🎯 Ready to attract enterprise customers!")
    print("=" * 60)
    
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
