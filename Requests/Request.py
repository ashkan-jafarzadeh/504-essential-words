import json
from urllib.parse import parse_qs


class Request:
    data = {}
    request = {}

    def __init__(self):
        pass

    @classmethod
    def set_data(cls, key, value):
        cls.data[key] = value

    @classmethod
    def set_request(cls, request):
        cls.request = request
        try:
            for key, value in json.loads(request.get_data().decode('utf-8')).items():
                Request.set_data(key, value)
        except:
            pass

    @classmethod
    def set_data_dict(cls, values: dict):
        cls.data = values

    @classmethod
    def get_data(cls, key=None):
        if key:
            if key in cls.data:
                return cls.data[key]
            else:
                return None
        return cls.data

    @classmethod
    def set_from_environ(cls, environ):
        for key, value in parse_qs(environ["wsgi.input"].read().decode("utf-8")).items():
            Request.set_data(key, value[0])
        for key, value in parse_qs(environ['QUERY_STRING']).items():
            Request.set_data(key, value[0])
        pass
