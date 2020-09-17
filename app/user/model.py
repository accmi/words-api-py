from db import DB
from flask_bcrypt import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError


class UserModel(DB.Model):
    __tablename__ = 'users'

    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(80), unique=True)
    password = DB.Column(DB.String(128))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def save(self):
        try:
            DB.session.add(self)
            DB.session.commit()
            return None
        except IntegrityError:
            DB.session.rollback()
            return f'the user with email {self.email} already exists'

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()
