"""
Django settings for cnpm (quanlychungcu) project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv  # <-- Thư viện để đọc file .env
from urllib.parse import urlparse

# === TẢI BIẾN MÔI TRƯỜNG ===
# (Đọc file .env ở thư mục gốc)
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env') # <-- Đọc file .env


# === CẤU HÌNH CSDL TỪ NEON (DATABASE_URL) ===
db_url = os.getenv("DATABASE_URL")

if db_url:
    tmpPostgres = urlparse(db_url)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': tmpPostgres.path.replace('/', ''),
            'USER': tmpPostgres.username,
            'PASSWORD': tmpPostgres.password,
            'HOST': tmpPostgres.hostname,
            'PORT': tmpPostgres.port or 5432, # <-- Tự động lấy port từ URL
            'OPTIONS': {
                'sslmode': 'require', # <-- Quan trọng cho Neon
            },
        }
    }
else:
    # Cấu hình SQLite dự phòng nếu không tìm thấy DATABASE_URL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Quick-start development settings
SECRET_KEY = 'django-insecure-u!6=52=yf34!wk$a%wg8j5mx&f2!mh+=ct+oz+wd-#77v0*y4('
DEBUG = True # Giữ DEBUG = True khi dùng ngrok

# === ALLOWED_HOSTS (RẤT QUAN TRỌNG) ===
ALLOWED_HOSTS = [
    '.ngrok-free.app',
    '127.0.0.1',
    'localhost',
]


# Application definition
# === CÁC APP CỦA BẠN (RẤT QUAN TRỌNG) ===
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Ứng dụng bên thứ ba
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    # Ứng dụng của bạn
    'users',
    'api',
    # 'cnpm', # <-- Tên app này có vẻ là tên project, có thể bạn không cần nó
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # <-- Đã thêm CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'quanlychungcu.urls' # <-- Tên project của bạn là 'quanlychungcu'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'quanlychungcu.wsgi.application' # <-- Tên project của bạn

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    # ... (Giữ nguyên các validators) ...
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# === CÁC CẤU HÌNH QUAN TRỌNG ĐÃ SỬA ===

# 1. Chỉ định Custom User Model
AUTH_USER_MODEL = 'users.CustomUser'

# 2. Cấu hình CORS
CORS_ALLOW_ALL_ORIGINS = True # (OK để test)
CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'ngrok-skip-browser-warning',
]

# 3. Cấu hình Django Rest Framework (để sửa lỗi 403)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}