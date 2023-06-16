#!/bin/bash

# Define the image name
IMAGE_NAME="henandog"

# Generate the current date and time as the version
NEW_VERSION=$(date +%Y%m%d%H%M%S)

# Build and run the container
docker build -t $IMAGE_NAME:$NEW_VERSION .
docker run -d --restart=always --name $IMAGE_NAME "$IMAGE_NAME:$NEW_VERSION"
