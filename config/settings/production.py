import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *  # noqa: F403

DEBUG = False
ALLOWED_HOSTS = ["bin.io"]
STATIC_ROOT = BASE_DIR / "static"

sentry_sdk.init(
    dsn=config("SENTRY_DSN"),  # noqa: F405
    integrations=[
        DjangoIntegration(),
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
