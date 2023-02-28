from .base import *

DEBUG = False
SECRET_KEY = os.getenv("APP_SECRET_KEY", 'dj-insecure-@80m8q)xvbro&(z6#x0s^xtdzb3c51dv)6-!n-vnt8(#1x6r=&')
CSRF_TRUSTED_ORIGINS = os.getenv("APP_CSRF_TRUSTED_ORIGINS", 'http://localhost,https://localhost').split(',')
ALLOWED_HOSTS = ['*'] 
try:
    from .local import *
except ImportError:
    pass
