import sys
sys.path.append('../')
import config as configuration

class Package():
    __access = configuration.Package._data
    _name = __access['name']
    _version = __access['version']