class Collection:
    items: list

    def __init__(self, items=[]):
        self.items = items
        pass

    def __repr__(self):
        dict = {"class": self.__class__, "items": self.to_list()}
        return str(dict)

    def to_list(self):
        return self.items

    def first(self):
        if len(self.items) > 0:
            return self.items[0]
        return {}

    def append(self, item):
        self.items.append(item)

        return self

    def pluck(self, field):
        data = []
        for item in self.items:
            if hasattr(item, field):
                data.append(getattr(item, field))

        return data
