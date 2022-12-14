from flask_sqlalchemy import SQLAlchemy
from app import app

from models.user import *
from models.role import *
from models.application import *


db = SQLAlchemy(app)

# class Access(db.Model, User.User, Role.Role, App.App):
class Access(db.Model):
    __tablename__ = 'Access'
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey(User.id))
    userAccess = db.relationship(User, backref=db.backref('user'), lazy=True)
    id_role = db.Column(db.Integer, db.ForeignKey(Role.id))
    roleAccess = db.relationship(Role, backref=db.backref('role'), lazy=True)
    id_app = db.Column(db.Integer, db.ForeignKey(App.id))
    appAccess = db.relationship(App, backref=db.backref('app'), lazy=True)
    is_permited = db.Column(db.Boolean, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False)



    def __repr__(self):
        return "<Name: {}>".format(self.id_user)