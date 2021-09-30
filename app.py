from Helpers.EnvironParser import EnvironParser
from Requests.Request import Request
from Router import web
from Router.Router import Router
from werkzeug.wrappers import Request as WrapperRequest


# the main app
def application(environ, start_response):
    Request.set_request(WrapperRequest(environ))
    EnvironParser.set(environ)
    web.routing()
    response_body = Router.call(environ)

    if Router.is_api():
        return api_call(start_response, response_body)

    return web_call(start_response, response_body)


def web_call(start_response, response_body):
    response_headers = [('Content-Type', 'text/html')]
    start_response(http_status(Router.status), response_headers)
    return [response_body.encode('UTF-8')]


def api_call(start_response, response_body):
    response_headers = [
        ('Content-Type', "application/json"),
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Request-Method', '*'),
        ('Access-Control-Allow-Headers', 'Authorization, Content-Type'),
    ]

    start_response(http_status(Router.status), response_headers)
    return [response_body]


# get the http status base on Router status
def http_status(status):
    statuses = {
        200: "200 OK",
        404: "404 Not Found",
    }

    return statuses[status] if status in statuses else statuses[400]
