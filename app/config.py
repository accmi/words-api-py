import os
from dotenv import load_dotenv


class AppConfig:
    def __init__(self, app):
        load_dotenv()
        self.app = app
        self.USER = os.getenv('POSTGRES_USER')
        self.PASSWORD = os.getenv('POSTGRES_PASSWORD')
        self.DB_NAME = os.getenv('POSTGRES_DB')
        self.DB_HOST = os.getenv('POSTGRES_HOST')
        self.DB_PORT = os.getenv('POSTGRES_PORT')
        self.connection_string = f'postgresql://{self.USER}:{self.PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?sslmode=disable'
        self.SECRET_KEY = os.getenv('SECRET_KEY')
        self.PORT = os.getenv('PORT')
        self.HOST = os.getenv('HOST')

        self.install()

    def install(self):
        self.app.secret_key = self.SECRET_KEY
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.connection_string
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['JWT_AUTH_URL_RULE'] = '/api/signin'
        self.app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
