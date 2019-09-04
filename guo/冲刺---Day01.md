# 冲刺---Day01

## 一，Django基础 - 经典重点内容回顾 - 高速版

### Django的框架设计模式

MVC 设计模式

- MVC 代表 Model-View-Controller（模型-视图-控制器） 模式。
- 作用: 降低模块间的耦合度(解耦)
- MVC
  - M 模型层(Model), 主要用于对数据库层的封装
  - V 视图层(View), 用于向用户展示结果
  - C 控制(Controller ，用于处理请求、获取数据、返回结果(重要)



MTV 模式
MTV 代表 Model-Template-View（模型-模板-视图） 模式。这种模式用于应用程序的分层开发

- 作用: 
  - 降低模块间的耦合度(解耦)
- MTV 
  - M -- 模型层(Model)  负责与数据库交互
  - T -- 模板层(Template)  负责呈现内容到浏览器
  - V -- 视图层(View)  是核心，负责接收请求、获取数据、返回结果



### 创建项目

​	django-admin startproject 项目名称

### 目录结构

```shell
$ django-admin startproject mysite1
$ tree mysite1/
mysite1/
├── manage.py
└── mysite1
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

项目目录结构解析:

- manage.py

  - 此文件是项目管理的主程序,在开发阶段用于管理整个项目的开发运行的调式
  - `manage.py` 包含项目管理的子命令, 如:
    - `python3 manage.py runserver` 启动服务
    - `python3 manage.py startapp` 创建应用
    - `python3 manage.py migrate` 数据库迁移
    - `...`

- mysite1 项目包文件夹

  - 项目包的主文件夹(默认与项目名称一致)

  1. `__init__.py`
     - 包初始化文件,当此项目包被导入(import)时此文件会自动运行
  2. `wsgi.py`
     - WSGI 即 Web Server Gateway Interface
     - WEB服务网关接口的配置文件，仅部署项目时使用
  3. `urls.py`
     - 项目的基础路由配置文件，所有的动态路径必须先走该文件进行匹配
  4. `settings.py`
     - Django项目的配置文件, 此配置文件中的一些全局变量将为Django框架的运行传递一些参数
     - setting.py 配置文件,启动服务时自动调用，
     - 此配置文件中也可以定义一些自定义的变量用于作用全局作用域的数据传递

settings.py` 文件介绍

1. `BASE_DIR`

   - 用于绑定当前项目的绝对路径(动态计算出来的), 所有文件都可以依懒此路径

2. `DEBUG`

   - 用于配置Django项目的启用模式, 取值:
     1. True 表示开发环境中使用 `调试模式`(用于开发中)
     2. False 表示当前项目运行在`生产环境中`(不启用调试)

3. `ALLOWED_HOSTS`

   - 设置允许访问到本项目的网络地址列表,取值:

     1. [] 空列表,表示只有`127.0.0.1`, `localhost`, '[::1]' 能访问本项目
     2. ['*']，表示任何网络地址都能访问到当前项目
     3. ['*.tedu.cn', 'weimingze.com'] 表示只有当前两个主机能访问当前项目

     - 注意:
       - 如果要在局域网其它主机也能访问此主机,启动方式应使用如下模式:

   - `python3 manage.py runserver 0.0.0.0:5000` # 指定网络设备所有主机都可以通过5000端口访问(需加`ALLOWED_HOSTS = ['*']`) 

4. `INSTALLED_APPS`

   - 指定当前项目中安装的应用列表

5. `MIDDLEWARE`

   - 用于注册中间件

6. `TEMPLATES`

   - 用于指定模板的配置信息

7. `DATABASES`

   - 用于指定数据库的配置信息

8. `LANGUAGE_CODE`

   - 用于指定语言配置
   - 取值:
     - 英文 : `"en-us"`
     - 中文 : `"zh-Hans"`

9. `TIME_ZONE`

   - 用于指定当前服务器端时区
   - 取值:
     - 世界标准时间: `"UTC"`
     - 中国时区 : `"Asia/Shanghai"`

10. `ROOT_URLCONF`

    - 用于配置根级 url 配置 'mysite1.urls'
    - 如:
      - `ROOT_URLCONF = 'mysite1.urls'`

> 注: 此模块可以通过 `from django.conf import settings` 导入和使用  

### 视图函数(view)

- 视图函数是用于接收一个浏览器请求并通过HttpResponse对象返回数据的函数。此函数可以接收浏览器请求并根据业务逻辑返回相应的内容给浏览器

- 视图处理的函数的语法格式:

  ```python
  def xxx_view(request[, 其它参数...]):
      return HttpResponse对象
  ```

- 参数:

  - request用于绑定HttpRequest对象，通过此对象可以获取浏览器的参数和数据

- 示例:

  - 视图处理函数 `views.py`  FBV function base view and CBV class base view

    ```python
    # file : <项目名>/views.py
    from django.http import HttpResponse
    def page1_view(request):
        html = "<h1>这是第1个页面</h1>"
        
        return HttpResponse(html)
    ```

### Django 中的路由配置

- settings.py 中的`ROOT_URLCONF` 指定了主路由配置列表urlpatterns的文件位置

- urls.py 主路由配置文件

  ```python
  # file : <项目名>/urls.py
  urlpatterns = [
      url(r'^admin/', admin.site.urls),
      ...  # 此处配置主路由
  ]
  ```

  > urlpatterns 是一个路由-视图函数映射关的列表,此列表的映射关系由url函数来确定

3. url() 函数

   - 用于描述路由与视图函数的对应关系
   - 模块
     - `from django.conf.urls import url`
   - 语法:
     - url(regex, views, name=None)
     - 参数：
       1. regex: 字符串类型，匹配的请求路径，允许是正则表达式
       2. views: 指定路径所对应的视图处理函数的名称
       3. name: 为地址起别名，在模板中地址反向解析时使用

   > 每个正则表达式前面的r表示`'\'`不转义的原始字符串



### Django中的应用 - app

创建应用app

- 创建步骤
  1. 用manage.py 中的子命令 startapp 创建应用文件夹
  2. 在settings.py 的 INSTALLED_APPS 列表中配置安装此应用
- 创建应用的子命令
  - python3 manage.py startapp 应用名称(必须是标识符命令规则)
  - 如:
    - python3 manage.py startapp music

配置安装应用

- 在 settings.py 中配置应用, 让此应用能和整个项目融为一体

```python
# file : settings.py 
INSTALLED_APPS = [
    ... ...,
    '自定义应用名称'
]
```

如:

```python
INSTALLED_APPS = [
    # ....
    'user',  # 用户信息模块
    'music',  # 收藏模块
]
```

### 数据库 和 模型

1.mysql 数据库配置

```python
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mywebdb',  # 数据库名称,需要自己定义
        'USER': 'root',
        'PASSWORD': '123456',  # 管理员密码
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
```

​	添加 mysql 支持

```python
import pymysql
pymysql.install_as_MySQLdb()
```

2. 数据库的迁移

   - 迁移是Django同步您对模型所做更改（添加字段，删除模型等） 到您的数据库模式的方式

   1. 生成或更新迁移文件
      - 将每个应用下的models.py文件生成一个中间文件,并保存在migrations文件夹中
      - `python3 manage.py makemigrations`
   2. 执行迁移脚本程序
      - 执行迁移程序实现迁移。将每个应用下的migrations目录中的中间文件同步回数据库
      - `python3 manage.py migrate`

   - 注:

- 每次修改完模型类再对服务程序运行之前都需要做以上两步迁移操作。
        

  - 生成迁移脚本文件`bookstore/migrations/0001_initial.py`并进行迁移

    ```shell
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
    ```

3. 编写模型类Models

- 模型类需继承自`django.db.models.Model`

  Models的语法规范

  ```
  from django.db import models
  class 模型类名(models.Model):
      字段名 = models.字段类型(字段选项)
  ```

  > 模型类名是数据表名的一部分，建议类名首字母大写
  > 字段名又是当前类的类属性名，此名称将作为数据表的字段名
  > 字段类型用来映射到数据表中的字段的类型
  > 字段选项为这些字段提供附加的参数信息



1. CharField()

   - 数据库类型:varchar(300) 1-2 存储当前实际存储长度  256 + 2        char(30)   
   - 注意:
     - 必须要指定max_length参数值

2. DateField()

   - 数据库类型:date
   - 作用:表示日期
   - 编程语言中:使用字符串来表示具体值
   - 参数:
     - DateField.auto_now: 每次保存对象时，自动设置该字段为当前时间(取值:True/False)。
     - DateField.auto_now_add: 当对象第一次被创建时自动设置当前时间(取值:True/False)。
     - DateField.default: 设置当前时间(取值:字符串格式时间如: '2019-6-1')。
     - 以上三个参数只能多选一

3. DateTimeField()

   - 数据库类型:datetime(6)
   - 作用:表示日期和时间
   - auto_now_add=True

4. DecimalField()

   - 数据库类型:decimal(x,y)

   - 编程语言中:使用小数表示该列的值

   - 在数据库中:使用小数

   - 参数:

     - DecimalField.max_digits: 位数总数，包括小数点后的位数。 该值必须大于等于decimal_places.
     - DecimalField.decimal_places: 小数点后的数字数量

   - 示例:

     ```
     money=models.DecimalField(
         max_digits=7,  
         decimal_places=2,
         default=0.0
     )
     ```

5. FloatField()

   - 数据库类型:double
   - 编程语言中和数据库中都使用小数表示值

6. EmailField()

   - 数据库类型:varchar
   - 编程语言和数据库中使用字符串

7. IntegerField()

   - 数据库类型:int
   - 编程语言和数据库中使用整数

8. URLField()

   - 数据库类型:varchar(200)
   - 编程语言和数据库中使用字符串

9. ImageField()

   - 数据库类型:varchar(100)

   - 作用:在数据库中为了保存图片的路径

   - 编程语言和数据库中使用字符串

   - 示例:

     ```
     image=models.ImageField(
         upload_to="static/images"
     )
     ```

   - upload_to:指定图片的上传路径
     在后台上传时会自动的将文件保存在指定的目录下

10. TextField()

    - 数据库类型:longtext
    - 作用:表示不定长的字符数据

- 参考文档 <https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types>

字段选项FIELD_OPTIONS

- 字段选项, 指定创建的列的额外的信息
- 允许出现多个字段选项,多个选项之间使用,隔开

1. primary_key
   - 如果设置为True,表示该列为主键,如果指定一个字段为主键，则此数库表不会创建id字段
2. blank
   - 设置为True时，字段可以为空。设置为False时，字段是必须填写的。字符型字段CharField和TextField是用空字符串来存储空值的。 默认值是False。
3. null
   - 如果设置为True,表示该列值允许为空。日期型、时间型和数字型字段不接受空字符串。所以设置IntegerField，DateTimeField型字段可以为空时，需要将blank，null均设为True。
   - 默认为False,如果此选项为False建议加入default选项来设置默认值
4. default
   - 设置所在列的默认值,如果字段选项null=False建议添加此项
5. db_index
   - 如果设置为True,表示为该列增加索引
6. unique
   - 如果设置为True,表示该字段在数据库中的值必须是唯一(不能重复出现的)
7. db_column
   - 指定列的名称,如果不指定的话则采用属性名作为列名
8. verbose_name
   - 设置此字段在admin界面上的显示名称。

- 示例:

  ```python
  # 创建一个属性,表示用户名称,长度30个字符,必须是唯一的,不能为空,添加索引
  name = models.CharField(max_length=30, unique=True, null=False, db_index=True)
  ```

- 文档参见:
  
  - <https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-options>

### 查询数据

- 数据库的查询需要使用管理器对象进行

- 通过 MyModel.objects 管理器方法调用查询接口

  | 方法     | 说明                                  |
  | -------- | ------------------------------------- |
  | all()    | 查询全部记录,返回QuerySet查询对象集合 |
  | get()    | 查询符合条件的单一记录                |
  | filter() | 查询符合条件的多条记录                |

all()方法

- 语法: MyModel.objects.all()

  ```python
  MyModel.objects.all()
  ```

- 作用: 查询MyModel实体中所有的数据

  - 等同于
    - select * from tabel

- 返回值: QuerySet容器对象,内部存放 MyModel 实例



 filter()方法

- 语法: 

  ```python
  MyModel.objects.filter(属性1=值1, 属性2=值2)
  ```

- 作用：条件查询

- 返回值:

  - QuerySet容器对象,内部存放 MyModel 实例

- 说明:

  - 当多个属性在一起时为"与"关系，即当`Books.objects.filter(price=20, pub="清华大学出版社")` 返回定价为20 `且` 出版社为"清华大学出版社"的全部图书



get()方法

- 语法:

  ```python
  MyModel.objects.get(条件)
  ```

- 作用：

  - 返回满足条件的唯一一条数据

- 返回值:

  - MyModel 对象

- 

- 说明:

  - 该方法只能返回一条数据
  - 查询结果多余一条数据则抛出,Model.MultipleObjectsReturned异常
  - 查询结果如果没有数据则抛出Model.DoesNotExist异常

### 修改数据记录

修改单个实体的某些字段值的步骤:

1. 查

   - 通过 get() 得到要修改的实体对象

2. 改

   - 通过 对象.属性 的方式修改数据

3. 保存

   - 通过 对象.save() 保存数据

     ```python
     from bookstore import models
     abook = models.Book.objects.get(id=10)
     abook.market_price = "10.5"
     abook.save()
     ```

     

通过 QuerySet 批量修改 对应的全部字段

- 直接调用QuerySet的update(属性=值) 实现批量修改

- 如:

  ```python
  # 将 id大于3的所有图书价格定为0元
  books = Book.objects.filter(id__gt=3)
  books.update(price=0)
  # 将所有书的零售价定为100元
  books = Book.objects.all()
  books.update(market_price=100)
  ```

  ### 删除记录

删除单个对象

- 步骤
  1. 查找查询结果对应的一个数据对象
  2. 调用这个数据对象的delete()方法实现删除

```python
try:
    auth = Author.objects.get(id=1)
    auth.delete()
except:
    print(删除失败)
```

删除查询结果集

步骤

1. 查找查询结果集中满足条件的全部QuerySet查询集合对象

2. 调用查询集合对象的delete()方法实现删除

   ```python
   # 删除全部作者中，年龄大于65的全部信息
   auths = Author.objects.filter(age__gt=65)
   auths.delete()
   ```

### 原生的数据库操作方法

- 使用django中的游标cursor对数据库进行 增删改操作

  - 在Django中可以使用 如UPDATE,DELETE等SQL语句对数据库进行操作。

  - 在Django中使用上述非查询语句必须使用游标进行操作

  - 使用步骤:

    1. 导入cursor所在的包

       - Django中的游标cursor定义在 django.db.connection包中，使用前需要先导入
       - 如：
         - `from django.db import connection`

    2. 用创建cursor类的构造函数创建cursor对象，再使用cursor对象,为保证在出现异常时能释放cursor资源,通常使用with语句进行创建操作

       - 如:

         ```python
         from django.db import connection
         with connection.cursor() as cur:
             cur.execute('执行SQL语句')
         ```

    - 示例

      ```python
      # 用SQL语句将id 为 10的 书的出版社改为 "XXX出版社"
      from django.db import connection
      with connection.cursor() as cur: 
          cur.execute('update bookstore_book set pub_house="XXX出版社" where id=10;')
      
      with connection.cursor() as cur:
          # 删除 id为1的一条记录
          
          cur.execute('delete from bookstore_book where id=10;')
      ```

### cookies 和 session(会话)

#### cookies

- cookies是保存在客户端浏览器上的存储空间，通常用来记录浏览器端自己的信息和当前连接的确认信息

- cookies 在浏览器上是以键-值对的形式进行存储的，键和值都是以ASCII字符串的形存储(不能是中文字符串)

- cookies 的内部的数据会在每次访问此网址时都会携带到服务器端，如果cookies过大会降低响应速度

- 在Django 服务器端来设置 设置浏览器的COOKIE 必须通过 HttpResponse 对象来完成

- HttpResponse 关于COOKIE的方法

  - 添加、修改COOKIE
    - HttpResponse.set_cookie(key, value='', max_age=None, expires=None)
      - key:cookie的名字
      - value:cookie的值
      - max_age:cookie存活时间，秒为单位
      - expires:具体过期时间
        <!-- 
      - path：cookie的访问路径，只有在某个路径下访问
      - domain:域名，只有在某个域名下访问
        -->
  - 删除COOKIE
    - HttpResponse.delete_cookie(key)
    - 删除指定的key 的Cookie。 如果key 不存在则什么也不发生。

- Django中的cookies

  - 使用 响应对象HttpResponse 等 将cookie保存进客户端

    1. 方法1

       ```py
       from django.http import HttpResponse
       resp = HttpResponse()
       resp.set_cookie('cookies名', cookies值, 超期时间)
       ```

       - 如:

       ```py
       resp = HttpResponse()
       resp.set_cookie('myvar', "weimz", 超期时间)
       ```

    2. 方法二, 使用render对象

       ```py
       from django.shortcuts import render
       resp = render(request,'xxx.html',locals())
       resp.set_cookie('cookies名', cookies值, 超期时间)
       ```

    3. 方法三, 使用redirect对象

       ```py
       from django.shortcuts import redirect
       resp = redirect('/')
       resp.set_cookie('cookies名', cookies值, 超期时间)
       ```

  3. 获取cookie

     - 通过 request.COOKIES 绑定的字典(dict) 获取客户端的 COOKIES数据

       ```py
       value = request.COOKIES.get('cookies名', '没有值!')
       print("cookies名 = ", value)
       ```

  4. 注:

     - Chrome 浏览器 可能通过开发者工具的 `Application` >> `Storage` >> `Cookies` 查看和操作浏览器端所有的 Cookies 值

#### session 会话控制

- 什么是session

  - session又名会话控制，是在服务器上开辟一段空间用于保留浏览器和服务器交互时的重要数据

- session的起源

  - 客户端与服务器端的一次通信，就是一次会话
  - http协议是无状态的：每次请求都是一次新的请求，不会记得之前通信的状态
  - 实现状态保持的方式：在客户端或服务器端存储与会话有关的数据
  - 推荐使用sesison方式，所有数据存储在服务器端

- 实现方式

  - 使用session 需要在浏览器客户端启动 cookie，且用在cookie中存储sessionid
  - 每个客户端都可以在服务器端有一个独立的Session
  - 注意：不同的请求者之间不会共享这个数据，与请求者一一对应

- Django启用Session

  - 在 settings.py 文件中

  - 向 INSTALLED_APPS 列表中添加：

    ```py
    INSTALLED_APPS = [
        # 启用 sessions 应用
        'django.contrib.sessions',
    ]
    ```

  - 向 MIDDLEWARE_CLASSES 列表中添加：

    ```py
    MIDDLEWARE = [
        # 启用 Session 中间件
        'django.contrib.sessions.middleware.SessionMiddleware',
    ]
    ```

- session的基本操作:

  - session对于象是一个在似于字典的SessionStore类型的对象, 可以用类拟于字典的方式进行操作
  - session 只能够存储能够序列化的数据,如字典，列表等。
  - 保存 session 的值到服务器
    - `request.session[键] = 值`
    - 如: `request.session['KEY'] = VALUE`
  - 获取session的值
    - `VALUE = request.session['KEY']`
    - 或
    - `VALUE = request.session.get('KEY', 缺省值)`
  - 删除session的值
    - `del request.session['KEY']`
  - 在 settings.py 中有关 session 的设置
    1. SESSION_COOKIE_AGE
       - 作用: 指定sessionid在cookies中的保存时长(默认是2周)，如下:
       - `SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2`
    2. SESSION_EXPIRE_AT_BROWSER_CLOSE = True
       设置只要浏览器关闭时,session就失效 (默认为False)



#### 跨站请求伪造保护 CSRF

- 跨站请求伪造攻击

  - 某些恶意网站上包含链接、表单按钮或者JavaScript，它们会利用登录过的用户在浏览器中的认证信息试图在你的网站上完成某些操作，这就是跨站请求伪造。 www.bank.com?to=1111&num=2000

- CSRF 

  ```
  Cross-Site Request Forgey
  跨     站点   请求    伪装
  ```

- 说明:

  - CSRF中间件和模板标签提供对跨站请求伪造简单易用的防护。 

- 作用:

  - 不让其它表单提交到此 Django 服务器

- 解决方案:

  1. 取消 csrf 验证(不推荐)

     - 删除 settings.py 中 MIDDLEWARE 中的 `django.middleware.csrf.CsrfViewMiddleware` 的中间件

  2. 开放验证

     ```
     在视图处理函数增加: @csrf_protect
     @csrf_protect
     def post_views(request):
         pass
     ```

  3. 通过验证

     ```
     需要在表单中增加一个标签 
     {% csrf_token %}
     ```

