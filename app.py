from api import app, Api
from config import Config





if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)