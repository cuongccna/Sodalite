"""
Tests for Enhanced License Manager Features
"""

import pytest
import tempfile
import os
from datetime import datetime, date

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from core.license_manager import LicenseManager
from database.manager import DatabaseManager


class TestEnhancedLicenseFeatures:
    """Test enhanced license manager features"""
    
    def setup_method(self):
        """Set up test environment"""
        # Create temporary database
        self.db_file = tempfile.NamedTemporaryFile(delete=False, suffix='.sqlite')
        self.db_file.close()
        
        # Create database manager with just the file path
        self.db_manager = DatabaseManager()
        # Set the master db path manually
        self.db_manager.master_db_path = self.db_file.name
        self.db_manager.data_dir = os.path.dirname(self.db_file.name)
        self.db_manager.init_database()
        
        # Create license manager
        self.license_manager = LicenseManager(self.db_manager)
        
        # Create test user and company
        self.test_user = self.db_manager.create_user(
            username="testuser",
            email="test@example.com",
            password="password123",
            full_name="Test User"
        )
        
        self.test_company = self.db_manager.create_company(
            tax_code="0123456789",
            company_name="Test Company",
            creator_user_id=self.test_user['id']
        )
        
        # Load user license
        self.license_manager.load_user_license(self.test_user['id'])
    
    def teardown_method(self):
        """Clean up test environment"""
        try:
            os.unlink(self.db_file.name)
        except:
            pass
    
    def test_get_feature_usage_stats_free(self):
        """Test getting usage stats for free license"""
        stats = self.license_manager.get_feature_usage_stats()
        
        assert stats['license_type'] == 'free'
        assert stats['companies']['current'] == 1
        assert stats['companies']['max'] == 1
        assert stats['companies']['usage_percent'] == 100
        assert 'manual' in stats['available_integrations']
        assert 'csv' in stats['export_formats']
        assert stats['premium_features']['ai_suggestions'] == False
    
    def test_check_upgrade_recommendations_free(self):
        """Test upgrade recommendations for free license"""
        recommendations = self.license_manager.check_upgrade_recommendations()
        
        # Should have company limit warning (100% usage)
        company_recs = [r for r in recommendations if r['type'] == 'company_limit']
        assert len(company_recs) > 0
        assert company_recs[0]['suggested_plan'] == 'pro'
        assert company_recs[0]['priority'] == 'high'
        
        # Should have feature upgrade suggestion
        feature_recs = [r for r in recommendations if r['type'] == 'feature_upgrade']
        assert len(feature_recs) > 0
        assert feature_recs[0]['suggested_plan'] == 'pro'
    
    def test_get_plan_comparison(self):
        """Test plan comparison data"""
        comparison = self.license_manager.get_plan_comparison()
        
        assert 'plans' in comparison
        assert 'free' in comparison['plans']
        assert 'pro' in comparison['plans']
        assert 'agency' in comparison['plans']
        
        # Check free plan
        free_plan = comparison['plans']['free']
        assert free_plan['price'] == 0
        assert free_plan['features']['max_companies'] == 1
        assert 'manual' in free_plan['features']['api_integrations']
        
        # Check pro plan
        pro_plan = comparison['plans']['pro']
        assert pro_plan['price'] == 299000
        assert pro_plan['features']['max_companies'] == 3
        assert 'viettel' in pro_plan['features']['api_integrations']
        assert pro_plan['features']['ai_suggestions'] == True
        
        # Check agency plan
        agency_plan = comparison['plans']['agency']
        assert agency_plan['price'] == 999000
        assert agency_plan['features']['max_companies'] == -1  # Unlimited
        assert agency_plan['features']['white_label'] == True
        
        assert comparison['current_plan'] == 'free'
    
    def test_can_use_provider_free(self):
        """Test provider access for free license"""
        assert self.license_manager.can_use_provider('manual') == True
        assert self.license_manager.can_use_provider('viettel') == False
        assert self.license_manager.can_use_provider('mobifone') == False
    
    def test_can_export_format_free(self):
        """Test export format access for free license"""
        assert self.license_manager.can_export_format('csv') == True
        assert self.license_manager.can_export_format('excel') == False
        assert self.license_manager.can_export_format('pdf') == False
    
    def test_upgrade_to_pro(self):
        """Test license upgrade to pro"""
        # Simulate upgrade to pro
        with self.db_manager.get_session() as session:
            from database.models import License
            
            license_record = session.query(License).filter_by(
                user_id=self.test_user['id']
            ).first()
            
            license_record.license_type = 'pro'
            session.commit()
        
        # Reload license
        self.license_manager.load_user_license(self.test_user['id'])
        
        # Test pro features
        assert self.license_manager.get_license_type() == 'pro'
        assert self.license_manager.can_use_provider('viettel') == True
        assert self.license_manager.can_export_format('excel') == True
        assert self.license_manager.is_feature_enabled('ai_suggestions') == True
        
        # Test pro limits
        stats = self.license_manager.get_feature_usage_stats()
        assert stats['companies']['max'] == 3
        assert stats['invoices_this_month']['max'] == 1000
    
    def test_upgrade_to_agency(self):
        """Test license upgrade to agency"""
        # Simulate upgrade to agency
        with self.db_manager.get_session() as session:
            from database.models import License
            
            license_record = session.query(License).filter_by(
                user_id=self.test_user['id']
            ).first()
            
            license_record.license_type = 'agency'
            session.commit()
        
        # Reload license
        self.license_manager.load_user_license(self.test_user['id'])
        
        # Test agency features
        assert self.license_manager.get_license_type() == 'agency'
        assert self.license_manager.can_use_provider('fpt') == True
        assert self.license_manager.can_export_format('xml') == True
        assert self.license_manager.is_feature_enabled('white_label') == True
        assert self.license_manager.is_feature_enabled('bulk_operations') == True
        
        # Test unlimited limits
        stats = self.license_manager.get_feature_usage_stats()
        assert stats['companies']['max'] == -1
        assert stats['invoices_this_month']['max'] == -1
    
    def test_multiple_companies_usage(self):
        """Test usage stats with multiple companies"""
        # Add another company for pro simulation
        company2 = self.db_manager.create_company(
            tax_code="9876543210",
            company_name="Test Company 2",
            creator_user_id=self.test_user['id']
        )
        
        stats = self.license_manager.get_feature_usage_stats()
        assert stats['companies']['current'] == 2
        assert stats['companies']['usage_percent'] == 200  # Over limit for free
        
        # Check recommendations
        recommendations = self.license_manager.check_upgrade_recommendations()
        company_recs = [r for r in recommendations if r['type'] == 'company_limit']
        assert len(company_recs) > 0
        assert company_recs[0]['priority'] == 'high'
    
    def test_license_feature_gating_integration(self):
        """Test integration with existing feature gating"""
        # Test free license restrictions
        result = self.license_manager.check_feature_access('use_api', api_type='viettel')
        assert result['allowed'] == False
        assert 'viettel' in result['message']
        
        result = self.license_manager.check_feature_access('export', format='excel')
        assert result['allowed'] == False
        assert 'excel' in result['message']
        
        result = self.license_manager.check_feature_access('ai_suggestion')
        assert result['allowed'] == False
        assert 'Pro' in result['message']


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
