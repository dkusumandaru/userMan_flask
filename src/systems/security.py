# import os, sys
# import __init__ as configuration

import sys
sys.path.append('../')
import config as configuration


class BlackJack():
    __access = configuration.Security._data
    _salt = __access['salt']
    _secret = __access['secret_key']
