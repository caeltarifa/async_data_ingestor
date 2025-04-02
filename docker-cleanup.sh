#!/bin/bash

# Stop the container if it's running
docker stop camera-ingestor 2>/dev/null || true

# Remove the container
docker rm camera-ingestor 2>/dev/null || true

echo "Camera Data Ingestor container stopped and removed."