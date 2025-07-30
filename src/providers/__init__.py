"""
Invoice Providers Package

This package contains all invoice data providers for FinanTidy.
Providers are responsible for fetching invoice data from various sources
such as APIs, manual entry, file imports, etc.

Available Providers:
- ManualProvider: For manual invoice entry
- ViettelProvider: For Viettel API integration
- (More providers can be added: MobiFone, VNPT, etc.)

Usage:
    from providers import ProviderFactory, ProviderType, ProviderConfig
    
    # Create a Viettel provider
    config = ProviderConfig(
        provider_type=ProviderType.VIETTEL,
        company_tax_code="0123456789",
        credentials={"username": "user", "password": "pass", "api_key": "key"}
    )
    provider = ProviderFactory.create_provider(ProviderType.VIETTEL, config)
    
    # Authenticate and get invoices
    if provider.authenticate():
        invoices = provider.get_invoices(start_date, end_date)
"""

from .base import (
    BaseInvoiceProvider,
    ProviderType,
    ProviderConfig,
    InvoiceData,
    SyncStatus,
    SyncResult
)

from .manual import ManualProvider
from .viettel import ViettelProvider

from .factory import (
    ProviderFactory,
    create_manual_provider,
    create_viettel_provider,
    list_available_providers
)

__all__ = [
    # Base classes and types
    "BaseInvoiceProvider",
    "ProviderType", 
    "ProviderConfig",
    "InvoiceData",
    "SyncStatus",
    "SyncResult",
    
    # Provider implementations
    "ManualProvider",
    "ViettelProvider",
    
    # Factory and utilities
    "ProviderFactory",
    "create_manual_provider",
    "create_viettel_provider", 
    "list_available_providers"
]

# Version info
__version__ = "1.0.0"
__author__ = "FinanTidy Team"
