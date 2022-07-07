from api import db, date
from api.models.author import NameCard


"""Таблица для внесение платежа """

class Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date)
    cash = db.Column(db.TEXT, unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey(NameCard.id))
    sun = db.Column(db.Integer, unique=True)
    type = db.Column(db.String(32), unique=True)
    comment = db.Column(db.Text, unique=True)

    def __init__(self, cash: str, author: NameCard, sun: int, type: str, comment: str):
        self.cash = cash
        self.author_id = author.id
        self.sun = sun
        self.type = type
        self.comment = comment

    def to_dict(self):
        return {
            "id": self.id,
            # "date": self.date,
            "cash": self.cash,
            "name": self.author_id,
            "sun": self.sun,
            "type": self.type,
            "comment": self.comment

        }
