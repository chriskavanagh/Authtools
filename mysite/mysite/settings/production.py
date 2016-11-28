from my.settings.base import *
import dj_database_url
import os
from django.urls import reverse_lazy



DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}



#DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = False