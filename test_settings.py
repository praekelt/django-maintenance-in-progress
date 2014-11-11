import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mip.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = [
    'maintenance_in_progress',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware'
]

ROOT_URLCONF = "maintenance_in_progress.tests.urls"

TEMPLATE_DIRS = (os.path.realpath(os.path.dirname(__file__)) \
    + '/maintenance_in_progress/tests/templates/',)

STATIC_URL = '/static/'
