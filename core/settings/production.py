from . import *

import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['www.erischon.dev', 'erischon.dev', '127.0.0.1', '167.71.39.195', '62.171.165.6']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'), 
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': 'localhost', 
        'PORT': '5432',
    }
}


sentry_sdk.init(
    dsn="https://17e5b37213464b05a42d9f2171116080@o570822.ingest.sentry.io/5741629",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
