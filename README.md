# Docker Tutorial with Poetry and Miniconda as env managers, FastAPI, Uvicorn, Debugpy and Redis as remote dev setup on Docker containers
This tutorial demonstrates how to use Poetry and Miniconda in Docker to manage dependencies and run your Python applications.

This tutorial demonstrates how to use FastAPI, Redis, and Docker to build a simple web application.

## Project Structure

- `main.py`: This is the main Python script that runs the FastAPI application. It includes two endpoints: one for the root (`/`) and one for hits (`/hits`).

- `Dockerfile`: This file contains the instructions to build a Docker image for the application.

## Docker CLI

### Docker Images
- List Images: To list all Docker images on your system.
```sh
docker images
```

- Pull an Image: To download an image from Docker Hub.
```sh
docker pull nginx
```

- Build an Image: To build a Docker image from a Dockerfile. Run this command in the directory containing your Dockerfile.
```sh
docker build -t my-nginx-image .
```

- Remove an Image: To remove a Docker image from your local system.
```sh
docker rmi my-nginx-image
```

### Docker Containers
Run a Container: To create and start a container from an image.
```sh
docker run --name my-nginx -d -p 8080:80 nginx
```
This command runs an NGINX container named my-nginx, detaches it (-d) to run in the background, and maps port 8080 on the host to port 80 on the container.

- List Containers: To list running containers. Use -a to list all containers (running and stopped).
```sh
docker ps
```

- Stop a Container: To stop a running container.
```sh
docker stop my-nginx
```

- Start a Container: To start a stopped container.
```sh
docker start my-nginx
```

- Remove a Container: To remove a stopped container.
```sh
docker rm my-nginx
```

### Docker Volumes
- Create a Volume: To create a new volume.
```sh
docker volume create my-volume
```

- List Volumes: To list all volumes.
```sh
docker volume ls
```

- Using Volumes: To run a container with a volume attached for persistent data storage.
```sh
docker run -d --name my-nginx -v my-volume:/usr/share/nginx/html nginx
```
This mounts the volume my-volume to /usr/share/nginx/html inside the NGINX container.

- Remove a Volume: To remove an unused volume.
```sh
docker volume rm my-volume
```

### Docker Networking
- Create a Network: To create a user-defined bridge network.
```sh
docker network create my-network
```

- List Networks: To list all networks.
```sh
docker network ls
```

- Run Container with Network: To run a container within a specified network.
```sh
docker run -d --name my-nginx --network my-network nginx
```

- Inspect Network: To view network configuration details.
```sh
docker network inspect my-network
```

- Remove a Network: To remove a network.
```sh
docker network rm my-network
```

### In Container Usage
Executing Commands Inside Containers: To execute a command inside a running container.
```sh
docker exec -it my-nginx bash
```
This command opens a bash shell inside the my-nginx container.

Executing Commands Using Images by Running Containers.
```sh
docker run -it <image_name_or_id> <command>
```

### NGINX Example
Let's say you want to serve a static website using NGINX. You could create a Docker container with a custom NGINX image.

1. Create a directory for your project and place your website's files in it.
2. Create a Dockerfile in the same directory with the following content to use NGINX to serve your site:
```Dockerfile
FROM nginx:alpine
COPY . /usr/share/nginx/html
```

3. Build your Docker image:
```sh
docker build -t my-website .
```

4. Run your container:
```sh
docker run --name my-website-container -d -p 8080:80 my-website
```

5. Your website should now be accessible at http://localhost:8080.
This example demonstrates how to use Docker to easily deploy applications with dependencies, such as an NGINX web server, in a consistent and isolated environment.

<!-- # Using Poetry in Docker
## Dockerfile Example with Poetry:

# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install Poetry
RUN pip install poetry

# Install project dependencies with Poetry
RUN poetry config virtualenvs.create false && poetry install

# Run the app
CMD ["python", "./your-script.py"]


# poetry init | poetry new /directory_name # poetry env use /path/to/python # poetry shell
# pip freeze | awk -F '==' '{print $1}' | xargs poetry add
# poetry build # poetry publish # poetry show --tree


# Using Miniconda in Docker
## Dockerfile Example with Miniconda:

# Start with a base image containing Miniconda
FROM continuumio/miniconda3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Create a Conda environment using the environment.yml file
RUN conda env create -f environment.yml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# Run the app
CMD ["conda", "run", "-n", "myenv", "python", "./your-script.py"] -->


