from marshmallow import Schema, fields
from definition.schema import DefinitionSchema
from .helper import PronunciationField


class SyllablesSchema(Schema):
    count = fields.Int()
    list = fields.List(fields.Str())


class WordSchema(Schema):
    word = fields.Str()
    frequency = fields.Float()
    pronunciation = PronunciationField()
    results = fields.List(fields.Nested(DefinitionSchema))
    syllables = fields.Nested(SyllablesSchema)
