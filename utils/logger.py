#!/usr/bin/env python3
"""
Logging Configuration
"""

import logging
import sys
from pathlib import Path


def setup_logging(name: str, level=logging.INFO) -> logging.Logger:
    """
    Setup logging for AI Line
    
    Args:
        name: Logger name
        level: Logging level
        
    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(formatter)
    
    # Add handler
    if not logger.handlers:
        logger.addHandler(console_handler)
    
    return logger
