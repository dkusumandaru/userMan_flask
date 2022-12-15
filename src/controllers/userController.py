from flask import render_template, request, redirect, flash, url_for
from flask_hashing import Hashing
from app import app

import os, sys
sys.path.append('../')
from models.user import db, User
from systems import security
from helpers.generator import generator

hashing = Hashing(app)

@app.route('/user/list', methods=['GET'])
def userList():
    result = User.query.filter_by(is_deleted=False).all()
    return render_template("user/index.html", data=enumerate(result,1))

@app.route('/user/add', methods=['POST'])
def userAdd():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        passview = generator.id_generator()
        
        salt = str(security.BlackJack._salt)
        print(salt)
        password = hashing.hash_value(passview, salt=salt)
        # password = request.form['password']
        is_deleted = False
        try:
            user = User(name=name, email=email, password=password, passview=passview, is_deleted=is_deleted)
            db.session.add(user)
            db.session.commit()

            flash('Insert successful...')
        except Exception as e:            
            flash('Insert failed!!!')

    return redirect(url_for('userList'))

@app.route('/user/edit', methods=['POST'])
def userUpdate():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        id = request.form['id']
        try:
            user = User.query.get(id)
            user.name = name
            user.email = email
            db.session.commit()
            flash('Update successful...')
        except Exception as e:
            flash('Update failed!!!')
    return redirect(url_for('userList'))

@app.route('/user/change_password', methods=['POST'])
def userUpdatePassword():
    if request.method == 'POST':
        passwordLast = request.form['password']
        passwordNew = request.form['password_new']
        passwordRetype = request.form['password_retype']
        id = request.form['id']

        try:
            user = User.query.get(id)
            if user.password == passwordLast :
                if passwordNew == passwordRetype :
                    user.password = passwordNew
                    db.session.commit()
                    flash('Update successful...')
                else:
                    flash("New Password not match!!")                
            else:
                flash("Password not match!!")

        except Exception as e:
            flash('Update failed!!!')
    return redirect(url_for('userList'))

@app.route('/user/remove', methods=['POST'])
def userRemove():
    if request.method == 'POST':
        # name = request.form['name']
        id = request.form['id']
        is_deleted = True
        try:
            user = User.query.get(id)
            user.is_deleted = is_deleted

            db.session.commit()
            flash('Remove successful...')
        except Exception as e:
            flash('Remove failed!!!')

    return redirect(url_for('userList')) 