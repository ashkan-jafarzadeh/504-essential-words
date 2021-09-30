from Helpers.UserInput import UserInput
from Models.Word import Word


class Learning:
    def __init__(self):
        self.word = Word()
        self.user_input = UserInput()
        self.current_word = Word
        pass

    # show a word and make a choice
    def show_word(self, word):
        self.current_word = word
        choices = ["next", "bookmark", "meaning", "definition", "show_examples", "break_learning"]
        choice = self.user_input.choice("\n#" + str(word.id) + " : " + word.title, choices)
        step = self.handle_choice(choice)
        if step == 'repeat':
            self.show_word(word)

    # handle searching title or id
    def search(self):
        search = self.user_input.ask("Give me an Id or Title?")
        word = self.word.where_like('title', search).or_where('id', search).first()
        self.show_word(word)

    # start learning
    def start(self):
        lesson = self.user_input.ask("Witch Lesson? (1-42)")
        words = self.word.where("lesson", lesson).get()
        for word in words.to_list():
            self.show_word(word)

    # handle the choices of start
    def handle_choice(self, choice):
        if choice == "next":
            return "next"
        if hasattr(self, choice) and callable(getattr(self, choice)):
            getattr(self, choice)()
            return "repeat"

    # show meaning of current word
    def meaning(self):
        self.user_input.print(self.current_word.trans, 10, 2, 3)

    # bookmark the current word
    def bookmark(self):
        # self.current_word.bookmark(1)
        self.current_word.update({"is_bookmarked": 1})
        self.user_input.print(self.current_word.title + " bookmarked ", 0, 1, 0)
        pass

    # show the definition of the current word
    def definition(self):
        # show definition
        self.user_input.print(self.current_word.definition, 0, 1, 1)

        # ask what to do
        understand = self.user_input.choice("...", ["Pass", "show trans", "show examples"])
        if understand == "show trans":
            self.user_input.print(self.current_word.definition_trans, 10, 2, 3)
        elif understand == "show examples":
            self.show_examples()
        pass

    # handle break learning
    def break_learning(self):
        another = self.user_input.choice("Where to go?", ["restart", "another word", "exit"])
        if another == "restart":
            self.start()
        elif another == "exit":
            exit()
        else:
            self.search()

    # show the examples of the current word
    def show_examples(self):
        examples = ["first_example", "second_example", "third_example"]
        for example in examples:
            self.user_input.print(getattr(self.current_word, example), 0, 1, 0)
            handle = self.user_input.choice("", ["next", "trans", "break"])
            if handle == "trans":
                self.user_input.print(getattr(self.current_word, example + "_trans"), 10, 1, 1)
                self.user_input.show("")
            elif handle == "break":
                return
