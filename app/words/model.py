from db import DB
from sqlalchemy.exc import IntegrityError
from .helper import PronunciationSchema


class WordModel(DB.Model):
    __tablename__ = 'words'

    id = DB.Column(DB.Integer, primary_key=True)
    word = DB.Column(DB.String)
    frequency = DB.Column(DB.Float)
    pronunciation = DB.Column(DB.String)
    results = DB.relationship('DefinitionModel', backref='words')

    def __init__(self, word, frequency, pronunciation):
        self.word = word
        self.frequency = frequency

        if isinstance(pronunciation, str):
            self.pronunciation = pronunciation
        elif isinstance(pronunciation, PronunciationSchema):
            self.pronunciation = pronunciation.get('all', None)
        else:
            self.pronunciation = ''

    def save(self):
        try:
            DB.session.add(self)
            DB.session.commit()
            return self.id, None
        except IntegrityError as err:
            DB.session.rollback()
            return None, err.statement, 500