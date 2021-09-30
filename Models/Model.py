from Database.DB import DB
from Libraries.Collection import Collection


class Model(DB):
    attributes: tuple
    query_where: list
    dict_item: dict
    where_params: list
    query_select: str
    select_params: list
    group_by_query: str
    order_by_query: str
    limit_query: str
    id = 0

    def __init__(self):
        super().__init__()
        self.init_pops()

    def __repr__(self):
        dict = {"model": self.__class__, "table": self.table, "attributes": self.to_dict()}
        return str(dict)

    def init_pops(self):
        self.query_where = []
        self.where_params = []
        self.query_select = "*"
        self.group_by_query = ""
        self.order_by_query = ""
        self.limit_query = ""
        self.select_params = []
        self.dict_item = {}

    def create(self, attributes, values):
        self.insert_many(attributes, values)

    def update(self, values: dict):

        value_params = []
        values_str = ""
        for field, value in values.items():
            value_params.append(value)
            values_str += field + "=%s,"

        where_query = " ".join(self.query_where)
        if self.exists():
            where_query = " WHERE id = %s"
            self.where_params = [self.id]
        query = "UPDATE " + self.get_table() + " SET " + values_str.rstrip(',') + where_query

        self.execute(query, value_params + self.where_params).commit()
        self.init_pops()

    def count(self):
        count = self.select(["COUNT(id) as count"]).first()

        self.init_pops()
        return count.count

    def exists(self):
        return self.id > 0

    def to_dict(self):
        return self.dict_item

    def first(self):
        item = self.execute(self.fetch_query(), self.where_params).fetch()
        self.set_attributes(item)
        self.init_pops()
        return self

    def set_attributes(self, item):
        self.dict_item = item
        for field, value in item.items():
            setattr(self, field, value)

    def get(self):
        result = self.execute(self.fetch_query(), self.where_params).fetch_all()

        data = Collection([])
        # data = []
        for item in result:
            instance = self.__class__()
            instance.set_attributes(item)
            data.append(instance)

        self.init_pops()

        return data

    def sql(self):
        print(self.fetch_query())
        print(self.where_params)
        self.init_pops()
        exit()

    def fetch_query(self):
        return "SELECT " + self.query_select + " FROM " + self.get_table() + " ".join(
            self.query_where) + " " + self.group_by_query + " " + self.order_by_query + " " + self.limit_query

    def select(self, columns: [list, str]):
        if type(columns) == str:
            self.query_select = columns
            self.select_params = [columns]
            return self

        self.select_params = columns
        if len(columns):
            self.query_select = ", ".join(columns)
        return self

    def where(self, column, value=None, operator="=", conjunctor="AND "):
        if len(self.query_where) == 0:
            conjunctor = " WHERE "

        if callable(column):
            new_model = Model()
            column(new_model)

            query = " ".join(new_model.query_where).lstrip(" WHERE ")

            self.query_where.append(conjunctor + "(" + query + ")")
            self.where_params += new_model.where_params

            return self

        self.where_params.append(value)
        self.query_where.append(conjunctor + column + " " + operator + " %s")

        return self

    def or_where(self, column, value=None):
        return self.where(column, value, "=", "OR ")

    def where_like(self, column, value=None, conjunctor="AND "):
        return self.where(column, "%" + str(value) + "%", "like", conjunctor)

    def or_where_like(self, column, value=None, conjunctor="OR "):
        return self.where(column, "%" + str(value) + "%", "like", conjunctor)

    def group_by(self, column):
        self.group_by_query = " GROUP BY " + column
        return self

    def limit(self, limit):
        self.limit_query = " LIMIT " + str(limit)
        return self

    def order_by(self, column, sort="ASC"):
        self.order_by_query = " ORDER BY " + column + " " + sort
        return self

    def order_by_desc(self, column):
        return self.order_by(column, "DESC")
