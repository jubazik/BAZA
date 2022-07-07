from api import db, date


"""Карточка для создания контрагента обязательным аргументом является name room не может быть оденаковым как у всех """

class NameCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date)
    name = db.Column(db.String(32), nullable=False, server_default='Default')
    surname = db.Column(db.String(32), nullable=False, server_default="Default")
    room = db.Column(db.String, unique=True)
    sun = db.relationship('Payments', backref='author', lazy='dynamic')

    def __init__(self, name, surname = 'Нет записи', room = 'нет записи'):
        self.name = name
        self.surname = surname
        self.room = room

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            'room': self.room

        }
