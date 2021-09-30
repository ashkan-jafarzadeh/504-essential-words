from abc import ABC, abstractmethod

from Database.DB import DB


class MainMigration(ABC):
    def __init__(self):
        self.db = DB()

    @abstractmethod
    def up(self):
        pass

    @abstractmethod
    def down(self):
        pass

    def execute(self, statement):
        self.db.cursor.execute(statement)

    def drop_table(self, table):
        return self.execute("DROP TABLE " + table)
        pass
