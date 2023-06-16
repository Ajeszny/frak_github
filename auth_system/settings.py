# settings.py
import os

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '7777erik777@gmail.com'
EMAIL_HOST_PASSWORD = 'Lidas131'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
STATIC_URL = '/static/'
INSTALLED_APPS = [
    'django.contrib.staticfiles',
]
ALLOWED_HOSTS = [
    '194.233.168.205'
]
