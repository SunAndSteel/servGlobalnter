import ldap
from django_auth_ldap.config import LDAPSearch
import ssl


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-p(e5+^2xg^3k=^32pv6o*n!)$h3yn+1a*@1nt=8hy#ius$a=dz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Tous les sous domaines de hopital.lan seront autorisés à faire
# des requêtes SQL
ALLOWED_HOSTS = ['hospital.lan', '127.0.0.1']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'servGeneral',
    'synchroDB',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'servGeneral.middleware.IPValidationMiddleware',
    'servGeneral.middleware.SQLPermissionMiddleware'
]

ROOT_URLCONF = 'servGeneral.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'servGeneral.wsgi.application'


DB = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': BASE_DIR / 'db.mysql',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LDAP_AUTH_TLS_VERSION = ssl.PROTOCOL_TLSv1_2

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC+1'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = 'srv/web/static'

STATIC_URL = 'static/'

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    'servGeneral.middleware.LDAPBackend',
    'django_python3_ldap.auth.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
]


LDAP_AUTH_URL = "ldap://SERVER-HOPITAL.hopital.lan"
LDAP_AUTH_SEARCH_BASE = "ou=users,dc=hopital,dc=lan"
LDAP_AUTH_USER_FIELDS = {
    "username": "sAMAccountName",
    "email": "mail",
    "first_name": "givenName",
    "last_name": "sn",
}

LOGIN_REDIRECT_URL = '/'
