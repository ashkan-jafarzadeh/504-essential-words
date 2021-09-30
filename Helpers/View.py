from jinja2 import Environment, FileSystemLoader, select_autoescape

from Models.Word import Word

file_loader = FileSystemLoader(searchpath="./Resources/Views")
env = Environment(loader=file_loader, autoescape=select_autoescape(['html', 'xml']))


class View:
    @staticmethod
    def render(file, params={}):
        template = env.get_template(file)
        return template.render(p=params, lessons=View.load_lessons())

    @staticmethod
    def load_lessons():
        word = Word()
        return word.select("lesson").group_by("lesson").get().pluck("lesson")
