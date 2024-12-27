# Recommender System Project - Backend

This README file provides an overview of the backend implementation of the recommender system project. The backend is built using Django and serves as the API for the recommender system.

## Project Structure

The backend consists of the following main components:

- **recommender**: This directory contains the core functionality of the recommender system.
  - `admin.py`: Register models with the Django admin site.
  - `apps.py`: Configuration for the recommender app.
  - `models.py`: Data models for the recommender system.
  - `tests.py`: Test cases for the recommender app.
  - `urls.py`: URL patterns for the recommender app.
  - `views.py`: View functions for handling requests.

- **recommender_system**: This directory contains the main Django project settings and configurations.
  - `settings.py`: Settings and configuration for the Django project.
  - `urls.py`: URL patterns for the entire Django project.
  - `wsgi.py`: WSGI deployment for the Django application.

- **manage.py**: Command-line utility for interacting with the Django project.

- **requirements.txt**: Lists the dependencies required for the Django backend.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd recommender-system-project/backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Server

To start the Django development server, run:
```
python manage.py runserver
```

The server will be available at `http://127.0.0.1:8000/`.

## API Endpoints

The API endpoints for the recommender system can be defined in the `urls.py` files within the `recommender` and `recommender_system` directories. 

## Testing

To run the tests for the recommender app, use:
```
python manage.py test recommender
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.