# Django settings for bradbury project.
import os

import djcelery
djcelery.setup_loader()

here = lambda * x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

PROJECT_ROOT = here("..")
root = lambda * x: os.path.join(os.path.abspath(PROJECT_ROOT), *x)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ("Kenneth Love", "kenneth@brack3t.com"),
)

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.",
        "NAME": '',
        "USER": '',
        "PASSWORD": '',
        "HOST": '',
        "PORT": '',
    }
}

BROKER_URL = "redis://localhost:6379/9"

TIME_ZONE = "America/Los_Angeles"

LANGUAGE_CODE = "en-us"

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = root("..", "media")

MEDIA_URL = "http://media.ourreadinglist.com/"

STATIC_ROOT = root("..", "static")

STATIC_URL = "http://static.ourreadinglist.com/"

STATICFILES_DIRS = (
    root("assets"),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "bradbury.urls"

WSGI_APPLICATION = "bradbury.wsgi.application"

TEMPLATE_DIRS = (
    root("templates"),
)

DJANGO_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
)
THIRD_PARTY_APPS = (
    "south",
    "djcelery",
    "djcelery_email",
    "registration",
    "braces",
    "crispy_forms",
    "floppyforms",
    "bootstrap-pagination",
)
LOCAL_APPS = (
    "generic",
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}
