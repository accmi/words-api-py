import os

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt import JWT
from flask_restful import Api

from db import DB
from security import authenticate, identity
from user.resource import SignUp

load_dotenv()

USER = os.getenv('POSTGRES_USER')
PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')

connection_string = f'postgresql://{USER}:{PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=disable'

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_AUTH_URL_RULE'] = '/signin'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

bcrypt = Bcrypt(app)
api = Api(app)


@app.before_first_request
def create_table():
    try:
        DB.create_all()
    except ValueError:
        print(ValueError)


# /auth
jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity)

api.add_resource(SignUp, '/signup')


if __name__ == '__main__':
    DB.init_app(app)
    PORT = os.getenv('PORT')
    HOST = os.getenv('HOST')
    app.run(port=PORT, host=HOST, debug=True)
