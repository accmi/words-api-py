from marshmallow import Schema, fields


class DefinitionSchema(Schema):
    definition = fields.Str()
    partOfSpeech = fields.Str()
    synonyms = fields.List(fields.Str())
    typeOf = fields.List(fields.Str())
    hasTypes = fields.List(fields.Str())
    derivation = fields.List(fields.Str())
    examples = fields.List(fields.Str())
    similarTo = fields.List(fields.Str())
    verbGroup = fields.List(fields.Str())
    entails = fields.List(fields.Str())
    also = fields.List(fields.Str())
    inCategory = fields.List(fields.Str())
