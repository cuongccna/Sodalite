"""
Development Setup Script
Initializes development environment and creates sample data
"""

import os
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from database.manager import DatabaseManager
from database.models import User, Company, UserCompanyAccess, License


def setup_development_environment():
    """Setup development environment with sample data"""
    print("🚀 Setting up FinanTidy development environment...")
    
    # Initialize database manager
    data_dir = Path.home() / "FinanTidy" / "dev_data"
    db_manager = DatabaseManager(str(data_dir))
    
    try:
        # Initialize master database
        print("📊 Initializing master database...")
        db_manager.initialize_master_db()
        
        # Create sample companies
        print("🏢 Creating sample companies...")
        create_sample_companies(db_manager)
        
        print("✅ Development environment setup complete!")
        print(f"📁 Data directory: {data_dir}")
        print("👤 Default login: admin / admin123")
        print("🎯 Ready to run: python src/main.py")
        
    except Exception as e:
        print(f"❌ Error setting up environment: {e}")
        return False
    
    finally:
        db_manager.close_all_connections()
    
    return True


def create_sample_companies(db_manager):
    """Create sample companies for testing"""
    
    sample_companies = [
        {
            "tax_code": "0123456789",
            "company_name": "Công ty TNHH Công nghệ ABC",
            "legal_name": "Công ty Trách nhiệm Hữu hạn Công nghệ ABC",
            "address": "123 Nguyễn Văn Cừ, Quận 1, TP.HCM",
            "phone": "028-3456-7890",
            "email": "info@abc-tech.vn",
            "business_type": "Công nghệ thông tin"
        },
        {
            "tax_code": "9876543210",
            "company_name": "Cửa hàng Tạp hóa XYZ",
            "legal_name": "Hộ kinh doanh Tạp hóa XYZ",
            "address": "456 Lê Văn Việt, Quận 9, TP.HCM",
            "phone": "0909-123-456",
            "email": "xyz.grocery@gmail.com",
            "business_type": "Bán lẻ"
        }
    ]
    
    with db_manager.get_master_session() as session:
        # Get admin user
        admin_user = session.query(User).filter(User.username == "admin").first()
        
        if not admin_user:
            print("❌ Admin user not found!")
            return
        
        for company_data in sample_companies:
            # Check if company already exists
            existing_company = session.query(Company).filter(
                Company.tax_code == company_data["tax_code"]
            ).first()
            
            if existing_company:
                print(f"⚠️  Company {company_data['tax_code']} already exists, skipping...")
                continue
            
            # Create company
            company = Company(**company_data)
            session.add(company)
            session.flush()
            
            # Give admin access to company
            access = UserCompanyAccess(
                user_id=admin_user.id,
                company_id=company.id,
                role="owner"
            )
            session.add(access)
            
            print(f"✅ Created company: {company.company_name}")
        
        session.commit()
        
        # Update admin license to allow multiple companies
        admin_license = session.query(License).filter(
            License.user_id == admin_user.id
        ).first()
        
        if admin_license:
            admin_license.license_type = "agency"
            admin_license.max_companies = -1  # Unlimited
            admin_license.max_invoices_per_month = -1  # Unlimited
            session.commit()
            print("🎯 Updated admin license to Agency (unlimited)")


if __name__ == "__main__":
    setup_development_environment()
