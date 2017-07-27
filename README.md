# easyPyMySQL
python3的简单易用的mysql的ORM,依赖于pymysql。
用此模块跑SQL比直接用pymysql慢，但是开发效率更高，属于消费计算资源换取开发效率。如果你的项目受制与计算资源限制，则不推荐你使用此模块。
此模块的意义在于一定程度上封装了SQL，使得程序员的思维不必在SQL与python之间来回跳跃，减少了写代码的脑力消耗，程序员可以把更多精力集中在业务逻辑上。

</br></br></br>
___________
* 使用pip安装
```
pip install easypymysql
```
___________

* dbconf帮助你连接数据库

将此github项目根目录下demo文件夹中的dbConf.xhtml拷贝到你的项目中，这是连接数据库时使用的配置文件，请在此文件正确地配置你的数据库ip地址、端口号、帐号、密码以及库名。

一个dbconf文件对应mysql中的一个数据库，如需在一个项目中同时连接多个数据库，请拷贝此文件并修改配置信息。

测试数据库结构如下:
![](https://github.com/AkiYama-Ryou/easyPyMySQL/blob/master/demo/testdb.png)
___________

代码示例
===========
* 导入模块:
```
from easyPyMySQL import mysqlHelper
```
* 创建数据库连接:
```
testdb = mysqlHelper("dbConf.xhtml")
```
* 直接使用SQL语句查询，返回普通的python数据结构（列表、字典）:
```
testdb.do(your_SQL_sentence)
```
* 支持参数化查询↓，占位符使用%s。
```
testdb.do(your_SQL_sentence_with_out_values, (values))
```

ORM部分
___________
* 选择数据库的某张表:
```
test_table1 = testdb.table("test_table1")
```
* 选择表中的某个字段
```
id = test_table1['id']
```
* 创建一个查询条件/查询规则/where子句，嗯，你可以随意称呼它
```
select_condition = (id == 10)
```
* SQL()方法将sql语句从查询条件中取出
```
testdb.do(select_condition.SQL()[0],select_condition.SQL()[1])
```
* 使用table对象提供的find方法查询，返回一个列表，列表的每个成员是某个类的实例对象，代表数据库中的一行数据，可以print直接打印此对象查看数据，也可以直接修改此对象来间接地修改数据库
```
datas = test_table1.find(select_condition)
print(datas)
one_line_of_data = datas[0]
one_line_of_data['value'] << 2
one_line_of_data['id'] << 10
datas[0].flush()
```
  修改数据使用符号<<（两个小于号），修改只会生成SQL，而不会立即生效，需要调用此对象的flush()方法提交SQL。

* 使用table类提供的add方法可以想表中新增数据，你可以向add传一个字典，字典的键代表数据库表的键，字典的值代表新增数据的值。你也可以向add传一个列表，省略掉键，而仅仅把值写在列表里，这样做虽然方便，但你必须保证你的列表数据顺序与数据库定义相同，且数量也必须与数据库表的列数相同。
```
test_table1.add({'id': 100, 'value': 255})
test_table1.add([100, 255])
```

__________________
不提供删除语句支持，因为我从没用碰到过需要用delete语句的场景，如需要使用delete遇见请使用do()方法直接运行SQL

have fun
