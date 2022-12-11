# import os, sys
# import __init__ as configuration

import sys
sys.path.append('../')
import config as configuration


class Database():
    # print(config._configuration)
    __access = configuration.Config._db
    _connection = 'mysql://'+__access["uname"]+':'+__access["pswd"]+'@'+__access["host"]+':'+__access["port"]+'/'+__access["db"]

    # aprint(_connection)
