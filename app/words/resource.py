import os
from flask_restful import Resource, request
from requests import get as request_get, RequestException
from marshmallow import ValidationError
from .schema import WordSchema
from .model import WordModel
from definition.model import DefinitionModel


class Search(Resource):
    def get(self):
        args = request.args
        word = args['search']

        value, err = WordModel.get_word_by_name(word)

        if err:
            return {'error': err}, 400
        elif value:
            try:
                schema = WordSchema()
                res = schema.dump(value)
                return res, 200
            except ValidationError as err:
                return {'error': err.messages}, 500

        return self.request_word(word)

    @staticmethod
    def post():
        json = request.json
        schema = WordSchema()

        try:
            data = schema.load(json)
        except ValidationError as err:
            print(err.valid_data)
            return err.messages, 400

        new_word = WordModel(
            word=data.get('word', None),
            frequency=data.get('frequency', None),
            pronunciation=data.get('pronunciation', None)
        )

        word_id, err = new_word.save()

        if err:
            return {'error': err}, 500

        if word_id:
            for definition in data.get('results', None):
                new_definition = DefinitionModel(
                    parent=word_id,
                    value=definition.get('definition', None),
                    part_of_speech=definition.get('partOfSpeech', None),
                    synonyms=definition.get('synonyms', None),
                    type_of=definition.get('typeOf', None),
                    has_types=definition.get('hasTypes', None),
                    examples=definition.get('examples', None)
                )
                err = new_definition.save()
                if err:
                    return {'error': err}, 500

        return {'message': 'added'}, 201

    @classmethod
    def request_word(cls, word):
        url = f'https://wordsapiv1.p.rapidapi.com/words/{word}'
        headers = {
            'x-rapidapi-host': os.getenv('RAPID_API_HOST'),
            'x-rapidapi-key': os.getenv('RAPID_API_KEY')
        }

        print(f'searching "{word}" in rapid api')

        try:
            res = request_get(url, headers=headers)
            return res.json(), 200
        except RequestException:
            return RequestException.strerror, 400
