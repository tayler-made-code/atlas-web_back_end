# Makefile for Node.js Docker Container

# Variables
DOCKER_IMAGE_NAME = unittests_in_js
DOCKER_CONTAINER_NAME = unittests_in_js_container
HOST_DIRECTORY = ./
CONTAINER_DIRECTORY = /unittests_in_js

.PHONY: build run exec stop clean

#Build the docker image
build:
	docker build -t $(DOCKER_IMAGE_NAME) .

# Run the Docker container with the directory binding
run:
	docker run -d --name $(DOCKER_CONTAINER_NAME) -v $(HOST_DIRECTORY):$(CONTAINER_DIRECTORY) $(DOCKER_IMAGE_NAME)

# Execute a command inside the Docker container
exec:
	docker exec -it $(DOCKER_CONTAINER_NAME) bash

# Stop and remove the Docker container
stop:
	docker stop $(DOCKER_CONTAINER_NAME)
	docker rm $(DOCKER_CONTAINER_NAME)

# Clean up Docker images and containers
clean:
	docker stop $(DOCKER_CONTAINER_NAME) || True
	docker rm $(DOCKER_CONTAINER_NAME) || True
	docker rmi $(DOCKER_IMAGE_NAME) || True