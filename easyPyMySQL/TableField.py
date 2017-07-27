"""
一个TableField对象代表数据表中的某列
添加持久化支持
"""
class TableField(object):
    """
    返回一个对象代表一行数据
    """
    def __init__(self, table_name, field_name, s = ["",[]]):
        self.table_name = table_name
        self.field_name = field_name
        self.sql = s


    def SQL(self):
        SQL = self.sql[0]
        L = []
        I = 0
        for i, letter in enumerate(SQL):
            if letter == " ":
                I = i
            if letter == ".":
                if SQL[I+1:i] not in L:
                    L.append(SQL[I+1:i])
        s = ''
        for l in L:
            s += l + ","
        else:
            s = s[:-1]
        # self.table_name = []
        return "select * from " + s + " where" + SQL, self.sql[1]

    def change_attr(self, other):
        # 改变self的table_name与field_name值
        if type(self.table_name) != type([]):
            self.table_name = [self.table_name]
        self.table_name.append(other.table_name)
        if type(self.field_name) != type([]):
            self.field_name = [self.field_name]
        self.field_name.append(other.field_name)

    def __eq__(self, other):
        if type(other) == type(self):
            self.sql[0] = " {0}.{1} = {2}.{3}".format(self.table_name, self.field_name, other.table_name, other.field_name)
            self.change_attr(other)
            return TableField(self.table_name, self.field_name, [self.sql[0], []])
        else:
            self.sql[0] = " {0}.{1} = %s".format(self.table_name, self.field_name)
            self.sql[1] = [other]
            return TableField(self.table_name, self.field_name, [self.sql[0], [other]])

    def __ne__(self, other):
        # 不等于!=
        if type(other) == type(self):
            self.sql[0] = " {0}.{1} = {2}.{3}".format(self.table_name, self.field_name, other.table_name, other.field_name)
            self.change_attr(other)
            return TableField(self.table_name, self.field_name, [self.sql[0], []])
        else:
            self.sql[0] = " {0}.{1} != %s".format(self.table_name, self.field_name)
            self.sql[1] = [other]
            return TableField(self.table_name, self.field_name, [self.sql[0], [other]])

    def __lt__(self, other):
        # <
        if type(other) == type(self):
            self.sql[0] = " {0}.{1} = {2}.{3}".format(self.table_name, self.field_name, other.table_name, other.field_name)
            self.change_attr(other)
            return TableField(self.table_name, self.field_name, [self.sql[0], []])
        else:
            self.sql[0] = " {0}.{1} < %s".format(self.table_name, self.field_name)
            self.sql[1] = [other]
            return TableField(self.table_name, self.field_name, [self.sql[0], [other]])

    def __gt__(self, other):
        # >
        if type(other) == type(self):
            self.sql[0] = " {0}.{1} = {2}.{3}".format(self.table_name, self.field_name, other.table_name, other.field_name)
            self.change_attr(other)
            return TableField(self.table_name, self.field_name, [self.sql[0], []])
        else:
            self.sql[0] = " {0}.{1} > %s".format(self.table_name, self.field_name)
            self.sql[1] = [other]
            return TableField(self.table_name, self.field_name, [self.sql[0], [other]])

    def __le__(self, other):
        # <=
        if type(other) == type(self):
            self.sql[0] = " {0}.{1} = {2}.{3}".format(self.table_name, self.field_name, other.table_name, other.field_name)
            self.change_attr(other)
            return TableField(self.table_name, self.field_name, [self.sql[0], []])
        else:
            self.sql[0] = " {0}.{1} <= %s".format(self.table_name, self.field_name)
            self.sql[1] = [other]
            return TableField(self.table_name, self.field_name, [self.sql[0], [other]])

    def __ge__(self, other):
        # >=
        if type(other) == type(self):
            self.sql[0] = " {0}.{1} = {2}.{3}".format(self.table_name, self.field_name, other.table_name, other.field_name)
            self.change_attr(other)
            return TableField(self.table_name, self.field_name, [self.sql[0], []])
        else:
            self.sql[0] = " {0}.{1} >= %s".format(self.table_name, self.field_name)
            self.sql[1] = [other]
            return TableField(self.table_name, self.field_name, [self.sql[0], [other]])

    def __and__(self, other):
        self.sql[0] = self.sql[0] + " and " + other.sql[0]
        self.sql[1].extend(other.sql[1])
        self.change_attr(other)
        return self

    def __or__(self, other):
        self.sql[0] = "( " + self.sql[0] + " or " + other.sql[0] + ")"
        self.sql[1].extend(other.sql[1])
        self.change_attr(other)
        return self

if __name__ == "__main__":
    a = TableField("test_table", "id")

    a = (a >= 1) & ((a < 5) | (a > 100))
    print(a.SQL())




    #
    # class A(object):
    #     def __init__(self, x):
    #         self.x = x
    # class B(object):
    #     def __init__(self, y):
    #         self.y = y
    # a = A(1)
    # print(a.x)
    # b = B(a.x)
    # print(b.y)
    # a.x = 2
    # print(b.y)

