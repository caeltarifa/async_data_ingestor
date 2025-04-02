import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Application settings.
    
    This class can be extended with configuration parameters as the application grows.
    For now, it's a placeholder for future configuration options.
    """
    # API settings
    api_title: str = "Camera Data Ingestor"
    api_description: str = "API for ingesting camera data"
    api_version: str = "1.0.0"
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True
    
    # Logging settings
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create a global settings object
settings = Settings()
