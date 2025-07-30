#!/usr/bin/env python3
"""
Demo Script để kiểm tra Dashboard với dữ liệu mẫu
"""

import sys
import os
import time
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from PySide6.QtWidgets import QApplication, QMessageBox
from core.app import FinanTidyApp

def demo_dashboard():
    """Demo dashboard với dữ liệu mẫu"""
    print("🚀 Khởi động FinanTidy Demo...")
    
    app = QApplication(sys.argv)
    
    # Khởi tạo ứng dụng
    try:
        finan_tidy = FinanTidyApp()
        
        print("✅ Ứng dụng khởi động thành công!")
        print("\n📋 Các tính năng có sẵn:")
        print("   • Dashboard với 6 thống kê chính")
        print("   • Bảng hóa đơn gần đây (5 hóa đơn)")
        print("   • Tab Hóa đơn với 10 hóa đơn mẫu")
        print("   • Tab Providers với trạng thái kết nối")
        print("   • Tab Phân tích với thống kê license")
        print("   • Auto-refresh mỗi 5 phút")
        print("   • Giao diện tiếng Việt hoàn chỉnh")
        
        print("\n🎯 Hướng dẫn sử dụng:")
        print("   1. Login với tài khoản demo")
        print("   2. Xem Dashboard với dữ liệu mẫu")
        print("   3. Chuyển qua các tab khác nhau")
        print("   4. Click vào các nút để xem dialogs")
        print("   5. Kiểm tra menu và toolbar")
        
        print("\n💡 Dữ liệu mẫu bao gồm:")
        print("   • 27 hóa đơn tháng này")
        print("   • Tổng chi: 156.8M VNĐ")
        print("   • VAT: 15.7M VNĐ")
        print("   • 3 công ty quản lý")
        print("   • 2 providers kết nối")
        print("   • 12 báo cáo đã tạo")
        
        print(f"\n🎉 Dashboard hiện đã có dữ liệu mẫu đầy đủ!")
        
        # Chạy ứng dụng
        sys.exit(app.exec())
        
    except Exception as e:
        print(f"❌ Lỗi khởi động: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    demo_dashboard()
