# Camera Data Ingestor API

A FastAPI application for ingesting camera data asynchronously.

## Docker Setup

### Build & Run
```sh
cd camera_data_ingestor
./docker-build.sh
```
- Builds `camera-data-ingestor` image
- Runs `camera-ingestor` container on port 8000

### API
- `GET /` - Health check
- `POST /ingest` - Ingest data

#### Example Request
```json
POST /ingest
{
  "timestamp": "2025-04-02T12:00:00",
  "company_name": "Example Corp",
  "device_id": "CAM001",
  "person_count": 3,
  "ages": [25, 30, 45]
}
```

### Docker Management
```sh
docker logs camera-ingestor  # View logs
./docker-cleanup.sh          # Stop & remove container
```

## Manual Setup
```sh
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Development
- `main.py` - Main application
- `data_ingestion/data_models.py` - Data models
- `data_ingestion/data_ingestion_service.py` - Business logic
