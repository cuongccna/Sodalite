"""
Manual Invoice Provider
Handles manually entered invoices
"""

from typing import List, Optional, Tuple
from datetime import date
from .base import BaseInvoiceProvider, ProviderType, ProviderConfig, InvoiceData


class ManualProvider(BaseInvoiceProvider):
    """
    Manual invoice provider for user-entered data
    
    This provider doesn't connect to any external API.
    It's used when users manually enter invoice data.
    """
    
    def __init__(self, config: ProviderConfig):
        # Override config to ensure it's manual type
        config.provider_type = ProviderType.MANUAL
        config.api_endpoint = "local"
        super().__init__(config)
        # Manual provider is always "authenticated"
        self._authenticated = True
    
    def authenticate(self) -> bool:
        """Manual provider doesn't need authentication"""
        self._authenticated = True
        return True
    
    def test_connection(self) -> Tuple[bool, str]:
        """Manual provider connection test always succeeds"""
        return True, "Manual entry mode - no external connection required"
    
    def get_invoices(
        self, 
        start_date: date, 
        end_date: date,
        limit: Optional[int] = None
    ) -> List[InvoiceData]:
        """
        Get invoices from manual storage
        For testing, we store invoices in memory
        """
        if not hasattr(self, '_invoices'):
            self._invoices = []
        
        # Filter by date range
        filtered = []
        for invoice in self._invoices:
            if start_date <= invoice.issue_date <= end_date:
                filtered.append(invoice)
        
        if limit:
            filtered = filtered[:limit]
            
        return filtered
    
    def add_invoice(self, invoice_data: InvoiceData) -> bool:
        """
        Add a manual invoice to storage
        
        Args:
            invoice_data: Invoice data to add
            
        Returns:
            bool: True if successful
        """
        if not hasattr(self, '_invoices'):
            self._invoices = []
        
        # Process the invoice
        processed_invoice = self.create_manual_invoice(invoice_data)
        self._invoices.append(processed_invoice)
        return True
    
    def get_invoice_details(self, external_id: str) -> Optional[InvoiceData]:
        """
        Manual provider doesn't have external IDs
        """
        return None
    
    def get_required_credential_fields(self) -> List[str]:
        """Manual provider doesn't need credentials"""
        return []
    
    def create_manual_invoice(self, invoice_data: InvoiceData) -> InvoiceData:
        """
        Create a manual invoice entry
        
        Args:
            invoice_data: Invoice data entered by user
            
        Returns:
            InvoiceData: Processed invoice data
        """
        # Add manual provider specifics
        invoice_data.external_id = f"manual_{invoice_data.invoice_number}"
        if not invoice_data.raw_data:
            invoice_data.raw_data = {"source": "manual_entry"}
        
        return invoice_data
