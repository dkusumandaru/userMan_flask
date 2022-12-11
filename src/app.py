import os
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
from systems import database


app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = database.Database._connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Hell0"
db = SQLAlchemy(app)


from routers import __init__
# from controllers import userController
from controllers import appController

# @app.route('/')
# def index():
# 	print('Hello w')
# 	return 'Hello WOrld'
	



# if __name__ == '__main__':
# 	app.run(debug=True)
# # 
