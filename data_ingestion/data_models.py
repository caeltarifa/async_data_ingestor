from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime

class CameraDataPayload(BaseModel):
    """
    Pydantic model for camera data payload.
    
    Attributes:
        timestamp (datetime): The timestamp when the data was captured
        company_name (str): The name of the company sending the data
        device_id (str): The ID of the camera device
        person_count (int): Number of persons detected by the camera
        ages (List[int]): List of ages of people detected by the camera
    """
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp of data capture")
    company_name: str = Field(..., description="Name of the company")
    device_id: str = Field(..., description="ID of the camera device")
    person_count: int = Field(..., description="Number of persons detected by camera")
    ages: List[int] = Field(..., description="Ages of people detected by camera")
    
    @field_validator('company_name')
    def company_name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('company_name cannot be empty')
        return v
    
    @field_validator('device_id')
    def device_id_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('device_id cannot be empty')
        return v
    
    @field_validator('person_count')
    def person_count_must_be_non_negative(cls, v):
        if v < 0:
            raise ValueError('person_count must be a non-negative integer')
        return v
    
    @field_validator('ages')
    def validate_ages(cls, v):
        if not v:
            raise ValueError('ages list cannot be empty if persons are detected')
        for age in v:
            if age < 0 or age > 120:
                raise ValueError('age must be between 0 and 120')
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "timestamp": "2025-04-02T12:00:00",
                "company_name": "Example Corp",
                "device_id": "CAM001",
                "person_count": 3,
                "ages": [25, 30, 45]
            }
        }
