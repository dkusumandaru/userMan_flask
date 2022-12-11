import os


class Config():
	_db = {}
	_db['uname'] = 'root'
	_db['pswd'] = ''
	_db['host'] = 'localhost'
	_db['port'] = '3306'
	_db['db'] = 'm_db'


# print(Config._db)
# print(Config._db['uname'])