#!/bin/bash

echo "🚀 Starting FinanTidy Development Environment..."
echo ""

cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run setup_dev.py first"
    read -p "Press enter to continue..."
    exit 1
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Check if core functionality works
echo "🧪 Running core functionality tests..."
python test_core.py
if [ $? -ne 0 ]; then
    echo ""
    echo "⚠️  Core tests failed. Please check the issues above."
    echo ""
    read -p "Press enter to continue..."
    exit 1
fi

echo ""
echo "✅ Core functionality verified!"
echo ""

# Try to run the main application
echo "🎨 Launching FinanTidy GUI..."
echo ""
echo "💡 If GUI fails to start due to PySide6 issues:"
echo "   - Check docs/TROUBLESHOOTING.md for solutions"
echo "   - The core business logic is working properly"
echo "   - You can continue with backend development"
echo ""

python src/main.py

echo ""
echo "👋 FinanTidy session ended."
