import os

class Config:
    DB_USER     = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST     = os.getenv('DB_HOST')
    DB_NAME     = os.getenv('DB_NAME', 'studentdb')

    # Validate required variables
    if not all([DB_USER, DB_PASSWORD, DB_HOST]):
        raise ValueError("Missing required database environment variables")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
