import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'gpooi81+)qei(%xrz41@7o05ttx)=su$j$w_t)3m2wtr_-+0c8'

DEBUG = True

ALLOWED_HOSTS = ["www.shortme.com", "shortme.com", "blog.shortme.com"]

ROOT_URLCONF = 'shortme.urls'
ROOT_HOSTCONF = 'shortme.hosts'
DEFAULT_HOST = 'www'
DEFAULT_REDIRECT_URL = "http://www.shortme.com:8000"
PARENT_HOST = 'shortme.com'
HOST_SCHEME = 'http'
HOST_PORT = '8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
