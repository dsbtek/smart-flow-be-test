from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0juf)78k)3!7ld0=$yy*qwfak(h%g)ko1smyg!*v93oe+-nk14'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"] 
BASE_URL = 'https://staging.rationaltruth.online'


SERVER_EMAIL='dsbtek@gmail.com'
CONTACT_US_EMAIL='dsbtek@gmail.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# maitrap settings
EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = '6402d9b0f9637b'
EMAIL_HOST_PASSWORD = '12d75331e5df52'
EMAIL_PORT = '2525'
EMAIL_USE_TLS = True 







try:
    from .local import *
except ImportError:
    pass
