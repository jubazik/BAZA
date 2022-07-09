from api import db, date
from api.models.author import NameCard


"""Таблица для внесение платежа """

class Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date)
    author_id = db.Column(db.Integer, db.ForeignKey(NameCard.id))
    cash = db.Column(db.TEXT, unique=False)
    sun = db.Column(db.Integer, unique=False)
    type = db.Column(db.String(32), nullable=False, server_default='Default')
    comment = db.Column(db.Text, nullable=False, server_default='Default')

    def __init__(self,  author: NameCard, cash: str, sun: int, type= "Наличные", comment = "За цемент"):

        self.author_id = author.id
        self.cash = cash
        self.sun = sun
        self.type = type
        self.comment = comment

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "cash": self.cash,
            "name": self.author_id,
            "sun": self.sun,
            "type": self.type,
            "comment": self.comment

        }
