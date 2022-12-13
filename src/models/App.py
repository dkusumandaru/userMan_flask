from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class App(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False)

    
    def __repr__(self):
        return "<Name: {}>".format(self.name)