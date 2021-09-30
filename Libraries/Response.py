import json


class Response():
    def __init__(self):
        pass

    @classmethod
    def json(cls, data={}):
        return bytes(json.dumps(data), 'utf-8')
