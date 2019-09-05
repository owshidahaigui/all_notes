SQL 注入是非常常见的一种网络攻击方式，主要是通过参数来让 mysql 执行 sql 语句时进行预期之外的操作。

```Python
import pymysql

sql = 'SELECT count(*) as count FROM user WHERE id = ' + str(input['id']) + ' AND password = "' + input['password'] + '"'
cursor = dbclient.cursor(pymysql.cursors.DictCursor)
cursor.execute(sql)
count = cursor.fetchone()
if count is not None and count['count'] > 0:
    print('登陆成功')
```

但是，如果传入参数是：

```Python
input['id'] = '2 or 1=1'
```

你会发现，用户能够直接登录到系统中，因为原本 sql 语句的判断条件被 or 短路成为了永远正确的语句。

预防方式一：
pymysql 的 execute 支持参数化 sql，通过占位符 %s 配合参数就可以实现 sql 注入问题的避免。

```Python
import pymysql

sql = 'SELECT count(*) as count FROM user WHERE id = %s AND password = %s'
valus = [input['id'], input['password']]
cursor = dbclient.cursor(pymysql.cursors.DictCursor)
cursor.execute(sql, values)
count = cursor.fetchone()
if count is not None and count['count'] > 0:
    print('登陆成功')
```

这样参数化的方式，让 mysql 通过预处理的方式避免了 sql 注入的存在。
需要注意的是，不要因为参数是其他类型而换掉 %s，pymysql 的占位符并不是 python 的通用占位符。
同时，也不要因为参数是 string 就在 %s 两边加引号，mysql 会自动去处理。