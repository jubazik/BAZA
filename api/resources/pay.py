from api import Resource, reqparse, db
from api.models.author import NameCard
from api.models.pay import Payments



class PayResource(Resource):
    def get(self, author_id, pay_id):
        pay = Payments.query.get(pay_id)
        if pay:
            return pay.to_dict(), 200

        return f"Нет записи", 404


    def put(self, pay_id):
        parser = reqparse.RequestParser()
        parser.add_argumen('cash')
        parser.add_argumen('name')
        parser.add_argumen('sum')
        parser.add_argumen('tupe')
        parser.add_argumen('comment')
        new_data = parser.parse_args()
        pay = Payments.query.get(pay_id)
        pay.cash = new_data['cash']
        pay.name = new_data['name']
        pay.sum = new_data['sum']
        pay.type = new_data['type']
        pay.comment = new_data['comment']
        db.session.commit()
        return pay.to_dict()


    def delete(self, pay_id):
        pay = Payments.query.get(pay_id)
        db.session.delete(pay)
        db.session.commit()
        return f'Успешно удалено'










