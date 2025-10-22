

from pathlib import Path
import os
import dj_database_url

# =============== BASE PROJECT CONFIG ===============
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-u7xcylsj8p02kg*j0w%7k^z)oicj6ggw5lq!1y%azr7$=rko79'  # default untuk lokal
)

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Ganti ini saat sudah deploy
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.onrender.com', 'pkbmassyariyah.my.id']

# =============== APPS ===============
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my App
    'pkbmapp',
    'pendaftaran',
    # Tambahan admin
    'django_adminlte3',
]

# =============== MIDDLEWARE ===============
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # agar static bisa dilayani di Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pkbm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'pkbm.wsgi.application'

# =============== DATABASE CONFIG ===============
# Gunakan SQLite secara default (local)
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}

# =============== PASSWORD VALIDATION ===============
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =============== INTERNATIONALIZATION ===============
LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Makassar'
USE_I18N = True
USE_TZ = True

# =============== STATIC & MEDIA CONFIG ===============
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise: untuk serving static di production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# =============== SECURITY FOR DEPLOYMENT ===============
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com',
    'https://*.pkbmassyariyah.my.id',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
