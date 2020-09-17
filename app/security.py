from werkzeug.security import safe_str_cmp
from user.model import UserModel


def authenticate(username, password):
    user = UserModel.get_by_email(username)

    if user and user.check_password(password):
        return user


def identity(payload):
    user_id = payload['identity']

    return UserModel.get_by_id(user_id)
