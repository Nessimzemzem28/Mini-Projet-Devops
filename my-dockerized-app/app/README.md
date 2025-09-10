# README for My Dockerized App

# My Dockerized App

This project is a Dockerized application that consists of a Python app, static files served by Nginx, and a PostgreSQL database. Below are the instructions for setting up and running the application.

## Prerequisites

- Docker
- Docker Compose

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd my-dockerized-app
   ```

2. **Build the Docker images:**
   Run the following command to build the images for the app, static files, and PostgreSQL:
   ```bash
   docker-compose build
   ```

3. **Run the application:**
   Start the application using Docker Compose:
   ```bash
   docker-compose up
   ```

4. **Access the application:**
   - The app will be available at `http://localhost:5000`
   - The static files will be served at `http://localhost:80`

## Usage

- The application is built using Python and Flask. You can modify the source code in the `app/src/app.py` file.
- Static files can be modified in the `static/public` directory.

## Database Initialization

The PostgreSQL database is initialized with the SQL commands specified in `postgres/initdb/init.sql`. You can modify this file to set up your database schema and initial data.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.