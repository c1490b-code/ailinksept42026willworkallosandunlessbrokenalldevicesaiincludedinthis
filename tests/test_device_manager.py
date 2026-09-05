#!/usr/bin/env python3
"""
Device Manager Tests
"""

import unittest
from core.device_manager import DeviceManager
from config.config import Config


class TestDeviceManager(unittest.TestCase):
    """
    Test device manager functionality
    """
    
    def setUp(self):
        """Setup test fixtures"""
        self.config = Config.load_default()
        self.manager = DeviceManager(self.config)
    
    def test_initialization(self):
        """Test device manager initialization"""
        self.assertIsNotNone(self.manager)
        self.assertEqual(len(self.manager.devices), 0)
    
    def test_get_events(self):
        """Test getting device events"""
        events = self.manager.get_events()
        self.assertIsInstance(events, list)
        self.assertEqual(len(events), 0)


if __name__ == '__main__':
    unittest.main()
