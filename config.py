from dotenv import load_dotenv
import os

# env 파일 로드
load_dotenv()

class Config:
    DB_HOST = os.environ.get('DB_HOST')
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_SCHEMA = os.environ.get('DB_SCHEMA')

    # AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    # AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
    # BUCKET_NAME = os.environ.get('BUCKET_NAME')
