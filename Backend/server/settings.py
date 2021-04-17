"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
import os, json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
secret_file = os.path.join(BASE_DIR, 'secrets.json') # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")
PRONUNCIATION_API_KEY = get_secret("PRONUNCIATION_API_KEY")
GRAMMARBOT_API_KEY = get_secret("GRAMMARBOT_API_KEY")
MS_API_KEY = get_secret("MS_API_KEY")
MSVS_API_KEY = get_secret("MSVS_API_KEY")
MSTR_API_KEY = get_secret("MSTR_API_KEY")
GRAMMAR_API_KEY = get_secret("GRAMMAR_API_KEY")



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'Accounts',
    'Notes',
    'Words',
    'Stats',
    'AI',

    'drf_yasg',
    'django_inlinecss',
    "rest_framework",
    # 'rest_framework_swagger',
    "corsheaders",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DB_NAME = get_secret("DB_NAME")
DB_USER = get_secret("DB_USER")
DB_PASSWORD = get_secret("DB_PASSWORD")
DB_HOST = get_secret("DB_HOST")
DB_PORT = get_secret("DB_PORT")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,               # default로 사용하려는 데이터베이스 명
        'USER': DB_USER,                        # 유저 명
        'PASSWORD': DB_PASSWORD,                    # 비밀번호
        'HOST': DB_HOST,                     # 호스트 명
        'PORT': DB_PORT,                            # 포트 번호 (default 3306)
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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




# 인증메일
EMAIL_HOST = get_secret("EMAIL_HOST")
# 메일을 호스트하는 서버
EMAIL_PORT = get_secret("EMAIL_PORT")
# gmail과의 통신하는 포트
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")
# 발신할 이메일
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")
# 발신할 메일의 비밀번호
EMAIL_USE_TLS = True
# TLS 보안 방법
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL='Accounts.User'

import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=15),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=15),
    'JWT_ALLOW_REFRESH': True, 
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

STATIC_URL = '/api/static/'
# STATIC_DIR = os.path.join(BASE_DIR,'static')
# STATICFILES_DIRS = [
#     STATIC_DIR,
#     ]

STATIC_ROOT = os.path.join(BASE_DIR,'static')
# print('BASE_DIR', BASE_DIR)