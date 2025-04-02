from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

from data_ingestion.data_models import CameraDataPayload
from data_ingestion.data_ingestion_service import DataIngestionService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Camera Data Ingestor",
    description="A FastAPI application for ingesting camera data asynchronously",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize data ingestion service
data_ingestion_service = DataIngestionService()

@app.get("/")
async def root():
    """Root endpoint to verify the API is running."""
    return {"message": "Camera Data Ingestion API is running"}

@app.post("/ingest")
async def ingest_data(payload: CameraDataPayload):
    """
    Endpoint to ingest camera data.
    
    Args:
        payload (CameraDataPayload): The camera data payload containing camera information
        
    Returns:
        dict: Success message with received data
    """
    try:
        await data_ingestion_service.ingest_data(payload)
        return {
            "status": "success",
            "message": "Data ingested successfully",
            "data": {
                "timestamp": payload.timestamp.isoformat(),
                "company_name": payload.company_name,
                "device_id": payload.device_id,
                "person_count": payload.person_count,
                "ages": payload.ages
            }
        }
    except Exception as e:
        logger.error(f"Error ingesting data: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Data ingestion failed: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
