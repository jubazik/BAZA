from api import Resource, reqparse, db, jsonify, request
from api.models.author import NameCard
from api.models.pay import Payments


class PayResource(Resource):
    def get(self, author_id:None, pay_id:None):

        if author_id is None and pay_id is None:
            pays = Payments.query.all()
            return [pay.to_dict() for pay in pays] # Возвращает все записи
        author = NameCard.query.get(author_id)
        if pay_id:
            pays = author.pays.all() # Возвращает все записи автора
            return [pay.to_dict() for pay in pays], 200

        pay = Payments.query.get(pay_id)
        if pay:
            return pay.to_dict(), 200
        return {"Error:", "Нет Записи"}


    def put(self, pay_id):
        pass

    def delete(self, pay_id):
        pass


class PaysResource(Resource):
    def get(self):
        pays = Payments.query.all()
        pay = [pay.to_dict() for pay in pays]
        return pay

    def post(self, author_id):
        author = NameCard.query.get(author_id)
        new_pay = request.json
        pay = Payments(author, **new_pay)
        db.session.add(pay)
        db.session.commit()
        return jsonify(pay.to_dict())
