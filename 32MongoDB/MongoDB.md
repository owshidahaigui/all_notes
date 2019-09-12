MongoDB （芒果数据库）

## 一. 基础概念

1. 数据：能够输入到计算机中并被识别处理的信息集合

2. 数据结构：研究一个数据集合中，数据元素关系

3. 数据库：按照数据结构，存储管理数据的仓库。数据仓库是在数据库管理系统管理控制下在一定介质中创建的

4. 数据库管理系统：数据库管理软件，用于建立维护操作数据库

5. 数据库系统：由数据库和数据库管理系统等构成的数据库开发工具集合。

## 二.  关系型数据库  &  非关系型数据库

 1. ### 关系型数据库：采用关系模型（二维表）来组织数据结构的数据库

   【1】 常见关系型数据库：Oracle  DB2  SQLServer
	 MySQL  SQLite

 	【2】 优缺点

​		-  优点:  逻辑清晰，容易理解，结构类似常见表格

​						使用SQL语句，技术成熟，使用方便

​						关系型数据库比较成熟，可以使用一些复杂的操作

​		-  缺点：每次操作都需要专门的sql解析

​					关系型数据库结构严格，内部加锁
​	         		在应对海量数据并发处理时读写速度差

  2. ## 非关系型数据库（NoSql-->not only sql）
	
	  【1】 常见的非关系型数据库

	 * 不是采用关系模型构建的数据库

	    ​    键值型 ： Redis
		​	列存储 ： HBase
		​	文档型 ： MongoDB
		​	 图形   ： Graph
     
	【2】 优缺点
	
	​	     优点 ：  读写速度快，更好的针对并发处理
	
	​					使用灵活，容易扩展	
	​		 缺点 ： *没有sql那样统一成熟的语句
	
	​				     技术成熟度较差，缺少一些复杂操作
	
	【3】 应用场景	   
	
	     1. 对数据格式要求不严格，比较灵活
	    2. 对数据处理速度，特别是海量数据的并发处理速度要求比较高
	    3. 特定场景：需要灵活扩展，需要作为缓存

## 三. MongoDB数据库

  1.  ### mongodb特点
	
	* 非关系型数据库，是属于文档型数据库
	 * 开源数据库，使用广泛
	 * 由 c++ 编写的数据库管理系统
	 * 支持丰富的存储类型和数据操作
	 * 提供了丰富的编程语言接口
	 * 方便扩展和部署
  
2. ## MongoDB 安装

    * Linux ：  sudo  apt-get install  mongodb

     * Mac OS:   brew  install  mongodb

     * Windows:  www.mongodb.com -->Try free -->server  下载安装

     Linux 安装目录    
    		* 安装位置： /var/lib/mongodb..
    		* 配置文件： /etc/mongodb.conf
    		* 命令集：  /usr/bin

     进入mongodb交互界面   
    	名称 ： mongodb shell
    	命令 ： mongo
    	退出 ： quit()    ctrl-c


         mongod 设置mongodb的基本信息
        		 mongod  -h  查看帮助
        		 mongod  --dbpath  [dir]  设置数据库存储位置
        		 mongod  --port  [port]  设置数据库端口
        		 mongodb默认端口27017

## 四. MongodDB 数据库数据结构

  1. 数据组织结构： 键值对->文档->集合->数据库

	 e.g.:	
	
	| ID   | NAME | AGE  |
	| ---- | ---- | ---- |
	| 1    | Lily | 17   |
	| 2    | Lucy | 18   |
	
	-----------------------------------
      
			{
			  "_id":1,   
				"NAME":'Lily',
				"AGE" :17	
			},
			{
			  "_id":2,
				"NAME":'Lucy',
				"AGE" :18	
			}

2. 基本概念对比

    | mysql    | mongodb    | 含义      |
    | -------- | ---------- | --------- |
    | database | database   | 数据库    |
    | table    | collection | 表/集合   |
    | column   | field      | 字段/域   |
    | row      | document   | 记录/文档 |
    | index    | index      | 索引      |

## 五. 数据库操作

  1. 创建数据库： use [database]
	
		 ```
	e.g.  创建一个叫stu的数据库
     	  use  stu
	```
	
	 * use实际是选择使用哪个数据库，当这个数据库不存在则自动建立
 * use创建数据库并不会立即建立起来，而是当真正插入数据时才会建立 
	
2. 查看数据库 ： show  dbs

  3. 数据库命名规则:

     - 使用utf-8字符串

     * 不能含有  空格  .  /   \  '\0' 字符
      * 不能超过64字节
      * 不要和系统库重名

4. 全局变量 db ： 代表当前正在使用的数据库

   * 不选择任何数据库时  db = test

5. 数据库的删除： db.dropDatabase()

6. 数据库的备份和恢复命名

    ```
     备份命令:
        mongodump -h [host] -d [db] -o [path]
        e.g. 将本机 stu 数据库备份在 当前目录下
          mongodump -h 127.0.0.1 -d stu -o  .
    恢复命令：
    	 mongorestore -h [host:port] -d [db]  [bak]
    
    e.g. 将stu备份 恢复到本机student数据库中
    	 mongorestore -h 127.0.0.1:27017 -d student stu
    ```

    

  7. 数据库运行监控

    查看数据库的运行状态： mongostat
    
    	insert query update delete：每秒增查改删次数
    
    查看数据库集合读写时长： mongotop
    
    	* 得到每个集合在一秒内的读写时间

## 六. 集合操作

  1. 创建集合

     ```
     db.createCollection(collectionName)
     
      e.g. 创建名为class1的集合
      db.createCollection('class1')
     
     db.colletion.insert(...)
     ```

     
     -   插入数据时如果集合不存在则自动创建

2. 查看集合： 

     ```
     	show collections    
     	show tables
     ```

  3. 集合命名规则
        * 使用utf-8 字符
        	 * 不能含有 '\0'
        	 * 不要以 system. 开头，这是系统集合默认开头
        	 * 不要和关键字重名

4. 删除集合

    ```
    db.collection.drop()
    
     e.g.  删除class集合
    			 db.class.drop()
    ```

    

5. 集合重命名

    ```
    db.collection.renameCollection(newName)
    
     e.g.  将class重命名为class0
     db.class.renameCollection('class0')
    ```

## 七. 文档操作

   1. 什么是文档？  
	
			   - 文档是mongodb数据库中基本的数据组织单元
	
	- 文档由键值对构成，每个键值对表达一个数据项

	- mongodb文档数据bson类型数据
	
	- 文档键值对特点
	  - 无序的
	  - 通过键取其值
	  - 不能重复
	  - 键是utf-8字符串，不能有'\0'字符
        - 值为bson支持数据类型，即存储的数据
	
	-   数据类型：    
	
	  整型 int  :    整数
	  浮点型 double ：  小数
	  布尔 boolean ： true   false
	  字符串 string ： utf-8字符串
	  ObjectId ： id对象 自动生成的不重复值
	
	  	* mongodb插入文档时，每个文档都要有一个_id域，可以自己指定一个不重复的值，也可以由系统自动生成


   2. 集合中文档设计

	   - 一个集合中的文档可以有不同的域，域的个数也可以不一致。
	- 集合中的文档层次不宜嵌套过多，如果层次过多时应考虑分为多个集合
	- 在一个集合中的文档应该尽量表达相同类型的数据内容

## 八. 数据操作

### 插入文档

 *  ```
    db.collection.insertOne(doc)
    	 功能: 插入一条文档
    	 参数：要插入的文档
    
     e.g. 插入一条文档
     db.class0.insertOne({'name':'Lucy','age':18,'sex':'w'})
    
    - 操作数据时，键可以不加引号
    - 可以自己设置_id值，但是不能重复
    
     db.collection.insertMany([{},{}...])
     功能: 插入多条文档
     参数: 数组中为多个文档
    
     e.g.  同时插入多个文档
     db.class1.insertMany([{name:'百合',age:33,sex:'w'},{name:'阿蓉',age:28,sex:'w'},{name:'小许',age:46,sex:'m'}])
    
    - 数组：使用 [] 表示的一组数据有序集合
      特点 ： 有序，使用序列号取值
    ```
    
    

练习 ： 创建 grade 数据库
				创建 class 集合
				集合中插入若干数据项格式如下
				{name:xxx,age:xxx,sex:x,hobby:[xx,xx,]}
				年龄：7-15
				hobby：'draw' 'dance' 'sing' 'football'
							 'basketball'  'computer'  'python'

```
 db.collection.insert()
     功能: 插入一条或多条文档
     参数：同 insertOne + insertMany

 db.collection.save()
	 功能：插入一条或多条文档
	 参数：同 insert 
```

	 * 使用save 如果_id重复会替换掉原有文档

### 查找操作

```
mysql  select ... from table where ...

mongo  db.collection.find(query,field)

db.collection.find(query,field)
	功能: 查找所有符合条件的文档
	参数：query 查找条件
		 field 要查找的域
	返回： 返回所有查找到的文档

db.collection.find() ==> select * from table
query :  是一个 键值对文档{},空则表示所有以键值对表示筛选条件，往往配合查找操作符完成
field ： 是一个键值对文档{}, 
		field:0表示不查	找这个与，
		field:1表示查找这个域。
  		_id域如果不想查找 _id:0
  		其他域设置要么全为0 要么全为1

e.g.  查找所有年龄18的文档，只查找name，age域
db.class0.find({age:18},{_id:0,name:1,age:1})
```

作业 ： 
 1. 能够回答关系型数据库和非关系型数据库差别
 2. 熟练mongo数据库创建，数据集合操作，插入操作
 3. 将mysql银行数据库表，写成mongo集合形式，插入一些数据



# 第二天内容

### 前情回顾

1. 关系型数据库和非关系型数据库
   - Nosql不是关系模型构建的数据库，不保证数据一致性，结构灵活
   - NoSql弥补了关系型数据库高并发数据处理速度慢的缺点
   - Nosql种类多样，技术成熟度不如关系型数据库

2. mongodb数据库特点，安装，命令设置

3. mongodb的组成结构

4. mongodb的数据类型 

5. 数据库操作
   
	 * use  database  选择数据库不存在则创建
	 * db.dropDatabase()  删除数据库
	 * show  dbs  查看数据库 

	 命令 ：    mongodump  备份
	 				 mongorestore 恢复
					 mongostat  数据库监控
					 mongotop   查看读写时长
	
6. 集合操作：
   
	  db.createCollection()  创建集合
	 db.collection.insert()   集合不存在自动创建
	 db.collection.drop()  删除集合
	 db.collection.renameCollection() 重命名
	 show  collections  查看集合
	 db.getCollection('class')  获取集合对象

7. 文档插入
   insertOne()  
	 insertMany()
	 insert()
	 save()  当_id冲突时会替换原文档

8. 查找函数

   find(query,field)

************************************************
cookie:

 计算机基础课 ： 计算机原理，算法导论，编程原理

 公众号 ： python程序员  python开发者  算法爱好者

 app ： 知乎    掘金

 网站 ： 伯乐在线    CSDN

## 一. 数据操作（续）

1. #### 查找函数

   ```
    db.collection.findOne(query,field)
   	 功能: 查找第一个复合条件的文档
   	 参数: 同find
   	 返回：返回查找到的文档
   
    e.g.  查找第一个性别为男的文档
    db.class0.findOne({sex:'m'},{_id:0}
   ```


  2. ### query操作符使用

	   操作符：mongodb中使用$符号注明的一个有特殊意义的字符串，用以表达丰富的含义，比如：$lt 表示小于 
	
	 比较操作符 
	
	```
	【1】 $eq  等于  = 
				
			e.g.  年龄等于17 
	        db.class0.find({age:{$eq:17}},{_id:0})
			
	【2】 $lt  小于  < 
				
		  e.g. 字符串可以比较大小
	  db.class0.find({name:{$lt:'Tom'}},{_id:0})
      
【3】 $gt  大于  >
	
		  e.g. 查找一个区间范围
		db.class0.find({age:{$gt:17,$lt:20}},{_id:0})
	
		【4】 $lte  小于等于  <=
		【5】 $gte  大于等于  >=
	【6】 $ne   不等于    !=
	
	【7】 $in   包含
	
		e.g. 查找年龄在数组范围的
	db.class0.find({age:{$in:[17,19,21]}},{_id:0})
		
	【8】 $nin  不包含
	
		e.g. 查找年龄不在数组范围的
		db.class0.find({age:{$nin:[17,19,21]}},{_id:0})
	```
	
	####  **逻辑操作符**    
	
	```
	2. 【1】 $and   逻辑与
	
	   ​                 e.g.  查找年龄小于19 并且性别为w的
	   ​               db.class0.find({$and:[{age:{$lt:19}},{sex:{$ne:'w'}}]},{_id:0})
	
	   ​				query中的多个条件本身也表示并且关系
	
	   ​    【2】 $or  逻辑或
	
	   ​                 e.g.  查找年龄大于18或者性别为w
	   ​           db.class0.find({$or:[{age:{$gt:18}},{sex:'w'}]},{_id:0})
	
	   ​    【3】 $not  逻辑非
	   ​        ​		
	   ​        ​		e.g. 查找年龄不大于18的
	   ​        ​		 db.class0.find({age:{$not:{$gt:18}}},{_id:0})
	
	   ​    【4】 $nor 既不也不(多个条件均为假则结果为真)
	
	   ​                 e.g.  年龄不大于18 性别不为 m
	   ​           db.class0.find({$nor:[{age:{$gt:18}},{sex:'m'}]},{_id:0})
	
	   ​    【5】 混合条件语句
	
	   ​                 年龄大于等于19或者小于18  并且 性别为 w
	
	   ​        ​		  db.class0.find({$and:[{$or:[{age:{$gte:19}},{age:{$lt:18}}]},{sex:'w'}]},{_id:0})
	   ​        ​		 
	   ​        ​		 （年龄大于等于17的男生） 或者  (姓名叫 Abby 或者Emma)
	
	​        ​		 db.class0.find({$or:[{age:{$gte:17},sex:'m'},{name:{$in:['Abby','Emma']}}]},{_id:0})
	```

####    	数组操作符		

```
  【1】 查找数组中包含元素
		
			e.g.  查找score数组中元素包含大于90的文档
		    db.class2.find({score:{$gt:90}},{_id:0})

   	  【2】 $all  查找数组中同时包含多项

  		  e.g. 查找数组中同时包含87,89的文档
			db.class2.find({score:{$all:[87,89]}},{_id:0})

 		【3】 $size 根据数组的元素个数查找
				
   		  e.g.  查找数组中包含3个元素的文档
			 db.class2.find({score:{$size:3}},{_id:0})

   		【4】 $slice 用于field参数，表示查找数组哪些项
			 
			 e.g.  查找数组中的前两项
			 db.class2.find({},{_id:0,score:{$slice:2}})
				
    		 e.g.  跳过数组第一项，查看后面两项
			 db.class2.find({},{_id:0,score:{$slice:[1,2]}})
```

​	

# 第三天内容	     

前情回顾

1. ```
  1. 查找操作
	 
   findOne(query,field)
  
  2. query 操作符
  
     比较： $eq  $lt $lte $gt $gte  $ne  $in  $nin
      逻辑:  $and  $or  $not   $nor
      数组： $all  $size
      其他:  $exists  $mod  $type
  
  3. 数据处理函数
  
     pretty()  limit()  skip()  sort()  count()  distinct()
  
  4. 修改操作
  
     updateOne(query,update,upsert)
      updateMany()
      update()
      findOneAndUpdate()
      findOneAndReplace()
  
  5. 修改器
     $set   $unset   $rename  $setOnInsert
  ```
  
  
  

***************************************************

## 一. 修改器的使用(续

```
1.$inc :  加法修改器

 	 e.g.  所有人年龄加1
	 db.class1.updateMany({},{$inc:{age:1}})

2.$mul  :  乘法修改器

	e.g. 所有人年龄乘以0.5
  	db.class1.updateMany({},{$mul:{age:0.5}})

	$inc  $mul 操作数可以是整数 小数 正数 负数
    
3. $max :  修改某个域的值，如果小于指定值则改为指定值，大于则不变

  	e.g.  如果age域小于30改为30，大于30则不变
	db.class1.updateMany({sex:'w'},{$max:{age:30}})

	$min :修改某个域的值，如果大于指定值则改为指定值，小于则不变

	e.g.  将age大于30的文档，如果age大于40改为40
	db.class1.updateMany({age:{$gt:30}},{$min:{age:40}})
```

###   数组修改器

```
1.$push  向数组中添加一项

e.g.  给小红score数组增加一个元素10
db.class2.updateOne({name:'小红'},{$push:{score:10}})
```

```
2.$pushAll  向数组中添加多项

e.g.  给小明score数组中增加多个元素
db.class2.updateOne({name:'小明'},{$pushAll:{score:[10,5]}})
```

```
3.$pull : 从数组中删除某个值

e.g. 删除小刚score数组中的90
db.class2.updateOne({name:'小刚'},{$pull:{score:90}})
```

```
4.$pullAll : 同时删除数组中多个值

e.g.  删除小明score数组多个值
db.class2.updateOne({name:'小明'},{$pullAll:{score:[69,5]}})
```

```
5.$pop ： 弹出数组中一项

e.g.  弹出数组中最后一项 （1表示最后一项，-1表示第一项）
db.class2.updateOne({name:'小红'},{$pop:{score:1}})
```

```
6.$addToSet : 向数组中添加一项，但是不能和已有的数值重复

e.g.  向score增加80，但是不能和已有的重复
db.class2.updateOne({name:'小刚'},{$addToSet:{score:80}})
```

```
7.$each : 对多个值逐一操作

e.g.  对90  10 都执行push操作
db.class2.updateOne({name:'小红'},{$push:{score:{$each:[90,10]}}})
```

```
8.$position : 指定数据插入位置 配合$each

e.g.  将90 插入到 索引1位置
db.class2.updateOne({name:'小刚'},{$push:{score:{$each:[90],$position:1}}})
```

```
9.$sort :  给数组排序  配合$each使用

e.g. 将小红score数组按照降序排序 （-1降序，1升序）
db.class2.updateOne({name:'小红'},{$push:{score:{$each:[],$sort:-1}}})
```


练习 ： 使用grade

  1. ```
	   1. 将小红年龄修改为8岁，兴趣爱好改为跳舞画画
   updateOne({name:'小红'},{$set:{age:8,hobby:['dance','draw']}})
	2. 小明多了一个兴趣爱好 唱歌
	   updateOne({name:'小明'},{$push:{hobby:'sing'}})
	
	3. 小王兴趣爱好多个吹牛，打篮球
	   updateOne({name:'小王'},{$push:{hobby:['吹牛','basketball']}})
	4. 小李兴趣增加跑步,唱歌，但是确保不和以前的重复
	   updateOne({name:'小李'},{$addToSet:{hobby:{$each:['running','sing']}}})
	5. 班级所有同学年龄增加1
	   updataMany({},{$inc:{age:1}})
	6. 删除小明的sex属性
	   updateOne({name:'小明'},{$unset:{sex:''}})
	7. 小李第一个兴趣爱好不要了
	   updateOne({name:'小明'},{$pop:{hobby:-1}})
	8. 小刚不喜欢计算机和画画了
	   updateOne({name:'小明'},{$pullAll:{hobby:['draw','computer']}})
	
	```

## 二. 删除操作

  1. ### 格式对比
	
	  mysql ： delete  from  table  where ... 

	 mongo ： db.collection.deleteOne(query)

  2. ### 删除函数

	 ```
	db.collection.deleteOne(query)
	 功能: 删除第一个符合条件文档
    参数: 筛选条件
	
	 e.g.  删除第一个不存在 gender域的文档
	  db.class0.deleteOne({gender:{$exists:false}})
	```
	
	```
	 db.collection.deleteMany(query)
		 功能: 删除所有符合条件文档
		 参数: 筛选条件
	
	 e.g.  删除所有小于18岁的文档
	 db.class0.deleteMany({age:{$lt:18}})
	
			删除一个集合中所有文档
	  db.class1.deleteMany({})
	  
	 db.collection.remove(query,justOne)
	 	功能: 删除文档
	 	参数: query  筛选条件
	 			 justOne=>false 删除所有符合条件文档(默认)
	     justOne=>true  只删除一个符合条件文档
		
		 e.g.  删除第一个性别为m的文档
		 db.class0.remove({gender:'m'},true)
	```
	
	```
	 db.collection.findOneAndDelete(query)
		功能: 查找一个文档并删除之
		参数: 查找条件
		返回: 查找到的文档
	
		e.g. 查找Levi并删除
		db.class0.findOneAndDelete({name:'Levi'})
	```
	
	

练习 ： 使用grade
 1. 删除所有年龄小于8岁或大于12岁的同学
	 deleteMany({$or:[{age:{$gt:12}},{age:{$lt:8}}]})

 2. 删除兴趣爱好中没画画或跳舞的同学
	
	 deleteMany({hobby:{$nin:['draw','dance']}})

	 

## 三. 一些数据类型

  1. ### 时间类型

	  【1】 获取当前时间
		    
				* new  Date()  自动生成当前时间
				
				e.g. 
				db.class1.insertOne({book:'Python入门',date:new Date()})
	
				* Date()  获取计算机当前时间生成字符串
				
				e.g.
				db.class1.insertOne({book:'Python精通',date:Date()})

    【2】 时间函数
    
    	    ISODate()
    			功能 ： 将制定时间转换为标准时间存入
    			参数： 默认同  new  Date() 获取当前时间
    						 或者字符串制定时间
    						 "2019-01-01  08:08:08"
    						 "20190101  08:08:08"
    						 "20190101"
    			
    			e.g.  传入制定时间
    			db.class1.insertOne({book:'Python疯狂',date:ISODate("2019-01-01 08:08:08")})
    
      【3】 时间戳
    	    
    			valueOf()
    			功能: 将标准时间转化为时间戳
    
        e.g. 将标准时间转换为时间戳
    			db.class1.insertOne({book:'Python涅槃',date:ISODate().valueOf()})

  2. Null 类型

	  【1】 值 ： null

		【2】 含义 ： 
		     
				 * 表示某个域的值为空
				 
				 e.g.  price域的值为空
				 db.class1.insertOne({book:'Python Web',price:null})
	
				 * 查找时表示某个域没有
					
				 e.g. 查找到price域为null或者没有该域的
				 db.class1.find({price:null},{_id:0})

  3. 内部文档（Object类型）

	  【1】 定义: 文档中某个域的值为内部文档，则该值为object类型数据

		【2】 使用方法：当使用内部文档某个域的值时，需要采用个"外部域.内部域"的方法,此时该格式需要用引号表示为字符串
	
		e.g.  找到出版社为中国文学的
		db.class3.find({"intro.publication":'中国文学出版社'},{_id:0})

练习： grade

   1. 将小红爱好的第二项变为 唱歌
	 		
			updateOne({name:'小红'},{$set:{'hobby.1':'sing'}})

	 2. 给小王增加一个域 
	    备注:{民族:'回族',习俗:'注意饮食禁忌'}

			updateOne({name:'小王'},{$set:{备注:{民族:'回族',习俗:'注意饮食禁忌'}}})
	
	 3. 修改小王的备注域，增加一项 
	    宗教 : '伊斯兰'

			updateOne({name:'小王'},{$set:{'备注.宗教':'伊斯兰'}})

四. 索引操作 

  1. 什么是索引：索引是建立文档所在位置的查找清单，使用索引可以方便快速查找，减少遍历次数，提高查找效率

	2. 索引约束： * 数据量很小时不需要创建索引
								* 创建索引会增加磁盘的使用空间
								* 对数据库操作大多时写操作而不是读操作时不宜创建索引
	
	3. 创建索引
	   
		 【1】 db.collection.createIndex(index,option)
				   功能: 创建索引
					 参数：索引域和索引选项

					 e.g. 为name域创建索引
					 db.class0.createIndex({name:1})
					 
					 * _id域会由系统自动生成索引
					 * 1 表示正向索引，-1表示逆向索引					
		
		 【2】 db.collection.getIndexes()
		      功能： 查看集合中索引
			
		 【3】 通过第二个参数定义索引名

					e.g.  创建索引名字为ageIndex
					db.class0.createIndex({age:-1},{name:'ageIndex'})
     
		 【4】 其他索引创建方法
		      
					ensureIndex()
					功能: 创建索引
					参数： 同 createIndex()
	
					createIndexes([{},{}..])
					功能: 创建多个索引
					参数: 数组中写多个键值对
   
   4. 删除索引
	 		
		【1】 db.collection.dropIndex(index or name)
				  功能: 删除一个索引
					参数: 索引名称或者键值对
					
					e.g.  通过名称或者键值对删除
					db.class0.dropIndex('name_-1')
					db.class0.dropIndex({age:-1})

    【2】 db.collection.dropIndexes()
    				功能 ： 删除所有索引
    				
    				* _id索引不会被删除
    
    5.  其他类型索引
       
    	【1】 复合索引: 根据多个域创建一个索引
    
    			db.class0.createIndex({name:1,age:-1})
    		
    	【2】object/数组索引 ： 如果对object域或者数组域创建索引则针对object或者数组中某一个元素的查询也是索引查询
    
    	e.g. 如果对intro创建了索引，则该查找也是索引查找
    	db.class3.find({'intro.author':'曹雪芹'})
    
     【3】 唯一索引 ： 要求创建索引的域不能有重复值
    
      e.g. 对name域创建唯一索引
    		db.class0.createIndex({name:1},{unique:true})
    	
     【4】 稀疏索引 ： 如果创建稀疏索引则对没有索引域的文档会忽略
    
        e.g. 对age 创建稀疏索引
    		 db.class0.createIndex({age:1},{sparse:true,name:'Age'})


五.  聚合操作

  1. 什么是聚合 ： 对文档进行数据整理统计，得到统计结果

  2. 集合函数 
     
  	 db.collection.aggregate(aggr)
  	 功能: 执行聚合操作
  	 参数: 聚合条件，配合聚合操作符使用
     
  3. 聚合操作符

    【1】 $group  分组聚合  需要配合统计操作符
  	    
  			* 统计求和 ： $sum
  				
  				e.g. 按性别分组统计每组人数
  			 db.class0.aggregate({$group:{_id:'$gender',num:{$sum:1}}})
  			
  			* 求平均数 ： $avg 
  			
  			e.g.  按性别分组求平均年龄
  			db.class0.aggregate({$group:{_id:'$gender',num:{$avg:'$age'}}})
  	
  			* 求最大最小值 : $max / $min
  	
  			e.g. 按性别分组求每组的最大值
  			db.class0.aggregate({$group:{_id:'$gender',num:{$max:'$age'}}})

     * $first/$last   求第一项值和最后一项值

  			【3】 $match  数据筛选

    * match 值的写法同find函数中query写法
      

    e.g. 筛选年龄大于18的文档
    db.class0.aggregate({$match:{age:{$gt:18}}})

  		 【4】 $limit  显示集合中前几条文档
  	
  				e.g. 显示前3个文档内容
  	db.class0.aggregate([{$limit:3}])

    【5】$skip  跳过前几个文档显示后面的内容

       e.g. 跳过前3个文档显示后面内容
       db.class0.aggregate([{$skip:3},{$project:{_id:0}}])

    【6】 $sort  对集合文档排序

       e.g. 对文档按年龄排序
       db.class0.aggregate([{$sort:{age:1}},{$project:{_id:0}}])

   4. 聚合管道 

     定义： 指将第一个聚合的结果交给第二个聚合操作继续执行，直到所有聚合完成。
    
     形式： aggregate([{聚合1},{聚合2}...])
    
     e.g. 查找年龄大于18的文档，不显示_id
     db.class0.aggregate([{$match:{age:{$gt:18}}},{$project:{_id:0}}])


# 第四天

前情回顾

1. 修改器

   $inc  $mul  $max   $min
	 $push  $pushAll  $pull  $pullAll  $pop  $addToSet $each  $sort  $position

2. 删除文档

   deleteOne(query)
	 deleteMany()
	 remove()
	 findOneAndDelete()

3. 数据类型
   
	 【1】 时间类型 ： new Date()
	 									 Date()
										 ISODate()
										 ValueOf()
										 
	 【2】 Null :  null  表示空

   【3】 Object类型 ："外部域.内部域"


4. 索引操作

	 * 索引约束
	 * 创建索引
    
		  createIndex()
			createIndexes()
			ensureIndex()
	
	    getIndexes()
			dropIndex()
			dropIndexes()
	
5. 聚合操作 

   aggregate([{},{},{}....])
	
	 $group 
	 $sum
	 $avg
	 $max
	 $min 
	 $match
	 $limit
	 $skip
	 $sort

**************************************************
一. 聚合操作符（续）

	1. $project :  选择显示的域（值的写法同field参数）
	 
	 e.g.  筛选结果不显示_id
	 db.class0.aggregate([{$match:{}},{$project:{_id:0,Name:'$name',Age:'$age'}}])

练习:  使用grade

  1.  将所有男生按照年龄升序排序，结果不显示_id

			aggregate([$match:{sex:'m'},{$sort:{age:1}},{$project:{_id:0}}])

	2.  将所有喜欢画画的女生按照年龄排序，取年龄最小的三个，只显示姓名，年龄，爱好

	    aggregate([{$match:{hobby:'draw',sex:'w'}},{$sort:{age:1}},{$limit:3},{$project:{_id:0,name:1,age:1,hobby:1}}])


二.  固定集合

   定义: 指的是mongodb中创建固定大小的集合，称之为固定集合

	 特点： 1. 能够淘汰早期数据
	 				2. 可以控制集合大小
					3. 数据插入，查找速度快
	
	 使用 : 日志处理，临时缓存
	
	 创建 : db.createCollection(collection,{capped:true,size:10000,max:20})
	
	 capped:true   表示创建固定集合
	 size ：10000  固定集合大小 字节
	 max ：20    固定集合可存放文档数量

   e.g. 创建固定集合log，最多存放3条文档
	 db.createCollection('log',{capped:true,size:1000,max:3})


三. 文件存储

  1. 文件存储数据库方式 
	
		【1】 存储路径：将本地文件所在的路径以字符串存储到数据库中。

		   优点: 操作简单，节省数据库空间
			 缺点：当数据库或者文件发生变化需要修改数据库
		 
		【2】 存储文件本身：将文件转换为二进制存储到数据库中。
	
		   优点：文件绑定数据库，不容易丢失
			 缺点: 占用数据库空间大，文件存取效率低

  2. GridFS文件存储方案
	
		 目的：更方便的存取mongodb中大文件（>16M）

		 说明: 
		 1. mongodb数据库中创建两个集合共同存储文件
		 2. fs.files集合中为每个文件建立一个信息文档，存储文件的基本信息
		 3. fs.chunks集合中每个文档建立与fs.files的关联，并将文件分块存储
	
		 存储方法:
		 mongofiles -d  dbname  put  file
		 
		 e.g.  将Postman... 存储到grid数据库中
		 mongofiles -d grid put Postman.tar.gz 
			
		 提取方法：
		 mongofiles -d  dbname  get  file
	
		 e.g. 从数据库中获取Post...文件
		 mongofiles -d grid  get Postman.tar.gz

     优缺点 ： 对大文件的存储提取方便，但是读写效率仍然比较低，不建议用来存储小文件。


四. mongo shell 对 JavaScript支持

  * mongo shell界面中支持基本的JS代码
	* 通过js处理mongo的一些数据逻辑


五. Python操作MongoDB

  1. 第三方模块 ： pymongo
	   安装 ： sudo  pip3 install  pymongo 

	2. 操作步骤
	   
		 【1】 导入模块，连接mongodb数据库
		
			  from  pymongo  import  MongoClient
				conn = MongoClient('localhost',27017)

     【2】 选择要操作的数据库和集合
		     
				 db = conn.stu   # 选择数据库
				 myset = db.class0  # 选择集合
			
		 【3】 通过集合对象调用接口完成数据操作
		       
					 数据书写转换：
					 
					 文档 ----》 字典
					 数组 ----》 列表
					 布尔 ----》 python布尔
					 null ----》 None
     	  操作符 ----》 字符串形式原样书写
					  $lt               "$lt"
		  
		 【4】 关闭数据库连接
	
		     conn.close() 


   3. 数据操作函数 （mongodb/mongo.py）
			
		【1】 插入文档
		      
					insert_one()  插入一条文档
					insert_many()  插入多条文档
					insert()  插入一条或多条文档
					save()  插入文档，如果_id重复会覆盖  

    【2】 查找操作
    	     
    			 cursor = find(query，field)  
    			 功能：查找所有文档
    			 参数：形式同mongo中 find
    			 返回值：查找结果的游标对象
    
    			 cursor对象属性
    
    			 * 通过迭代获取每个查找文档结果
    			 * 通过调用属性方法对结果进行进一步操作
            next()
    					limit()
    					skip()
    					count()
    					sort([('age',1),('name',1)])
    
    					注意: 
    					1.调用limit，skip，sort时游标必须没有遍历过
    					2. sort排序写法域mongoshell不同
    					{age:1,name:1}->[('age',1),('name',1)]

 

				 find_one(query，field)  
				 功能：查找一个文档
				 参数: 同find
				 返回值: 文档字典
	
	【3】 修改操作
		   
			 update_one()  修改一个文档
			 update_many()  修改多个文档
			 update() 
	
		【4】 删除操作
		   delete_one()  删除一个文档
			 delete_many()  删除多个文档
			 remove()
	
	【5】 复合操作
		   
			 find_one_and_delete() 
	
		【6】 索引操作
	
		   create_index(index,**kwargs) 
			 功能: 创建索引
			 参数: {name:1} --> [('name',1)] 
			 				kwargs 索引选项
			 返回值: 索引名称
	
			 list_indexes()  查看索引
			 drop_index() 删除索引
			 drop_indexes()  删除所有索引
	
	【7】 聚合操作
		   
			 cursor = aggregate([{},{}])
			 功能: 完成聚合操作
			 参数: 聚合管道，同mongo shell
			 返回值： 数据结果游标

  4. 文件存储

	   import  bson

		 1. 将文件内容转换为bson二进制格式存储
		    
				content = bson.binary.Binary(bytes)
				功能: 将python字节串转换为bson格式
				参数: 要转换的字节串
				返回值: bson数据
		
		 2. 将bson数据 插入到mongo数据库文档中