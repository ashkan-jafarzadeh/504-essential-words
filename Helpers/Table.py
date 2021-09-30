from terminaltables import AsciiTable


class Table:
    table_data = {}
    header_data = []
    rows = []
    columns = []
    numeric = True

    def __init__(self):
        pass

    @classmethod
    def fresh_data(cls):
        cls.table_data = {}
        cls.header_data = []
        cls.rows = []
        cls.columns = []
        cls.numeric = True

    @classmethod
    def show(cls):

        columns = {}
        if len(cls.columns) > 0:
            for items in cls.columns:
                for k, column in enumerate(items):
                    if k in columns:
                        columns[k].append(column)
                    else:
                        columns[k] = []
                        columns[k].append(column)
        if len(columns) > 0:
            rows = list(columns.values())
        else:
            rows = cls.rows

        rows = cls.numbered_rows(rows)

        header = cls.header_data
        if len(cls.header_data) == 0:
            for i in range(0, len(rows[0])):
                header.append('-')

        table_data = [
                         header,
                     ] + rows

        table = AsciiTable(table_data)
        print(table.table)
        cls.fresh_data()

    @classmethod
    def header(cls, header=[]):
        cls.header_data = header
        return cls

    @classmethod
    def add_row(cls, row):
        if isinstance(row, dict):
            row = row.items()

        if isinstance(row, str):
            row = [row]

        cls.rows.append(row)
        return cls

    @classmethod
    def set_rows(cls, rows):
        for row in rows:
            cls.add_row(row)

        return cls

    @classmethod
    def set_columns(cls, columns):
        cls.columns.append(columns)

        return cls

    @classmethod
    def numbered_rows(cls, rows):
        if cls.numeric:
            for i, row in enumerate(rows):
                row.insert(0, i + 1)

            cls.header_data.insert(0, 'Num')
        return rows

    @classmethod
    def should_numeric(cls, numeric=True):
        cls.numeric = numeric

        return cls
