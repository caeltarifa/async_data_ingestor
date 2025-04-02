# Camera Data Ingestor API

A FastAPI application for ingesting camera data asynchronously.

## Docker Setup

This application can be run in a Docker container. Here's how to set it up:

### Prerequisites

- Docker installed on your system
- Basic knowledge of terminal/command line

### Building and Running the Container

1. Navigate to the project directory:
   ```
   cd camera_data_ingestor
   ```

2. Build and run the Docker container using the provided script:
   ```
   ./docker-build.sh
   ```

   This will:
   - Build a Docker image named `camera-data-ingestor`
   - Run a container named `camera-ingestor`
   - Map port 8000 from the container to port 8000 on your host machine

3. The API will be available at: http://localhost:8000

### API Endpoints

- `GET /` - Root endpoint to verify the API is running
- `POST /ingest` - Endpoint to ingest camera data

### Example Request

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

- View logs:
  ```
  docker logs camera-ingestor
  ```

- Stop and remove the container:
  ```
  ./docker-cleanup.sh
  ```

## Manual Setup

If you prefer to run the application without Docker:

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

## Development

- The main application is defined in `main.py`
- Data models are in `data_ingestion/data_models.py`
- Business logic is in `data_ingestion/data_ingestion_service.py`