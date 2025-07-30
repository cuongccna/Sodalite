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
    
    def get_feature_usage_stats(self) -> Dict[str, Any]:
        """
        Get usage statistics for current license
        
        Returns:
            Dict[str, Any]: Usage statistics
        """
        if not self._current_license:
            return {}
        
        license_type = self._current_license.get('license_type', 'free')
        features = self.LICENSE_FEATURES.get(license_type, {})
        
        try:
            # Count current companies
            with self.db_manager.get_session() as session:
                from database.models import Company, UserCompanyAccess
                
                company_count = session.query(Company).join(
                    UserCompanyAccess,
                    Company.id == UserCompanyAccess.company_id
                ).filter(
                    UserCompanyAccess.user_id == self.current_license['user_id']
                ).count()
            
            # Calculate usage percentages
            max_companies = features.get('max_companies', 1)
            company_usage = (company_count / max_companies * 100) if max_companies > 0 else 0
            
            return {
                'license_type': license_type,
                'companies': {
                    'current': company_count,
                    'max': max_companies,
                    'usage_percent': min(company_usage, 100)
                },
                'invoices_this_month': {
                    'current': 0,  # TODO: Calculate from invoice data
                    'max': features.get('max_invoices_per_month', 100),
                    'usage_percent': 0
                },
                'available_integrations': features.get('api_integrations', []),
                'export_formats': features.get('export_formats', []),
                'premium_features': {
                    'ai_suggestions': features.get('ai_suggestions', False),
                    'advanced_reports': features.get('advanced_reports', False),
                    'multi_user': features.get('multi_user', False),
                    'priority_support': features.get('priority_support', False)
                }
            }
            
        except Exception as e:
            print(f"Error getting usage stats: {e}")
            return {
                'license_type': license_type,
                'error': str(e)
            }
    
    def check_upgrade_recommendations(self) -> List[Dict[str, Any]]:
        """
        Check if user should upgrade license based on usage
        
        Returns:
            List[Dict[str, Any]]: Upgrade recommendations
        """
        stats = self.get_feature_usage_stats()
        recommendations = []
        
        if not stats or 'error' in stats:
            return recommendations
        
        license_type = stats['license_type']
        
        # Check company limit
        if stats['companies']['usage_percent'] > 80:
            if license_type == 'free':
                recommendations.append({
                    'type': 'company_limit',
                    'message': 'Bạn đang sử dụng gần hết giới hạn công ty. Nâng cấp Pro để quản lý 3 công ty.',
                    'suggested_plan': 'pro',
                    'priority': 'high'
                })
            elif license_type == 'pro':
                recommendations.append({
                    'type': 'company_limit',
                    'message': 'Bạn đang sử dụng gần hết giới hạn công ty. Nâng cấp Agency để không giới hạn.',
                    'suggested_plan': 'agency',
                    'priority': 'medium'
                })
        
        # Check invoice limit
        if stats['invoices_this_month']['usage_percent'] > 80:
            if license_type == 'free':
                recommendations.append({
                    'type': 'invoice_limit',
                    'message': 'Bạn đang sử dụng gần hết giới hạn hóa đơn tháng này. Nâng cấp Pro để xử lý 1000 hóa đơn/tháng.',
                    'suggested_plan': 'pro',
                    'priority': 'high'
                })
        
        # Suggest features
        if license_type == 'free':
            recommendations.append({
                'type': 'feature_upgrade',
                'message': 'Nâng cấp Pro để sử dụng AI gợi ý, báo cáo nâng cao và tích hợp Viettel API.',
                'suggested_plan': 'pro',
                'priority': 'low'
            })
        
        return recommendations
    
    def get_plan_comparison(self) -> Dict[str, Any]:
        """
        Get plan comparison for upgrade UI
        
        Returns:
            Dict[str, Any]: Plan comparison data
        """
        return {
            'plans': {
                'free': {
                    'name': 'Miễn phí',
                    'price': 0,
                    'currency': 'VND',
                    'period': 'month',
                    'features': self.LICENSE_FEATURES['free'],
                    'highlight': False
                },
                'pro': {
                    'name': 'Chuyên nghiệp',
                    'price': 299000,
                    'currency': 'VND',
                    'period': 'month',
                    'features': self.LICENSE_FEATURES['pro'],
                    'highlight': True,
                    'discount': '20% off first 3 months'
                },
                'agency': {
                    'name': 'Đại lý',
                    'price': 999000,
                    'currency': 'VND',
                    'period': 'month',
                    'features': self.LICENSE_FEATURES['agency'],
                    'highlight': False,
                    'contact_sales': True
                }
            },
            'current_plan': self.get_license_type(),
            'recommendations': self.check_upgrade_recommendations()
        }
    
    def can_use_provider(self, provider_type: str) -> bool:
        """
        Check if current license can use specific provider
        
        Args:
            provider_type: Provider type (e.g., 'viettel', 'mobifone')
            
        Returns:
            bool: True if allowed
        """
        if not self.current_license:
            return False
        
        license_type = self.current_license.get('license_type', 'free')
        allowed_integrations = self.LICENSE_FEATURES.get(license_type, {}).get('api_integrations', [])
        
        return provider_type.lower() in allowed_integrations
    
    def can_export_format(self, format_type: str) -> bool:
        """
        Check if current license can export in specific format
        
        Args:
            format_type: Export format (e.g., 'excel', 'pdf')
            
        Returns:
            bool: True if allowed
        """
        if not self.current_license:
            return False
        
        license_type = self.current_license.get('license_type', 'free')
        allowed_formats = self.LICENSE_FEATURES.get(license_type, {}).get('export_formats', [])
        
        return format_type.lower() in allowed_formats
