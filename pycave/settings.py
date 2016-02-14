"""
Django settings for pycave project.

Generated by 'django-admin startproject' using Django 1.9c2.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import environ

root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = root()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '4h)*+i@fe=diwbnrwfy3gsd$l=9qo+#an@o=4i#s1=p(((xwi('

SECRET_KEY = env('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*']
# INTERNAL_IPS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pycave.apps.blog',
    'ckeditor', 'ckeditor_uploader'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pycave.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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
    #
    #     {
    #     'BACKEND': 'django.template.backends.jinja2.Jinja2',
    #     'DIRS':  [os.path.join(BASE_DIR, 'templates')],
    # },
]

WSGI_APPLICATION = 'pycave.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': env.db(), # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en_us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

public_root = root.path('public/')
STATIC_ROOT = public_root('static')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = public_root('media')
MEDIA_URL = '/media/'

# log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': "ERROR",
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': root.path('log/')('django-error.log'),
            'maxBytes': 1024000,
            'backupCount': 10,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

###########################
# Other apps conf
###########################

REST_FRAMEWORK = {
    'PAGE_SIZE': 10
}

BLOGPOST_PAGINATE_BY = 10

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_JQUERY_URL = '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
    },
    'blog_ckeditor': {
        'toolbar': 'Full',
    }
}

# DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'
# DEFAULT_FILE_STORAGE = 'django_hashedfilenamestorage.storage.HashedFilenameFileSystemStorage'
# DEFAULT_FILE_STORAGE = 'pycave.libs.storage.HashedFilenameFileSystemStorage'