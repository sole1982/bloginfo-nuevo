from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587  
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'comision2.grupo4@outlook.es'    
EMAIL_HOST_PASSWORD = 'info2023'

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogdb',
        'USER': 'root',
        'PASSWORD': 'root',


    }
}"""
