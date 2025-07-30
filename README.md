# 🎯 FinanTidy Professional v2.0 - Database Edition
**Complete Financial Management System with Database Integration**

A comprehensive business financial management application built with Python, SQLAlchemy, and CustomTkinter, featuring real database persistence, multi-user authentication, and a modern professional interface.

## ✨ Features

### �️ **Database Integration**
- SQLAlchemy ORM with SQLite backend
- Multi-user authentication system
- Company-based data isolation
- Real-time data persistence
- Secure password hashing

### 🔐 **Authentication System**
- Real database-backed user authentication
- Company access control
- Session management
- Password security with cryptography

### 🏠 **Dashboard**
- Live financial statistics from database
- Real-time data updates
- Professional navigation system
- Modern card-based layout with actual data

### 📄 **Invoice Management**
- Complete CRUD operations
- Invoice list and detail views
- Search and filtering capabilities
- Export functionality (PDF, Excel, CSV)
- Sample data for testing

### 📋 **Viettel eInvoice Integration** 🆕
- Electronic invoice generation compliant with Vietnamese regulations
- Direct integration with Viettel SInvoice API
- Automatic invoice format conversion (FinanTidy → Viettel)
- PDF download and storage of issued e-invoices
- Real-time invoice status tracking
- Secure credential management
- Test and production environment support

### 🏪 **Provider Management**
- Comprehensive provider database
- Rating and review system
- Service categorization
- Contact management
- Advanced filtering options

### 📊 **Analytics Dashboard**
- Interactive financial charts
- Revenue trend analysis
- Provider breakdown visualization
- Business insights and recommendations
- Performance metrics tracking

### 💳 **Transaction Management**
- Complete transaction tracking
- Income, expense, and transfer categorization
- Advanced filtering and search
- Status monitoring
- Bulk operations support

### ⚙️ **Settings & Configuration**
- Company information management
- Display and theme preferences
- Notification settings
- Backup and security options
- Invoice configuration

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- CustomTkinter library

### Installation

1. **Clone or download the project**
2. **Install dependencies:**
   ```bash
   pip install customtkinter
   ```

3. **Run the application:**
   ```bash
   python run_finantidy.py
   ```

### Default Login Credentials
- **Username:** `admin`
- **Password:** `admin`

## 📁 Project Structure

```
Sodalite/
├── src/
│   ├── integrations/                    # External API integrations
│   │   ├── __init__.py
│   │   └── viettel_einvoice.py         # Viettel eInvoice API service
│   └── ui/
│       └── modern/
│           ├── login_window.py          # Authentication interface
│           ├── main_window.py           # Main dashboard
│           ├── invoices_window.py       # Invoice management
│           ├── providers_window.py      # Provider management
│           ├── analytics_window.py      # Analytics dashboard
│           ├── transactions_window.py   # Transaction management
│           ├── settings_window.py       # Application settings
│           └── viettel_config_window.py # Viettel eInvoice configuration
└── run_finantidy.py                     # Main application launcher
```

## 🎨 Design Features

### Modern Interface
- **Dark Theme:** Professional dark color scheme
- **Card-based Layout:** Clean, organized content presentation
- **Responsive Design:** Adapts to different screen sizes
- **Consistent Typography:** Professional font styling throughout

### Professional Styling
- **Color-coded Elements:** Visual categorization for better UX
- **Interactive Components:** Hover effects and smooth transitions
- **Modern Icons:** Emoji-based iconography for clarity
- **Intuitive Navigation:** Easy-to-use sidebar and navigation

## 🔧 Module Details

### 📄 Invoice Management
- **List View:** Paginated invoice listing with search
- **Detail View:** Comprehensive invoice information
- **Status Tracking:** Draft, Sent, Paid, Overdue statuses
- **Export Options:** PDF generation, Excel export
- **Sample Data:** Pre-loaded test invoices

### 🏪 Provider Management
- **Provider Database:** Complete supplier information
- **Rating System:** 5-star rating with reviews
- **Service Categories:** Organized service classification
- **Contact Integration:** Phone, email, website links
- **Filter Options:** Type, rating, status filtering

### 📊 Analytics Dashboard
- **Revenue Charts:** Monthly revenue trend visualization
- **Provider Breakdown:** Expense distribution by provider
- **Status Analysis:** Invoice status overview
- **Business Insights:** Automated recommendations
- **Export Reports:** Analytics data export

### 💳 Transaction Management
- **Transaction Types:** Income, Expense, Transfer
- **Advanced Filtering:** Date, type, status, amount ranges
- **Search Functionality:** Multi-field search capabilities
- **Status Management:** Completed, Pending, Failed tracking
- **Account Integration:** Multi-account support

### ⚙️ Settings System
- **Company Settings:** Business information management
- **Display Options:** Theme, language, currency settings
- **Notifications:** Email alerts and reminder configuration
- **Backup Management:** Automatic backup scheduling
- **Security Settings:** Password and encryption options

## 📋 Viettel eInvoice Configuration

### Prerequisites for Viettel Integration
1. **Viettel SInvoice Account:** Register with Viettel for electronic invoice services
2. **API Credentials:** Obtain API endpoint, username, and password from Viettel
3. **Company Information:** Valid Vietnamese business tax code and company details
4. **Template Setup:** Configure invoice templates in Viettel SInvoice portal

### Configuration Steps

#### 1. Access Viettel Configuration
- **Via Main Dashboard:** Click "📋 Viettel eInvoice" in Quick Actions
- **Via Settings:** Go to Settings > Viettel eInvoice category

#### 2. Basic Configuration
```
API Endpoint: https://sinvoice.viettel.vn (production)
             https://sinvoice-demo.viettel.vn (test)
Username: [Your Viettel username - typically tax_code-user_id]
Password: [Your Viettel API password]
```

#### 3. Company Information
```
Company Name: [Your registered company name]
Tax Code: [Vietnamese business tax code]
Address: [Registered business address]
Phone: [Company phone number]
Email: [Company email for invoices]
```

#### 4. Invoice Template Settings
```
Template Code: [e.g., "01GTKT0/001" - from Viettel portal]
Invoice Series: [e.g., "C22T" - from Viettel portal]
Authentication Method: Token (recommended) or Basic Auth
```

### Testing Configuration
1. **Test Connection:** Use the "Test Connection" button in configuration window
2. **Test Invoice:** Create a test invoice to verify integration
3. **Download PDF:** Verify PDF generation and download functionality

### Usage Workflow
1. **Create Invoice:** Use standard FinanTidy invoice creation
2. **Configure eInvoice:** Click "📋 Configure eInvoice" button in invoice details
3. **Generate eInvoice:** Click "📤 Create eInvoice" to send to Viettel
4. **Download PDF:** Use "📄 Download PDF" for the issued electronic invoice

### Important Notes
- **Test Environment:** Always test with Viettel demo environment first
- **Credentials Security:** Configuration is stored locally and encrypted
- **API Limits:** Respect Viettel API rate limits and usage policies
- **Compliance:** Ensure all invoice data meets Vietnamese electronic invoice regulations

## 🎯 Key Benefits

### For Businesses
- **Complete Financial Overview:** All financial data in one place
- **Professional Reporting:** Generate professional invoices and reports
- **Provider Management:** Maintain comprehensive supplier database
- **Analytics Insights:** Data-driven business decisions

### For Developers
- **Modern Framework:** Built with CustomTkinter for professional UI
- **Modular Architecture:** Easy to extend and maintain
- **Clean Code:** Well-organized, documented codebase
- **Scalable Design:** Ready for additional features

## 🔮 Future Enhancements

### Planned Features
- **Database Integration:** PostgreSQL/MySQL backend
- **Multi-user Support:** Role-based access control
- **API Integration:** Banking and payment gateway APIs
- **Mobile App:** React Native companion app
- **Advanced Reporting:** Custom report builder
- **Cloud Sync:** Multi-device synchronization

### Technical Improvements
- **Data Persistence:** File-based or database storage
- **PDF Generation:** Advanced invoice PDF creation
- **Email Integration:** Automated invoice sending
- **Backup System:** Automated cloud backups
- **Import/Export:** Excel, CSV, JSON data exchange

## 🛠️ Development

### Code Organization
- **Separation of Concerns:** UI, business logic, data layers
- **Reusable Components:** Modular UI components
- **Error Handling:** Comprehensive error management
- **Documentation:** Inline code documentation

### Testing
- Each module can be run independently for testing
- Sample data provided for all modules
- Error handling with user-friendly messages

## 📞 Support

For questions, issues, or feature requests:
- Review the code documentation
- Test individual modules using their main() functions
- Check error messages for troubleshooting guidance

## 📄 License

This project is developed for educational and business use. Modify and extend as needed for your specific requirements.

---

**FinanTidy Professional v2.0** - *Your Complete Financial Management Solution* 🎯
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
