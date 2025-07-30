"""
FinanTidy Application Launcher - Fixed Window Management
"""

import sys
import os
import customtkinter as ctk

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """Main application launcher with proper window management"""
    
    # Configure CustomTkinter
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    while True:
        # Step 1: Show login window
        from ui.modern.login_window import ModernLoginWindow
        
        login_app = ModernLoginWindow()
        login_app.mainloop()
        
        # Check if user completed login
        if hasattr(login_app, 'session_data') and login_app.session_data:
            session_data = login_app.session_data
            
            # Clean up login window completely
            try:
                login_app.destroy()
            except:
                pass
            
            # Step 2: Show main window
            try:
                from ui.modern.main_window import ModernMainWindow
                
                main_app = ModernMainWindow(session_data)
                main_app.mainloop()
                
                # Check if user wants to logout and login again
                if hasattr(main_app, 'logout_requested') and main_app.logout_requested:
                    continue  # Go back to login
                else:
                    break  # Exit application
                    
            except Exception as e:
                print(f"Error starting main application: {e}")
                break
        else:
            # User cancelled login
            break
    
    print("FinanTidy application closed.")

if __name__ == "__main__":
    main()
