import os
from dotenv import load_dotenv

# .env 파일을 읽어서 환경변수에 적용
load_dotenv() 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['JOB_DATABASE_NAME'],
        'USER': os.environ['JOB_DATABASE_USER'],
        'PASSWORD': os.environ['JOB_DATABASE_PASSWORD'],
        'HOST': os.environ['JOB_DATABASE_HOST'],
        'PORT': int(os.environ.get('JOB_DATABASE_PORT', '3306')),
        'OPTIONS': {'charset': 'utf8mb4'}
    }
}

SECRET_KEY = os.environ['JOB_SECRET_KEY']