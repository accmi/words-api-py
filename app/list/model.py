from db import DB
from sqlalchemy.exc import IntegrityError


class ListModel(DB.Model):
    __tablename__ = 'list'

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String)
    words = DB.relationship('WordModel', backref='list')

    def __init__(self, name):
        self.name = name

    def json(self):
        print(self.words)
        return {'name': self.name, 'id': self.id, 'words': [word.json() for word in self.words.all()]}

    def save(self):
        try:
            DB.session.add(self)
            DB.session.commit()
            return self.id, None
        except IntegrityError as err:
            DB.session.rollback()
            return None, err.statement, 500
