
import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _  # for multi-language
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] # ['admin.credence.uz', '62.209.129.3'] #[config("ALLOWED_HOST", default="*")]

CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True


CSRF_TRUSTED_ORIGINS = 'admin.credence.uz'  #   config("TRUSTED_ORIGINS", default="127.0.0.1")

CORS_REPLACE_HTTPS_REFERER = True

CSRF_COOKIE_DOMAIN = 'admin.credence.uz' #config("TRUSTED_ORIGINS", default="127.0.0.1")

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    # 'jet.dashboard',
    # 'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'accounts.apps.AccountsConfig',
    'my_works.apps.MyWorksConfig',
    'Tests.apps.TestsConfig',

    'crispy_forms',
    'rest_framework',

    'django_filters',
    'rest_framework.authtoken',
    'corsheaders',
    'phonenumber_field',
    'drf_yasg',
    'whitenoise',
    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_UPLOAD_PATH = "uploads/"
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'Full',
#         'toolbar_Custom': [
#             ['Bold', 'Italic', 'Underline'],
#             ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
#             ['Link', 'Unlink'],
#             ['RemoveFormat', 'Source']
#         ]
#     }
# }
CKEDITOR_CONFIGS = {
 "default": {
 "removePlugins": "stylesheetparser",
 'allowedContent': True,
 'toolbar_Full': [
 ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ],
 ['Image', 'Flash', 'Table', 'HorizontalRule'],
 ['TextColor', 'BGColor'],
 ['Smiley','sourcearea', 'SpecialChar'],
 [ 'Link', 'Unlink', 'Anchor' ],
 [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ],
 [ 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ],
 [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ],
 [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ],
 [ 'Maximize', 'ShowBlocks' ]
],
}
}

#SITE_URL = 'http://credence.uz'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",  # for multi language
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CSRF_USE_SESSIONS = True


ROOT_URLCONF = 'IrrigatsiyaUz.urls'

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
                'django.template.context_processors.i18n',
                'accounts.context_processors.notifications',
               # 'IrrigatsiyaUz.views.my_site_url'
            ],
        },
    },
]

WSGI_APPLICATION = 'IrrigatsiyaUz.wsgi.application'


# JET_THEMES = [
#     {
#         'theme': 'default', # theme folder name
#         'color': '#47bac1', # color of the theme's button in user menu
#         'title': 'Default' # theme title
#     },
#     {
#         'theme': 'green',
#         'color': '#44b78b',
#         'title': 'Green'
#     },
#     {
#         'theme': 'light-green',
#         'color': '#2faa60',
#         'title': 'Light Green'
#     },
#     {
#         'theme': 'light-violet',
#         'color': '#a464c4',
#         'title': 'Light Violet'
#     },
#     {
#         'theme': 'light-blue',
#         'color': '#5EADDE',
#         'title': 'Light Blue'
#     },
#     {
#         'theme': 'light-gray',
#         'color': '#222',
#         'title': 'Light Gray'
#     }
# ]

# JET_SIDE_MENU_COMPACT = True




# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DB_USER=config("DB_USER")
DB_NAME=config("DB_NAME", default="")
DB_PASS=config("DB_PASS", default="")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'), #DB_NAME,
        'HOST': 'localhost',
        'PORT': 5432,
        'USER': config('DB_USER'), #DB_USER,
        'PASSWORD': config('DB_PASS'), #DB_PASS,
    }
}


# DJANGO REST FRAMEWORK
REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': "%Y/%m/%d %H:%M:%S", 
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/


MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_FALLBACK_LANGUAGES = ('en', 'uz', 'ru')
MODELTRANSLATION_PREPOPULATE_LANGUAGES = ('en')

LANGUAGES = (
    ("uz", _('Uzbek')),
    ("ru", _('Russian')),
    ("en", _('English')),
)
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

#  Contains the path list where Django should look into for django.po files for all supported languages
LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

USE_TZ = True


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config("CLOUD_NAME", default="*"),
    'API_KEY': config("API_KEY", default="*"),
    'API_SECRET': config("API_SECRET", default="*"),
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


# EMAIL_CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config("EMAIL_USER", default="a@gmail.com")
EMAIL_HOST_PASSWORD = config("EMAIL_PASS", default="pass111")

LOGIN_URL = '/en/admin/'

LOGOUT_REDIRECT_URL = config("LOGOUT_REDIRECT_URL", default="/")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
