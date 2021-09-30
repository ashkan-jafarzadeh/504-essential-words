from Models.Word import Word
from Console.Study.Learning import Learning


class Exam(Learning):

    def start(self):
        lesson = self.user_input.ask("Witch Lesson? (1-43)")
        words = self.word.where("lesson", lesson).select(["title", "trans", "id"]).get()

        for word in words.to_list():
            answer = input(word.title + ": ")
            if Word.check_answer(answer):
                print("Correct!")
                print(word.trans, "\n")
            else:
                print("Wrong!")
                print(word.trans, "\n")
