import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# TODO: create the gke resource from the yml

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('DJANGO_SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'realestate',
    'rest_framework',
    'corsheaders',
    'pages.apps.PagesConfig',
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://0.0.0.0:8000"
]

ROOT_URLCONF = 'realestate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'realestate.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': os.environ.get('DB_NAME'),
#             'USER': os.environ.get('DB_USER'),
#             'PASSWORD': os.environ.get('DB_PASS'),
#             'HOST': os.environ.get('DB_HOST'),
#             'PORT': '5432'
#         }
#     } 

DATABASES = {
    'default': {
    # If you are using Cloud SQL for MySQL rather than PostgreSQL, set
    # 'ENGINE': 'django.db.backends.mysql' instead of the following.
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'realestate',
    'USER': os.getenv('POSTGRES_USER'),
    'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
    'HOST': '127.0.0.1',
    'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# run `python manage.py collectstatic` will copy all the static files from STATICFILES_DIRS here
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
print(STATIC_ROOT)
STATIC_URL = '/static/'
#STATIC_URL = 'http://storage.googleapis.com/polls-storage-bucket/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'realestate/static')
]


# Media folder settings: this media folder correlates with the models file upload fields
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.SUCCESS: 'success'
}

# EMAIL CONFIG
# 'localhost' -> test on local 
# EMAIL_HOST = 'smtp.gamil.com'
# # 25 as default
# EMAIL_PORT = 587
# EMAIL_HOST_USER = str(os.getenv('EMAIL_HOST_USER'))
# EMAIL_HOST_PASSWORD = str(os.getenv('EMAIL_HOST_PASSWORD'))
# EMAIL_USE_TLS = True

# for the production server
try:
    from .local_settings import *
except ImportError:
    pass