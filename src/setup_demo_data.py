#!/usr/bin/env python3
"""
Setup demo data cho FinanTidy
"""

import sys
import os
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent
sys.path.insert(0, str(src_path))

from database.manager import DatabaseManager
from core.license_manager import LicenseManager

def setup_demo_data():
    """Setup demo data for FinanTidy"""
    print("🔧 Setting up FinanTidy demo data...")
    
    try:
        # Initialize database
        print("📊 Initializing database...")
        db_manager = DatabaseManager()
        db_manager.initialize_master_db()
        print("✅ Master database initialized")
        
        # Initialize license manager
        print("🔑 Initializing license manager...")
        license_manager = LicenseManager(db_manager)
        print("✅ License manager initialized")
        
        # Create demo user
        print("👤 Creating demo user...")
        with db_manager.get_master_session() as session:
            from database.models import User, Company, License, UserCompanyAccess
            
            # Check if demo user exists
            existing_user = session.query(User).filter_by(username='demo').first()
            if not existing_user:
                demo_user = User(
                    username='demo',
                    full_name='Demo User',
                    email='demo@sodalite.vn',
                    password_hash='demo_hash'  # In real app, this would be properly hashed
                )
                session.add(demo_user)
                session.flush()
                print(f"✅ Demo user created with ID: {demo_user.id}")
            else:
                demo_user = existing_user
                print(f"✅ Demo user already exists with ID: {demo_user.id}")
            
            # Create demo company
            existing_company = session.query(Company).filter_by(tax_code='0123456789').first()
            if not existing_company:
                demo_company = Company(
                    tax_code='0123456789',
                    company_name='Công ty Demo TNHH',
                    legal_name='Công ty Trách nhiệm hữu hạn Demo',
                    address='123 Đường Demo, Quận 1, TP.HCM',
                    phone='0901234567',
                    email='info@demo.com'
                )
                session.add(demo_company)
                session.flush()
                print(f"✅ Demo company created: {demo_company.company_name}")
            else:
                demo_company = existing_company
                print(f"✅ Demo company already exists: {demo_company.company_name}")
            
            # Create demo license
            existing_license = session.query(License).filter_by(user_id=demo_user.id).first()
            if not existing_license:
                demo_license = License(
                    user_id=demo_user.id,
                    license_type='free',
                    is_active=True
                )
                session.add(demo_license)
                session.flush()
                print(f"✅ Demo license created: {demo_license.license_type}")
            else:
                print(f"✅ Demo license already exists: {existing_license.license_type}")
            
            # Create user-company access
            existing_access = session.query(UserCompanyAccess).filter_by(
                user_id=demo_user.id, 
                company_id=demo_company.id
            ).first()
            if not existing_access:
                user_access = UserCompanyAccess(
                    user_id=demo_user.id,
                    company_id=demo_company.id,
                    role='admin'
                )
                session.add(user_access)
                print("✅ User-company access created")
            else:
                print("✅ User-company access already exists")
            
            session.commit()
        
        # Initialize company database
        print("🏢 Initializing company database...")
        db_manager.initialize_company_db('0123456789')
        print("✅ Company database initialized")
        
        print("\n🎉 Demo data setup complete!")
        print("📋 Demo credentials:")
        print("   Username: demo")
        print("   Password: demo")
        print("   Company: Công ty Demo TNHH")
        print("   Tax Code: 0123456789")
        print("   License: Free tier")
        
        return True
        
    except Exception as e:
        print(f"❌ Error setting up demo data: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    setup_demo_data()
