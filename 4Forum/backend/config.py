class Config:
SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost:5432/4forum'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'your-secret-key-here'
UPLOAD_FOLDER = '/opt/4forum/uploads'
MAX_CONTENT_LENGTH = 25 1024 1024 25MB max-size
REDIS_URL = 'redis://localhost:6379/0'