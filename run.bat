@echo off
echo 🚀 Starting FinanTidy Development Environment...
echo.

cd /d "%~dp0"

REM Check if virtual environment exists
if not exist "venv\" (
    echo ❌ Virtual environment not found!
    echo Please run setup_dev.py first
    pause
    exit /b 1
)

REM Activate virtual environment
echo 📦 Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if core functionality works
echo 🧪 Running core functionality tests...
python test_core.py
if %ERRORLEVEL% neq 0 (
    echo.
    echo ⚠️  Core tests failed. Please check the issues above.
    echo.
    pause
    exit /b 1
)

echo.
echo ✅ Core functionality verified!
echo.

REM Try to run the main application
echo 🎨 Launching FinanTidy GUI...
echo.
echo 💡 If GUI fails to start due to PySide6 issues:
echo    - Check docs\TROUBLESHOOTING.md for solutions
echo    - The core business logic is working properly
echo    - You can continue with backend development
echo.

python src\main.py

echo.
echo 👋 FinanTidy session ended.
pause
