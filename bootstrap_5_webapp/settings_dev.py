from .settings import *

# Development-specific settings
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Example: use SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# You can add more development-specific settings below

