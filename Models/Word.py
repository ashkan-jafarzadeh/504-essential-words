from Models.Model import Model


class Word(Model):
    table = "words"
    title: str
    trans: str
    lesson: int
    word: str
    definition: str
    definition_trans: str
    first_example: str
    first_example_trans: str
    second_example: str
    second_example_trans: str
    third_example: str
    third_example_trans: str
    story_title: str
    story_title_trans: str
    text: str
    text_trans: str

    @classmethod
    def check_answer(cls, answer):
        return cls().select(["COUNT(id)"]).where_like("trans", answer).count()

    def bookmark(self, flag):
        return self.update({"is_bookmarked": flag})
