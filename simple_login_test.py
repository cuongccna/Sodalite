"""
Simple Login Test - Minimal version to test basic functionality
"""

import customtkinter as ctk
from tkinter import messagebox
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SimpleLoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("FinanTidy - Login Test")
        self.geometry("400x500")
        self.resizable(False, False)
        
        # Center window
        self.center_window()
        
        # Create UI
        self.create_ui()
        
    def center_window(self):
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.winfo_screenheight() // 2) - (500 // 2)
        self.geometry(f"400x500+{x}+{y}")
    
    def create_ui(self):
        # Main frame
        main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Title
        title = ctk.CTkLabel(main_frame, text="FinanTidy Login", font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=(20, 30))
        
        # Username
        self.username_entry = ctk.CTkEntry(main_frame, placeholder_text="Username", height=40, width=300)
        self.username_entry.pack(pady=10)
        self.username_entry.insert(0, "admin")
        
        # Password  
        self.password_entry = ctk.CTkEntry(main_frame, placeholder_text="Password", show="*", height=40, width=300)
        self.password_entry.pack(pady=10)
        self.password_entry.insert(0, "admin")
        
        # Login button
        login_btn = ctk.CTkButton(main_frame, text="LOGIN", height=40, width=300, command=self.login)
        login_btn.pack(pady=20)
        
        # Cancel button
        cancel_btn = ctk.CTkButton(main_frame, text="CANCEL", height=40, width=300, 
                                  fg_color="red", hover_color="darkred", command=self.cancel)
        cancel_btn.pack(pady=5)
        
        # Bind Enter key
        self.bind('<Return>', lambda e: self.login())
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username == "admin" and password == "admin":
            messagebox.showinfo("Success", "Login successful!")
            self.destroy()
            self.open_main()
        else:
            messagebox.showerror("Error", "Invalid credentials!")
    
    def cancel(self):
        self.destroy()
    
    def open_main(self):
        # Import and create main window
        try:
            from ui.modern.main_window import ModernMainWindow
            
            session_data = {
                'user_id': 1,
                'username': 'admin',
                'full_name': 'Demo User', 
                'company_id': 1,
                'company_name': 'Demo Company',
                'role': 'admin',
                'license': {'type': 'demo'}
            }
            
            main_window = ModernMainWindow(session_data)
            main_window.mainloop()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open main window: {e}")

if __name__ == "__main__":
    app = SimpleLoginWindow()
    app.mainloop()
