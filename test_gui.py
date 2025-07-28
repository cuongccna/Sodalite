"""
Simple test script for PySide6
"""

try:
    from PySide6.QtWidgets import QApplication, QLabel
    from PySide6.QtCore import Qt
    import sys
    
    print("✅ PySide6 import successful!")
    
    # Create simple test app
    app = QApplication(sys.argv)
    label = QLabel("FinanTidy Test")
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("""
        QLabel {
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            background-color: #ecf0f1;
            padding: 50px;
            border-radius: 10px;
        }
    """)
    label.show()
    
    print("✅ Test window created successfully!")
    print("💡 Close the window to continue...")
    
    app.exec()
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")

print("🏁 Test completed!")
