# FinanTidy Development Troubleshooting Guide

## 🐛 Vấn đề PySide6 DLL Load Failed

### Triệu chứng
```
ImportError: DLL load failed while importing QtWidgets: The specified module could not be found.
```

### Nguyên nhân có thể
1. **Missing Visual C++ Redistributables**: PySide6 yêu cầu Visual C++ runtime
2. **PATH Environment Issues**: Python không tìm thấy Qt DLLs
3. **Conflicting Python Installations**: Multiple Python versions gây xung đột
4. **Corrupted Installation**: PySide6 cài đặt không hoàn chỉnh

### Giải pháp A: Cài đặt Visual C++ Redistributables
```bash
# Download và cài đặt từ Microsoft:
# https://aka.ms/vs/17/release/vc_redist.x64.exe
```

### Giải pháp B: Reinstall với conda
```bash
# Tạo conda environment
conda create -n finantiday python=3.11
conda activate finantiday
conda install -c conda-forge pyside6

# Cài đặt remaining packages
pip install -r requirements.txt
```

### Giải pháp C: Alternative với PyQt5
```bash
# Temporary workaround
pip uninstall PySide6
pip install PyQt5

# Update imports trong code:
# from PySide6.QtWidgets import -> from PyQt5.QtWidgets import
# from PySide6.QtCore import -> from PyQt5.QtCore import
```

### Giải pháp D: System Check
```python
# test_system.py
import sys
import os

print("Python Version:", sys.version)
print("Python Path:", sys.executable)
print("PATH:", os.environ.get('PATH', '')[:200] + "...")

try:
    import shiboken6
    print("✅ shiboken6 imported successfully")
except ImportError as e:
    print("❌ shiboken6 import failed:", e)

try:
    from PySide6 import QtCore
    print("✅ PySide6.QtCore imported successfully")
    print("Qt Version:", QtCore.__version__)
except ImportError as e:
    print("❌ PySide6.QtCore import failed:", e)
```

## 🔧 Development Workflow (GUI Issue Workaround)

### Tạm thời phát triển không cần GUI
1. **Focus on Business Logic**
   ```bash
   # Test database operations
   python -c "from src.database.manager import DatabaseManager; print('DB OK')"
   
   # Test license manager
   python -c "from src.core.license_manager import LicenseManager; print('License OK')"
   ```

2. **CLI Interface tạm thời**
   ```python
   # cli_test.py
   from src.database.manager import DatabaseManager
   from src.core.license_manager import LicenseManager
   
   def test_basic_operations():
       db = DatabaseManager()
       db.initialize_master_db()
       
       # Test authentication
       user = db.authenticate_user("admin", "admin123")
       print(f"User authenticated: {user}")
       
       # Test companies
       companies = db.get_user_companies(user['id'])
       print(f"User companies: {companies}")
   
   if __name__ == "__main__":
       test_basic_operations()
   ```

3. **Web Interface Alternative**
   ```bash
   # Nếu cần, có thể tạo web interface với Flask
   pip install flask
   ```

### Test Framework Setup
```bash
# Run tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_database.py -v

# Coverage report
pip install pytest-cov
python -m pytest --cov=src tests/
```

## 📱 Cross-Platform Notes

### Windows Specific
- Yêu cầu Visual C++ Redistributable 2015-2022
- PowerShell command separators: `;` thay vì `&&`
- Path separators: `\` thay vì `/`

### macOS Specific
```bash
# May need Xcode command line tools
xcode-select --install

# Use homebrew python
brew install python@3.11
```

### Linux Specific
```bash
# Ubuntu/Debian
sudo apt-get install python3-dev python3-pip
sudo apt-get install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools

# CentOS/RHEL
sudo yum install python3-devel python3-pip qt5-qtbase-devel
```

## 🚀 Deployment Notes

### PyInstaller Issues
```bash
# Specific to PySide6
pip install pyinstaller[encryption]

# Build command
pyinstaller --windowed --onefile src/main.py --name FinanTidy

# If DLL issues persist
pyinstaller --windowed --onefile --add-binary "venv/Lib/site-packages/PySide6/Qt6/bin/*.dll;." src/main.py
```

### Alternative Packaging
```bash
# cx_Freeze (Windows)
pip install cx_Freeze

# py2app (macOS)
pip install py2app

# briefcase (Cross-platform)
pip install briefcase
```

---

## 📞 Getting Help

### Debug Information to Collect
```python
# debug_info.py
import sys
import platform
import os
from pathlib import Path

print("=== SYSTEM INFO ===")
print(f"Platform: {platform.platform()}")
print(f"Python: {sys.version}")
print(f"Architecture: {platform.architecture()}")
print(f"Working Directory: {os.getcwd()}")

print("\n=== PYTHON ENVIRONMENT ===")
print(f"Executable: {sys.executable}")
print(f"Virtual Env: {os.environ.get('VIRTUAL_ENV', 'None')}")

print("\n=== INSTALLED PACKAGES ===")
try:
    import pkg_resources
    packages = [f"{d.project_name}=={d.version}" for d in pkg_resources.working_set]
    for pkg in sorted(packages)[:10]:  # First 10 packages
        print(pkg)
    print(f"... and {len(packages)-10} more packages")
except:
    print("Could not list packages")

print("\n=== QT ENVIRONMENT ===")
try:
    import PySide6
    print(f"PySide6 location: {PySide6.__file__}")
    print(f"PySide6 version: {PySide6.__version__}")
except ImportError as e:
    print(f"PySide6 import error: {e}")

print("\n=== PATH ANALYSIS ===")
paths = os.environ.get('PATH', '').split(os.pathsep)
python_paths = [p for p in paths if 'python' in p.lower()]
for path in python_paths[:5]:  # First 5 Python-related paths
    print(f"  {path}")
```

### 🆘 Nếu vẫn gặp vấn đề
1. Chạy `debug_info.py` và save output
2. Try different Python versions (3.9, 3.10, 3.11)
3. Test trên máy khác nếu có thể
4. Sử dụng Docker container như backup plan
