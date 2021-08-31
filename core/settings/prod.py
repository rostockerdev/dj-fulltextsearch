from decouple import config

from core.settings.base import MIDDLEWARE

from .base import *

###########################################
#        SECRET CONFIGURATION             #
###########################################

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

###########################################
#        DATABASE CONFIGURATION           #
###########################################

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default=5432, cast=int),
    }
}

###########################################
#          WSGI CONFIGURATION             #
###########################################
WSGI_APPLICATION = "core.wsgi.application"


###########################################
#           LOGGING CONFIGURATION         #
###########################################
try:
    from .log_settings import *
except Exception:
    pass
