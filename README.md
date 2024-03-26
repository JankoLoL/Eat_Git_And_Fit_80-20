# Eat Git And Fit - Web Application

## Overview
It's a web application that offers a collection of healthy recipes.
Inspired by the model 80/20 which means healthy but not a strict diet.
It's a place where you can find recipes according to meal type, occasion, region, or ingredients.
For registered and logged-in users, there are additional features,
including the ability to add, save, and edit their own recipes.

## Requirements
- asgiref==3.6.0
- crispy-bootstrap5==2023.10
- Django==4.2.1
- django-crispy-forms==2.1
- django-widget-tweaks==1.5.0
- iniconfig==2.0.0
- packaging==23.1
- pillow==10.2.0
- pluggy==1.0.0
- psycopg2-binary==2.9.6
- pytest==7.3.1
- python-decouple==3.8
- pytz==2023.3.post1
- router==0.1
- sqlparse==0.4.4

## How to Install and Run Eat_Git_And_Fit_80-20

### Prerequisites
- Python 3.x should be installed on your system.
- PostgreSQL database should be installed and running.
- Virtual environment (optional but recommended).
- Docker and Docker Compose (for Docker setup).

### Installation
1. **Clone the repository** to your local machine (or download the .zip file and extract it):
    ```bash
    git clone https://github.com/JankoLoL/Eat_Git_And_Fit_80-20.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd Eat_Git_And_Fit_80-20
    ```
3. **(Optional) Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```
4. **Install the project dependencies** using pip:
    ```bash
    pip install -r requirements.txt
    ```

### Database Configuration (Local Setup)
- Create a PostgreSQL database for the project.
- Update the database settings in the `.env` file located in the project's root directory with your PostgreSQL database credentials and other configuration options.
- **Important**: Ensure sensitive information like passwords is not included in the repository.

### Running the Project Locally
1. **Apply database migrations** to set up the necessary tables in the database:
    ```bash
    python manage.py migrate
    ```
2. **Start the development server**:
    ```bash
    python manage.py runserver
    ```
3. Open your web browser and go to http://localhost:8000 to access the Eat Git And Fit 80-20 application.

## Docker Setup and Usage

### Building and Running with Docker
- Ensure Docker and Docker Compose are installed on your system.
- Create a `.env` file in the project root with the necessary environment variables:
    ```plaintext
    DEBUG=True
    DB_NAME=eat_fit_db
    DB_USER=postgres
    DB_PASSWORD=yourpassword
    SECRET_KEY=yoursecretkey
    ```
- To **build and start the containers**, run:
    ```bash
    docker-compose up --build
    ```
- The application should now be accessible at http://localhost:8000. Django and any services defined in `docker-compose.yml` will be running in Docker containers.

### Note on Database in Docker
- If using Docker to run PostgreSQL, ensure the `db` service is correctly configured in your `docker-compose.yml`. For local PostgreSQL setup, adjust `DB_HOST` in your `.env` file to point to `localhost` or `host.docker.internal` if accessing the host PostgreSQL from Docker.

---

**Author: Adam Chrzanowski**
