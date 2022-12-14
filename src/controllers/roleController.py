from flask import render_template, request, redirect, flash, url_for
from app import app

import os, sys
sys.path.append('../')

from models.role import db, Role

@app.route('/role/list', methods=['GET'])
def roleList():
    result = Role.query.filter_by(is_deleted=False).all()
    return render_template("role/index.html", data=enumerate(result,1))

@app.route('/role/add', methods=['POST'])
def roleAdd():
    if request.method == 'POST':
        name = request.form['name']
        is_deleted = False
        try:
            role = Role(name=name, is_deleted=is_deleted)
            db.session.add(role)
            db.session.commit()

            flash('Insert successful...')
        except Exception as e:            
            flash('Insert failed!!!')

    return redirect(url_for('roleList'))

@app.route('/role/edit', methods=['POST'])
def roleUpdate():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        try:
            role = Role.query.get(id)
            role.name = name
            db.session.commit()
            flash('Update successful...')
        except Exception as e:
            flash('Update failed!!!')
    return redirect(url_for('roleList'))

@app.route('/role/remove', methods=['POST'])
def roleRemove():
    if request.method == 'POST':
        # name = request.form['name']
        id = request.form['id']
        is_deleted = True
        try:
            role = Role.query.get(id)
            role.is_deleted = is_deleted

            db.session.commit()
            flash('Remove successful...')
        except Exception as e:
            flash('Remove failed!!!')

    return redirect(url_for('roleList')) 