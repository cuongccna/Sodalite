"""
License Manager
Handles license validation and feature access control
"""

from typing import Dict, Any, List, Optional
from datetime import datetime, date
from database.manager import DatabaseManager


class LicenseManager:
    """Manages license validation and feature restrictions"""
    
    # Feature definitions by license type
    LICENSE_FEATURES = {
        'free': {
            'max_companies': 1,
            'max_invoices_per_month': 100,
            'api_integrations': ['manual'],
            'export_formats': ['csv'],
            'ai_suggestions': False,
            'advanced_reports': False,
            'multi_user': False,
            'priority_support': False
        },
        'pro': {
            'max_companies': 3,
            'max_invoices_per_month': 1000,
            'api_integrations': ['manual', 'viettel', 'mobifone'],
            'export_formats': ['csv', 'excel', 'pdf'],
            'ai_suggestions': True,
            'advanced_reports': True,
            'multi_user': False,
            'priority_support': True
        },
        'agency': {
            'max_companies': -1,  # Unlimited
            'max_invoices_per_month': -1,  # Unlimited
            'api_integrations': ['manual', 'viettel', 'mobifone', 'fpt', 'vnpost'],
            'export_formats': ['csv', 'excel', 'pdf', 'xml'],
            'ai_suggestions': True,
            'advanced_reports': True,
            'multi_user': True,
            'priority_support': True,
            'white_label': True,
            'bulk_operations': True
        }
    }
    
    def __init__(self, db_manager: Optional[DatabaseManager] = None):
        self.db_manager = db_manager
        self._current_license = None
    
    def load_user_license(self, user_id: int) -> bool:
        """Load and cache user's current license"""
        if not self.db_manager:
            return False
        
        self._current_license = self.db_manager.get_user_license(user_id)
        return self._current_license is not None
    
    def get_license_type(self) -> str:
        """Get current license type"""
        if not self._current_license:
            return 'free'
        return self._current_license.get('license_type', 'free')
    
    def is_feature_enabled(self, feature: str) -> bool:
        """Check if a specific feature is enabled for current license"""
        license_type = self.get_license_type()
        features = self.LICENSE_FEATURES.get(license_type, self.LICENSE_FEATURES['free'])
        return features.get(feature, False)
    
    def get_max_companies(self) -> int:
        """Get maximum number of companies allowed"""
        license_type = self.get_license_type()
        return self.LICENSE_FEATURES[license_type]['max_companies']
    
    def get_max_invoices_per_month(self) -> int:
        """Get maximum number of invoices per month"""
        license_type = self.get_license_type()
        return self.LICENSE_FEATURES[license_type]['max_invoices_per_month']
    
    def can_add_company(self, current_company_count: int) -> bool:
        """Check if user can add another company"""
        max_companies = self.get_max_companies()
        if max_companies == -1:  # Unlimited
            return True
        return current_company_count < max_companies
    
    def can_add_invoices(self, current_month_count: int) -> bool:
        """Check if user can add more invoices this month"""
        max_invoices = self.get_max_invoices_per_month()
        if max_invoices == -1:  # Unlimited
            return True
        return current_month_count < max_invoices
    
    def get_available_api_integrations(self) -> List[str]:
        """Get list of available API integrations"""
        license_type = self.get_license_type()
        return self.LICENSE_FEATURES[license_type]['api_integrations']
    
    def get_available_export_formats(self) -> List[str]:
        """Get list of available export formats"""
        license_type = self.get_license_type()
        return self.LICENSE_FEATURES[license_type]['export_formats']
    
    def is_license_valid(self) -> bool:
        """Check if current license is valid (not expired)"""
        if not self._current_license:
            return True  # Free license never expires
        
        expires_at = self._current_license.get('expires_at')
        if expires_at is None:
            return True  # No expiration date
        
        if isinstance(expires_at, str):
            expires_at = datetime.fromisoformat(expires_at)
        
        return datetime.now() < expires_at
    
    def get_license_status(self) -> Dict[str, Any]:
        """Get comprehensive license status"""
        license_type = self.get_license_type()
        features = self.LICENSE_FEATURES[license_type]
        
        status = {
            'license_type': license_type,
            'is_valid': self.is_license_valid(),
            'features': features.copy(),
            'limits': {
                'max_companies': self.get_max_companies(),
                'max_invoices_per_month': self.get_max_invoices_per_month(),
                'api_integrations': self.get_available_api_integrations(),
                'export_formats': self.get_available_export_formats()
            }
        }
        
        if self._current_license and self._current_license.get('expires_at'):
            status['expires_at'] = self._current_license['expires_at']
        
        return status
    
    def get_upgrade_suggestions(self) -> List[Dict[str, Any]]:
        """Get suggestions for license upgrades"""
        current_type = self.get_license_type()
        suggestions = []
        
        if current_type == 'free':
            suggestions.append({
                'target_license': 'pro',
                'benefits': [
                    'Tăng giới hạn lên 1,000 hóa đơn/tháng',
                    'Tích hợp API với Viettel, MobiFone',
                    'Xuất Excel và PDF',
                    'Gợi ý phân loại thông minh bằng AI',
                    'Báo cáo nâng cao',
                    'Hỗ trợ ưu tiên'
                ]
            })
            
            suggestions.append({
                'target_license': 'agency',
                'benefits': [
                    'Không giới hạn công ty và hóa đơn',
                    'Tất cả tích hợp API có sẵn',
                    'Quản lý nhiều người dùng',
                    'Tính năng xử lý hàng loạt',
                    'White-label cho đại lý',
                    'Hỗ trợ VIP'
                ]
            })
        
        elif current_type == 'pro':
            suggestions.append({
                'target_license': 'agency',
                'benefits': [
                    'Không giới hạn công ty và hóa đơn',
                    'Thêm API FPT, VNPOST',
                    'Quản lý nhiều người dùng',
                    'Tính năng dành cho đại lý',
                    'White-label tùy chỉnh'
                ]
            })
        
        return suggestions
    
    def validate_action(self, action: str, **kwargs) -> Dict[str, Any]:
        """Validate if an action is allowed under current license"""
        result = {'allowed': True, 'message': ''}
        
        if action == 'add_company':
            current_count = kwargs.get('current_count', 0)
            if not self.can_add_company(current_count):
                result['allowed'] = False
                result['message'] = f'Giới hạn {self.get_max_companies()} công ty. Nâng cấp gói để thêm công ty.'
        
        elif action == 'add_invoice':
            current_count = kwargs.get('current_month_count', 0)
            if not self.can_add_invoices(current_count):
                result['allowed'] = False
                result['message'] = f'Đã đạt giới hạn {self.get_max_invoices_per_month()} hóa đơn/tháng.'
        
        elif action == 'use_api':
            api_type = kwargs.get('api_type', 'manual')
            if api_type not in self.get_available_api_integrations():
                result['allowed'] = False
                result['message'] = f'API {api_type} không khả dụng với gói {self.get_license_type()}.'
        
        elif action == 'export':
            export_format = kwargs.get('format', 'csv')
            if export_format not in self.get_available_export_formats():
                result['allowed'] = False
                result['message'] = f'Định dạng {export_format} không khả dụng với gói {self.get_license_type()}.'
        
        elif action == 'ai_suggestion':
            if not self.is_feature_enabled('ai_suggestions'):
                result['allowed'] = False
                result['message'] = 'Gợi ý AI chỉ khả dụng với gói Pro và Agency.'
        
        return result
