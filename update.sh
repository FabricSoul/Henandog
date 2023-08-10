#!/bin/bash
# Define the image name
IMAGE_NAME="henandog"
# Generate the current date and time as the version
NEW_VERSION=$(date +%Y%m%d%H%M%S | tr -d '\r')
# Build a new Docker image version
docker build -t $IMAGE_NAME:$NEW_VERSION .
# Check if container exists and if so, stop and remove it
if [ $(docker ps -a -f name=$IMAGE_NAME | grep -w $IMAGE_NAME | wc -l) -eq 1 ]; then
    docker stop $IMAGE_NAME
    docker rm $IMAGE_NAME
fi
# Delete the old image if no container is using it
OLD_IMAGE=$(docker images --format "{{.Repository}}:{{.Tag}}" | grep $IMAGE_NAME | grep -v $NEW_VERSION)
if [ ! -z "$OLD_IMAGE" ]; then
    if [ $(docker ps -a | grep -w "$OLD_IMAGE" | wc -l) -eq 0 ]; then
        docker rmi "$OLD_IMAGE"
    fi
fi
# Run a new container with the updated image and version
docker run -d --restart=always --name "$IMAGE_NAME" "$IMAGE_NAME:$NEW_VERSION"
