from flask import render_template, request, redirect, flash, url_for
from flask_hashing import Hashing
from app import app

import os, sys
sys.path.append('../')
from models.access import db, Access
from systems import security
from helpers.generator import generator

hashing = Hashing(app)

@app.route('/access/list', methods=['GET'])
def accessList():
    result = Access.query.filter_by(is_deleted=False).all()
    print(result)
    return render_template("access/index.html", data=enumerate(result,1))

@app.route('/access/add', methods=['POST'])
def accessAdd():
    if request.method == 'POST':
        id_user = request.form['user']
        id_role = request.form['role']
        id_app = request.form['app']
        is_permited = True
        is_deleted = False
        try:
            access = Access(id_user=id_user, id_role=id_role, id_app=id_app, is_permited=is_permited, is_deleted=is_deleted)
            db.session.add(access)
            db.session.commit()

            flash('Insert successful...')
        except Exception as e:
            flash('Insert failed!!!')

    return redirect(url_for('accessList'))

@app.route('/access/edit', methods=['POST'])
def accessUpdate():
    if request.method == 'POST':
        id_user = request.form['user']
        id_role = request.form['role']
        id_app = request.form['app']
        is_permited = request.form['permited']
        id = request.form['id']
        try:
            access = Access.query.get(id)
            access.id_user = id_user
            access.id_role = id_role
            access.id_app = id_app
            access.is_permited = is_permited
            db.session.commit()
            flash('Update successful...')
        except Exception as e:
            flash('Update failed!!!')
    return redirect(url_for('accessList'))


@app.route('/access/remove', methods=['POST'])
def accessRemove():
    if request.method == 'POST':
        # name = request.form['name']
        id = request.form['id']
        is_deleted = True
        try:
            access = Access.query.get(id)
            access.is_deleted = is_deleted

            db.session.commit()
            flash('Remove successful...')
        except Exception as e:
            flash('Remove failed!!!')

    return redirect(url_for('accessList')) 