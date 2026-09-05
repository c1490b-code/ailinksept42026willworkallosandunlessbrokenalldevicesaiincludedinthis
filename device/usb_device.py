#!/usr/bin/env python3
"""
USB Device Communication
"""

import logging
from typing import Optional
from .protocols import DeviceProtocol

logger = logging.getLogger(__name__)


class USBDevice(DeviceProtocol):
    """
    USB device communication
    """
    
    def __init__(self, vendor_id: int, product_id: int):
        """
        Initialize USB device
        
        Args:
            vendor_id: USB vendor ID
            product_id: USB product ID
        """
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.device = None
        logger.info(f"USBDevice initialized: {vendor_id:04x}:{product_id:04x}")
    
    def connect(self) -> bool:
        """Connect to USB device"""
        try:
            import usb.core
            self.device = usb.core.find(idVendor=self.vendor_id, idProduct=self.product_id)
            if self.device is None:
                logger.error("USB device not found")
                return False
            logger.info("Connected to USB device")
            return True
        except Exception as e:
            logger.error(f"Failed to connect: {e}")
            return False
    
    def disconnect(self) -> bool:
        """Disconnect from USB device"""
        try:
            self.device = None
            logger.info("Disconnected from USB device")
            return True
        except Exception as e:
            logger.error(f"Error disconnecting: {e}")
            return False
    
    def send(self, data: bytes) -> bool:
        """Send data via USB"""
        try:
            if self.device:
                self.device.write(0x01, data)
                return True
            return False
        except Exception as e:
            logger.error(f"Send error: {e}")
            return False
    
    def receive(self) -> Optional[bytes]:
        """Receive data from USB"""
        try:
            if self.device:
                return self.device.read(0x81, 64, timeout=100)
            return None
        except Exception as e:
            logger.error(f"Receive error: {e}")
            return None
