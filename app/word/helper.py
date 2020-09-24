from marshmallow import fields, ValidationError, Schema


class PronunciationSchema(Schema):
    all = fields.Str()


class PronunciationField(fields.Field):
    def _deserialize(
        self,
        value,
        attr,
        data,
        **kwargs
    ):
        if value.get('all', None) or isinstance(value, str):
            return value
        else:
            raise ValidationError('Invalid input type')
