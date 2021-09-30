class UserInput:
    spaces_count: int
    first_blanks_count: int
    last_blanks_count: int

    @staticmethod
    def ask(text, options=()):
        options_text = ": "
        if len(options):
            options_text = " (" + ", ".join(options) + ")\n: "

        return UserInput.input(text + options_text)

    @staticmethod
    def choice(text, choices=()):
        choices_text = ""
        for i, v in enumerate(choices):
            choices_text += "\n [" + str(i) + "] " + str(v)
        result = UserInput.input("\n" + text + "\n" + choices_text + "\n: ")
        if result == "":
            result = 0

        try:
            result = int(result)
        except:
            return UserInput.choice("\nOut of range!", choices)
        if 0 <= result < len(choices):
            return choices[result]

        return UserInput.choice("\nOut of range!", choices)

    @staticmethod
    def show(text):
        return UserInput.input(text + " ")

    @staticmethod
    def input(text):
        try:
            return input(text)
        except:
            exit("\n")

    @staticmethod
    def print(txt, spaces=0, first_blanks=0, last_blanks=0, func='print'):
        text = ''

        for i in range(first_blanks):
            text += "\n"

        for i in range(spaces):
            text += " "
        text += txt
        for i in range(spaces):
            text += " "

        for i in range(last_blanks):
            text += "\n"

        if callable(func):
            func(text)
        else:
            print(text)

    def spaces(self, count):
        self.spaces_count = count

        return self

    def first_blanks(self, count):
        self.first_blanks_count = count

        return self

    def last_blanks(self, count):
        self.last_blanks_count = count

        return self

    def echo(self, txt):
        self.print(txt, self.spaces_count, self.first_blanks_count, self.last_blanks_count)
