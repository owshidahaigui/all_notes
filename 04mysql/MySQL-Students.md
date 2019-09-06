

# MySQL基础回顾

## **1、数据库概念**

**数据库**

- 存储数据的仓库（逻辑概念，并未真实存在）

**数据库软件**

- 真实软件，用来实现数据库这个逻辑概念

**数据仓库**

- 数据量更加庞大，更加侧重数据分析和数据挖掘，供企业决策分析之用，主要是数据查询，修改和删除很少



## **2、MySQL的特点**

- 关系型数据库
- 跨平台
- 支持多种编程语言（python、java、php）
- 基于磁盘存储，数据是以文件形式存放在数据库目录/var/lib/mysql下

## **3、启动连接**

- 服务端启动 

```mysql
sudo /etc/init.d/mysql start|stop|restart|status
sudo service mysql start|stop|restart|status
```

- 客户端连接

```mysql
mysql -hIP地址 -p3306 -u用户名 -p密码
本地连接可省略 -h 选项
```



## **4、基本SQL命令**

**库管理**

```mysql
    1、查看已有库；
        show databases;
    2、创建库并指定字符集；
        crete database 库名 charset utf8;
        crete database 库名 character set utf8;
        查看库字符集;
        show crete database 库名;
    3、查看当前所在库；
        select database();
    4、切换库；
        use 库名;
    5、查看库中已有表；
        show tables;
    6、删除库；
        drop database 库名;
```

**表管理**

```mysql
    1、创建表并指定字符集；
        create table 表名(字段名 数据类型,) charset=utf8;
    2、查看创建表的语句 (字符集、存储引擎)；
        show create table 表名\G;
    3、查看表结构;
        desc 表名;
    4、删除表;
        drop table 表1,表2,..;
```

**表记录管理**

```mysql
    1、增 ：insert into 表名 values(),();
    2、删 ：delete from 表名 where 条件;
    3、改 ：update 表名 set 字段名=值，字段名=值 where 条件；
    4、查 ：select 字段名,xx from 表名 where 条件;
```

**表字段管理(alter table 表名)**

```mysql
    1、增 ：alter table 表名 add 字段名 类型;first |after 
    2、删 ：alter table 表名 drop 字段名; 
    3、改 ：alter table 表名 modify 字段名 新类型；
    4、表重命名 ：alter table 表名 rename 新表名;
```



## **5、数据类型**

**四大数据类型**

-  数值类型

```mysql
    int smallint bigint tingyint
    float(m,n) double decimal
```

- 字符类型

```mysql
    char() 空格规定展现位数 varchar() text longtext blob 
```

- 枚举类型 

```mysql
    enum()  set() 规定范围
```

- 
  日期时间类型

```mysql
    data time year datetime timestamp 
```

**日期时间函数** 

```mysql
    NOW() CURDATE() YEAR(字段名) DATE(字段名) TIME(字段名)
```

**日期时间运算**

```mysql
    select * from 表名 where 字段名 运算符(now()-interval 时间间隔单位)
    时间间隔单位：1day |3 month |2 year
    eg1:查询一年以前的用户信息
        select * from tab where time<(now()-interval 1 year)
```



## 6、MySQL运算符

- **数值比较**

```mysql
> >= < <= = !=
eg1 : 查询成绩不及格的学生
    select * from stu where score<60;
eg2 : 删除成绩不及格的学生
    delete from stu where score <60;
eg3 : 把id为3的学生的姓名改为 周芷若
    update stu set name='周直落' where id=3;
```

- **逻辑比较** 

```mysql
and  or
eg1 : 查询成绩不及格的男生
    select * from stu where score < 60 and sex='男';
eg2 : 查询成绩在60-70之间的学生
    select * from stu where score>=60 and score<=70;
```

- **范围内比较** 

```mysql
between 值1 and 值2 、in()范围元素用逗号隔开 、not in()
eg1 : 查询不及格的学生姓名及成绩
    select name,score from stu where score between 0 and 59;
eg2 : 查询AID1903和AID1902班的学生姓名及成绩
    select name,score from stu where class in ('AID1903','AID1902');
```

- **模糊比较（like）**

```mysql
where 字段名 like '%%__' 表达式(% _) %表示任意数量任意字符，_表示固定数量任意字符
eg1 : 查询北京的姓赵的学生信息
    select * from stu where address='北京' and name like '赵%';冒号
```


- **NULL判断**

```mysql
is NULL 、is not NULL
eg1 : 查询姓名字段值为NULL的学生信息
    select * from students where name is NULL;
```

## 7、查询

- **order by**

给查询的结果进行排序(永远放在SQL命令的倒数第二的位置写)

```mysql
order by 字段名 ASC/DESC
eg1 : 查询成绩从高到低排列
    select * from stu order by score DESC;
```

- **limit**

限制显示查询记录的条数（永远放在SQL命令的最后写）

```mysql
limit n ：显示前n条
limit m,n ：从第(m+1)条记录开始，显示n条,默认从0开始
分页：每页显示10条，显示第6页的内容
    limit (6-1)*10,10;
```

******************************************************************************************
# Day01

## **MySQL基础巩固**

- **创建库 ：country（指定字符编码为utf8）**
- **创建表 ：sanguo 字段：id 、name、attack、defense、gender、country**
                   **要求 ：id设置为主键,并设置自增长属性**
- **插入5条表记录（id 1-5,name-诸葛亮、司马懿、貂蝉、张飞、赵云），攻击>100,防御<100）**
- **查找所有蜀国人的信息**

    select * from sanguo where country='蜀国';

- **将赵云的攻击力设置为360,防御力设置为68**

    update sanguo set attack=360,defense=68 where name='赵云';

- **将吴国英雄中攻击值为110的英雄的攻击值改为100,防御力改为60**

    update sanguo set attack=100,defense=60 where country='吴国' and attack=100;

- **找出攻击值高于200的蜀国英雄的名字、攻击力**

    select name,attack from sanguo 
    where attack>200 and country='蜀国';

- **将蜀国英雄按攻击值从高到低排序**

    select * from sanguo 
    where country= '蜀国' 
    order by attack DESC;

- **魏蜀两国英雄中名字为三个字的按防御值升序排列**

    select name from sanguo 
    where country in ('魏国','蜀国') and name like '___' 
    order by defense ASC;

- **在蜀国英雄中,查找攻击值前3名且名字不为 NULL 的英雄的姓名、攻击值和国家**
  
    select name,attack,country from sanguo 
    where country='蜀国' and name is not null order 
    by attack DESC 
    limit 3;

## MySQL普通查询

```mysql
    3、select ...聚合函数 from 表名
    1、where ...
    2、group by ...
    4、having ...
    5、order by ...
    6、limit ...;
```

- **聚合函数**

| 方法          | 功能                 |
| ------------- | -------------------- |
| avg(字段名)   | 该字段的平均值       |
| max(字段名)   | 该字段的最大值       |
| min(字段名)   | 该字段的最小值       |
| sum(字段名)   | 该字段所有记录的和   |
| count(字段名) | 统计该字段记录的个数 |
|               |                      |

eg1 : 找出表中的最大攻击力的值？

```mysql
    select max(attack) as xx from sanguo;
        as 改名
```

eg2 : 表中共有多少个英雄？

```mysql
    select count(name)  from sanguo;

```

eg3 : 蜀国英雄中攻击值大于200的英雄的数量

```mysql
    select count(name)from sanguo where country='蜀国' and attack>200;
```

- **group by**

给查询的结果进行分组

eg1 : 计算每个国家的平均攻击力

```mysql
    select country,avg(attack) from sanguo group by country;
```
    先分组再聚会，后面用country，前面也用country

eg2 : 所有国家的男英雄中 英雄数量最多的前2名的 国家名称及英雄数量

```mysql
    select country,count(id) as number from sanguo 
    where gender='m'
    group by country
    order by count(id) DESC
    limit 2;

```
    先分组再聚会，
​	==group by后字段名必须要为select后的字段==
​	==查询字段和group by后字段不一致,则必须对该字段进行聚合处理(聚合函数)==

- **having语句**

对分组聚合后的结果进行进一步筛选

```mysql
eg1 : 找出平均攻击力大于105的国家的前2名,显示国家名称和平均攻击力
    select country,avg(attack) as a from sanguo
    group by country
    having a>105
    order by a DESC
    limit 2;
```

注意

```mysql
having语句通常与group by联合使用
having语句存在弥补了where关键字不能与聚合函数联合使用的不足,where只能操作表中实际存在的字段,having操作的是聚合函数生成的显示列
```

- **distinct语句**

不显示字段重复值,对显示结果进行去重

```mysql
      select distinct name,country from sanguo; 还能这么使用
eg1 : 表中都有哪些国家
    select distinct country from sanguo;
eg2 : 计算蜀国一共有多少个英雄
    select count(distinct id) from sanguo where country='蜀国';
                先去重，再统计                     where 最先走
```


注意

```mysql
distinct和from之间所有字段都相同才会去重
distinct不能对任何字段做聚合处理
```

- **查询表记录时做数学运算**

运算符 ： +  -  *  /  %  **

```mysql
​```
查询时显示攻击力翻倍

    select name,attack*2 from sanguo;

更新蜀国所有英雄攻击力 * 2
update sanguo set attack=attack*2 where country='蜀国';
​```

## 嵌套查询(子查询)

- **定义**

把内层的查询结果作为外层的查询条件,注意:嵌套效率低，少用

- **语法格式**

​```mysql
select ... from 表名 where 条件(select ....);
​```
```

- **示例**

```mysql

把攻击值小于平均攻击值的英雄名字和攻击值显示出来
select avg(attack) from sanguo;
select name,attack from sanguo where attack<平均值;
找出每个国家攻击力最高的英雄的名字和攻击值
select name,attack from sanguo
where (country,attack) in
(select country,max(attack0 from sanguo group by country)
;
```



## 多表查询

**sql脚本资料：join_query.sql**

```
mysql -uroot -p123456
mysql>source /home/tarena/join_query.sql 导入sql 文档
```

if not exists  代码注意;

```mysql
create database if not exists db1 character set utf8;
use db1;

create table if not exists province(
id int primary key auto_increment,
pid int,
pname varchar(15)
)default charset=utf8;

insert into province values
(1, 130000, '河北省'),
(2, 140000, '陕西省'),
(3, 150000, '四川省'),
(4, 160000, '广东省'),
(5, 170000, '山东省'),
(6, 180000, '湖北省'),
(7, 190000, '河南省'),
(8, 200000, '海南省'),
(9, 200001, '云南省'),
(10,200002,'山西省');

create table if not exists city(
id int primary key auto_increment,
cid int,
cname varchar(15),
cp_id int
)default charset=utf8;

insert into city values
(1, 131100, '石家庄市', 130000),
(2, 131101, '沧州市', 130000),
(3, 131102, '廊坊市', 130000),
(4, 131103, '西安市', 140000),
(5, 131104, '成都市', 150000),
(6, 131105, '重庆市', 150000),
(7, 131106, '广州市', 160000),
(8, 131107, '济南市', 170000),
(9, 131108, '武汉市', 180000),
(10,131109, '郑州市', 190000),
(11,131110, '北京市', 320000),
(12,131111, '天津市', 320000),
(13,131112, '上海市', 320000),
(14,131113, '哈尔滨', 320001),
(15,131114, '雄安新区', 320002);

create table if not exists county(
id int primary key auto_increment,
coid int,
coname varchar(15),
copid int
)default charset=utf8;

insert into county values
(1, 132100, '正定县', 131100),
(2, 132102, '浦东新区', 131112),
(3, 132103, '武昌区', 131108),
(4, 132104, '哈哈', 131115),
(5, 132105, '安新县', 131114),
(6, 132106, '容城县', 131114),
(7, 132107, '雄县', 131114),
(8, 132108, '嘎嘎', 131115);
```

- **笛卡尔积**

```mysql
select 字段名列表 from 表名列表; 
```

- **多表查询**

```mysql
select 字段名列表 from 表名列表 where 条件;
```

- **示例**

```mysql
显示省和市的详细信息
河北省  石家庄市
select province.pname,city.cname from provoce,city where province.pid=city.cp_id;
河北省  廊坊市
湖北省  武汉市
显示省市县详细信息
select province.pname,city.cname,county.coname from province,city,county
where province.pid=city.cp_id and city.cid=county.copid;

```

## 连接查询(重点)

- **内连接(结果同多表查询,显示匹配到的记录)**

```mysql
select 字段名 from  表1 inner join 表2 on 条件 inner join 表3 on 条件;
	注意：有inner join 就有 on 
eg1 : 显示省市详细信息
	select province.pname,city.cname from province inner join city on
	province.pid = city.cp_id;
eg2 : 显示省市县详细信息
	select province.pname,city.cname,county.coname from province inner join city on 
    province.pid=city.cp_id inner join county on county.copid=city.cid;

```

- **左外连接** 

以 左表 为主显示查询结果,左表中达不到条件的显示字段为**null**

```mysql
select 字段名 from 表1 left join 表2 on 条件 left join 表3 on 条件;
eg1 : 显示省市详细信息
select province.pname,city.cname from province left join city on
province.pid = city.cp_id;
```

- **右外连接**

用法同左连接,以右表为主显示查询结果

```mysql
select 字段名 from 表1 right join 表2 on 条件 right join 表3 on 条件;
```

## 索引(key)概述

- **定义**

对数据库表的一列或多列的值进行排序的一种结构(Btree方式)

- **优点**

加快数据检索速度

- **缺点**

```
占用实际物理存储空
间
当对表中数据更新时,
+ 索引需要动态维护,降低数据维护速度
```
show variables like *** ; 查看相对的mysql属性
- **索引示例**

```mysql
#cursor.executemany(ins,data_list)
#此io执行多条表记录,将数据一次性上传
1、开启运行时间检测
    mysql>show variables like '%pro%'; 查看MySQL属性
    mysql>set profiling=1;
2、执行查询语句
    mysql>select name from stu where name='tom8888';
3、查看执行时间
4、在name字段创建索引
    create index name on stu(name);
5、再执行查询语句
    select name from stu where name='tom8888';
6、查看执行时间
    show profiles;
```

## 索引分类

#### 普通(MUL)  and 唯一(UNI)

- **使用规则**

```mysql
1、可设置多个字段
2、普通索引 ：字段值无约束,KEY标志为 MUL
3、唯一索引 ：字段值不允许重复,但可为 NULL , KEY标志为 UNI
4 哪些字段创建索引：经常用来查询的字段、where条件判断字段、order by 排序的字段
```

- **创建普通索引and唯一索引**

创建表时

```mysql
create table 表名(
字段名 数据类型，
字段名 数据类型，
index(字段名), 普通索引 
index(字段名),  
unique(字段名)  唯一索引
);
```
这样默认索引名与字段名相同
已有表中创建

```mysql
create [unique] index 索引名 on 表名(字段名);
```

- **查看索引**

```mysql
1、desc 表名;  --> KEY标志为：MUL 、UNI
2、show index from 表名\G;
			Non_Unique:1 :index
  			Non_Unique:0 :unique
```

- **删除索引**

```mysql
drop index 索引名 on 表名;
```

#### **主键(PRI)and自增长(auto_increment)**

- **使用规则**

```mysql
1、只能有一个主键字段
2、所带约束 ：不允许重复,且不能为NULL
3、KEY标志(primary) ：PRI
4、通常设置记录编号字段id,能唯一锁定一条记录
```

- **创建**

创建表添加主键

```mysql
create table student(
id int primary key auto_increment,
name varchar(20),
[primary key(id)] 也可以这样设置
)auto_increment=10000,charset=utf8;##设置自增长起始值
```

已有表添加主键

```mysql
alter table 表名 add primary key(id);
```

已有表操作自增长属性	

```mysql
1、已有表添加自增长属性
  alter table 表名 modify id int auto_increment;
2、已有表重新指定起始值：
  alter table 表名 auto_increment=20000;
```

- **删除**

```mysql
1、删除自增长属性(modify)
    alter table 表名 modify id int;
2、删除主键属性索引(有时失效，先用上面方法，再执行这段)
    alter table 表名 drop primary key;
```

#### **外键(foreign key)-记住3点**

- **定义** 

让当前表字段的值在另一个表的范围内选择

- **作用：**为了保证数据完整性的约束

- **语法代码**

```mysql
foreign key(参考字段名)
references 主表(被参考字段名)
on delete 级联动作
on update 级联动作
```

- **使用规则**

```
1、主表、从表字段数据类型要一致
2、主表被参考字段 ：KEY的一种，一般为主键
```

- **示例**

表1、缴费信息表(财务)

```Mysql
id   姓名     班级     缴费金额
1   唐伯虎   AID1903     300
2   点秋香   AID1903     300
3   祝枝山   AID1903     300
```
	create table master(
	id int primary key,
	name varchar(20),
	class char(7),
	money decimal(10,2)
	)charset=utf8;

表2、学生信息表(班主任) -- 做外键关联

```mysql
id   姓名   缴费金额
1   唐伯虎   300
2   点秋香   300
	create  table salve (
	stu_id int,
	name varchar(20),
	money decimal(10,2),
	foreign key (stu_id) references master(id)
	on delete cascade on update cascade 
	)charset =utf8;
	insert into salve values (1,'唐伯虎',300),(2,'点秋香',300);
```

- **删除外键**

```mysql
alter table 表名 drop foreign key 外键名;
​外键名 ：show create table 表名;
constraint‘外键名’    查看方法
```

- **级联动作**

```mysql
cascade
​数据级联删除、更新(参考字段)
restrict(默认)
​从表有相关联记录,不允许主表操作
set null
​主表删除、更新,从表相关联记录字段值为NULL
```

- **已有表添加外键**

```mysql
alter table 表名 add foreign key(参考字段) references 主表(被参考字段) on delete 级联动作 on update 级联动作
```

------

# MySQL高级-Day02

## mysql day01回顾

- **SQL查询总结**

```mysql
    3、select ...聚合函数 from 表名
    1、where ...
    2、group by ...
    4、having ...
    5、order by ...
    6、limit ...;
```

- **聚合函数（铁三角之一）**

avg(...) sum(...) max(...) min(...) 
count(字段名)  # 空值NULL不会被统计

- **group by（铁三角之二）**

给查询结果进行分组
如果select之后的字段名和group by之后的字段不一致,则必须对该字段进行聚合处理(聚合函数)

- **having语句（铁三角之三）**

对查询的结果进行进一步筛选
**注意**
1、having语句通常和group by语句联合使用,过滤由group by语句返回的记录集
2、where只能操作表中实际存在字段,having可操作由聚合函数生成的显示列

- **distinct** 

select distinct 字段1,字段2 from 表名;

- **查询时做数学运算**

select 字段1*2,字段2*3 from 表名;

- **索引(BTree)**

优点 ：加快数据检索速度
缺点 ：占用物理存储空间,需动态维护,占用系统资源
SQL命令运行时间监测
		1、开启 ：mysql> set profiling=1;
		2、查看 ：mysql> show profiles;
		3、关闭 ：mysql> set profiling=0;

- **普通(MUL)、唯一(UNI,字段值不能重复,可为NULL)**

  **创建**
  		index(字段名),index(字段名)
  		unique(字段名),unique(字段名)
  		create [unique] index 索引名 on 表名(字段名);

  **查看**
  		desc 表名;
  		show index from 表名\G;  
  			Non_Unique:1 :index
  			Non_Unique:0 :unique

  **删除**
  		drop index 索引名 on 表名; (只能一个一个删)

# Day02笔记

## **数据导入**

==掌握大体步骤==

==source 文件名.sql==

**作用**

把文件系统的内容导入到数据库中
**语法（方式一）**

load data local infile "文件名"     

先把文件放到数据库搜索路径中，一般为/var/lib/mysql-flies/                                    

into table 表名
fields terminated by "分隔符"   字段分隔
lines terminated by "\n"     		记录分隔
**示例**
scoretable.csv文件导入到数据库db2的表aid1903中

```
1、将scoretable.csv放到数据库搜索路径中
	mysql>show variables like 'secure_file_priv'
	cp scoretable.csv /var/lib/mysql-flies/
	
2、在数据库中创建对应的表
	create table scoretab(
	rank int,
	name varchar(20),/var
	phone char(11),
	class char(7)
	)charset=utf8;
	
3、执行数据导入语句
	load data local infile 'scoretable.csv'
	into table score
	fields terminated by ","
	lines terminated by "\n"  
4、练习
	添加id字段，要求主键自增长，显示宽度为3 ，位数不够用0填充
	alter table scoretab add id int(3) zerofill primary key auto_increment first;
```

额外： chmod 666  文件名    修改文件权限

sudo -i  获得管理员权限

alter database  xxx  charset utf8; 修改库编码

id int(3)  zerofill  表示位数不够 0 来填充

字符类型 和 数字类型的长度影响储存不同；

字符方式超过显示宽度无法存储，数字类型只是显示长度问题,随意存储,



**语法（方式二）**

source 文件名.sql

## **数据导出**

**作用**

将数据库中表的记录保存到系统文件里

**语法格式**

select ... from 表名   	 可以根据需要确定导出内容
into outfile "文件名"   	还是要在数据库搜索路径上/var/lib/mysql-files/
fields terminated by "分隔符"
lines terminated by "分隔符";

额外: mysql>> system 。。。。。      执行linux命令

**练习**

```mysql
把sanguo表中英雄的姓名、攻击值和国家三个字段导出来,放到 sanguo.csv中
select name,attack,country from sanguo
into outfile '/var/lib/mysql-files/sanguo.csv'
fields terminated by ','
lines terminated by '\n';
将mysql库下的user表中的 user、host两个字段的值导出到 user2.txt，将其存放在数据库目录下
```

**注意**

```
1、导出的内容由SQL查询语句决定
2、执行导出命令时路径必须指定在对应的数据库目录下
```

## **表的复制**

**语法**

```mysql
create table 表名 select 查询命令;
```

**练习**

```mysql
1、复制sanguo表的全部记录和字段,sanguo2
create table sanguo2 select * from country.sanguo;
2、复制sanguo表的前3条记录,sanguo3
3、复制sanguo表的 id,name,country 三个字段的前3条记录,sanguo4
create table sanguo4 select id,name,country from country.sanguo limit 3;
```

**注意**

复制表的时候不会把原有表的 键 属性复制过来

**单纯复制表结构**
create table 表名 select 查询命令 where false;

## **锁**

**目的**

解决客户端并发访问的冲突问题

**锁类型分类**

读锁(共享锁) ：select 加读锁之后别人不能更改表记录,但可以进行查询
写锁(互斥锁、排他锁) ：加写锁之后别人不能查、不能改

**锁粒度分类**

锁名：	引擎名

表级锁 ：myisam  
行级锁 ：innodb

# MySQL-Day02必须掌握**

## **外键**

**原理** 

```
让当前表字段的值在另一张表的范围内去选择
```

**使用规则**

```mysql
1、数据类型要一致
2、主表被参考字段必须为KEY的一种 : PRI
```

**级联动作**

```mysql
1、cascade : 删除 更新同步(被参考字段)
2、restrict(默认) : 不让主表删除 更新
3、set null : 删除 更新,从表该字段值设置为NULL
```

## **嵌套查询（子查询）**

**定义**

```
把内层的查询结果作为外层查询的条件
```

## **多表查询**

**笛卡尔积**

```
多表查询不加where条件,一张表的每条记录分别和另一张表的所有记录分别匹配一遍
```

## **连接查询**

**分类**

```mysql
1、内连接（表1 inner join 表2 on 条件）
2、外连接（表1 left|right join 表2 on 条件）
	1、左连接 ：以左表为主显示查询结果
	2、右连接 ：以右表为主显示查询结果
```

**语法**

```mysql
select 表名.字段名 from 表1 inner join 表2 on 条件；
```

## **锁**

**1、目的** ：解决客户端并发访问的冲突问题

**2、锁分类**

```mysql
1、锁类型 : 读锁 写锁
2、锁粒度 : 行级锁(InnoDB) 表级锁(MyISAM)
```

## **数据导入**

**方式一（使用source命令）**

```mysql
mysql> source /home/tarena/xxx.sql
```

**方式二（使用load命令）**

```mysql
1、将导入文件拷贝到数据库搜索路径中
   show variables like 'secure%';
2、在数据库中创建对应的表
3、执行数据导入语句
```

## **索引**

**定义**

```
对数据库表中一列或多列的值进行排序的一种结构(BTree)
```

**优点**

```mysql
加快数据的检索速度
```

**缺点**

```mysql
1、占用实际物理存储空间
2、索引需动态维护，消耗资源，降低数据的维护速度
```

**分类及约束**

```mysql
1、普通索引（MUL）: 无约束
2、唯一索引（UNI）：字段值不允许重复，但可为NULL
3、主键（PRI）	：字段值不允许重复，不可为NULL
4、外键		 ：让当前表字段的值在另一张表的范围内选择
```

# **Day03笔记**

## 3大范式

**1**．第一范式(确保每列保持原子性)

**2**．第二范式(确保表中的每列都和主键相关)

**3**．第三范式(确保每列都和主键列直接相关,而不是间接相关)

## **存储引擎**

**定义**

```mysql
处理表的处理器
```

**基本操作**

```mysql
1、查看所有存储引擎
   mysql> show engines;
2、查看已有表的存储引擎
   mysql> show create table 表名;
3、创建表指定
   create table 表名(...)engine=MyISAM,charset=utf8,auto_increment=10000;
4、已有表指定
   alter table 表名 engine=InnoDB;
```

**==常用存储引擎及特点==**

- InnoDB		

```mysql
1、支持行级锁
2、支持外键、事务、事务回滚
3、表字段和索引同存储在一个文件中
   1、表名.frm ：表结构及索引文件
   2、表名.ibd : 表记录
```

- MyISAM

```mysql
1、支持表级锁
2、表字段和索引分开存储
   1、表名.frm ：表结构
   2、表名.MYI : 索引文件(my index)
   3、表名.MYD : 表记录(my data)
```

- MEMORY

```mysql
1、表记录存储在内存中，效率高
2、服务或主机重启，表记录清除
```

**如何选择存储引擎**

```mysql
1、执行查操作多的表用 MyISAM(使用InnoDB浪费资源)
2、执行写操作多的表用 InnoDB
3、临时表 ： MEMORY
```

## **MySQL的用户账户管理**

**开启MySQL远程连接**

```mysql
更改配置文件，重启服务！
1、sudo -i
2、cd /etc/mysql/mysql.conf.d
3、cp mysqld.cnf mysqld.cnf.bak
4、vi mysqld.cnf #找到44行左右,加 # 注释
   #bind-address = 127.0.0.1
   [mysqld]
   character_set_server = utf8
5、保存退出
6、service mysql restart

vi使用 : 按a ->编辑文件 ->ESC ->shift+: ->wq
```

**添加授权用户**

```mysql
1、用root用户登录mysql
   mysql -uroot -p123456
2、授权
   grant 权限列表 on 库.表 to "用户名"@"%" identified by "密码" with grant option;
3、刷新权限
   flush privileges;
```

**权限列表**

```shell
all privileges 、select 、insert ... ... 
库.表 ： *.* 代表所有库的所有表
```

**示例**

```mysql
1、添加授权用户work,密码123,对所有库的所有表有所有权限
  mysql>grant all privileges on *.* to 'work'@'%' identified by '123' with grant option;
  mysql>flush privileges;
2、添加用户duty,对db2库中所有表有所有权限
```

## **==事务和事务回滚==**

**事务定义**

```mysql
 一件事从开始发生到结束的过程
```

**作用**

```mysql
确保数据的一致性、准确性、有效性
```

**事务操作**

```mysql
1、开启事务
   mysql>begin; # 方法1
   mysql>start transaction; # 方法2
2、开始执行事务中的1条或者n条SQL命令
3、终止事务
   mysql>commit; # 事务中SQL命令都执行成功,提交到数据库,结束!
   mysql>rollback; # 有SQL命令执行失败,回滚到初始状态,结束!
```

**==事务四大特性（ACID）==**

- **1、原子性（atomicity）**

```
一个事务必须视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，要么全部失败回滚，对于一个事务来说，不可能只执行其中的一部分操作
```

- **2、一致性（consistency）**

```
数据库总是从一个一致性的状态转换到另一个一致性的状态
```

- **3、隔离性（isolation）**

```
一个事务所做的修改在最终提交以前，对其他事务是不可见的
```

- **4、持久性（durability）**

```
一旦事务提交，则其所做的修改就会永久保存到数据库中。此时即使系统崩溃，修改的数据也不会丢失
```

**注意**

```mysql
1、事务只针对于表记录操作(增删改)有效,对于库和表的操作无效
2、事务一旦提交结束，对数据库中数据的更改是永久性的
```

## **E-R模型(Entry-Relationship)**

**定义**		

```mysql
E-R模型即 实体-关系 数据模型,用于数据库设计
用简单的图(E-R图)反映了现实世界中存在的事物或数据以及他们之间的关系
```

**实体、属性、关系**

- 实体

```mysql
1、描述客观事物的概念
2、表示方法 ：矩形框
3、示例 ：一个人、一本书、一杯咖啡、一个学生
```

- 属性

```mysql
1、实体具有的某种特性
2、表示方法 ：椭圆形
3、示例
   学生属性 ：学号、姓名、年龄、性别、专业 ... 
   感受属性 ：悲伤、喜悦、刺激、愤怒 ...
```

- ==关系（重要）==

```mysql
1、实体之间的联系
2、一对一关联(1:1) ：老公对老婆
   A中的一个实体,B中只能有一个实体与其发生关联
   B中的一个实体,A中只能有一个实体与其发生关联
3、一对多关联(1:n) ：父亲对孩子
   A中的一个实体,B中有多个实体与其发生关联
   B中的一个实体,A中只能有一个与其发生关联
4、多对多关联(m:n) ：兄弟姐妹对兄弟姐妹、学生对课程
   A中的一个实体,B中有多个实体与其发生关联
   B中的一个实体,A中有多个实体与其发生关联
```

**ER图的绘制**

矩形框代表实体,菱形框代表关系,椭圆形代表属性

- 课堂示例（老师研究课题）

```mysql
1、实体 ：教师、课题
2、属性
   教师 ：教师代码、姓名、职称
   课题 ：课题号、课题名
3、关系
   多对多（m:n)
   # 一个老师可以选择多个课题，一个课题也可以被多个老师选
```

- 练习

设计一个学生选课系统的E-R图

```mysql
1、实体：学生、课程、老师
2、属性
3、关系
   学生 选择 课程 (m:n)
   课程 任课 老师 (1:n)
```

==**关系映射实现（重要）**==

```mysql
1:1实现 --> 主外键关联,外键字段添加唯一索引
  表t1 : id int primary key,
          1
  表t2 : t2_id int unique,
         foreign key(t2_id) references t1(id)
          1
1:n实现 --> 主外键关联
  表t1 : id int primary key,
         1
  表t2 : t2_id int,
         foreign key(t2_id) references t1(id)
         1
         1        
m:n实现(借助中间表):
   t1 : t1_id 
   t2 : t2_id 
```

**==多对多实现==**

- 老师研究课题

```
表1、老师表
表2、课题表
问题？如何实现老师和课程之间的多对多映射关系？
中间表：
```

- 后续

```mysql
1、每个老师都在研究什么课题？
  select teacher.tname,course.cname from teacher 
  inner join middle on teacher.id=middle.tid 
  inner join course on course.id=middle.cid;
2、程序员姐姐在研究什么课题？
  select teacher.tname,course.cname from teacher 
  inner join middle on teacher.id=middle.tid 
  inner join course on course.id=middle.cid 
  where teacher.tname='程序员姐姐';
```

## **==MySQL调优==**

**存储引擎优化**

```mysql
1、读操作多：MyISAM
2、写操作多：InnoDB
```

**索引优化**

```
在 select、where、order by 常涉及到的字段建立索引
```

**SQL语句优化**

```mysql
1、单条查询最后添加 LIMIT 1，停止全表扫描
2、where子句中不使用 != ,否则放弃索引全表扫描
3、尽量避免 NULL 值判断,否则放弃索引全表扫描
   优化前：select number from t1 where number is null;
   优化后：select number from t1 where number=0;
   # 在number列上设置默认值0,确保number列无NULL值
4、尽量避免 or 连接条件,否则放弃索引全表扫描
   优化前：select id from t1 where id=10 or id=20;
   优化后： select id from t1 where id=10 union all 
           select id from t1 where id=20;
5、模糊查询尽量避免使用前置 % ,否则全表扫描
   select name from t1 where name like "c%";
6、尽量避免使用 in 和 not in,否则全表扫描
   优化前：select id from t1 where id in(1,2,3,4);
   优化后：select id from t1 where id between 1 and 4;
7、尽量避免使用 select * ...;用具体字段代替 * ,不要返回用不到的任何字段
```



Ubuntu重装MySQL（卸载再安装）

```mysql
1、删除mysql
  1、sudo apt-get autoremove --purge mysql-server-5.5
  2、sudo apt-get remove mysql-common
2、清理残留数据
 dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P 
3、重新安装mysql
  1、sudo apt-get install mysql-server
  2、sudo apt-get install mysql-client
```

**作业讲解**

有一张文章评论表comment如下

| **comment_id** | **article_id** | **user_id** | **date**            |
| -------------- | -------------- | ----------- | ------------------- |
| 1              | 10000          | 10000       | 2018-01-30 09:00:00 |
| 2              | 10001          | 10001       | ... ...             |
| 3              | 10002          | 10000       | ... ...             |
| 4              | 10003          | 10015       | ... ...             |
| 5              | 10004          | 10006       | ... ...             |
| 6              | 10025          | 10006       | ... ...             |
| 7              | 10009          | 10000       | ... ...             |

以上是一个应用的comment表格的一部分，请使用SQL语句找出在本站发表的所有评论数量最多的10位用户及评论数，并按评论数从高到低排序

备注：comment_id为评论id

​            article_id为被评论文章的id

​            user_id 指用户id

```
答案：
select user_id,count(user_id) from comment group by user_id order by count(user_id) DESC limit 10;
```

2、把 /etc/passwd 文件的内容导入到数据库的表中

```mysql
tarena:x:1000:1000:tarena,,,:/home/tarena:/bin/bash
1、拷贝文件
   sudo cp /etc/passwd /var/lib/mysql-files
2、建表
  create table user(
  username varchar(20),
  password char(1),
  uid int,
  gid int,
  comment varchar(50),
  homedir varchar(100),
  shell varchar(50)
  )charset=utf8;
3、导入
  load data infile '/var/lib/mysql-files/passwd'
  into table user
  fields terminated by ':'
  lines terminated by '\n';
```

**3、外键及查询题目**

综述：两张表，一张顾客信息表customers，一张订单表orders

表1：顾客信息表，完成后插入3条表记录

```
c_id 类型为整型，设置为主键，并设置为自增长属性
c_name 字符类型，变长，宽度为20
c_age 微小整型，取值范围为0~255(无符号)
c_sex 枚举类型，要求只能在('M','F')中选择一个值
c_city 字符类型，变长，宽度为20
c_salary 浮点类型，要求整数部分最大为10位，小数部分为2位
```

```mysql
create table customers(
c_id int primary key auto_increment,
c_name varchar(20),
c_age tinyint unsigned,
c_sex enum('M','F'),
c_city varchar(20),
c_salary decimal(12,2)
)charset=utf8;
insert into customers values(1,'Tom',25,'M','上海',10000),(2,'Lucy',23,'F','广州',12000),(3,'Jim',22,'M','北京',11000);
```

表2：顾客订单表（在表中插入5条记录）

```
o_id 整型
o_name 字符类型，变长，宽度为30
o_price 浮点类型，整数最大为10位，小数部分为2位
设置此表中的o_id字段为customers表中c_id字段的外键,更新删除同步
insert into orders values(1,"iphone",5288),(1,"ipad",3299),(3,"mate9",3688),(2,"iwatch",2222),(2,"r11",4400);
```

```mysql
create table orders(
o_id int,
o_name varchar(30),
o_price decimal(12,2),
foreign key(o_id) references customers(c_id) on delete cascade on update cascade
)charset=utf8;
insert into orders values(1,"iphone",5288),(1,"ipad",3299),(2,"iwatch",2222),(2,"r11",4400);
```

增删改查题

```mysql
1、返回customers表中，工资大于4000元，或者年龄小于29岁，满足这样条件的前2条记录
  select * from customers where c_salary>4000 or c_age<29 limit 2;
2、把customers表中，年龄大于等于25岁，并且地址是北京或者上海，这样的人的工资上调15%
  update customers set c_salary=c_salary*1.15 where c_age>=25 and c_city in('北京','上海');
3、把customers表中，城市为北京的顾客，按照工资降序排列，并且只返回结果中的第一条记录
  select * from customers where c_city='北京' order by c_salary DESC limit 1;
4、选择工资c_salary最少的顾客的信息
  select * from customers where c_salary=(select min(c_salary) from customers);
5、找到工资大于5000的顾客都买过哪些产品的记录明细	
  select * from orders where o_id in(select c_id from customers where c_salary>5000);
6、删除外键限制
  1、show create table orders;
  2、alter table orders drop foreign key 外键名;
7、删除customers主键限制
  1、alter table customers modify id int;
  2、alter table customers drop primary key;
8、增加customers主键限制c_id
  alter table customers add primary key(c_id);
```

