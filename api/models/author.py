from api import db, date



class NameCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date)
    name = db.Column(db.String(32), nullable=False, serve_default='Default')
    room = db.Column(db.Integer, unique=True)
    sun = db.relationship('Payments', backref='author', lazy='dinamic')

    def __init__(self, name, room = 'нет записи'):
        self.name = name
        self.room = room

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            'room': self.room

        }
