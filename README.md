# University Api System Based On Django Python DRF Framework

## Overview

This project serves as a template for the Api of the system customized for the university. This Api system allows you to perform ``CRUD`` operations on the data of students, teachers, semesters, and so on. Convenient, Competent and Short, without unnecessary things.

## Installation

To install the project, follow these steps:

1. Clone the repository:

   ```bash
   https://github.com/alexop89056/university-api-system.git
2. Navigate to the project directory:
 
    ```bash
    cd university-api-system
3. Install dependencies:
 
    ```bash
    pip install -r requirements.txt

## Project Structure
- ``/api``: This directory contains the main api endpoints.
- ``/db_seeder``: This directory contains the script that fills the database with data.
- ``/djangoTestApp``: This directory contains the main parent app.

## Usage
- With default django server:

   ```bash
   python manage.py runserver
- With gunicorn http server (``Supports only Linux-like systems``):

   ```bash
   gunicorn djangoTestApp.wsgi:application

## Notes
- File ``settings_local.py`` : Is used to overwrite settings from ``settings.py`` , y ``settings_local.py`` file has more priority.
- The Swagger UI URL is located at ``/schema/swagger-ui``.
- Access to the admin panel via the path ``/admin``, Username: ``admin``, password: ``123``.
- ``Jwt tokens`` are also connected to this project.

  
## License
This project is licensed under the MIT License - see the [main page](https://mit-license.org/) for the details.