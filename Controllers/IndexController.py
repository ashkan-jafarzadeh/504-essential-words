from Controllers.BaseController import BaseController
from Helpers.View import View
from Libraries.Response import Response
from Models.Word import Word
from Requests.Request import Request


class IndexController(BaseController):
    def index(self):
        return View.render('base.html')

    def lesson(self):
        word = Word()
        lesson = 1
        if Request.get_data('lesson'):
            lesson = Request.get_data('lesson')

        words = word.where("lesson", lesson).get()

        if not words.first():
            return self.error_not_found()

        return View.render('lesson.html', {
            "words": words.to_list(),
            "lesson": words.first().lesson
        })

    def bookmark(self):
        word = Word()
        word = word.where("id", Request.get_data("word")).first()
        word.bookmark(Request.get_data("flag"))
        return Response.json({
            "result": "success",
        })

    def search(self):
        search = Request.get_data('search')
        word = Word()
        words = {}
        if search:
            words = word.where_like("title", search).limit(12).get().to_list()

        return View.render('lesson.html', {"words": words})

    def bookmarks(self):
        word = Word()
        words = word.where("is_bookmarked", 1).get().to_list()

        return View.render('lesson.html', {"words": words})
