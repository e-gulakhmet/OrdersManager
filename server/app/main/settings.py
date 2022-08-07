from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-%^#%y*d!zsd@_%xw-3b07(2psnj5o7hfn1mpdw=tfcp!hv3w@&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    'orders.apps.OrdersConfig',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

WSGI_APPLICATION = "main.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'main',
        'USER': 'postgres',
        'PASSWORD': 'main',
        'HOST': 'postgres,localhost',
        'PORT': '5432',
    }
}

TIME_ZONE = "UTC"

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

GOOGLE_DRIVE_SETTINGS_FILE = os.path.join(BASE_DIR, 'google/credentials/google_drive_config.yaml')
GOOGLE_DRIVE_ORDERS_FILE_ID = '1V0-N-URwHuZ6kUYQZU-3rF39kwebkK3tBYex283VlI8'