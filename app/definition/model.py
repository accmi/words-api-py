from db import DB
from sqlalchemy.exc import IntegrityError


class DefinitionModel(DB.Model):
    __tablename__ = 'definitions'

    id = DB.Column(DB.Integer, primary_key=True)
    value = DB.Column(DB.String)
    part_of_speech = DB.Column(DB.String)
    synonyms = DB.Column(DB.ARRAY(DB.String))
    type_of = DB.Column(DB.ARRAY(DB.String))
    has_types = DB.Column(DB.ARRAY(DB.String))
    examples = DB.Column(DB.ARRAY(DB.String))
    parent_id = DB.Column(DB.Integer, DB.ForeignKey('words.id'))
    selected = DB.Column(DB.Boolean)

    def __init__(self,
                 parent,
                 value,
                 part_of_speech,
                 synonyms,
                 type_of,
                 has_types,
                 examples,
                 selected=False
                 ):
        self.value = value,
        self.part_of_speech = part_of_speech
        self.synonyms = synonyms
        self.type_of = type_of
        self.has_types = has_types
        self.examples = examples
        self.parent_id = parent
        self.selected = selected

    def save(self):
        try:
            DB.session.add(self)
            DB.session.commit()
            return None
        except IntegrityError as err:
            DB.session.rollback()
            return err.statement, 500
