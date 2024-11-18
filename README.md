# Two-Tier Flask Application with Docker and Jenkins

This is a basic two-tier application with a **Flask-based back-end** and a **Dockerized deployment**. The application includes:
- A simple **Flask API** to demonstrate basic functionality.
- A **Dockerized back-end** for easy deployment.
- A **Jenkinsfile** to automate CI/CD pipelines for building and deploying the application.

### Project Structure

The project consists of the following structure:


### Features

- **Flask-based API**: A basic back-end API built using Flask.
- **Health Check Endpoint**: `/health` endpoint for system health monitoring.
- **Greeting API**: `/api/greet` endpoint that returns a custom greeting message.
- **Dockerized Back-End**: The Flask back-end is containerized using Docker for easy deployment.
- **CI/CD Pipeline with Jenkins**: A Jenkins pipeline file that builds, tests, and deploys the Dockerized application.

### Requirements

- **Docker**: For containerizing the application and creating Docker images.
- **Jenkins**: For automating the CI/CD process.
- **GitHub**: For source code hosting and version control.

### Getting Started

Follow these steps to set up the project locally or run it using Docker.

#### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/preshbaba/big.git
cd big
