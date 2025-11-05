## Installation

1. **Clone the repository** and navigate to the project directory

2. **Install dependencies**:
    pip install -r requirements.txt

## Database Setup
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'cws13',
            'USER': 'postgres',
            'PASSWORD': '123123',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }

## Run migrations
    python manage.py makemigrations
    python manage.py migrate

## Create superuser (optional, for admin access):
    python manage.py createsuperuser

## Usage
    python manage.py runserver
   
    1. Command Line Interface
        python data_manager.py
    2. Web Interface
        Access the web dashboard at http://localhost:8000/
        Access the admin at http://localhost:8000/admin
