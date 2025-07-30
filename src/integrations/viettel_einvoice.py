"""
FinanTidy - Viettel eInvoice Integration Service
Handles electronic invoice generation through Viettel SInvoice API
"""

import json
import requests
import uuid
from datetime import datetime
import logging
from typing import Dict, List, Optional, Any
from decimal import Decimal

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ViettelEInvoiceService:
    """Service for integrating with Viettel SInvoice API"""
    
    def __init__(self, config):
        """
        Initialize Viettel eInvoice service
        
        Args:
            config: Configuration dict or ViettelEInvoiceConfig object containing:
                - base_url: Viettel API base URL
                - username: API username (tax code + user)
                - password: API password
                - supplier_tax_code: Company tax code
                - template_code: Invoice template code
                - invoice_series: Invoice series code
                - auth_method: 'basic' or 'token'
        """
        # Handle both dict and config object
        if hasattr(config, 'get_config'):  # ViettelEInvoiceConfig object
            config_dict = config.get_config()
        elif isinstance(config, dict):
            config_dict = config
        else:
            raise ValueError("Config must be dict or ViettelEInvoiceConfig object")
        
        self.config = config_dict
        self.base_url = config_dict.get('base_url', 'https://sinvoice.viettel.vn')
        self.username = config_dict['username']
        self.password = config_dict['password']
        self.supplier_tax_code = config_dict['supplier_tax_code']
        self.template_code = config_dict.get('template_code', '')
        self.invoice_series = config_dict.get('invoice_series', '')
        self.auth_method = config_dict.get('auth_method', 'token')
        
        self.access_token = None
        self.session = requests.Session()
        
        # Setup request headers
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'FinanTidy/2.0'
        })
    
    def authenticate(self) -> bool:
        """
        Authenticate with Viettel API
        
        Returns:
            bool: True if authentication successful
        """
        try:
            if self.auth_method == 'token':
                return self._authenticate_token()
            else:
                return self._authenticate_basic()
        except Exception as e:
            logger.error(f"Authentication failed: {e}")
            return False
    
    def _authenticate_token(self) -> bool:
        """Authenticate using token method"""
        url = f"{self.base_url}/auth/login"
        
        payload = {
            "username": self.username,
            "password": self.password
        }
        
        response = self.session.post(url, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            self.access_token = result.get('access_token')
            
            if self.access_token:
                # Set cookie header for subsequent requests
                self.session.headers['Cookie'] = f"access_token={self.access_token}"
                logger.info("Token authentication successful")
                return True
        
        logger.error(f"Token authentication failed: {response.status_code} - {response.text}")
        return False
    
    def _authenticate_basic(self) -> bool:
        """Authenticate using basic auth method"""
        from requests.auth import HTTPBasicAuth
        
        self.session.auth = HTTPBasicAuth(self.username, self.password)
        logger.info("Basic authentication configured")
        return True
    
    def create_invoice(self, invoice_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create electronic invoice via Viettel API
        
        Args:
            invoice_data: Invoice data in FinanTidy format
            
        Returns:
            Dict containing API response
        """
        try:
            # Ensure authentication
            if not self.access_token and self.auth_method == 'token':
                if not self.authenticate():
                    raise Exception("Authentication failed")
            
            # Convert FinanTidy invoice to Viettel format
            viettel_payload = self._convert_to_viettel_format(invoice_data)
            
            # Create invoice via API
            url = f"{self.base_url}/InvoiceAPI/InvoiceWS/createInvoice/{self.supplier_tax_code}"
            
            response = self.session.post(url, json=viettel_payload)
            
            if response.status_code == 200:
                result = response.json()
                logger.info(f"Invoice created successfully: {result}")
                return {
                    'success': True,
                    'invoice_no': result.get('result', {}).get('invoiceNo'),
                    'transaction_id': result.get('result', {}).get('transactionID'),
                    'reservation_code': result.get('result', {}).get('reservationCode'),
                    'response': result
                }
            else:
                logger.error(f"Invoice creation failed: {response.status_code} - {response.text}")
                return {
                    'success': False,
                    'error': f"API Error: {response.status_code}",
                    'details': response.text
                }
                
        except Exception as e:
            logger.error(f"Invoice creation error: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def get_invoice_file(self, transaction_id: str, file_type: str = 'pdf') -> Dict[str, Any]:
        """
        Download invoice file from Viettel
        
        Args:
            transaction_id: Transaction ID from invoice creation
            file_type: File type ('pdf', 'xml', etc.)
            
        Returns:
            Dict containing file data or error
        """
        try:
            url = f"{self.base_url}/InvoiceAPI/InvoiceUtilsWS/getInvoiceRepresentationFile"
            
            payload = {
                "transactionID": transaction_id,
                "templateCode": self.template_code,
                "invoiceSeries": self.invoice_series,
                "fileType": file_type.upper()
            }
            
            response = self.session.post(url, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                
                if result.get('errorCode') is None:
                    file_data = result.get('result', {}).get('fileToBytes')
                    return {
                        'success': True,
                        'file_data': file_data,
                        'file_name': f"invoice_{transaction_id}.{file_type.lower()}"
                    }
                else:
                    return {
                        'success': False,
                        'error': result.get('description', 'Unknown error')
                    }
            else:
                return {
                    'success': False,
                    'error': f"API Error: {response.status_code}"
                }
                
        except Exception as e:
            logger.error(f"File download error: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def search_invoice(self, transaction_uuid: str) -> Dict[str, Any]:
        """
        Search invoice by transaction UUID
        
        Args:
            transaction_uuid: Unique transaction identifier
            
        Returns:
            Dict containing invoice information
        """
        try:
            url = f"{self.base_url}/InvoiceAPI/InvoiceWS/searchInvoiceByTransactionUuid"
            
            payload = {
                "transactionUuid": transaction_uuid
            }
            
            response = self.session.post(url, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                return {
                    'success': True,
                    'invoice_info': result.get('result')
                }
            else:
                return {
                    'success': False,
                    'error': f"API Error: {response.status_code}"
                }
                
        except Exception as e:
            logger.error(f"Invoice search error: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def cancel_invoice(self, invoice_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cancel electronic invoice
        
        Args:
            invoice_data: Invoice cancellation data
            
        Returns:
            Dict containing cancellation result
        """
        try:
            url = f"{self.base_url}/InvoiceAPI/InvoiceWS/cancelTransactionInvoice"
            
            payload = {
                "supplierTaxCode": self.supplier_tax_code,
                "invoiceNo": invoice_data['invoice_no'],
                "templateCode": self.template_code,
                "invoiceSeries": self.invoice_series,
                "additionalReferenceDesc": invoice_data.get('reason', 'Cancelled by user'),
                "additionalReferenceDate": int(datetime.now().timestamp() * 1000)
            }
            
            response = self.session.post(url, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                return {
                    'success': True,
                    'result': result
                }
            else:
                return {
                    'success': False,
                    'error': f"API Error: {response.status_code}"
                }
                
        except Exception as e:
            logger.error(f"Invoice cancellation error: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def _convert_to_viettel_format(self, invoice_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert FinanTidy invoice format to Viettel API format
        
        Args:
            invoice_data: Invoice data from FinanTidy
            
        Returns:
            Dict in Viettel API format
        """
        # Generate unique transaction UUID
        transaction_uuid = str(uuid.uuid4())
        
        # Convert invoice date to timestamp
        invoice_date = invoice_data.get('invoice_date')
        if isinstance(invoice_date, str):
            invoice_date = datetime.strptime(invoice_date, '%Y-%m-%d')
        invoice_timestamp = int(invoice_date.timestamp() * 1000)
        
        # Convert items
        viettel_items = []
        total_amount = Decimal('0')
        total_tax = Decimal('0')
        
        for item in invoice_data.get('items', []):
            quantity = Decimal(str(item.get('quantity', 1)))
            unit_price = Decimal(str(item.get('unit_price', 0)))
            tax_rate = Decimal(str(item.get('tax_rate', 0)))
            discount_rate = Decimal(str(item.get('discount_rate', 0)))
            
            # Calculate line total
            line_total = quantity * unit_price
            discount_amount = line_total * discount_rate / 100
            taxable_amount = line_total - discount_amount
            tax_amount = taxable_amount * tax_rate / 100
            
            total_amount += taxable_amount
            total_tax += tax_amount
            
            viettel_item = {
                "lineNumber": len(viettel_items) + 1,
                "itemCode": item.get('item_code', ''),
                "itemName": item['item_name'],
                "unitName": item.get('unit', 'Cái'),
                "unitPrice": float(unit_price),
                "quantity": float(quantity),
                "itemTotalAmountWithoutTax": float(taxable_amount),
                "taxPercentage": float(tax_rate),
                "taxAmount": float(tax_amount),
                "discount": float(discount_amount),
                "itemDiscount": float(discount_rate),
                "itemNote": item.get('description', '')
            }
            viettel_items.append(viettel_item)
        
        # Build Viettel payload
        viettel_payload = {
            "transactionUuid": transaction_uuid,
            "generalInvoiceInfo": {
                "templateCode": self.template_code,
                "invoiceSeries": self.invoice_series,
                "invoiceIssuedDate": invoice_timestamp,
                "currencyCode": invoice_data.get('currency', 'VND'),
                "adjustmentType": 1,  # Original invoice
                "paymentMethodName": invoice_data.get('payment_method', 'Tiền mặt'),
                "invoiceNote": invoice_data.get('description', '')
            },
            "buyerInfo": {
                "buyerName": invoice_data.get('buyer_name', ''),
                "buyerTaxCode": invoice_data.get('buyer_tax_code', ''),
                "buyerAddressLine": invoice_data.get('buyer_address', ''),
                "buyerPhoneNumber": invoice_data.get('buyer_phone', ''),
                "buyerEmail": invoice_data.get('buyer_email', ''),
                "buyerBankAccount": invoice_data.get('buyer_bank_account', ''),
                "buyerBankName": invoice_data.get('buyer_bank_name', '')
            },
            "sellerInfo": {
                "sellerTaxCode": self.supplier_tax_code,
                "sellerFullName": invoice_data.get('seller_name', ''),
                "sellerAddressLine": invoice_data.get('seller_address', ''),
                "sellerPhoneNumber": invoice_data.get('seller_phone', ''),
                "sellerEmail": invoice_data.get('seller_email', ''),
                "sellerBankAccount": invoice_data.get('seller_bank_account', ''),
                "sellerBankName": invoice_data.get('seller_bank_name', '')
            },
            "itemInfo": viettel_items,
            "summarizeInfo": {
                "sumOfTotalLineAmountWithoutTax": float(total_amount),
                "totalAmountWithoutTax": float(total_amount),
                "totalTaxAmount": float(total_tax),
                "totalAmountWithTax": float(total_amount + total_tax),
                "totalAmountAfterDiscount": float(total_amount + total_tax),
                "totalPaymentAmount": float(total_amount + total_tax)
            },
            "taxBreakdowns": self._calculate_tax_breakdowns(viettel_items)
        }
        
        return viettel_payload
    
    def _calculate_tax_breakdowns(self, items: List[Dict]) -> List[Dict]:
        """Calculate tax breakdown by tax rates"""
        tax_groups = {}
        
        for item in items:
            tax_rate = item['taxPercentage']
            if tax_rate not in tax_groups:
                tax_groups[tax_rate] = {
                    'taxableAmount': 0,
                    'taxAmount': 0
                }
            
            tax_groups[tax_rate]['taxableAmount'] += item['itemTotalAmountWithoutTax']
            tax_groups[tax_rate]['taxAmount'] += item['taxAmount']
        
        breakdowns = []
        for tax_rate, amounts in tax_groups.items():
            breakdowns.append({
                "taxPercentage": tax_rate,
                "taxableAmount": amounts['taxableAmount'],
                "taxAmount": amounts['taxAmount']
            })
        
        return breakdowns


class ViettelEInvoiceConfig:
    """Configuration manager for Viettel eInvoice integration"""
    
    def __init__(self, config_file: str = None):
        """Initialize config manager"""
        self.config_file = config_file or "viettel_config.json"
        self.config = self.load_config(self.config_file)
    
    def is_configured(self) -> bool:
        """Check if Viettel eInvoice is properly configured"""
        required_fields = ['base_url', 'username', 'password', 'supplier_tax_code', 'template_code']
        return all(self.config.get(field) for field in required_fields)
    
    def get_config(self) -> Dict[str, Any]:
        """Get current configuration"""
        return self.config.copy()
    
    def update_config(self, updates: Dict[str, Any]):
        """Update configuration"""
        self.config.update(updates)
    
    def save(self):
        """Save current configuration to file"""
        self.save_config(self.config, self.config_file)
    
    @staticmethod
    def load_config(config_file: str = None) -> Dict[str, Any]:
        """Load configuration from file or environment"""
        import os
        
        # Default configuration
        config = {
            'base_url': os.getenv('VIETTEL_API_URL', 'https://sinvoice.viettel.vn'),
            'username': os.getenv('VIETTEL_USERNAME', ''),
            'password': os.getenv('VIETTEL_PASSWORD', ''),
            'supplier_tax_code': os.getenv('VIETTEL_TAX_CODE', ''),
            'template_code': os.getenv('VIETTEL_TEMPLATE_CODE', ''),
            'invoice_series': os.getenv('VIETTEL_INVOICE_SERIES', ''),
            'auth_method': os.getenv('VIETTEL_AUTH_METHOD', 'token')
        }
        
        # Load from file if specified
        if config_file and os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    file_config = json.load(f)
                    config.update(file_config)
            except Exception as e:
                logger.warning(f"Could not load config file {config_file}: {e}")
        
        return config
    
    @staticmethod
    def save_config(config: Dict[str, Any], config_file: str):
        """Save configuration to file"""
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Could not save config file {config_file}: {e}")


# Usage example and testing
if __name__ == "__main__":
    # Example configuration
    test_config = {
        'base_url': 'https://sinvoice.viettel.vn',
        'username': '0100109106-509',  # Test account
        'password': 'test_password',    # Contact Viettel for test password
        'supplier_tax_code': '0100109106',
        'template_code': '01GTKT0/001',
        'invoice_series': 'C22T',
        'auth_method': 'token'
    }
    
    # Example invoice data
    test_invoice = {
        'invoice_date': '2025-07-30',
        'currency': 'VND',
        'description': 'Test invoice from FinanTidy',
        'buyer_name': 'Công ty TNHH ABC',
        'buyer_tax_code': '0123456789',
        'buyer_address': '123 Test Street, Hanoi',
        'buyer_email': 'test@abc.com',
        'items': [
            {
                'item_name': 'Software License',
                'quantity': 1,
                'unit_price': 1000000,
                'tax_rate': 10,
                'discount_rate': 0,
                'description': 'Annual software license'
            }
        ]
    }
    
    # Test the service (commented out for security)
    # service = ViettelEInvoiceService(test_config)
    # result = service.create_invoice(test_invoice)
    # print(json.dumps(result, indent=2, ensure_ascii=False))
