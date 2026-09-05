#!/usr/bin/env python3
"""
AI Line Core System
Main orchestrator for device-linked AI operations
"""

import asyncio
import logging
from typing import Dict, List, Optional
from .device_manager import DeviceManager
from .inference_engine import InferenceEngine

logger = logging.getLogger(__name__)


class AILine:
    """
    Main AI Line System - Coordinates AI models with physical devices
    """
    
    def __init__(self, config):
        """
        Initialize AI Line system
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.device_manager = DeviceManager(config)
        self.inference_engine = InferenceEngine(config)
        self.running = False
        logger.info("AI Line core initialized")
    
    def run(self):
        """
        Start the main AI Line event loop
        """
        logger.info("Starting AI Line main loop")
        self.running = True
        
        try:
            # Initialize devices
            self.device_manager.initialize()
            logger.info(f"Devices initialized: {len(self.device_manager.devices)} devices found")
            
            # Load AI models
            self.inference_engine.load_models()
            logger.info("AI models loaded")
            
            # Run event loop
            asyncio.run(self._main_loop())
            
        except Exception as e:
            logger.error(f"Error in main loop: {e}", exc_info=True)
            raise
        finally:
            self.shutdown()
    
    async def _main_loop(self):
        """
        Async main event loop
        """
        while self.running:
            try:
                # Check for device updates
                device_events = self.device_manager.get_events()
                
                for event in device_events:
                    logger.debug(f"Device event: {event}")
                    # Process event through AI
                    response = await self.inference_engine.process(event)
                    # Send response to device
                    if response:
                        self.device_manager.send_command(response)
                
                # Small sleep to prevent busy waiting
                await asyncio.sleep(0.1)
                
            except Exception as e:
                logger.error(f"Error in main loop iteration: {e}")
                await asyncio.sleep(1)
    
    def shutdown(self):
        """
        Gracefully shutdown AI Line
        """
        logger.info("Shutting down AI Line")
        self.running = False
        self.device_manager.cleanup()
        self.inference_engine.cleanup()
        logger.info("AI Line shutdown complete")
