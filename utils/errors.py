#!/usr/bin/env python3
"""
AI Line Error Types
"""


class AILineError(Exception):
    """Base AI Line exception"""
    pass


class DeviceError(AILineError):
    """Device communication error"""
    pass


class InferenceError(AILineError):
    """Model inference error"""
    pass


class ConfigurationError(AILineError):
    """Configuration error"""
    pass
