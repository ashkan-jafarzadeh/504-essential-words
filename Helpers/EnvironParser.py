class EnvironParser:
    environ = {}

    @classmethod
    def set(cls,environ):
        cls.environ = environ

    @classmethod
    def request_method(cls):
        return cls.environ["REQUEST_METHOD"]
