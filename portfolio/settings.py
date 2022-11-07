from pathlib import Path
import configparser

BASE_DIR = Path(__file__).resolve().parent.parent

config = configparser.ConfigParser()
config.read(BASE_DIR/'conf.ini')

ALLOWED_HOSTS = ['*']


###
# Applications

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'info',
    # 'cloudinary_storage',
    # 'cloudinary',

    'ckeditor',
    'rest_framework',
]

###
# Middleware

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True # If this is used then `CORS_ORIGIN_WHITELIST` will not have any effect
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
                'filter_tags': 'info.templatetags.filter',
            }
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

###
# DATABASE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
###
# MEDIA
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'media'

STATIC_URL = 'static/'
STATIC_ROOT = "var/static"

STATICFILES_DIRS = [BASE_DIR/'static']

###############################
###############################


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGE_CODE = 'FR-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

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


# Email settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True if config['MAIL']['EMAIL_USE_TLS'].lower()=='true' else False
EMAIL_PORT = int(config['MAIL']['EMAIL_PORT'])
EMAIL_HOST_USER = config['MAIL']['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['MAIL']['EMAIL_HOST_PASSWORD']


SECRET_KEY = config['OTHERS']['SECURE_KEY']
DEBUG = True #if config['OTHERS']['DEBUG'].lower()=='true' else False

RECAPTCHA_KEY = config['OTHERS']['RECAPTCHA_KEY']