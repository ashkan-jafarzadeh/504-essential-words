from Database.Connection import Connection
import inflect
from Helpers.StrHelper import StrHelper


class DB(Connection):
    table = ""

    def __init__(self):
        super().__init__()

    def called_class(self):
        return self.__class__.__name__

    def get_table(self):
        p = inflect.engine()
        return StrHelper.snake_case(p.plural(self.called_class()))

    def insert_many(self, attributes, values):
        values_str = ""
        for value in range(len(values[0])):
            values_str += "%s,"
        query = "INSERT INTO " + self.get_table() + " (" + ",".join(attributes) + ") VALUES(" + values_str.rstrip(
            ',') + ")"

        self.execute_many(query, values).commit()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        return self

    def execute_many(self, query, params):
        self.cursor.executemany(query, params)
        return self

    def commit(self):
        self.db.commit()

    def fetch(self):
        item = self.cursor.fetchone()
        field_names = [i[0] for i in self.cursor.description]
        each = {}
        for key, value in enumerate(item):
            each[field_names[key]] = value

        return each

    def fetch_all(self):
        field_names = [i[0] for i in self.cursor.description]
        items = self.cursor.fetchall()
        result = []
        for k, item in enumerate(items):
            each = {}
            for key, value in enumerate(item):
                each[field_names[key]] = value
            result.append(each)

        return result
