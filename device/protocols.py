#!/usr/bin/env python3
"""
Device Communication Protocols
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional


class DeviceProtocol(ABC):
    """
    Abstract base class for device communication protocols
    """
    
    @abstractmethod
    def connect(self) -> bool:
        """Connect to device"""
        pass
    
    @abstractmethod
    def disconnect(self) -> bool:
        """Disconnect from device"""
        pass
    
    @abstractmethod
    def send(self, data: bytes) -> bool:
        """Send data to device"""
        pass
    
    @abstractmethod
    def receive(self) -> Optional[bytes]:
        """Receive data from device"""
        pass
