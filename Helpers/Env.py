import re


class Env:
    @staticmethod
    def get(key):
        txt = Env.read_file()
        s = re.findall(key + "\s*=\s*(.+)", txt)
        if len(s) == 0:
            return ""

        return str(s[0]).strip('"').strip("'")

    @staticmethod
    def read_file():
        try:
            file = open('./.env')
            return file.read()
        except FileNotFoundError:
            print(".env not found")
            exit()
