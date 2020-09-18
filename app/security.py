from marshmallow import ValidationError

from user.model import UserModel
from user.validation import UserCredentials


def authenticate(email, password):
    schema = UserCredentials()

    try:
        schema.load({'email': email, 'password': password})
    except ValidationError:
        return

    user = UserModel.get_by_email(email)

    if user and user.check_password(password):
        return user


def identity(payload):
    user_id = payload['identity']

    return UserModel.get_by_id(user_id)
