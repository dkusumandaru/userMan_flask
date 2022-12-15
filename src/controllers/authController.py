from flask import render_template, request, redirect, flash, url_for, session
from app import app

import os, sys
sys.path.append('../')
from systems import package
from systems import gateway
from config import API


@app.route('/coffeearea', methods=['GET'])
def coffeearea():
    
    session['AppName'] = package.Package._name
    session['AppVersion'] = package.Package._version
    
    # print(session['userid'])
    userLogAccess = session.get('userid', 'FALSE')
	
    if userLogAccess != 'FALSE':
         return redirect(url_for('dashboard'))
    else:
        return render_template("auth/index.html")


@app.route('/dashboard', methods=['GET'])
def dashboard():
    session['AppName'] = package.Package._name
    session['AppVersion'] = package.Package._version
    userLogAccess = session.get('userid', 'FALSE')
	
    if userLogAccess != 'FALSE':
        return render_template("dashboard/index.html")
    else:
        return redirect(url_for('coffeearea'))


@app.route('/espresso', methods=['POST'])
def espresso():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        loginUrl = API._login
        apiUrl = API._auth
        contents = API._auth_content
        headers = API._auth_header

        contents['username'] = email
        contents['password'] = password
        contents['application'] = session['AppName']

        # resp = requests.post(url, data={}, auth=('user', 'pass'))
        print("hello")
        try:
            print("hello 1")
            getToken = gateway.Gateway.auth(loginUrl, {}, (email, password))

            print(getToken)
            print(getToken["token"])

            print(app.secret_key+" "+getToken["token"])
            headers['x-access-tokens'] = app.secret_key+" "+getToken["token"]
            getAccess = gateway.Gateway.post(apiUrl, contents, headers)

            print(getAccess["data"]["access"])
    
            if getAccess["data"]["access"] == True :
                # print("here")
                session['userid'] = getAccess["data"]["id"]
                session['username'] = getAccess["data"]["username"]
                session['role'] = getAccess["data"]["role"]
                session['application_id'] = getAccess["data"]["application_id"]
                session['role_id'] = getAccess["data"]["role_id"]
                session['access'] = getAccess["data"]["access"]

                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('coffeearea'))
                flash('Login Failed...')
        except Exception as e:
            flash('Login Failed...')
            return redirect(url_for('coffeearea'))


@app.route('/logout')
def logout():
	session.clear()
	return redirect('coffeearea')