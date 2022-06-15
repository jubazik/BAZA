from api import app
from config import Config



§

if __name__ == '__main__':
    app.run(debng=Config.DEBUG, port=Config.PORT)