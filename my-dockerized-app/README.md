# My Dockerized App

This project is a Dockerized application that consists of three main components: a Python web application, a static file server, and a PostgreSQL database. Below are the details for each component and instructions on how to set up and run the project.

## Project Structure

```
my-dockerized-app
├── app                # Python web application
│   ├── Dockerfile     # Dockerfile for the app
│   ├── src            # Source code for the app
│   │   └── app.py     # Main application file
│   ├── requirements.txt # Python dependencies
│   └── README.md      # Documentation for the app
├── static             # Static file server
│   ├── Dockerfile     # Dockerfile for serving static files
│   ├── public         # Public static files
│   │   └── index.html # Main HTML file
│   └── nginx.conf     # Nginx configuration
├── postgres           # PostgreSQL database
│   ├── Dockerfile     # Dockerfile for PostgreSQL
│   └── initdb        # Initialization scripts
│       └── init.sql   # SQL commands to initialize the database
├── docker-compose.yml  # Docker Compose configuration
├── .env               # Environment variables
└── README.md          # Documentation for the entire project
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-dockerized-app
   ```

2. Create a `.env` file in the root directory and set the necessary environment variables for your application, such as database credentials.

### Running the Application

To build and run the application, use Docker Compose:

```
docker-compose up --build
```

This command will build the Docker images for the app, static files, and PostgreSQL, and start the services.

### Accessing the Application

- The web application will be accessible at `http://localhost:5000`.
- The static files will be served at `http://localhost:8080`.

### Stopping the Application

To stop the application, press `CTRL+C` in the terminal where Docker Compose is running, or use:

```
docker-compose down
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.