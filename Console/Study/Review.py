from Helpers.Table import Table
from Helpers.UserInput import UserInput
from Models.Word import Word


class Review:
    def __init__(self):
        self.word = Word()
        self.user_input = UserInput()
        pass

    # show a word and make a choice
    def show_lesson(self, lesson):
        words = self.word.where("lesson", lesson).select(['title', 'trans']).get()
        Table.set_rows(words.pluck('title')).header(["lesson: " + str(lesson)]).show()
        choice = self.user_input.choice("We are good?", ['Definition', "Yes go to next"])
        if choice == "Definition":
            Table.set_columns(words.pluck('title')).set_columns(words.pluck('trans')).header(
                ['Title', 'Translation']).show()
            self.user_input.show("next?")
            self.show_lesson(int(lesson) + 1)
        else:
            self.show_lesson(int(lesson) + 1)

    # start learning
    def start(self):
        lesson = self.user_input.ask("Witch Lesson? (1-42)")
        self.show_lesson(lesson)
