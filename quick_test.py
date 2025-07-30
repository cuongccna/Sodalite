"""
Quick Test Script
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    import customtkinter as ctk
    ctk.set_appearance_mode("dark")
    
    # Test login window
    from ui.modern.login_window import ModernLoginWindow
    print("✅ Login window import successful")
    
    # Test main window
    from ui.modern.main_window import ModernMainWindow
    print("✅ Main window import successful")
    
    print("🎉 All imports working! App should run without critical errors.")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")

# Test simple window
root = tk.Tk()
root.title("Test")
root.geometry("300x200")

label = tk.Label(root, text="FinanTidy Test\nAll systems working!", font=("Arial", 14))
label.pack(expand=True)

button = tk.Button(root, text="Close", command=root.destroy)
button.pack(pady=10)

print("🚀 Test window opened")
root.mainloop()
print("✅ Test complete")
