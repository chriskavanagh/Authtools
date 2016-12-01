from __future__ import absolute_import
from .base import *
#from django.urls import reverse_lazy

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'authtools',     # name of d.b. (in postgres).
        'USER': 'postgres',      # name always postgres.
        'PASSWORD': 'alstar01',
        'HOST': 'localhost',     # always set to localhost on postgres.
        'PORT': '',              # Set to empty string for default on postgres.
        'CONN_MAX_AGE': 600,     # number of seconds database connections should persist for
    }
}

DEBUG = True