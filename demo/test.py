import time
from easyPyMySQL import mysqlHelper
t1 = time.time()

# 使用配置文件创建数据库连接，析构时自动断开链接
testdb = mysqlHelper("dbConf.xhtml")

# 选择数据库的某张表
test_table1 = testdb.table("test_table1")
test_table2 = testdb.table("test_table2")

# 两表连接查询
select1 = (test_table1['id'] == test_table2 ['id']) & (test_table1['value'] >= 10) & (test_table1['value'] < 1000)
S = select1.SQL()[0]
print(testdb.do(S, select1.SQL()[1]))
# 单表查询
id = test_table1['id']
select2 = (id >= 1) & (id < 200) & ((id < 5) | (id > 100))
print(testdb.do(select2.SQL()[0],select2.SQL()[1]))


# 更简便的查询接口，使用此接口进行单表查询后，可直接复制修改查到的数据
id = test_table1['id']
# select_condition3 = (id == 10) | (test_table2['id'] ==id)
select_condition3 = (id == 10)
datas = test_table1.find(select_condition3)
print(datas)
# 修改数据
one_line_of_data = datas[0]
one_line_of_data['value'] << 2
one_line_of_data['id'] << 10
# 提交修改
datas[0].flush()


# 对某张表新增数据

test_table1.add({'id': 100, 'value': 255})
# test_table1.add([100, 255])


print("总耗时：", time.time() - t1)