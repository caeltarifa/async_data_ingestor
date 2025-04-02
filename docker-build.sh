#!/bin/bash

# Build the Docker image
docker build -t camera-data-ingestor .

# Run the container
# -p 8000:8000 maps port 8000 from the container to port 8000 on the host
# --name gives the container a name for easy reference
# -d runs the container in detached mode (in the background)
docker run -p 8000:8000 --name camera-ingestor -d camera-data-ingestor

echo "Camera Data Ingestor API is running at http://localhost:8000"
echo "To view logs: docker logs camera-ingestor"
echo "To stop the container: docker stop camera-ingestor"