#!/bin/bash

# Build the Docker image
docker build -t analyticsrepository.azurecr.io/camera-data-ingestor:latest .

# Run the container
# -p 8000:8000 maps port 8000 from the container to port 8000 on the host
# --name gives the container a name for easy reference
docker run -p 8000:8000 --name camera-ingestor -d camera-data-ingestor

echo "Camera Data Ingestor API is running at http://localhost:8000"
echo "To view logs: docker logs camera-ingestor"
echo "To stop the container: docker stop camera-ingestor"
echo "To deploy: log in and push the image"
