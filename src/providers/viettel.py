"""
Viettel Invoice Provider
Integrates with Viettel's invoice API system
"""

import json
import hashlib
import time
from typing import List, Optional, Tuple, Dict, Any
from datetime import date, datetime
from decimal import Decimal
from .base import BaseInvoiceProvider, ProviderType, ProviderConfig, InvoiceData


class ViettelProvider(BaseInvoiceProvider):
    """
    Viettel invoice provider for API integration
    
    This provider connects to Viettel's electronic invoice system
    to retrieve invoice data automatically.
    """
    
    # Viettel API endpoints (these would be real endpoints)
    API_BASE_URL = "https://api.viettel.com.vn/einvoice/v1"
    AUTH_ENDPOINT = "/auth/login"
    INVOICES_ENDPOINT = "/invoices"
    INVOICE_DETAIL_ENDPOINT = "/invoices/{invoice_id}"
    
    def __init__(self, config: ProviderConfig):
        # Ensure config is set for Viettel
        config.provider_type = ProviderType.VIETTEL
        if not config.api_endpoint:
            config.api_endpoint = self.API_BASE_URL
        super().__init__(config)
        
        self._access_token = None
        self._token_expires = None
    
    def authenticate(self) -> bool:
        """
        Authenticate with Viettel API
        
        Returns:
            bool: True if authentication successful
        """
        try:
            # Validate credentials first
            is_valid, errors = self.validate_credentials()
            if not is_valid:
                self._last_error = f"Invalid credentials: {', '.join(errors)}"
                return False
            
            # Prepare authentication request
            auth_url = f"{self.config.api_endpoint}{self.AUTH_ENDPOINT}"
            
            # Create authentication payload
            auth_data = {
                "username": self.config.credentials.get("username"),
                "password": self.config.credentials.get("password"),
                "company_tax_code": self.config.company_tax_code,
                "timestamp": int(time.time())
            }
            
            # Add signature if API key is provided
            if "api_key" in self.config.credentials:
                auth_data["signature"] = self._generate_signature(auth_data)
            
            # Make authentication request
            response = self._session.post(auth_url, json=auth_data)
            
            if response.status_code == 200:
                auth_result = response.json()
                
                if auth_result.get("success"):
                    self._access_token = auth_result.get("access_token")
                    self._token_expires = datetime.now().timestamp() + auth_result.get("expires_in", 3600)
                    
                    # Update session headers with token
                    self._session.headers.update({
                        "Authorization": f"Bearer {self._access_token}"
                    })
                    
                    self._authenticated = True
                    self._last_error = None
                    return True
                else:
                    self._last_error = auth_result.get("message", "Authentication failed")
                    return False
            else:
                self._last_error = f"HTTP {response.status_code}: {response.text}"
                return False
                
        except Exception as e:
            self._last_error = f"Authentication error: {str(e)}"
            return False
    
    def test_connection(self) -> Tuple[bool, str]:
        """
        Test connection to Viettel API
        
        Returns:
            Tuple[bool, str]: (success, message)
        """
        try:
            # Try a simple ping endpoint
            ping_url = f"{self.config.api_endpoint}/ping"
            response = self._session.get(ping_url, timeout=10)
            
            if response.status_code == 200:
                return True, "Connection to Viettel API successful"
            else:
                return False, f"Connection failed: HTTP {response.status_code}"
                
        except Exception as e:
            return False, f"Connection error: {str(e)}"
    
    def get_invoices(
        self, 
        start_date: date, 
        end_date: date,
        limit: Optional[int] = None
    ) -> List[InvoiceData]:
        """
        Retrieve invoices from Viettel API
        
        Args:
            start_date: Start date for invoice retrieval
            end_date: End date for invoice retrieval
            limit: Maximum number of invoices to retrieve
            
        Returns:
            List[InvoiceData]: List of retrieved invoices
        """
        if not self.is_authenticated:
            if not self.authenticate():
                return []
        
        try:
            # Check if token is still valid
            if self._token_expires and datetime.now().timestamp() > self._token_expires:
                if not self.authenticate():
                    return []
            
            # Prepare request parameters
            params = {
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat(),
                "company_tax_code": self.config.company_tax_code
            }
            
            if limit:
                params["limit"] = limit
            
            # Make API request
            invoices_url = f"{self.config.api_endpoint}{self.INVOICES_ENDPOINT}"
            response = self._session.get(invoices_url, params=params)
            
            if response.status_code == 200:
                api_result = response.json()
                
                if api_result.get("success"):
                    invoices_data = api_result.get("data", [])
                    return [self._convert_api_to_invoice_data(item) for item in invoices_data]
                else:
                    self._last_error = api_result.get("message", "Failed to retrieve invoices")
                    return []
            else:
                self._last_error = f"API error: HTTP {response.status_code}"
                return []
                
        except Exception as e:
            self._last_error = f"Error retrieving invoices: {str(e)}"
            return []
    
    def get_invoice_details(self, external_id: str) -> Optional[InvoiceData]:
        """
        Get detailed information for a specific invoice
        
        Args:
            external_id: Viettel's unique identifier for the invoice
            
        Returns:
            Optional[InvoiceData]: Invoice details or None if not found
        """
        if not self.is_authenticated:
            if not self.authenticate():
                return None
        
        try:
            detail_url = f"{self.config.api_endpoint}{self.INVOICE_DETAIL_ENDPOINT.format(invoice_id=external_id)}"
            response = self._session.get(detail_url)
            
            if response.status_code == 200:
                api_result = response.json()
                
                if api_result.get("success"):
                    invoice_data = api_result.get("data")
                    return self._convert_api_to_invoice_data(invoice_data)
                else:
                    self._last_error = api_result.get("message", "Invoice not found")
                    return None
            else:
                self._last_error = f"API error: HTTP {response.status_code}"
                return None
                
        except Exception as e:
            self._last_error = f"Error retrieving invoice details: {str(e)}"
            return None
    
    def get_required_credential_fields(self) -> List[str]:
        """Get required credential fields for Viettel"""
        return ["username", "password", "api_key"]
    
    def _generate_signature(self, data: Dict[str, Any]) -> str:
        """
        Generate API signature for authentication
        
        Args:
            data: Data to sign
            
        Returns:
            str: Generated signature
        """
        api_key = self.config.credentials.get("api_key", "")
        
        # Create signature string (example implementation)
        sig_string = ""
        for key in sorted(data.keys()):
            if key != "signature":
                sig_string += f"{key}={data[key]}&"
        
        sig_string += f"key={api_key}"
        
        # Generate MD5 hash
        return hashlib.md5(sig_string.encode()).hexdigest()
    
    def _convert_api_to_invoice_data(self, api_data: Dict[str, Any]) -> InvoiceData:
        """
        Convert Viettel API response to standardized InvoiceData
        
        Args:
            api_data: Raw API response data
            
        Returns:
            InvoiceData: Standardized invoice data
        """
        try:
            # Parse dates
            issue_date = datetime.strptime(api_data["issue_date"], "%Y-%m-%d").date()
            payment_date = None
            if api_data.get("payment_date"):
                payment_date = datetime.strptime(api_data["payment_date"], "%Y-%m-%d").date()
            
            # Parse financial amounts
            subtotal = float(api_data.get("subtotal", 0))
            vat_amount = float(api_data.get("vat_amount", 0))
            total_amount = float(api_data.get("total_amount", 0))
            
            return InvoiceData(
                # Basic information
                invoice_number=api_data["invoice_number"],
                invoice_series=api_data.get("invoice_series"),
                invoice_template=api_data.get("template_code"),
                
                # Provider information
                provider_tax_code=api_data["seller_tax_code"],
                provider_name=api_data["seller_name"],
                provider_address=api_data.get("seller_address"),
                
                # Dates
                issue_date=issue_date,
                payment_date=payment_date,
                
                # Financial data
                subtotal=subtotal,
                vat_amount=vat_amount,
                total_amount=total_amount,
                currency=api_data.get("currency", "VND"),
                
                # Additional data
                description=api_data.get("description"),
                notes=api_data.get("notes"),
                
                # Source tracking
                external_id=api_data["invoice_id"],
                raw_data=api_data
            )
            
        except Exception as e:
            # If conversion fails, create minimal invoice data
            return InvoiceData(
                invoice_number=api_data.get("invoice_number", "UNKNOWN"),
                provider_tax_code=api_data.get("seller_tax_code", ""),
                provider_name=api_data.get("seller_name", "Unknown Provider"),
                issue_date=date.today(),
                subtotal=0,
                vat_amount=0,
                total_amount=0,
                external_id=api_data.get("invoice_id"),
                raw_data=api_data,
                notes=f"Conversion error: {str(e)}"
            )
