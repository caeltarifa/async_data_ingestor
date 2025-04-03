import logging
import asyncio
from datetime import datetime
from .data_models import CameraDataPayload

logger = logging.getLogger(__name__)

class DataIngestionService:
    """
    Service responsible for handling the ingestion of camera data.
    
    This service provides asynchronous methods to process and handle
    the camera data received from various sources.
    """
    
    def __init__(self):
        """Initialize the DataIngestionService."""
        logger.info("DataIngestionService initialized")
    
    async def ingest_data(self, payload: CameraDataPayload) -> None:
        """
        Asynchronously ingest camera data from the provided payload.
        
        Args:
            payload (CameraDataPayload): The data payload containing camera information
            
        Returns:
            None
        """
        # Log the received data
        formatted_time = payload.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        
        logger.info(f"[{formatted_time}] Ingested data:")
        logger.info(f"  Company: {payload.company_name}")
        logger.info(f"  Device ID: {payload.device_id}")
        logger.info(f"  Number of Persons: {payload.person_count}")
        
        # Log each person's data including age and gender
        logger.info("  People detected:")
        for i, person in enumerate(payload.people, 1):
            logger.info(f"    Person {i}: Age {person.age}, Gender: {person.gender.value}")
        
        # Simulate some async processing
        await asyncio.sleep(0.1)
        
        # Additional processing logic could be added here in the future
        # For example:
        # - Data validation
        # - Database storage
        # - Real-time analytics
        # - Notifications or alerts
        
        logger.info(f"Successfully processed data from {payload.company_name} device {payload.device_id}")
