[TOC]
# 一、函数
## 1） 作用 
  	封装一段待执行的代码
## 2）语法 
```javascript
  //函数声明
  function 函数名(参数列表){
  	函数体
  	return 返回值;
  }
  //函数调用
  函数名(参数列表);
```
##  3）使用 
  	函数名自定义，见名知意，命名规范参照变量的命名规范。普通函数以小写字母开头，用于区分构造函数(构造函数使用大写字母开头，定义类)
##  4）匿名函数
匿名函数：省略函数名的函数。语法为：
+ 匿名函数自执行
```javascript
 (function (形参){
  
 })(实参);
```
+ 定义变量接收匿名函数
```javascript
 var fn = function (){};
 fn(); //函数调用
```
“有名函数”的致命问题：
	JS中所有的全局变量/函数都会自动成为window对象的成员，可能出现“覆盖window原有成员”或者“不同
开发者创建的同名函数互相覆盖”这样的问题——称为“window对象的污染”。

解决办法：匿名函数
匿名函数的两种用法：
	(1)匿名自调函数：
		(function(形参){
			函数主体
		})(实参);
	(2)匿名回调(Callback)函数：
		在指定的事件(单击/时间到了)发生时由JS解释器
		自动调用的函数
## 5）作用域
JS中作用域分为全局作用域和函数作用域，以函数的{ }作为划分作用域的依据
1. 全局变量和全局函数
    + 只要在函数外部使用var关键字定义的变量,或函数都是全局变量和全局函数,在任何地方都可以访问
    + 所有省略var关键字定义的变量,一律是全局变量
2. 局部变量/局部函数
	+ 在函数内部使用var关键字定义的变量为局部变量,函数内部定义的函数也为局部函数,只能在当前作用域中使用,外界无法访问
3. 作用域链
  	局部作用域中访问变量或函数,首先从当前作用域中查找,当前作用域中没有的话,向上级作用域中查找,直至全局作用域
# 二、 内置对象
## 1） 对象
  对象是由属性和方法组成的,使用点语法访问
+ JS中的对象的分类：
 	1. ES原生对象(百度搜MDN)
		Array、String、Math、...总共十几个
	2. 宿主对象(由浏览器提供的对象)
		window、document、location、...等数百个 
	3. 用户自定义对象
		var stu = { math: 80, ... }
+ JS中对象的语法：
	Object = Field + Method
	JS中创建对象有很多种方法，
	最常用的是“对象直接量法”，语法：
	var 实例名 = {
		成员名: 值,
		成员名: 值,
		....
	}
	例如：
	var user2 = {
		userName: 'dingding',	
		age: 20,
		isOnline: true,
		login: function(){ console.log(this.age) },
		logout: function(){}
	};
## 2） Array 数组
#### 1. 创建 
+ 创建一个新的数组：
	var 数组变量名 = [];  //长度为0的数组
	var 数组变量名 = new Array(); //长度为0的数组
	var 数组变量名 = [值, 值, ...];
	var 数组变量名 = new Array(值, 值, ...);
	var 数组变量名 = new Array(100);//长度为100的数组
#### 2. 特点 
+ 数组用于存储若干数据,自动为每位数据分配下标,从0开始
+ 数组中的元素不限数据类型,长度可以动态调整
+ 动态操作数组元素 ：根据元素下标读取或修改数组元素，arr[index]
#### 3. 属性和方法
1. 属性 : length 表示数组长度,可读可写
2. 方法 :
    + push(data)
    在数组的末尾添加一个或多个元素,多个元素之间使用逗号隔开
    返回添加之后的数组长度

    + pop()
    移除末尾元素
    返回被移除的元素

    + unshift(data)
    在数组的头部添加一个或多个元素
    返回添加之后的数组长度

    + shift()
    移除数组的第一个元素
    返回被移除的元素

    + toString()
    将数组转换成字符串类型,得到的是一个元素用逗号隔开的长字符串
    返回字符串结果

    + join(param)
    将数组转换成字符串,可以指定元素之间的连接符,如果参数省略,默认按照逗号连接
    返回字符串

    + reverse()
    反转数组,倒序重排
    返回重排的数组,注意该方法直接修改原数组的结构

    + sort(function(){})
    对数组中元素排序,默认按照Unicode编码升序排列
    返回重排后的数组,直接修改原有数组
    参数 : 可选,自定义排序算法
    	例：
        ```javascript
        //自定义升序
        function sortASC(a,b){
          return a-b;
        }
        ```
       作用：作为参数传递到sort()中,会自动传入两个元素进行比较,如果a-b>0(主要看函数的返回值1,0,-1),交换元素的值,自定义升序排列
        ```javascript
        //自定义降序
        function sortDESC(a,b){
        	return b-a;
        }
        //如果返回值>0,交换元素的值,b-a表示降序排列
        ```
     + forEach(param)
    遍历数组元素
    参数为函数
    例 :
        ```javascript
        arr.forEach(function (elem,index){
            //forEach()方法会自动调用匿名函数,依次传入元素及下标
	    //对数组中的每个元素都进行function函数操作;
        });
        ```
    + splice(index,count)
	从index下标开始删除，删除count个元素

    + splice(index,count,replacement..)
	同上，这里是替换，replacement为替换内容,如果替换内容的数量比count少，没有被替换的就被删除
	arr.splice(2,0,'aa') 下标2插入aa值
    + indexOf(e)
	返回数组中第一个与e值相等的元素下标，不存在则返回-1
    + lastIndexOf(e)
	同上，找寻最后一个的下标，不存在返回-1
#### 4. 二维数组 
数组中的每个元素又是数组
```javascript
 var arr1 = [1,2,3];
 var arr2 = [[1,2],[3,4],[5,6,7]];
 //操作数组元素
 var r1 = arr2[0] //内层数组
 var num = r1[0]; //值 1
 //简写
 var num2 = arr2[1][0];
```
### Math 数学类
Math.random()*(max-min)+min  可以随机取min到max之间的数 取不到max
## 3）String 对象  字符串
#### 1. 创建 
```javascript
    var str = "100";
    var str2 = new String("hello");
```
注意：Js中所有的字符串都是不可变的，所有改变字符串内容的函数都不是改变原字符串的内容，而是返回一个新的字符串
#### 2. 特点 
字符串采用数组结构存储每位字符,自动为字符分配下标,从0开始
#### 3. 属性 
length ：获取字符串长度（字符个数）
#### 4. 方法 
+ 转换字母大小写
    toUpperCase() 转大写字母
    toLowerCase() 转小写字母
    返回转换后的字符串,不影响原始字符串

+ 获取字符或字符编码
    charAt(index)	   获取指定下标的字符
    charCodeAt(index)      获取指定下标的字符编码
    参数为指定的下标,可以省略,默认为0
+ unicode编号：
	数字  48到57
	A到Z  65到90
	a到z  97到122
	中文  19968~40869
+ 获取指定字符的下标

    + indexOf(str,fromIndex)
    作用 : 获取指定字符的**下标**,从前向后查询,找到即返回
    参数 :
    	str 表示要查找的字符串,必填
    	fromIndex 表示起始下标,默认为0
    返回 :
    	返回指定字符的下标,查找失败返回-1

    + lastIndexOf(str,fromIndex)
      作用 : 获取指定字符最后一次出现的**下标**,从后向前查找,找到即返回
      参数 :
      	str 必填,表示要查找的内容
      	fromIndex	选填,指定起始下标

+ 截取字符串
    substring(startIndex,endIndex)
    作用 : 根据指定的下标范围截取字符串,startIndex ~ (endIndex-1)
    参数 :
     startIndex	表示起始下标
     endIndex	表示结束下标(不包含),可以省略,省略表示截止末尾，
     索引规则同Python最后一个元素索引为-1

+ 分割字符串
    split(param)（该方法与arr.join()是反操作）
    作用 : 将字符串按照指定的字符进行分割,以数组形式返回分割结果
    参数 : 指定**分隔符**,必须是字符串中存在的字符,如果字符串中不存在,分割失败,仍然**返回数组**

+ 模式匹配
    作用 : 借助正则表达式实现字符串中固定格式内容的查找和替换
    正则表达式 :
     var reg1 = /字符模式/修饰符;
     修饰符 : 
      i : ignorecase 忽略大小写
      g : global 全局范围
    字符串方法 :
    + match(regExp/subStr)
	作用 : 查找字符串中满足正则格式或满足指定字符串的内容
  	返回 : **数组**,存放查找结果
    + replace(regExp/subStr,newStr)(正则表达式，新内容)
    作用 : 根据正则表达式或字符串查找相关内容并进行替换
    返回 : **替换后的字符串,不影响原始字符串**
    注意 ：如果第一个参数为字符串时，只能替换一个
	eg.	var s= "共产党诞生于上个世纪，共产党引导中国走向解放，共产党是我们的领路人"
	 	var str=s.replace(/共产党/gi,"***")
	 	console.log(str)



