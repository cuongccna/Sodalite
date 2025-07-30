"""
Base Invoice Provider
Abstract base class for all invoice data providers
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime, date
from dataclasses import dataclass
from enum import Enum
import requests
import json


class ProviderType(Enum):
    """Enum for supported provider types"""
    MANUAL = "manual"
    VIETTEL = "viettel"
    MOBIFONE = "mobifone"
    FPT = "fpt"
    VNPOST = "vnpost"


class SyncStatus(Enum):
    """Status of synchronization operations"""
    SUCCESS = "success"
    PARTIAL = "partial"
    FAILED = "failed"
    AUTHENTICATION_ERROR = "auth_error"
    RATE_LIMITED = "rate_limited"
    NO_DATA = "no_data"


@dataclass
class ProviderConfig:
    """Configuration for a provider"""
    provider_type: ProviderType
    company_tax_code: str
    api_endpoint: str = ""
    credentials: Dict[str, str] = None  # Will be encrypted in storage
    name: str = ""
    auto_sync: bool = False
    sync_interval_hours: int = 24
    last_sync: Optional[datetime] = None
    is_active: bool = True
    
    def __post_init__(self):
        if self.credentials is None:
            self.credentials = {}


@dataclass
class InvoiceData:
    """Standardized invoice data structure"""
    # Required basic invoice information
    invoice_number: str
    provider_tax_code: str
    provider_name: str
    issue_date: date
    subtotal: float
    vat_amount: float
    total_amount: float
    
    # Optional fields with defaults
    invoice_series: Optional[str] = None
    invoice_template: Optional[str] = None
    provider_address: Optional[str] = None
    payment_date: Optional[date] = None
    currency: str = "VND"
    description: Optional[str] = None
    notes: Optional[str] = None
    external_id: Optional[str] = None
    raw_data: Optional[Dict] = None


@dataclass
class SyncResult:
    """Result of a synchronization operation"""
    status: SyncStatus
    invoices_processed: int
    invoices_new: int
    invoices_updated: int
    invoices_failed: int
    errors: List[str]
    warnings: List[str]
    duration_seconds: float
    last_sync_time: datetime


class BaseInvoiceProvider(ABC):
    """
    Abstract base class for all invoice providers
    
    This class defines the interface that all invoice providers must implement.
    Each provider (Viettel, MobiFone, etc.) will inherit from this class.
    """
    
    def __init__(self, config: ProviderConfig):
        self.config = config
        self._authenticated = False
        self._last_error = None
        self._session = requests.Session()
        self._setup_session()
    
    def _setup_session(self):
        """Setup HTTP session with common headers and timeout"""
        self._session.headers.update({
            'User-Agent': 'FinanTidy/1.0.0',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
        self._session.timeout = 30
    
    @property
    def provider_type(self) -> ProviderType:
        """Get provider type"""
        return self.config.provider_type
    
    @property
    def is_authenticated(self) -> bool:
        """Check if provider is authenticated"""
        return self._authenticated
    
    @property
    def last_error(self) -> Optional[str]:
        """Get last error message"""
        return self._last_error
    
    @abstractmethod
    def authenticate(self) -> bool:
        """
        Authenticate with the provider's API
        
        Returns:
            bool: True if authentication successful, False otherwise
        """
        pass
    
    @abstractmethod
    def test_connection(self) -> Tuple[bool, str]:
        """
        Test connection to provider API
        
        Returns:
            Tuple[bool, str]: (success, message)
        """
        pass
    
    @abstractmethod
    def get_invoices(
        self, 
        start_date: date, 
        end_date: date,
        limit: Optional[int] = None
    ) -> List[InvoiceData]:
        """
        Retrieve invoices from the provider for the given date range
        
        Args:
            start_date: Start date for invoice retrieval
            end_date: End date for invoice retrieval
            limit: Maximum number of invoices to retrieve
            
        Returns:
            List[InvoiceData]: List of retrieved invoices
        """
        pass
    
    @abstractmethod
    def get_invoice_details(self, external_id: str) -> Optional[InvoiceData]:
        """
        Get detailed information for a specific invoice
        
        Args:
            external_id: Provider's unique identifier for the invoice
            
        Returns:
            Optional[InvoiceData]: Invoice details or None if not found
        """
        pass
    
    def sync_invoices(
        self, 
        start_date: Optional[date] = None,
        end_date: Optional[date] = None
    ) -> SyncResult:
        """
        Synchronize invoices from provider
        
        Args:
            start_date: Start date for sync (defaults to last sync or 30 days ago)
            end_date: End date for sync (defaults to today)
            
        Returns:
            SyncResult: Result of synchronization operation
        """
        sync_start_time = datetime.now()
        errors = []
        warnings = []
        invoices_processed = 0
        invoices_new = 0
        invoices_updated = 0
        invoices_failed = 0
        
        try:
            # Set default date range
            if not start_date:
                if self.config.last_sync:
                    start_date = self.config.last_sync.date()
                else:
                    from datetime import timedelta
                    start_date = date.today() - timedelta(days=30)
            
            if not end_date:
                end_date = date.today()
            
            # Authenticate if needed
            if not self.is_authenticated:
                if not self.authenticate():
                    return SyncResult(
                        status=SyncStatus.AUTHENTICATION_ERROR,
                        invoices_processed=0,
                        invoices_new=0,
                        invoices_updated=0,
                        invoices_failed=0,
                        errors=["Authentication failed"],
                        warnings=[],
                        duration_seconds=0,
                        last_sync_time=sync_start_time
                    )
            
            # Get invoices from provider
            invoices = self.get_invoices(start_date, end_date)
            invoices_processed = len(invoices)
            
            # Process each invoice
            for invoice_data in invoices:
                try:
                    # Here we would save to database
                    # For now, just count as new
                    invoices_new += 1
                except Exception as e:
                    invoices_failed += 1
                    errors.append(f"Failed to process invoice {invoice_data.invoice_number}: {str(e)}")
            
            # Determine overall status
            if invoices_failed == 0:
                status = SyncStatus.SUCCESS
            elif invoices_new > 0:
                status = SyncStatus.PARTIAL
            else:
                status = SyncStatus.FAILED
            
            # Update last sync time
            self.config.last_sync = sync_start_time
            
        except Exception as e:
            errors.append(f"Sync failed: {str(e)}")
            status = SyncStatus.FAILED
        
        duration = (datetime.now() - sync_start_time).total_seconds()
        
        return SyncResult(
            status=status,
            invoices_processed=invoices_processed,
            invoices_new=invoices_new,
            invoices_updated=invoices_updated,
            invoices_failed=invoices_failed,
            errors=errors,
            warnings=warnings,
            duration_seconds=duration,
            last_sync_time=sync_start_time
        )
    
    def get_provider_info(self) -> Dict[str, Any]:
        """
        Get information about this provider
        
        Returns:
            Dict containing provider metadata
        """
        return {
            'name': self.provider_type.value.title(),
            'type': self.provider_type.value,
            'authenticated': self.is_authenticated,
            'last_sync': self.config.last_sync.isoformat() if self.config.last_sync else None,
            'auto_sync': self.config.auto_sync,
            'company_tax_code': self.config.company_tax_code,
            'is_active': self.config.is_active
        }
    
    def validate_credentials(self) -> Tuple[bool, List[str]]:
        """
        Validate provider credentials
        
        Returns:
            Tuple[bool, List[str]]: (valid, list of validation errors)
        """
        errors = []
        
        if not self.config.credentials:
            errors.append("No credentials provided")
            return False, errors
        
        # Basic validation - subclasses should override for specific requirements
        required_fields = self.get_required_credential_fields()
        for field in required_fields:
            if field not in self.config.credentials or not self.config.credentials[field]:
                errors.append(f"Missing required credential: {field}")
        
        return len(errors) == 0, errors
    
    @abstractmethod
    def get_required_credential_fields(self) -> List[str]:
        """
        Get list of required credential fields for this provider
        
        Returns:
            List[str]: List of required credential field names
        """
        pass
    
    def cleanup(self):
        """Cleanup resources (close sessions, etc.)"""
        if hasattr(self, '_session'):
            self._session.close()
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.cleanup()
