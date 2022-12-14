from flask import render_template, request, redirect, flash, url_for
from app import app

import os, sys
sys.path.append('../')

from models.application import  db, App

@app.route('/app/list', methods=['GET'])
def appList():
    result = App.query.filter_by(is_deleted=False).all()
    return render_template("application/index.html", data=enumerate(result,1))

@app.route('/app/add', methods=['POST'])
def appAdd():
    if request.method == 'POST':
        name = request.form['name']
        is_deleted = False
        try:
            app = App(name=name, is_deleted=is_deleted)
            db.session.add(app)
            db.session.commit()
            flash('Insert successful...')
        except Exception as e:            
            flash('Insert failed!!!')
    return redirect(url_for('appList'))

@app.route('/app/edit', methods=['POST'])
def appUpdate():
    if request.method == 'POST':
        name = request.form['name']
        id = request.form['id']
        is_deleted = False
        try:
            application = App.query.get(id)
            application.name = name
            db.session.commit()
            flash('Update successful...')
        except Exception as e:
            flash('Update failed!!!')

    return redirect(url_for('appList'))

@app.route('/app/remove', methods=['POST'])
def appRemove():
    if request.method == 'POST':
        # name = request.form['name']
        id = request.form['id']
        is_deleted = True
        try:
            application = App.query.get(id)
            application.is_deleted = is_deleted

            db.session.commit()
            flash('Remove successful...')
        except Exception as e:
            flash('Remove failed!!!')

    return redirect(url_for('appList')) 