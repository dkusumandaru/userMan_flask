from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
# from src.models.Access import Access as acs

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    email = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    passview = db.Column(db.String, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False)
    # access = db.relationship('Access', backref='id_user', lazy=True)

    def __repr__(self):
        return "<Name: {}>".format(self.name)