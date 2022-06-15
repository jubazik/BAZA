from api import Resource, reqparse, db
from api.models.author import NameCard

class NameCardResource(Resource):
    def get(self, author_id):
        author = NameCard.query.get(author_id)
        if author is None:
            return f"Нет автора с таким id={author_id}", 404


