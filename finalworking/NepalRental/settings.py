from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eirqac_e7v(j^c4(pjo5o1u3o-vsjubn)4pu@e36z=wuhtjo08'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'frontpage'

SESSION_COOKIE_AGE = 86400
CART_SESSION_ID = 'cart'

# Email Configuration for Sending Emails (For Email Verification)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'khatriamit231@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'rwno uyug vogp kfwh'  # Replace with your email password
DEFAULT_FROM_EMAIL = 'khatriamit231@gmail.com'  # Replace with your email

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'bootstrap4',  # Ensure this is included
    'apps.core',
    'apps.blog',
    'ckeditor',
    'apps.registration',
    'apps.home',
    'apps.property',
    'apps.cart',
    'apps.booking',
    'apps.chat',  # Chat app added here

    # Add this line for Django REST Framework
    'rest_framework',  # <-- Django REST framework

    # Add accounts app
    'accounts',  # This is the new app we created for user accounts
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NepalRental.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can add paths to your templates folder here if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.property.context_processors.menu_categories',
                'apps.cart.context_processors.cart',
                # Removed incorrect comma and context processor 'apps.chat' as it's not needed here
            ],
        },
    },
]

# WSGI_APPLICATION = 'NepalRental.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
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

JAZZMIN_SETTINGS = {
    "site_title": "Nepal Rental",
    "site_header": "Nepal Rental",
    "site_brand": "Nepal Rental Admin",
    "site_icon": "admin/images/black.png",
    "site_logo": "admin/images/black.png",
    "site_logo_classes": "img-circle",
    "welcome_sign": "Welcome to the Nepal Rental Admin Panel",
    "copyright": "NepalRental",
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Nepal Rental Homepage", "url": "home", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "users.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "admin.LogEntry": "fas fa-file",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    "related_modal_active": False,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar": "navbar-dark",
}

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'  # Added a leading slash
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'  # Added a leading slash
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
