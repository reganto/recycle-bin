from .base import *


DEBUG = config("DEBUG", default=False, cast=bool)
STATIC_ROOT = BASE_DIR / "static"
ALLOWED_HOSTS = [config("ALLOWED_HOSTS").split(" ")]
