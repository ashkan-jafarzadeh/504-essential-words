import os

from Helpers.Env import Env

host = Env.get('host')
port = Env.get('port')
os.system('gunicorn -b ' + host + ':' + port + ' -w 1 --reload app')
