#!/usr/bin/env python3
"""
Serial Device Communication
"""

import logging
from typing import Optional
from .protocols import DeviceProtocol

logger = logging.getLogger(__name__)


class SerialDevice(DeviceProtocol):
    """
    Serial port device communication
    """
    
    def __init__(self, port: str, baudrate: int = 9600):
        """
        Initialize serial device
        
        Args:
            port: Serial port (e.g., '/dev/ttyUSB0', 'COM3')
            baudrate: Baud rate
        """
        self.port = port
        self.baudrate = baudrate
        self.serial = None
        logger.info(f"SerialDevice initialized: {port} @ {baudrate}bps")
    
    def connect(self) -> bool:
        """Connect to serial device"""
        try:
            import serial
            self.serial = serial.Serial(self.port, self.baudrate, timeout=1)
            logger.info(f"Connected to {self.port}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect: {e}")
            return False
    
    def disconnect(self) -> bool:
        """Disconnect from serial device"""
        try:
            if self.serial:
                self.serial.close()
                logger.info(f"Disconnected from {self.port}")
            return True
        except Exception as e:
            logger.error(f"Error disconnecting: {e}")
            return False
    
    def send(self, data: bytes) -> bool:
        """Send data over serial"""
        try:
            if self.serial and self.serial.is_open:
                self.serial.write(data)
                return True
            return False
        except Exception as e:
            logger.error(f"Send error: {e}")
            return False
    
    def receive(self) -> Optional[bytes]:
        """Receive data from serial"""
        try:
            if self.serial and self.serial.is_open:
                if self.serial.in_waiting:
                    return self.serial.read(self.serial.in_waiting)
            return None
        except Exception as e:
            logger.error(f"Receive error: {e}")
            return None
