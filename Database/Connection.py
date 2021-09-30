import mysql.connector
from mysql.connector import CMySQLConnection
from mysql.connector.cursor_cext import CMySQLCursor

from Helpers.Env import Env


class Connection:
    db = None
    db: CMySQLConnection
    cursor: CMySQLCursor

    def __init__(self, with_database=True):
        if with_database:
            self.set_database()

        self.cursor = self.make_cursor()

    @staticmethod
    def set_database():
        if Connection.db is None:
            Connection.db = mysql.connector.connect(
                host=Env.get("host"),
                user=Env.get("user"),
                password=Env.get("password"),
                database=Env.get("database")
            )

    @classmethod
    def no_database(cls):
        Connection.db = mysql.connector.connect(
            host=Env.get("host"),
            user=Env.get("user"),
            password=Env.get("password")
        )
        return Connection(False)

    def make_cursor(self):
        return self.db.cursor()
