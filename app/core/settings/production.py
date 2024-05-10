# core/settings/production.py

from core.settings.base import *


DEBUG = False

ALLOWED_HOSTS = [
    "apps.e-lms.cl",
    "test.e-lms.cl",
    "dev.e-lms.cl",
]

CSRF_TRUSTED_ORIGINS = [
    "https://apps.e-lms.cl",
    "https://test.e-lms.cl",
    "https://dev.e-lms.cl",
]

ADMINS = [
    ("Área de Desarrollo de Software", "ext-dev@lms.cl"),
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
        },
        "logfile": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "/logs/boilerplate.log",
            "maxBytes": 1 * 1024 * 1024,
            "backupCount": 4,
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django": {
            "handlers": ["logfile"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
