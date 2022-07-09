from api import Resource, reqparse, db, jsonify, request
from api.models.author import NameCard
from api.models.pay import Payments


class PayResource(Resource):
    def get(self, author_id, pay_id):
        pass

    def put(self, pay_id):
        pass

    def delete(self, pay_id):
        pass


class PaysResource(Resource):
    def get(self):
        pays = Payments.query.all()
        pay = [pay.to_dict() for pay in pays]
        return jsonify(pay)

    def post(self, author_id):
        author = NameCard.query.get(author_id)
        new_pay = request.json
        pay = Payments(author, **new_pay)
        db.session.add(pay)
        db.session.commit()
        return jsonify(pay)
