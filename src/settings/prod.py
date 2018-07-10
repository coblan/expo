from .base import *

DATABASES = {
    'default': {
        'NAME': 'expo_admin',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root123456789',
        'HOST': '127.0.0.1', 
        'PORT': '3306',        
      },
    }

ALLOWED_HOSTS = ['expo.enjoyst.com']