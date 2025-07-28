"""
Debug database contents
"""

import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from database.manager import DatabaseManager
from database.models import User, Company, UserCompanyAccess, License

def debug_database():
    data_dir = Path.home() / "FinanTidy" / "dev_data"
    db_manager = DatabaseManager(str(data_dir))
    db_manager.initialize_master_db()
    
    with db_manager.get_master_session() as session:
        print("=== USERS ===")
        users = session.query(User).all()
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Name: {user.full_name}")
        
        print("\n=== COMPANIES ===")
        companies = session.query(Company).all()
        for company in companies:
            print(f"ID: {company.id}, Tax Code: {company.tax_code}, Name: {company.company_name}")
        
        print("\n=== USER COMPANY ACCESS ===")
        accesses = session.query(UserCompanyAccess).all()
        for access in accesses:
            print(f"User ID: {access.user_id}, Company ID: {access.company_id}, Role: {access.role}")
        
        print("\n=== LICENSES ===")
        licenses = session.query(License).all()
        for license in licenses:
            print(f"User ID: {license.user_id}, Type: {license.license_type}, Max Companies: {license.max_companies}")

if __name__ == "__main__":
    debug_database()
