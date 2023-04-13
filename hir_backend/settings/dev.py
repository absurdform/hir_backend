from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-v&y)pj94b(*a2hsd$fblh@gudh5%8h^cq+h#*-vd+^vd%kf3i%"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    "default": {
    "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
    "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
    "USER": os.environ.get("SQL_USER", "idy"),
    "PASSWORD": os.environ.get("SQL_PASSWORD", "p.ass.word##"),
    "HOST": os.environ.get("SQL_HOST", "localhost"),
    "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

try:
    from .local import *
except ImportError:
    pass
