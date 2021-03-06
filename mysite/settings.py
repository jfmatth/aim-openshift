"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
from django.conf.global_settings import LOGIN_REDIRECT_URL
from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# openshift is our PAAS for now.
ON_PAAS = 'OPENSHIFT_REPO_DIR' in os.environ

WWWNAME = ['www.stocksonthebeach.com','stocksonthebeach.com']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

if ON_PAAS:
    SECRET_KEY = os.environ['OPENSHIFT_SECRET_TOKEN']
else:
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = ')_7av^!cy(wfx=k#3*7x+(=j^fzv+ot^1@sh9s9t=8$bu@r(z$'

# SECURITY WARNING: don't run with debug turned on in production!
# adjust to turn off when on Openshift, but allow an environment variable to override on PAAS
DEBUG = not ON_PAAS
DEBUG = DEBUG or 'DEBUG' in os.environ
if ON_PAAS and DEBUG:
    print "*** Warning - Debug mode is on ***"

TEMPLATE_DEBUG = False or 'DEBUG_TEMPLATE' in os.environ

if ON_PAAS:
    ALLOWED_HOSTS = [os.environ['OPENSHIFT_APP_DNS'], socket.gethostname()] + WWWNAME
else:
    ALLOWED_HOSTS = []
    
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'aim',
    'loader',
    'alerter',
    'debug_toolbar',
    'django.contrib.humanize',
    'users',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

# JFM, removed 1/21/15 due to the way OS maps WGSI stuff.

#WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if ON_PAAS:
    # jfm, added CONN_MAX_AGE for persistent connections into Postgres.  See https://docs.djangoproject.com/en/1.6/ref/settings/#conn-max-age
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',  
            'NAME':     os.environ['OPENSHIFT_APP_NAME'],
            'USER':     os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
            'PASSWORD': os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
            'HOST':     os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
            'PORT':     os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'],
            'CONN_MAX_AGE':  600,
        }
    }
else:
    # stock django
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi','static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR,"static"),
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)




if ON_PAAS:
    logdir = os.environ['OPENSHIFT_PYTHON_LOG_DIR']
else:
    logdir = BASE_DIR

LOGLEVEL=os.environ.get('LOGLEVEL', 'ERROR')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s :%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'level':LOGLEVEL,
            'class':'logging.FileHandler',
            'filename': logdir + "/application.log",
            'formatter' : 'standard',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console', 'logfile'],
            'level': 'INFO',
            'propagate': False,
        },
        'loader': {
            'handlers': ['logfile', 'mail_admins'],
            'level': 'DEBUG',
        },
        'alerter': {
            'handlers': ['logfile'],
            'level': 'INFO',
        },
        'aim': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },

    }
}

# EMAIL settings
ADMINS = ( ('John', 'john@compunique.com'),)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_USER", None)
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD", None) 

## registration settings
#REGISTRATION_OPEN = True
#ACCOUNT_ACTIVATION_DAYS = 2

# browser settings
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# django toolbar for WSGI
DEBUG_TOOLBAR_PATCH_SETTINGS = False

def returnDEBUG(request):
    return TEMPLATE_DEBUG

DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': 'mysite.settings.returnDEBUG'}

# sites framework
SITE_ID = 1

# django-users2
AUTH_USER_MODEL = 'users.User'
USERS_CREATE_SUPERUSER = False
USERS_SPAM_PROTECTION = True
USERS_REGISTRATION_OPEN = True
USERS_VERIFY_EMAIL = True
USERS_AUTO_LOGIN_ON_ACTIVATION = True

# FTP information
FTPLOGIN = os.getenv("FTPLOGIN", None)
FTPPASS  = os.getenv("FTPPASS", None)

# Where to send users after a login reset
LOGIN_REDIRECT_URL = reverse_lazy('index')