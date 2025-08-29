INSTALLED_APPS = ("django_glide",)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
SECRET_KEY = "top_secret"
USE_TZ = True  # This is here to avoid Django's warning when running tests about the upcoming change in Django 5.0
