"""
Provider Factory
Creates and manages invoice provider instances
"""

from typing import Dict, Type, List, Optional
from .base import BaseInvoiceProvider, ProviderType, ProviderConfig
from .manual import ManualProvider
from .viettel import ViettelProvider


class ProviderFactory:
    """
    Factory class for creating invoice provider instances
    """
    
    # Registry of available providers
    _providers: Dict[ProviderType, Type[BaseInvoiceProvider]] = {
        ProviderType.MANUAL: ManualProvider,
        ProviderType.VIETTEL: ViettelProvider,
    }
    
    @classmethod
    def create_provider(
        self, 
        provider_type: ProviderType, 
        config: ProviderConfig
    ) -> BaseInvoiceProvider:
        """
        Create a provider instance
        
        Args:
            provider_type: Type of provider to create
            config: Provider configuration
            
        Returns:
            BaseInvoiceProvider: Provider instance
            
        Raises:
            ValueError: If provider type is not supported
        """
        if provider_type not in self._providers:
            available = ", ".join([p.value for p in self._providers.keys()])
            raise ValueError(f"Unsupported provider type: {provider_type.value}. Available: {available}")
        
        provider_class = self._providers[provider_type]
        return provider_class(config)
    
    @classmethod
    def get_available_providers(self) -> List[ProviderType]:
        """
        Get list of available provider types
        
        Returns:
            List[ProviderType]: Available provider types
        """
        return list(self._providers.keys())
    
    @classmethod
    def register_provider(
        self, 
        provider_type: ProviderType, 
        provider_class: Type[BaseInvoiceProvider]
    ) -> None:
        """
        Register a new provider type
        
        Args:
            provider_type: Provider type identifier
            provider_class: Provider class to register
        """
        self._providers[provider_type] = provider_class
    
    @classmethod
    def get_provider_info(self, provider_type: ProviderType) -> Optional[Dict[str, any]]:
        """
        Get information about a specific provider
        
        Args:
            provider_type: Provider type to get info for
            
        Returns:
            Optional[Dict]: Provider information or None if not found
        """
        if provider_type not in self._providers:
            return None
        
        provider_class = self._providers[provider_type]
        
        # Create a temporary instance to get required fields
        temp_config = ProviderConfig(
            provider_type=provider_type,
            company_tax_code="temp"
        )
        temp_instance = provider_class(temp_config)
        
        return {
            "type": provider_type.value,
            "class_name": provider_class.__name__,
            "description": provider_class.__doc__ or "No description available",
            "required_credentials": temp_instance.get_required_credential_fields(),
            "supports_real_time": provider_type != ProviderType.MANUAL
        }


# Convenience functions for common operations

def create_manual_provider(company_tax_code: str) -> ManualProvider:
    """
    Create a manual provider instance
    
    Args:
        company_tax_code: Company tax code
        
    Returns:
        ManualProvider: Manual provider instance
    """
    config = ProviderConfig(
        provider_type=ProviderType.MANUAL,
        company_tax_code=company_tax_code,
        name="Manual Entry"
    )
    return ProviderFactory.create_provider(ProviderType.MANUAL, config)


def create_viettel_provider(
    company_tax_code: str,
    username: str,
    password: str,
    api_key: str,
    name: str = "Viettel Provider"
) -> ViettelProvider:
    """
    Create a Viettel provider instance
    
    Args:
        company_tax_code: Company tax code
        username: Viettel username
        password: Viettel password
        api_key: Viettel API key
        name: Provider name
        
    Returns:
        ViettelProvider: Viettel provider instance
    """
    config = ProviderConfig(
        provider_type=ProviderType.VIETTEL,
        company_tax_code=company_tax_code,
        name=name,
        credentials={
            "username": username,
            "password": password,
            "api_key": api_key
        }
    )
    return ProviderFactory.create_provider(ProviderType.VIETTEL, config)


def list_available_providers() -> List[Dict[str, any]]:
    """
    Get information about all available providers
    
    Returns:
        List[Dict]: Provider information list
    """
    providers = []
    for provider_type in ProviderFactory.get_available_providers():
        info = ProviderFactory.get_provider_info(provider_type)
        if info:
            providers.append(info)
    return providers
