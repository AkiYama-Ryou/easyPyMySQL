"""
每个tableLine对象代表数据库中的一行数据，可以通过赋值修改数据库中的数据
"""
class TableLine(object):
    def __init__(self, data, condition, pk, db):
        # if type(condition.table_name) == type([]):
        #     raise SyntaxError("抛出一个异常")
        self.db = db
        self.message = condition
        self.data = data
        self.pk = pk
        self.field_name = ""
        self.fields = {}
        # print()

    def __repr__(self):
        # 重载打印方法
        return str(self.data)

    def __getitem__(self, field_name):
        # 选中某字段，可对此字段赋值
        self.field_name = field_name
        return self

    def __lshift__(self, other):
        # 修改此行数据的某字段值
        if type(self.message.table_name) == type([]):
            raise SyntaxError('这行数据来自多表连接查询，无法修改数据。\nthis data was selected by inner join query，can not amend')
        self.fields[self.field_name] = other
        # print()

    def flush(self):
        # 将对此行数据的修改提交到数据库
        SQL = "update {0} set ".format(self.message.table_name)
        values = list(self.fields.values())
        for key in self.fields:
            SQL += key + " = %s, "
        else:SQL = SQL[:-2]
        SQL += " where {0}={1}".format(self.pk, self.data[self.pk])
        self.db.do(SQL, values)

    def unflush(self):
        # 放弃此次修改，类状态重置
        self.fields = {}