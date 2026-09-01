from datetime import timedelta
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///mydb.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "3456e78riowejhwgytr67y8uijdfkhyugruh"
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)  # session TTL