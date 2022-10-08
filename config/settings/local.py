from .base import *


DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ["bin.io", "localhost", "127.0.0.1"]

INSTALLED_APPS += [
    "django_ptpython",
]
