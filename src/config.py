import os

class Package():
	_data = {}
	_data['name'] = 'UserMan'
	_data['version'] = '1.0.0'
	_data['release'] = '2022-11-12'
	_data['author'] = 'Ar'

class Config():
	_db = {}
	_db['uname'] = 'root'
	_db['pswd'] = ''
	_db['host'] = 'localhost'
	_db['port'] = '3306'
	_db['db'] = 'm_db'

class Security():
	_data = {}
	_data['salt'] = 'fly me to the moon'
	_data['secret_key'] = '<Hall0 W0rld>'

# print(Config._db)
# print(Config._db['uname'])