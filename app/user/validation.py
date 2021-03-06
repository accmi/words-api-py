from marshmallow import fields, Schema, validate


class UserCredentials(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8))
