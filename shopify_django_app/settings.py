import os
from shopify_app import *
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ.get('DJANGO_SECRET')

DEBUG = True

ALLOWED_HOSTS = ['pearchace.onrender.com', 'localhost', '127.0.0.1', '.vercel.app', '3.108.104.68','pearchace.up.railway.app', 'ec2-3-108-104-68.ap-south-1.compute.amazonaws.com', '.ngrok-free.app','devbackend.pearchace.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shopify_app.apps.ShopifyAppConfig',
    'home.apps.HomeConfig',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'shopify_app.middleware.LoginProtection',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'shopify_django_app.urls'

CORS_ALLOW_ALL_ORIGINS = True
 
CORS_ALLOWED_ORIGINS = [
    'http://3.108.104.68:80',
    'https://pearch.vercel.app',
    'http://localhost:80',
    'https://b175-49-249-156-158.ngrok-free.app'
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]

CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shopify_app.context_processors.current_shop',
            ],
        },
    },
]

WSGI_APPLICATION = 'shopify_django_app.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.vhqazpyiuprgikpygiig',
        'PASSWORD':'PearchTest@123',
        'HOST':'aws-0-us-east-1.pooler.supabase.com',
        'PORT':'6543',
    }
}

# user = postgres.vhqazpyiuprgikpygiig password=[YOUR-PASSWORD] host=aws-0-us-east-1.pooler.supabase.com port=6543 dbname=postgres
# user= pearchuser , name=pearchdb , password = PearchTest@123 , host=db , port = 5432 

MONGODB_SETTINGS = {
    'db': 'shopify_app', 
    'host': 'mongodb+srv://pearch:pearchpwd@cluster0.6sbdzti.mongodb.net/'
}

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

#celery settings 
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

AUTH_USER_MODEL = 'shopify_app.Client'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SHOPIFY_API_KEY = os.environ.get('SHOPIFY_API_KEY')
SHOPIFY_API_SECRET = os.environ.get('SHOPIFY_API_SECRET')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#     ),
# }

# import datetime
# JWT_AUTH = {
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),  # Set token expiry
#     'JWT_ALLOW_REFRESH': True,
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=14),
#     'JWT_RESPONSE_PAYLOAD_HANDLER': 'your_project.utils.jwt_response_payload_handler',  # Custom response handler
# }

# from datetime import timedelta
# from rest_framework_simplejwt.settings import api_settings

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': True,
#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUTH_HEADER_TYPES': ('Bearer',),
# }

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),  
    'REFRESH_TOKEN_LIFETIME': timedelta(days=28),  
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}



# INSTALLED_APPS += ['storages']

# # AWS S3 Settings
# AWS_ACCESS_KEY_ID = 'your-access-key-id'
# AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
# AWS_STORAGE_BUCKET_NAME = 'your-s3-bucket-name'
# AWS_S3_REGION_NAME = 'your-region'  # e.g., 'us-west-2'
# AWS_S3_SIGNATURE_VERSION = 's3v4'

# # Configure S3 as the default storage for logs
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
