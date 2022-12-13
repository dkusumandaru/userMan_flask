from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    email = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    passview = db.Column(db.String, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return "<Name: {}>".format(self.name)