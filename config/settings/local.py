from .base import *   # noqa: F403

DEBUG = config("DEBUG", default=True, cast=bool)  # noqa: F405

ALLOWED_HOSTS = ["bin.io", "localhost", "127.0.0.1"]

INSTALLED_APPS += [     # noqa: F405
    "django_ptpython",
]
