import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env", override=True)
DEBUG = True
SECRET_KEY = "local-sql-injection-learning-lab"
INSTALLED_APPS = ["lab.apps.LabConfig"]
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
MIDDLEWARE = ["django.middleware.csrf.CsrfViewMiddleware"]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    }
]

# DB 설정
DATABASES = {
    "default": {
        #mysql / .env 파일에서 DB 이름, 사용자 계정, 비밀번호 등을 가져옴
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DATABASE"),
        "USER": os.getenv("MYSQL_USER"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD"),
        "HOST": os.getenv("MYSQL_HOST"),
        "PORT": os.getenv("MYSQL_PORT"),
    }
}

LANGUAGE_CODE = "ko-kr"
TIME_ZONE = "Asia/Seoul"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
