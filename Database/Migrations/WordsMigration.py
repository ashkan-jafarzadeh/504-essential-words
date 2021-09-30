from abc import ABC

from Database.MainMigration import MainMigration


class WordsMigration(MainMigration, ABC):
    def up(self):
        return self.execute("CREATE TABLE words (id INT AUTO_INCREMENT PRIMARY KEY,"
                            " lesson INTEGER (2),"
                            " title VARCHAR(255),"
                            " trans VARCHAR(255),"
                            " definition TEXT NULL,"
                            " definition_trans TEXT NULL,"
                            " first_example TEXT NULL,"
                            " first_example_trans TEXT NULL,"
                            " second_example TEXT NULL,"
                            " second_example_trans TEXT NULL,"
                            " third_example TEXT NULL,"
                            " third_example_trans TEXT NULL,"
                            " story_title TEXT NULL,"
                            " story_title_trans TEXT NULL,"
                            " text TEXT NULL,"
                            " text_trans TEXT NULL,"
                            " is_bookmarked TINYINT(1) DEFAULT 0,"
                            " is_hard TINYINT(1) DEFAULT 0,"
                            " wrong_count INTEGER(4) DEFAULT 0"
                            ")")

    def down(self):
        return self.drop_table("words")
        pass
