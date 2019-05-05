from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^p%r8pewn-r7hww6h4n4=z_4_1s(fzgr^+($dzek68mvep)^lz'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

DOMAIN = "localhost:8000"
PYTRACKING_CONFIGURATION = {
    "webhook_url": DOMAIN + "w/",
    "base_open_tracking_url": DOMAIN + "o/",
    "base_click_tracking_url": DOMAIN + "c/",
    "default_metadata": {"pod": "dcs"}
}
INTERNAL_IPS = ['127.0.0.1']

try:
    from .local import *
except ImportError:
    pass

DOMAIN = "localhost:8000"
PYTRACKING_CONFIGURATION = {
    "webhook_url": BASE_DIR + "w/",
    "base_open_tracking_url": DOMAIN + "o/",
    "base_click_tracking_url": DOMAIN + "c/",
    "default_metadata": {"pod": "dcs"}
}
INTERNAL_IPS = ['127.0.0.1']
