#!/bin/bash

# Define the container name and image name
CONTAINER_NAME="henandog"
IMAGE_NAME="henandog"

# Check if container exists and if so, stop and remove it
if docker ps -a --format "{{.Names}}" | grep -q "$CONTAINER_NAME"; then
    docker stop "$CONTAINER_NAME"
    docker rm "$CONTAINER_NAME"
fi

# Delete the image(s) with the repository name
IMAGE_IDS=($(docker images --format "{{.ID}}" --filter "reference=$IMAGE_NAME:*"))
if [ ${#IMAGE_IDS[@]} -gt 0 ]; then
    docker rmi "${IMAGE_IDS[@]}"
fi
