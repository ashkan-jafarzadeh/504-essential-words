import json


class StrHelper:
    @staticmethod
    def snake_case(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

    @staticmethod
    def dd(dict_var):
        print(json.dumps(dict_var, indent=4, sort_keys=True))
        exit()

    @staticmethod
    def dump(dict_var):
        print(json.dumps(dict_var, indent=4, sort_keys=True))

    @staticmethod
    def get_class(s: str):
        parts = s.split('.')
        module = ".".join(parts[:-1])
        n = __import__(module)
        for comp in parts[1:]:
            n = getattr(n, comp)
        return n
