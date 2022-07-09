from api import app, api
from api.resources.author import NameCardResource, NameListCardResource
from api.resources.pay import PayResource, PaysResource
from config import Config


api.add_resource(PayResource,
                 '/authors/<int:author_id>/pays/<int:pay_id>')
api.add_resource(PaysResource,
                 '/authors/<int:author_id>/pays')

api.add_resource(NameCardResource,
                 '/authors/<int:author_id>')
api.add_resource(NameListCardResource,
                 '/authors')


if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)