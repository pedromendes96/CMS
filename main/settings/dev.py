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

IS_HTTPS = True if os.environ.get('IS_HTTPS', False) else False
SCHEME = 'https' if IS_HTTPS else 'http'
IM_RUNNING_INSIDE_CONTAINER = os.environ.get(
    'AM_I_IN_A_DOCKER_CONTAINER', False)
if IM_RUNNING_INSIDE_CONTAINER:
    DCS_BASE_URL = "{}://casclient0.dnoticias.pt:8010".format(SCHEME)
    POLL_BASE_URL = "{}://casclient3.dnoticias.pt:8013".format(SCHEME)
else:
    DCS_BASE_URL = "{}://casclient0.dnoticias.pt:9010".format(SCHEME)
    POLL_BASE_URL = "{}://casclient3.dnoticias.pt:9013".format(SCHEME)

DCAS_SESSION_ENDPOINT = urljoin(
    DCS_BASE_URL, 'api/1_0/dcas/__session/validate')
DCAS_SESSION_CACHE_TIMEOUT = 10  # timeout until revalidate SESSION with CAS server
DCS_API_TIMEOUT = 10


CSRF_COOKIE_SECURE = IS_HTTPS
SESSION_COOKIE_SECURE = IS_HTTPS

CAS_SERVER_URL = urljoin(DCS_BASE_URL, 'accounts/')
CAS_LOGIN_AJAX = urljoin(DCS_BASE_URL, 'api/1_0/dcas/login')
CAS_VERSION = '3'
CAS_CREATE_USER = True
CAS_CREATE_USER_WITH_ID = True
# CAS_RETRY_LOGIN = True
CAS_APPLY_ATTRIBUTES_TO_USER = True
CAS_LOGOUT_COMPLETELY = True
CAS_USERNAME_ATTRIBUTE = "email"

CAS_LOGGED_MSG = None
CAS_LOGIN_MSG = None
