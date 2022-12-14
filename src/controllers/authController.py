from flask import render_template, request, redirect, flash, url_for, session
from app import app

import os, sys
sys.path.append('../')
from systems import package

@app.route('/coffearea', methods=['GET'])
def coffearea():

    session['AppName'] = package.Package._name
    session['AppVersion'] = package.Package._version

    # result = App.query.filter_by(is_deleted=False).all()
    return render_template("auth/index.html")
