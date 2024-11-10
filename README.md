# f5-nginx-compose-ci

This project sets up an Nginx server using Docker and Docker Compose, featuring a simple HTML page and an error server. It includes automated testing with a Python script and a CI/CD pipeline configured with GitHub Actions.

## Features

- Nginx server running in a Docker container
- Docker Compose for orchestration
- Automated testing using Python and `requests`
- CI/CD pipeline using GitHub Actions

## Prerequisites

- Docker installed
- Docker Compose installed

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/OmriPer/f5-nginx-compose-ci.git
    cd f5-nginx-compose-ci
    ```

2. **Copy the environment variables example file:**

    ```bash
    cp .env.example .env
    ```

3. **Build the Docker images:**

    ```bash
    docker compose build
    ```

4. **Run the services:**

    ```bash
    docker compose up -d
    ```

5. **Access the HTML server:**

    Visit `http://localhost:8080` in your web browser.

6. **Access the error server:**

    Visit `http://localhost:8081` to receive a 500 error code.

The tests will verify:

- The HTML server returns the correct content with a 200 status code.
- The error server returns a 500 status code.

## CI/CD Pipeline

The project includes a GitHub Actions workflow that automatically builds the Docker images and runs the tests on each push or pull request to the `main` branch.

## Project Structure

- `nginx/` - Contains the Nginx server configuration and Dockerfile.
- `test/` - Contains the Python test script and Dockerfile.
- `.github/workflows/` - Contains the CI/CD pipeline configuration.
- `docker-compose.yaml` - Defines the services and networks.

## Configuration

Local environment variables are defined in the `.env` file:

```env
HTML_PORT=8080
ERROR_PORT=8081
```

CI\CD environment variables are defined in the `/.github/workflows/cicd.yaml` file:
``` yaml
env:
    HTML_PORT: 8081
    ERROR_PORT: 8082
```