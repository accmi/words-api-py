from flask_restful import Resource, reqparse

from .model import UserModel


class SignUp(Resource):
    @staticmethod
    def post():
        req = reqparse.RequestParser()
        req.add_argument(
            'email',
            type=str,
            required=True,
            location='json',
        )
        req.add_argument(
            'password',
            type=str,
            required=True,
            location='json',
        )
        body = req.parse_args()
        user = UserModel(**body)

        user.hash_password()

        error = user.save()

        if error:
            return {"status": error}, 400

        return {"status": "created"}, 201
