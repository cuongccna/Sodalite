# FinanTidy - Project Sodalite

## Tổng quan
**FinanTidy** là một ứng dụng desktop quản lý hóa đơn và tài chính được thiết kế đặc biệt cho các doanh nghiệp siêu nhỏ, startups và văn phòng dịch vụ kế toán tại Việt Nam.

## Sứ mệnh
Trao quyền cho các doanh nghiệp siêu nhỏ, startups và văn phòng dịch vụ kế toán tại Việt Nam khả năng quản lý hóa đơn và tài chính một cách thông minh, bảo mật và trực quan ngay trên máy tính cá nhân.

## Điểm khác biệt cốt lõi (USPs)
1. **Desktop First**: Dữ liệu được lưu và xử lý hoàn toàn trên máy tính người dùng
2. **Trợ lý AI Đơn giản**: Cung cấp cảnh báo, dự báo và gợi ý thông minh
3. **Mô hình Giá trị Linh hoạt**: Bản miễn phí hữu ích + các gói trả phí có giá trị rõ ràng

## Khách hàng mục tiêu
- **Chủ doanh nghiệp siêu nhỏ**: Cần công cụ đơn giản, chi phí thấp, bảo mật
- **Kế toán dịch vụ**: Cần công cụ hiệu quả xử lý nhiều khách hàng

## Công nghệ
- **Language**: Python 3.11+
- **GUI Framework**: PySide6 (Qt for Python)
- **Database**: SQLite với SQLAlchemy ORM
- **Packaging**: PyInstaller

## Cấu trúc Database
### master.sqlite
- Users, Companies, UserCompanyAccess, Licenses

### [TaxCode].sqlite (template cho mỗi công ty)
- Invoices, Providers, InvoiceItems, CompanyInfo

## Lịch phát triển (8 tuần)
- **Tuần 1**: Thiết lập nền móng & kiến trúc database
- **Tuần 2-3**: Xây dựng lõi logic & giao diện cơ bản
- **Tuần 4-5**: Phát triển tính năng chính (Dashboard, xử lý dữ liệu)
- **Tuần 6-8**: Hoàn thiện, báo cáo, đóng gói & phát hành

## Cài đặt
```bash
# Tạo virtual environment
python -m venv venv
venv\Scripts\activate

# Cài đặt dependencies
pip install -r requirements.txt
```

## Chạy ứng dụng
```bash
python src/main.py
```
