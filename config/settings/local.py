from .base import *  # noqa
from .base import env

DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="WQLUJifhUheqmibrYidbSADzGbhnLEtXBjpJK7bmngDNdZkorPMJdKyl5r1pBxaY",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# Apps
INSTALLED_APPS += ['django_extensions',]

# Media
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
