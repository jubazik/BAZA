from api import app, Api
from api.resources.author import NameCardResource, NameListCardResource
from config import Config






api.add_resource(NameCardResource,
                 '/authors/<int:author_id>')
api.add_resource(NameListCardResource,
                 '/authors')


if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)