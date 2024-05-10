from pathlib import Path

from core.functions import get_env_variable


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY", "django-insecure-reemplazame!")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_json_widget",
    "hijack",
    "hijack.contrib.admin",
    "crispy_forms",
    "formtools",
    "crispy_bootstrap5",
    "polls.apps.PollsConfig",
    "cbvpolls.apps.CbvpollsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "hijack.middleware.HijackUserMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": get_env_variable("DJANGO_DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": get_env_variable("DJANGO_DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": get_env_variable("DJANGO_DB_USER", ""),
        "PASSWORD": get_env_variable("DJANGO_DB_PASSWORD", ""),
        "HOST": get_env_variable("DJANGO_DB_HOST", ""),
        "PORT": get_env_variable("DJANGO_DB_PORT", ""),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "es-cl"
TIME_ZONE = "America/Santiago"
USE_I18N = True
USE_L10N = False
USE_TZ = True

DATETIME_FORMAT = "d/m/Y H:i:s"
DATE_FORMAT = "d/m/Y"

STATIC_URL = "static/"
STATIC_ROOT = get_env_variable("DJANGO_STATIC_ROOT", "/static")
STATICFILES_DIRS = ("_staticfiles",)

MEDIA_ROOT = get_env_variable("DJANGO_MEDIA_ROOT", "/media")
MEDIA_URL = get_env_variable("DJANGO_MEDIA_URL", "media/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = get_env_variable("DJANGO_EMAIL_BACKEND", "django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = get_env_variable("DJANGO_EMAIL_HOST", "")
EMAIL_PORT = get_env_variable("DJANGO_EMAIL_PORT", 587)
EMAIL_USE_TLS = get_env_variable("DJANGO_EMAIL_USE_TLS", True)
EMAIL_HOST_USER = get_env_variable("DJANGO_EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = get_env_variable("DJANGO_EMAIL_HOST_PASSWORD", "")

SERVER_EMAIL = get_env_variable("DJANGO_SERVER_EMAIL", "no-reply@e-lms.cl")

SESSION_COOKIE_PATH = get_env_variable("DJANGO_COOKIE_PATH", "/")
CSRF_COOKIE_PATH = get_env_variable("DJANGO_COOKIE_PATH", "/")
LANGUAGE_COOKIE_PATH = get_env_variable("DJANGO_COOKIE_PATH", "/")

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
