[TOC]
# 一、BOM
## 1. BOM 介绍 
BOM全称为“Browser Object Model”，浏览器对象模型。提供一系列操作浏览器的属性和方法。核心对象为window对象，不需要手动创建，跟随网页运行自动产生，直接使用，在使用时可以省略书写。
## 2.  window对象常用方法
#### 1）网页弹框
```javascript
alert()		//警告框
prompt()	//带输入框的弹框
confirm()	//确认框
```
#### 2）窗口的打开和关闭
```javascript
window.open("URL")	//新建窗口访问指定的URL
window.close()		//关闭当前窗口
```
#### 3）定时器方法
1. 间歇调用(周期性定时器)
   作用：每隔一段时间就执行一次代码
   开启定时器:
```javascript
var timerID = setInterval(function,interval);
/*
参数 :
 function : 需要执行的代码,可以传入函数名;或匿名函数
 interval : 时间间隔,默认以毫秒为单位 1s = 1000ms
返回值 : 返回定时器的ID,用于关闭定时器
*/
```
   关闭定时器 :
```javascript
//关闭指定id对应的定时器
clearInterval(timerID);
```
2. 超时调用(一次性定时器)
   作用：等待多久之后执行一次代码
```javascript
//开启超时调用:
var timerId = setTimeout(function,timeout);
//关闭超时调用:
clearTimeout(timerId);
```
## window 对象常用属性
window的大部分属性又是对象类型
#### 1）history
作用：保存**当前窗口**所访问过的URL
属性 : 
	length 表示当前窗口访问过的URL数量
方法 :
```Javascript
back() 对应浏览器窗口的后退按钮,访问前一个记录，效果等价浏览器后退箭头
forward() 对应前进按钮,访问记录中的下一个URL，效果等价浏览器前进按钮
go(n) 参数为number值,翻阅几条历史记录，正值表示前进,负值表示后退，通过n值调整跳转的页面，n=1或-1时同上面2个方法相同
```
使用：
	1. 超链接修改地址栏中URL。会增加历史记录
	2. 前进和后退按钮不会增加历史记录，只是指针的移动，指针到某个位置之后，重新使用超级连接跳转到新页面时，就会把这个指针原来后面的历史记录删除，把最近这次跳转记录加到最后。history.length也就改变了
#### 2）location
作用：保存当前窗口的地址栏信息(URL)
属性 :
    href 设置或读取当前窗口的地址栏信息
方法 :
    reload(param) 重载页面(刷新)
    参数为布尔值，默认为false，表示从**缓存中**加载，设置为true,强制从**服务器根目录**加载
#### 3）document
提供操作文档HTML 文档的方法，,参见DOM
# 二、DOM节点操作
DOM全称为“Document Object Model”，文档对象模型，提供操作HTML文档的方法。（注：每个html文件在浏览器中都视为一篇文档,操作文档实际就是操作页面元素。）
#### 1）节点对象
JS 会对html文档中的元素，属性，文本内容甚至注释进行封装，称为节点对象，提供相关的属性和方法。
#### 2）常用节点分类
+ 元素节点   (**操作标签**）类型编码1 <h1></h1> 这里h1整体就是一个元素节点
+ 属性节点（操作标签属性）类型编码2
+ 文本节点（操作标签的文本内容）类型编码3 <h1>你好</h1> 这里的”你好“就是文本节点，注意隐藏换行符也是文本节点
#### 3）获取元素节点
通过已存在的标签来获取元素节点对象，通过**document**对象调用方法
1. 根据标签名获取元素节点列表
```javascript
var elems = document.getElementsByTagName("");
/*
参数 : 标签名
返回值 : 节点列表,需要从节点列表中获取具体的元素节点对象
*/
```
2. 根据class属性值获取元素节点列表
```JavaScript
var elems = document.getElementsByClassName("");
/*
参数 : 类名(class属性值)
返回值 : 节点列表
*/
```
3. 根据id属性值取元素节点
```javascript
var elem = document.getElementById("");
/*
参数 : id属性值
返回值 : 元素节点
*/
```
4. 根据name属性值取元素列表
```javascript
var elems = document.getElementsByName("");
/*
参数 : name属性值
返回 : 节点列表
*/
```

#### 4）操作元素(文本)内容
元素节点对象提供了以下属性来操作元素内容
```text
innerHTML : 读取或设置元素文本内容,可识别标签语法
innerText : 设置元素文本内容,不能识别标签语法
value :     读取或设置表单控件的值
```
#### 5）操作修改元素属性
1. 通过元素节点对象的方法操作标签属性
```javascript
elem.getAttribute("attrname");//根据指定的属性名返回对应属性值
elem.setAttribute("attrname","value");//为元素添加属性,参数为属性名和属性值
elem.removeAttribute("attrname");//移除指定属性
```
这里class 属性不用更名,不用管关键字冲突问题
2. 标签属性都是元素节点对象的属性,可以使用点语法访问，例如：
```javascript
h1.id = "d1"; 		 //set 方法
console.log(h1.id);  //get 方法
h1.id = null;		//remove 方法
```
注意 :
+ 属性值以字符串表示
+ name 属性不能直接用h1.name设置,一般不设置name属性
+ class属性需要更名为className,避免与关键字冲突,例如：
   h1.className = "c1 c2 c3";
   其他 h1.id=""    h1.style ='' 都没事,注意与js语法不能冲突，class是类关键字

#### 6）操作元素style样式
1. 为元素添加id，class属性，对应选择器样式
2. 操作元素的行内样式,访问元素节点的style属性，获取样式对象；样式对象中包含CSS属性，使用点语法操作。
```javascript
p.style.color = "white";
p.style.width = "300px";
p.style.fontSize = "20px";
p.style.textAlign="left"
```
注意 :
+ 属性值以字符串形式给出,单位不能省略
+ 如果css属性名包含连接符,使用JS访问时,一律去掉连接符,改为驼峰. font-size -> fontSize
#### 7）元素节点的层次属性
1. parentNode
   子元素对象调用函数，获取父节点

2. childNodes
  父元素对象调用函数，获取子节点数组,只获取直接子节点(包含文本节点(换行符等)和元素节点)
	
3. children
  同上，获取子节点数组,只获取直接子元素节点(标签节点),不包含间接元素和文本节点
	+ lastChild 最后一个子元素对象
	+ firstChild 第一个子元素对象

4. previousSibling
  获取前一个兄弟节点(文本节点也可以是兄弟节点)
   previousElementSibling 获取前一个元素兄弟节点，省略文本节点
5. nextSibling
  获取后一个兄弟节点
  nextElementSibling 获取下一个元素兄弟节点，省略文本节点
6. attributes
  获取属性节点的数组

#### 8）节点的创建，添加和删除
动态创建新的元素节点对象，再增加到body中
1. 创建元素节点
```javascript 
var elem = document.createElement("标签名");//返回创建好的元素节点
```

2. 节点的添加
   添加和移除操作都必须由父元素执行，方法如下：
parendNode最外层是document.body . 
+ 在父元素的**末尾添加**子节点
```javascript
parendNode.appendChild(node);
```
+ 指定位置添加**插入**
```javascript
parendNode.insertBefore(newNode,oldNode);//在oldNode之前添加子节点
```
3. 移除节点
```javascript
parentNode.removeChild(node);//移除指定节点对象
```
注意：节点元素唯一，只能添加一次，添加同样的节点多次需要创建多个对象。

# 三、DOM 事件处理
事件：指用户的行为或元素的状态。由指定元素监听相关的事件，并且绑定事件处理函数。
事件处理函数：元素监听事件，并在事件发生时自动执行的相关操作。
#### 1） 事件函数分类
所有函数名都全小写，注意：window对象别忘了，这些都适用，而且不用写对象名。直接调用
1. 鼠标事件
```javascript
onclick		//单击
ondblclick	//双击
onmouseover	//鼠标移入
onmouseout	//鼠标移出
onmousemove	//鼠标移动
```
2. 键盘事件（了解就行）
```javascript
onkeydown	//键盘按键被按下
onkeyup		//键盘按键被抬起
onkeypress	//字符按键被按下,26字母，数字，标点符号

```
onkeydown=function(e){}   这里的e为键盘事件对象，可以
对象属性：
	key:获取按键名称（字符）
	keyCode:获取按键编码,在keydown事件中，字母键一律返回大写字母的ASC码，keypress事件中区分大小写字母的编码。
	which:获取按键编码
3. 文档,窗口或元素加载完毕（好好理解）
```javascript
onload		//元素或文档加载完毕,调整代码的
```
4. 表单控件状态监听
```javascript
onfocus 	//文本框获取焦点
onblur		//文本框失去焦点
oninput		//实时监听输入
onchange	//表单控件的值或者状态是否发生变化
两次输入内容发生变化时触发,只有内容不一样并且失去焦点时触发，或元素状态改变时触发

onsubmit	//监听表单数据是否发可以送

form元素监听(form.onsubmit=func,根据func的返回值判断是否发送请求),点击提交按钮后触发,允许在事件处理函数返回一个布尔值，True表示允许发送，False表示阻止提交，通过返回值控制数据是否可以发送给服务器
```
#### 2）事件绑定方式
1. 内联方式
   将事件名称作为标签属性绑定到元素上
   例 :
```javascript
<button onclick="alert()">点击</button>
```
2. 动态绑定
   获取元素节点，动态添加事件
   例 :
```javascript
btn.onclick = function (){

};
```
#### 3）事件函数使用
1. onload
   常用于等待文档加载完毕再进行下一步操作
2. 鼠标事件
   
3. 表单事件
   onchange： 监听输入框前后内容是否发生变化;也可以监听按钮的选中状态
   onsubmit ：表单元素负责监听,允许返回布尔值,表示数据是否可以发送;返回true,允许发送;返回false,不允许提交
4. 键盘事件
5. this关键字指代事件的触发对象；
```javascript
for(var i=0;i<lis.length;i++){	
	lis[i].onclick=function(){
		//传值
	span.innerHTML=this.innerHTML//lis[i].innerHTML
		//这里用this不用lis[i]是因为，函数内部实现时，i的数字已经是统一最大值，
		和外面的lis[i]触发对象不相同，而this代表的是调用函数的触发对象，可以实现不同对象调用结果不同。
		
	}
}

```

6. 事件对象
	事件对象跟随事件触发自动创建，保存与当前事件相关的信息，自动传入事件处理函数中，只需要接收。
	例如：
```javascript
	btn.onclick = function(event){
		console.log(event);
	}
```


