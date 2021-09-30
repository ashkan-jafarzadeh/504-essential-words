from Controllers.BaseController import BaseController
from Helpers.StrHelper import StrHelper
from Requests.Request import Request
import re


class Router:
    api = False
    path = ""
    routes = []
    status = 200

    @classmethod
    def register(cls, method: str, route: str, callback: callable, is_api=False):
        match = re.search(r'{(\w+)}', route)
        try:
            param = match.group(1)
        except:
            param = ""

        cls.routes.append({
            "main_route": re.sub(r'{\w+}', '', route),
            "route_pattern": re.sub(r'{\w+}', '.+', route),
            "request_method": method,
            "param": param,
            "controller": callback.split("@")[0],
            "method": callback.split("@")[1],
            "is_api": is_api
        })

    @classmethod
    def route_pattern(cls, route):
        return re.sub(r'{\w+}', '.+', route)
        pass

    @classmethod
    def get(cls, route: str, callback: callable):
        cls.register('GET', route, callback)

    @classmethod
    def post(cls, route: str, callback: str):
        cls.register('POST', route, callback)

    @classmethod
    def get_api(cls, route: str, callback: str):
        cls.register('GET', "/api" + route, callback, True)

    @classmethod
    def post_api(cls, route: str, callback: str):
        cls.register('POST', "/api" + route, callback, True)

    @classmethod
    def call(cls, environ):
        Request.set_from_environ(environ)
        path = environ["PATH_INFO"]

        for route in cls.routes:
            if cls.is_same_route(path, route, environ):
                controller = StrHelper.get_class("Controllers." + route["controller"] + "." + route["controller"])
                method = route["method"]
                cls.api = route["is_api"]
                cls.path = path

                if hasattr(controller, method) and callable(getattr(controller, method)):
                    cls.status = 200
                    return getattr(controller, method)(controller)

        cls.status = 404
        return BaseController.error_not_found()

    @classmethod
    def is_api(cls):
        return cls.api

    @classmethod
    def get_path(cls):
        return cls.path

    @classmethod
    def is_same_route(cls, path, route, environ):
        if route["request_method"] == environ["REQUEST_METHOD"] and bool(re.fullmatch(route['route_pattern'], path)):
            match = re.search(route['main_route'] + "(.+)", path)
            try:
                param = match.group(1)
                Request.set_data(route["param"], param)
            except:
                pass

            return True
        return False
