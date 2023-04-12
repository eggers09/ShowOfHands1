"""
Django settings for showofhands project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from django.shortcuts import redirect
from django.urls import reverse

# import environ
from dotenv import load_dotenv
import mimetypes

mimetypes.add_type("text/css", ".css", True)

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if "DJANGO_SECRET_KEY" in os.environ:
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
else:
    SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# if "SETTINGS_DEBUG" in os.environ:
#     DEBUG = bool(int(os.environ.get("SETTINGS_DEBUG")))
# else:
DEBUG = True

ALLOWED_HOSTS = ALLOWED_HOSTS = [
    "ShowofHands-dev.us-east-1.elasticbeanstalk.com",
    "ShowofHands-dev-2.us-east-1.elasticbeanstalk.com",
    "localhost",
    "0.0.0.0",
]


# Application definition

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # customs
    "login",
    "posts",
    "users",
    "chat",
    # builtins
    "rest_framework",
    "storages",
    "channels",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "showofhands.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "login", "templates"),
            os.path.join(BASE_DIR, "posts", "templates"),
            os.path.join(BASE_DIR, "showofhands", "templates"),
            os.path.join(BASE_DIR, "chat", "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "showofhands.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# sqlite3
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# postgres eb if available or local:
if "RDS_DB_NAME" in os.environ:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.environ["RDS_DB_NAME"],
            "USER": os.environ["RDS_USERNAME"],
            "PASSWORD": os.environ["RDS_PASSWORD"],
            "HOST": os.environ["RDS_HOSTNAME"],
            "PORT": os.environ["RDS_PORT"],
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.getenv("POSTGRES_DB_NAME"),
            "USER": os.getenv("POSTGRES_USER_NAME"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": os.getenv("POSTGRES_HOST"),
            "PORT": os.getenv("POSTGRES_PORT"),
            "TEST": {
                "NAME": "soh_test",
            },
        }
    }


# Email Settings
# if os.environ.get("DJANGO_TEST"):
#     EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
# else:
#     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
PASSWORD_RESET_TIMEOUT = 1800  # seconds


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "EST"

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "login.Custom_User"


# LOGIN_URL = redirect(reverse("login:login_page"))

LOGIN_URL = "/account/login/"

LOGOUT_REDIRECT_URL = "/home"


# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }


TIME_ZONE = "America/New_York"


if "AWS_ACCESS_KEY_ID" in os.environ:
    DEFAULT_FILE_STORAGE = "showofhands.custom_storage.MediaStorage"

    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")

    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

    # AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

    AWS_S3_FILE_OVERWRITE = False

else:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
STATICFILES_DIRS = (
    str(BASE_DIR) + "/login/static/",
    str(BASE_DIR) + "/posts/static/",
    str(BASE_DIR) + "/showofhands/static/",
    str(BASE_DIR) + "/chat/static/",
)

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"


# updates for chat application
ASGI_APPLICATION = "showofhands.asgi.application"

# TODO: temp fix for inmem chat to work, change later before deploy
## Redis for AWS
# if "USE_REDIS_ENDPOINT" in os.environ and os.environ["USE_REDIS_ENDPOINT"]:
#     CHANNEL_LAYERS = {
#         "default": {
#             "BACKEND": "channels_redis.core.RedisChannelLayer",
#             "CONFIG": {
#                 "hosts": [
#                     ("aws-my-1sw7m30jtg0i4.yxaols.0001.use1.cache.amazonaws.com", 6379)
#                 ],
#             },
#         },
#     }

# else:
CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}
