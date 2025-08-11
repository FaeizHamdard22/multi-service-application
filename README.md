
# Multi-Service Application (Flask + PostgreSQL + Redis)

This project demonstrates a simple multi-service application using:
- **Flask** as the web application framework
- **PostgreSQL** as the relational database
- **Redis** as the in-memory cache
- **Docker Compose** for orchestration

## Project Structure

```

my-app/
├── app.py                # Flask application code
├── requirements.txt      # Python dependencies
├── Dockerfile            # Image build instructions for Flask app
├── docker-compose.yml    # Multi-service configuration
└── README.md             # Project documentation

````

## Prerequisites

- Docker
- Docker Compose

Ensure Docker and Docker Compose are installed and running on your machine.

## How to Run

1. **Clone the repository**
   ```bash
   git clone git@github.com:FaeizHamdard22/multi-service-application.git
   cd multi-service-application
````

2. **Build and start the containers**

   ```bash
   docker compose up --build
   ```

3. **Access the application**

   * Flask app will be available at:

     ```
     http://localhost:5001
     ```
   * PostgreSQL will run on port `5432`
   * Redis will run on port `6379`

4. **Stop the application**

   ```bash
   docker compose down
   ```

## Notes

* This setup is for development purposes only.
* For production, use a production-ready WSGI server (e.g., Gunicorn) instead of the Flask built-in server.
* Make sure the ports in `docker-compose.yml` are open and not conflicting with other services.
