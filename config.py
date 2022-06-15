from pathlib import Path

BASE_DIR = Path(__file__).parent

# подключаем базу данных
class Config:
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR / 'main.db'}"
    SQLALCHEMY_TRACK_MAODIFICATIONS = False
    DEBUG = True
    PORT = 5000
    SECRET_KEY = 'supeR secret KeyS'
    TEST_DATABASE_URI = F"SQLITE:///{BASE_DIR / 'main.db'}"