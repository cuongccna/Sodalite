#!/usr/bin/env python3
"""
Test script to verify all translation keys are working
"""

import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from core.language_manager import LanguageManager

def test_translations():
    """Test translation keys"""
    print("🧪 Testing Translation System...")
    
    # Initialize language manager
    lang_manager = LanguageManager()
    
    # Test keys used in login form
    test_keys = [
        ('app.welcome', 'Welcome to FinanTidy'),
        ('app.subtitle', 'Modern financial management system'),
        ('app.version', 'FinanTidy v2.0'),
        ('login.form_title', 'Sign in to your account'),
        ('login.username_label', 'Username'),
        ('login.username_placeholder', 'Enter your username'),
        ('login.password_label', 'Password'),
        ('login.password_placeholder', 'Enter your password'),
        ('login.remember_me', 'Remember me'),
        ('login.forgot_password', 'Forgot password?'),
        ('login.login_button', 'Sign In'),
        ('login.demo_title', 'Default Login Credentials'),
        ('login.demo_info', 'Username: admin'),
        ('login.error_title', 'Login Failed'),
        ('login.error_message', 'Invalid username or password'),
        ('login.default_credentials', 'Default credentials'),
        ('common.ok', 'OK')
    ]
    
    print("\n📝 Testing Vietnamese translations...")
    lang_manager.set_language('vi')
    for key, fallback in test_keys:
        result = lang_manager.t(key, fallback)
        print(f"  {key}: {result}")
    
    print("\n📝 Testing English translations...")
    lang_manager.set_language('en')
    for key, fallback in test_keys:
        result = lang_manager.t(key, fallback)
        print(f"  {key}: {result}")
    
    print("\n✅ Translation test completed successfully!")
    print(f"Current language: {lang_manager.get_current_language()}")
    print(f"Available languages: {lang_manager.get_available_languages()}")

if __name__ == "__main__":
    test_translations()
