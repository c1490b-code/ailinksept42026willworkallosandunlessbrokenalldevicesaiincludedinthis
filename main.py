#!/usr/bin/env python3
"""
AI Line - Main Entry Point
Complete Device-Linked AI System
Created: September 4, 2026
"""

import sys
import logging
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from core.ailine import AILine
from config.config import Config
from utils.logger import setup_logging


def main():
    """
    Initialize and run AI Line system
    """
    # Setup logging
    logger = setup_logging(__name__)
    logger.info("Initializing AI Line system...")
    
    try:
        # Load configuration
        config = Config.load_default()
        logger.info(f"Configuration loaded: {config}")
        
        # Initialize AI Line
        ai_line = AILine(config)
        logger.info("AI Line initialized successfully")
        
        # Start main loop
        ai_line.run()
        
    except KeyboardInterrupt:
        logger.info("Shutdown requested by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
