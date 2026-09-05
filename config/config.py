#!/usr/bin/env python3
"""
Configuration Management
"""

import json
import logging
from pathlib import Path
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class Config:
    """
    Configuration management for AI Line
    """
    
    def __init__(self, config_dict: Dict):
        """
        Initialize configuration
        
        Args:
            config_dict: Configuration dictionary
        """
        self.config = config_dict
        logger.info("Configuration initialized")
    
    @staticmethod
    def load_default() -> "Config":
        """
        Load default configuration
        
        Returns:
            Config object with default settings
        """
        default_config = {
            "version": "1.0.0",
            "created_date": "2026-09-04",
            "device": {
                "auto_discover": True,
                "reconnect_interval": 5,
                "timeout": 10
            },
            "models": {
                "default_model": "gpt2",
                "cache_dir": "./models/cache",
                "download_timeout": 300
            },
            "inference": {
                "max_tokens": 100,
                "temperature": 0.7,
                "timeout": 30
            },
            "logging": {
                "level": "INFO",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
        return Config(default_config)
    
    @staticmethod
    def load_from_file(config_path: str) -> "Config":
        """
        Load configuration from file
        
        Args:
            config_path: Path to configuration file
            
        Returns:
            Config object
        """
        try:
            with open(config_path, 'r') as f:
                config_dict = json.load(f)
            logger.info(f"Configuration loaded from {config_path}")
            return Config(config_dict)
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return Config.load_default()
    
    def get(self, key: str, default=None):
        """
        Get configuration value
        
        Args:
            key: Configuration key (supports dot notation)
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default
    
    def __str__(self):
        return json.dumps(self.config, indent=2)
