from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt import JWT
from flask_restful import Api

from config import AppConfig
from db import DB
from security import authenticate, identity

from routes import Routes

app = Flask(__name__)

bcrypt = Bcrypt(app)
api = Api(app)
config = AppConfig(app)


# migrations
@app.before_first_request
def create_table():
    try:
        DB.create_all()
    except ValueError:
        print(ValueError)


# /auth
jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity)

# routes
routes = Routes(api)


if __name__ == '__main__':
    DB.init_app(app)
    app.run(port=config.PORT, host=config.HOST, debug=True)
