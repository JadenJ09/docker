# Docker Tutorial with Poetry and Miniconda as env managers, FastAPI, Uvicorn, Debugpy and Redis as remote dev setup on Docker containers
This tutorial demonstrates how to use Poetry and Miniconda in Docker to manage dependencies and run your Python applications.

This tutorial demonstrates how to use FastAPI, Redis, and Docker to build a simple web application.

## Project Structure

- `main.py`: This is the main Python script that runs the FastAPI application. It includes two endpoints: one for the root (`/`) and one for hits (`/hits`).

- `Dockerfile`: This file contains the instructions to build a Docker image for the application.


# Using Poetry in Docker
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
CMD ["conda", "run", "-n", "myenv", "python", "./your-script.py"]

