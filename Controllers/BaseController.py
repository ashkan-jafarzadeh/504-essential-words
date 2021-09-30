from Helpers.View import View


class BaseController:
    @staticmethod
    def error_not_found():
        return View.render("404.html")
