from .base import *
from decouple import config


# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = '_$!c@&mr1l=d(*av^iujxjas4up*2cs1_vc=2+$rw%%ckbpm^n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


LOGGING = {
    'version': 1,
    'loggers': {
        'django': {
            'handlers': ['debug-file', 'info-file', 'error-file'],
            'level': 'DEBUG',
        }
    },
    'handlers': {
        'debug-file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/debug.log',
            'formatter': 'simpleRe',
        },
        'info-file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/info.log',
            'formatter': 'simpleRe',
        },
        'error-file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logs/error.log',
            'formatter': 'simpleRe'
        },
    },
    'formatters': {
        'simpleRe': {
            'format': '{levelname} {asctime} {message} {module} {process:d} {thread:d}',
            'style': '{',
        }
    },
}
