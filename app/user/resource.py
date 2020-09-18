from flask_restful import Resource, reqparse
from marshmallow import ValidationError

from .model import UserModel
from .validation import UserCredentials


class SignUp(Resource):
    parser = reqparse.RequestParser()

    def post(self):
        self.parser.add_argument('email')
        self.parser.add_argument('password')

        body = self.parser.parse_args()

        schema = UserCredentials()
        try:
            schema.load(body)
        except ValidationError as error:
            return {"error": error.messages}

        user = UserModel(**body)
        user.hash_password()
        error = user.save()

        if error:
            return {"error": error}, 400

        return {"status": "created"}, 201
