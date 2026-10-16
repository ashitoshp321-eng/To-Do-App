# To-Do App Docker Setup

This project is a simple Flask-based To-Do application. It includes a Dockerfile that packages the app into a container so it can run consistently across environments.

## Project Files

- `app.py` - Flask application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker image configuration

## Prerequisites

Make sure you have Docker installed and running on your machine.

- Docker Desktop or Docker Engine
- Terminal or command prompt

## Build the Docker Image

From the project folder, run:

```bash
docker build -t todo-app .
```

This command builds a Docker image named `todo-app` from the current directory using the `Dockerfile`.

## Run the Container

To start the application in a container:

```bash
docker run -d -p 5000:5000 --name todo-app-container todo-app
```

### Parameters explained

- `-d` : run the container in detached mode
- `-p 5000:5000` : map port `5000` on your machine to port `5000` inside the container
- `--name todo-app-container` : assign a name to the container
- `todo-app` : the image name created earlier

## Access the App

Open your browser and go to:

```text
http://localhost:5000
```

## Useful Docker Commands

### View running containers

```bash
docker ps
```

### Stop the container

```bash
docker stop todo-app-container
```

### Start the container again

```bash
docker start todo-app-container
```

### Remove the container

```bash
docker rm -f todo-app-container
```

### Remove the image

```bash
docker rmi todo-app
```

### View logs

```bash
docker logs todo-app-container
```

## Notes

The app runs with Flask and is exposed on port `5000` inside the container. The `Dockerfile` uses the official Python base image and installs the dependencies from `requirements.txt` before starting the app.
