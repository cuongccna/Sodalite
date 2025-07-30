"""
Tests for Invoice Provider System
"""

import pytest
import tempfile
import json
from datetime import date, datetime
from decimal import Decimal
from unittest.mock import Mock, patch, MagicMock

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from providers import (
    ProviderFactory, 
    ProviderType, 
    ProviderConfig, 
    InvoiceData,
    ManualProvider,
    ViettelProvider,
    create_manual_provider,
    create_viettel_provider,
    list_available_providers
)


class TestProviderFactory:
    """Test the provider factory"""
    
    def test_get_available_providers(self):
        """Test getting available providers"""
        providers = ProviderFactory.get_available_providers()
        assert ProviderType.MANUAL in providers
        assert ProviderType.VIETTEL in providers
    
    def test_create_manual_provider(self):
        """Test creating manual provider"""
        config = ProviderConfig(
            provider_type=ProviderType.MANUAL,
            company_tax_code="0123456789"
        )
        
        provider = ProviderFactory.create_provider(ProviderType.MANUAL, config)
        assert isinstance(provider, ManualProvider)
        assert provider.config.company_tax_code == "0123456789"
    
    def test_create_viettel_provider(self):
        """Test creating Viettel provider"""
        config = ProviderConfig(
            provider_type=ProviderType.VIETTEL,
            company_tax_code="0123456789",
            credentials={
                "username": "test_user",
                "password": "test_pass",
                "api_key": "test_key"
            }
        )
        
        provider = ProviderFactory.create_provider(ProviderType.VIETTEL, config)
        assert isinstance(provider, ViettelProvider)
        assert provider.config.company_tax_code == "0123456789"
    
    def test_unsupported_provider_type(self):
        """Test creating unsupported provider type"""
        # Create a fake provider type
        fake_type = Mock()
        fake_type.value = "FAKE_PROVIDER"
        
        config = ProviderConfig(
            provider_type=fake_type,
            company_tax_code="0123456789"
        )
        
        with pytest.raises(ValueError) as exc_info:
            ProviderFactory.create_provider(fake_type, config)
        
        assert "Unsupported provider type" in str(exc_info.value)
    
    def test_get_provider_info(self):
        """Test getting provider information"""
        info = ProviderFactory.get_provider_info(ProviderType.MANUAL)
        assert info is not None
        assert info["type"] == "manual"
        assert "required_credentials" in info
        assert info["supports_real_time"] == False
        
        info = ProviderFactory.get_provider_info(ProviderType.VIETTEL)
        assert info is not None
        assert info["type"] == "viettel"
        assert "username" in info["required_credentials"]
        assert "password" in info["required_credentials"]
        assert "api_key" in info["required_credentials"]
        assert info["supports_real_time"] == True


class TestManualProvider:
    """Test manual provider functionality"""
    
    def test_initialization(self):
        """Test manual provider initialization"""
        config = ProviderConfig(
            provider_type=ProviderType.MANUAL,
            company_tax_code="0123456789"
        )
        
        provider = ManualProvider(config)
        assert provider.config.provider_type == ProviderType.MANUAL
        assert provider.is_authenticated == True  # Manual is always authenticated
    
    def test_test_connection(self):
        """Test connection testing"""
        provider = create_manual_provider("0123456789")
        success, message = provider.test_connection()
        assert success == True
        assert "Manual entry mode" in message
    
    def test_add_invoice(self):
        """Test adding invoice manually"""
        provider = create_manual_provider("0123456789")
        
        invoice_data = InvoiceData(
            invoice_number="INV-001",
            provider_tax_code="0987654321",
            provider_name="Test Provider",
            issue_date=date.today(),
            subtotal=100000,
            vat_amount=10000,
            total_amount=110000
        )
        
        result = provider.add_invoice(invoice_data)
        assert result == True
        
        # Check if invoice was added
        invoices = provider.get_invoices(date.today(), date.today())
        assert len(invoices) == 1
        assert invoices[0].invoice_number == "INV-001"
    
    def test_get_invoices_date_range(self):
        """Test getting invoices by date range"""
        provider = create_manual_provider("0123456789")
        
        # Add test invoices
        today = date.today()
        
        invoice1 = InvoiceData(
            invoice_number="INV-001",
            provider_tax_code="0987654321",
            provider_name="Test Provider",
            issue_date=today,
            subtotal=100000,
            vat_amount=10000,
            total_amount=110000
        )
        
        provider.add_invoice(invoice1)
        
        # Test retrieval
        invoices = provider.get_invoices(today, today)
        assert len(invoices) == 1
        
        # Test date range outside
        from datetime import timedelta
        yesterday = today - timedelta(days=1)
        invoices = provider.get_invoices(yesterday, yesterday)
        assert len(invoices) == 0


class TestViettelProvider:
    """Test Viettel provider functionality"""
    
    def test_initialization(self):
        """Test Viettel provider initialization"""
        config = ProviderConfig(
            provider_type=ProviderType.VIETTEL,
            company_tax_code="0123456789",
            credentials={
                "username": "test_user",
                "password": "test_pass",
                "api_key": "test_key"
            }
        )
        
        provider = ViettelProvider(config)
        assert provider.config.provider_type == ProviderType.VIETTEL
        assert provider.config.api_endpoint == ViettelProvider.API_BASE_URL
        assert provider.is_authenticated == False  # Not authenticated yet
    
    def test_validate_credentials(self):
        """Test credential validation"""
        # Valid credentials
        config = ProviderConfig(
            provider_type=ProviderType.VIETTEL,
            company_tax_code="0123456789",
            credentials={
                "username": "test_user",
                "password": "test_pass",
                "api_key": "test_key"
            }
        )
        
        provider = ViettelProvider(config)
        is_valid, errors = provider.validate_credentials()
        assert is_valid == True
        assert len(errors) == 0
        
        # Missing credentials
        config.credentials = {"username": "test_user"}
        provider = ViettelProvider(config)
        is_valid, errors = provider.validate_credentials()
        assert is_valid == False
        assert len(errors) > 0
    
    @patch('requests.Session.post')
    def test_authentication_success(self, mock_post):
        """Test successful authentication"""
        # Mock successful authentication response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "success": True,
            "access_token": "test_token_123",
            "expires_in": 3600
        }
        mock_post.return_value = mock_response
        
        provider = create_viettel_provider(
            company_tax_code="0123456789",
            username="test_user",
            password="test_pass",
            api_key="test_key"
        )
        
        success = provider.authenticate()
        assert success == True
        assert provider.is_authenticated == True
        assert provider._access_token == "test_token_123"
    
    @patch('requests.Session.post')
    def test_authentication_failure(self, mock_post):
        """Test failed authentication"""
        # Mock failed authentication response
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_post.return_value = mock_response
        
        provider = create_viettel_provider(
            company_tax_code="0123456789",
            username="wrong_user",
            password="wrong_pass",
            api_key="wrong_key"
        )
        
        success = provider.authenticate()
        assert success == False
        assert provider.is_authenticated == False
        assert "HTTP 401" in provider._last_error
    
    @patch('requests.Session.get')
    def test_test_connection(self, mock_get):
        """Test connection testing"""
        # Mock successful ping response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        provider = create_viettel_provider(
            company_tax_code="0123456789",
            username="test_user",
            password="test_pass",
            api_key="test_key"
        )
        
        success, message = provider.test_connection()
        assert success == True
        assert "successful" in message
    
    def test_generate_signature(self):
        """Test API signature generation"""
        provider = create_viettel_provider(
            company_tax_code="0123456789",
            username="test_user",
            password="test_pass",
            api_key="test_key"
        )
        
        test_data = {
            "username": "test_user",
            "timestamp": 1234567890
        }
        
        signature = provider._generate_signature(test_data)
        assert isinstance(signature, str)
        assert len(signature) == 32  # MD5 hash length
    
    def test_convert_api_to_invoice_data(self):
        """Test API data conversion"""
        provider = create_viettel_provider(
            company_tax_code="0123456789",
            username="test_user",
            password="test_pass",
            api_key="test_key"
        )
        
        api_data = {
            "invoice_id": "VT-001",
            "invoice_number": "INV-001",
            "invoice_series": "AA/24E",
            "template_code": "1/001",
            "seller_tax_code": "0987654321",
            "seller_name": "Test Seller",
            "seller_address": "123 Test St",
            "issue_date": "2024-01-15",
            "payment_date": "2024-01-30",
            "subtotal": "100000.00",
            "vat_amount": "10000.00",
            "total_amount": "110000.00",
            "currency": "VND",
            "description": "Test invoice",
            "notes": "Test notes"
        }
        
        invoice_data = provider._convert_api_to_invoice_data(api_data)
        
        assert invoice_data.invoice_number == "INV-001"
        assert invoice_data.provider_tax_code == "0987654321"
        assert invoice_data.provider_name == "Test Seller"
        assert invoice_data.subtotal == 100000.0
        assert invoice_data.vat_amount == 10000.0
        assert invoice_data.total_amount == 110000.0
        assert invoice_data.external_id == "VT-001"
        assert invoice_data.raw_data == api_data


class TestConvenienceFunctions:
    """Test convenience functions"""
    
    def test_create_manual_provider_function(self):
        """Test create_manual_provider convenience function"""
        provider = create_manual_provider("0123456789")
        assert isinstance(provider, ManualProvider)
        assert provider.config.company_tax_code == "0123456789"
        assert provider.config.name == "Manual Entry"
    
    def test_create_viettel_provider_function(self):
        """Test create_viettel_provider convenience function"""
        provider = create_viettel_provider(
            company_tax_code="0123456789",
            username="test_user",
            password="test_pass",
            api_key="test_key",
            name="Custom Viettel"
        )
        
        assert isinstance(provider, ViettelProvider)
        assert provider.config.company_tax_code == "0123456789"
        assert provider.config.name == "Custom Viettel"
        assert provider.config.credentials["username"] == "test_user"
    
    def test_list_available_providers_function(self):
        """Test list_available_providers convenience function"""
        providers = list_available_providers()
        assert len(providers) >= 2  # At least Manual and Viettel
        
        provider_types = [p["type"] for p in providers]
        assert "manual" in provider_types
        assert "viettel" in provider_types


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
