from api import db, date



class NameCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date)
    name = db.Column(db.String(32), unique=False)
    surname = db.Column(db.String(32), nullable=False, server_default='Default')
    room = db.Column(db.Integer, nullable=False, server_default='Default')
    sun = db.relationship('Payments', backref='author', lazy='dynamic')

    def __init__(self, name, surname='Нет записи', room = 'Нет записи'):
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
