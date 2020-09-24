from db import DB


class ListModel(DB.Model):

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String)
    words = DB.relationship('WordModel', backref='list')
