"""
Django settings for lowfat project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from collections import OrderedDict


URL_SRC = "https://github.com/softwaresaved/lowfat"
VERSION = "1.5.1"

SETTINGS_EXPORT = [
    'URL_SRC',
    'VERSION',
]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_iy7)5@ids_q5m(b4!q$-)ie)&-943zx37$+9-9b#988^*f-+4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_countries',
    'crispy_forms',
    'social_django',
    'dbbackup',
    'constance',
    'constance.backends.database',
    'django_extensions',
    'datetimewidget',
    'simple_history',
    'lowfat',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'lowfat.urls'

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
                'django_settings_export.settings_export',
                'social_django.context_processors.backends',
                'constance.context_processors.config',
                'lowfat.context.site',
                'lowfat.context.maintenance',
            ],
        },
    },
]

WSGI_APPLICATION = 'lowfat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',  # default pipeline
    'social_core.pipeline.social_auth.social_uid',  # default pipeline
    'social_core.pipeline.social_auth.auth_allowed',  # default pipeline
    'social_core.pipeline.social_auth.social_user',  # default pipeline
    'social_core.pipeline.user.get_username',  # default pipeline
    'social_core.pipeline.user.create_user',  # default pipeline
    'social_core.pipeline.social_auth.associate_user',  # default pipeline
    'social_core.pipeline.social_auth.load_extra_data',  # default pipeline
    'social_core.pipeline.user.user_details',  # default pipeline
    'lowfat.auth.wire_profile',
)

SOCIAL_AUTH_GITHUB_KEY = ''
SOCIAL_AUTH_GITHUB_SECRET = ''

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = False

DATE_FORMAT = "l, d F Y"  # British English style
DATETIME_FORMAT = "l, d F Y"  # British English style

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# Stored files
# https://docs.djangoproject.com/en/1.9/ref/settings/#media-url

MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')

# Authentication system
# https://docs.djangoproject.com/en/1.9/topics/auth/default/

LOGIN_URL = '/login/'  # The URL where requests are redirected for login, especially when using the login_required() decorator.
LOGIN_REDIRECT_URL = '/dashboard/'


# Email

# Email backend for development (print on console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Email backend for development (save on file)
# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = '/tmp/lowfat-emails'

# Default email address to use for various automated correspondence from the site manager(s).
DEFAULT_FROM_EMAIL = 'no-reply@software.ac.uk'

# The email address that error messages come from.
SERVER_EMAIL = 'no-reply@software.ac.uk'

# A list of all the people who get code error notifications.
ADMINS = [
    ('admin', 'admin@software.ac.uk'),
    ]

# Subject-line prefix for email messages sent
EMAIL_SUBJECT_PREFIX = ""


# Backup
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {
    'location': os.path.join(BASE_DIR, 'backups'),
}
DBBACKUP_GPG_ALWAYS_TRUST = True
DBBACKUP_GPG_RECIPIENT = ""  # XXX This variable need to be filled for --encrypt or --decrypt work properly.


# Run time variables
# Powered by Constance
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True
CONSTANCE_CONFIG = OrderedDict([
    ("FUNDS_FROM_DEFAULT", (
        "F",
        "Default funds used for expense",
    )),
    ("GRANTS_DEFAULT", (
        "SSI2",
        "Default grant for expenses",
    )),
    ("FELLOWS_MANAGEMENT_EMAIL", (
        "fellows-management@software.ac.uk",
        "Contact address to fellows management staffs",
    )),
    ("STAFFS_EMAIL", (
        "['Software Sustainability Institute <fellows-management@software.ac.uk>']",
        "Contact address of staffs, e.g. ['John <john@example.com>', 'Mary <mary@example.com>']",
    )),
    ("STAFF_EMAIL_NOTIFICATION", (
        False,
        "Notification to staffs by email",
    )),
    ("STAFF_EMAIL_REMINDER", (
        False,
        "Reminder staffs of pending tasks by email",
    )),
    ("DAYS_TO_ANSWER_BACK", (
        3,
        "Days to answer back before receive a email reminder.",
    )),
    ("CLAIMANT_EMAIL_NOTIFICATION", (
        False,
        "Notification to claimant by email",
    )),
    ("MAINTENANCE_DAY", (
        4,
        "Day when maintenance normaly take place",
    )),
    ("MAINTENANCE_HOUR", (
        9,
        "Hour when maintenance normaly take placece",
    )),
    ("FELLOWSHIP_EXPENSES_END_DAY", (
        31,
        "Day deadline that expenses must be submited.",
    )),
    ("FELLOWSHIP_EXPENSES_END_MONTH", (
        3,
        "Month deadline that expenses must be submited.",
    )),
])


# Flatpages

SITE_ID = 1
