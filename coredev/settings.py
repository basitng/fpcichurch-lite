import os
from pathlib import Path
import cloudinary_storage
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@ykf248&8re()lk2j$xhvsy%ty2g(zi&1az(pfssv)a3tayg_^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["https://fpcichurch.org","fpcichurch.up.railway.app", "127.0.0.1", "https://admin.fpcichurch.org", "admin.fpcichurch.org", "https://fpcichurch.up.railway.app"]
CSRF_TRUSTED_ORIGINS=["https://fpcichurch.up.railway.app", "https://admin.fpcichurch.org"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "corsheaders",
    'cloudinary_storage',
    'cloudinary',
    'blog',
    'blog_api',
    "pastors",
    "general",
    
    
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "https://fpcichurch.org",
    "https://fpcichurch.up.railway.app",
    "http://localhost:3000",
    "https://admin.fpcichurch.org",
]
ROOT_URLCONF = 'coredev.urls'

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

WSGI_APPLICATION = 'coredev.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'ThpvGROao3cE0yjhYz7K',
        'HOST': 'containers-us-west-166.railway.app',
        'PORT': '7114',
    }
}
X_FRAME_OPTIONS='SAMEORIGIN' # only if django version >= 3.0
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dbmnrmjlm',
    'API_KEY': '727994197945152',
    'API_SECRET': 'dpYf1eEC3qgeaK1qwzJgZOpIlB0'
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSIONS_CLASSES':[
        # allow anyone to access this endpoint
        'rest_framework.permissions.AllowAny',
    ]
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
