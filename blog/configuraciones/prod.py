from .settings import *

DEBUG = False

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587  
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'comision2.grupo4@outlook.es'       
EMAIL_HOST_PASSWORD = 'info2023'