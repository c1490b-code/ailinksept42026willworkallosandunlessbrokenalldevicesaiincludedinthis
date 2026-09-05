#!/usr/bin/env python3
"""
Configuration Tests
"""

import unittest
from config.config import Config


class TestConfig(unittest.TestCase):
    """
    Test configuration loading and access
    """
    
    def test_load_default(self):
        """Test loading default configuration"""
        config = Config.load_default()
        self.assertIsNotNone(config)
        self.assertEqual(config.get('version'), '1.0.0')
    
    def test_get_nested_value(self):
        """Test getting nested configuration values"""
        config = Config.load_default()
        value = config.get('device.timeout')
        self.assertEqual(value, 10)
    
    def test_get_default_value(self):
        """Test getting default value for missing key"""
        config = Config.load_default()
        value = config.get('nonexistent.key', 'default')
        self.assertEqual(value, 'default')


if __name__ == '__main__':
    unittest.main()
