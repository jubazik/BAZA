from api import db
import datetime


class NameCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # date = db.Column(db.Date, default=datetime.datetime.now())
    name = db.Column(db.String(32), unique=False)
    # room = db.Culumn(db.Inreger, unique=False)
    sun = db.relationship('Payments', backref='author', lazy='dinamic')

    def __init__(self, name, room):
        self.name = name
        self.room = room

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "name": self.name,
            'room': self.room

        }
