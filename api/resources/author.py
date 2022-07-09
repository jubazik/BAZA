from api import Resource, reqparse, db, request, jsonify
from api.models.author import NameCard


# GET: '/authors/<int:author_id>'
"""get запрос по id """
class NameCardResource(Resource):
    def get(self, author_id):
        author = NameCard.query.get(author_id)
        if author is None:
            return f"Нет автора с таким id={author_id}", 404
        return author.to_dict()


    def put(self, author_id):
        # parser = reqparse.RequstParser()
        # parser.add_argument('name', required=True)
        # author_data = parser.parse_args()
        author_data = request.json
        author = NameCard.query.get(author_id)
        if author is None:
            return {"Error": f"Author id={author_id} not found"}, 404
        for key, value in author_data.items:
            setattr(author, key, value)

        # author.name = author_data['name']

    """PUT запрос на изменение контрагенты по id  """
    def put(self, author_id):
        """не реализован!!!"""
        # parser = reqparse.RequstParser()
        # parser.add_argument('name', required=True)
        # author_data = parser.parse_args()
        new_author = request.json
        author = NameCard.query.get(author_id)
        if author is None:
            return {"Error": f"Author id={author_id} not found"}, 404
        # author.name = author_data['name']
        for key, value in new_author.items():
            setattr(author, key, value)

        db.session.commit()
        return jsonify( author.to_dict())

        """delete удаление контрагента по id """
    def delete(self, author_id):
        author = NameCard.query.get(author_id)
        db.session.delete(author)
        db.session.commit()
        return f"{author.to_dict()}, успешно удалено"
        # raise NatImplemented("Метод не реализован")



"""get и post запрос на создание и получние всех контрагентов"""

# GET : '/authors'
class NameListCardResource(Resource):
    def get(self):
        authors = NameCard.query.all()
        authors_list = [author.to_dict() for author in authors]
        return authors_list, 200

    def post(self):
        # parser = reqparse.RequstParser()
        # parser.add_argument('name', required=True)
        # authors_data = parser.parse_args()
        author_data = request.json
        author = NameCard(**author_data)
        db.session.add(author)
        db.session.commit()
        return author.to_dict(), 201
