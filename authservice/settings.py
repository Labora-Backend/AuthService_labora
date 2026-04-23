import os
from pathlib import Path
from datetime import timedelta
from decouple import config

# ==============================
# BASE
# ==============================
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ["*"]
=======
>>>>>>> 39b83a661fac86f7890b28cbcdcccc99585cf111

# ==============================
# DJANGO CORE
# ==============================
SECRET_KEY = config("DJANGO_SECRET_KEY")
DEBUG = config("DEBUG", cast=bool, default=False)

ALLOWED_HOSTS = ["*"]


# ==============================
# CORS
# ==============================
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


# ==============================
# APPS
# ==============================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",

    "myapp",
]


# ==============================
# MIDDLEWARE
# ==============================
MIDDLEWARE = [
<<<<<<< HEAD
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
=======
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
>>>>>>> 39b83a661fac86f7890b28cbcdcccc99585cf111
]


# ==============================
# URL / WSGI
# ==============================
ROOT_URLCONF = "authservice.urls"

WSGI_APPLICATION = "authservice.wsgi.application"


# ==============================
# TEMPLATES
# ==============================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ==============================
# DATABASE (SQLite for now)
# ==============================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]


# ==============================
# PASSWORD VALIDATORS
# ==============================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ==============================
# INTERNATIONALIZATION
# ==============================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ==============================
# STATIC & MEDIA
# ==============================
STATIC_URL = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ==============================
# DEFAULTS
# ==============================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "myapp.User"


# ==============================
# DRF
# ==============================
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}


# ==============================
# SIMPLE JWT (RS256 – CORRECT)
# ==============================
SIMPLE_JWT = {
    "ALGORITHM": "RS256",

    "SIGNING_KEY": open(BASE_DIR / "jwt_key" / "private.pem").read(),
    "VERIFYING_KEY": open(BASE_DIR / "jwt_key" / "public.pem").read(),

    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),

    "AUTH_HEADER_TYPES": ("Bearer",),
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'




EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'azph87453@gmail.com'
EMAIL_HOST_PASSWORD = 'xmotbojyzqbttomm'
DEFAULT_FROM_EMAIL = 'Labora <azph87453@gmail.com>'



# ==============================
# EMAIL (DEV)
# ==============================

