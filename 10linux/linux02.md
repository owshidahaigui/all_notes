# Linux系统第二天

1）制作压缩包tar与zip
2) 管理用户与组：
    用户UID  useradd  id  /etc/passwd  passwd  /etc/shdaow  userdel 
     组GID  groupadd  gpasswd  /etc/group

3）权限和归属：基本权限 基本归属  chmod  chown
4）进程管理：pstree  ps aux  pgrep  进程前后台调度  杀死进程

## 管道操作   | ：

​        **将前面命令的输出，专递给后面命令，作为后面命令的参数**

**查看文件/etc/passwd内容的头4行？**

```shell
tarena@tedu:~$ head -4 /etc/passwd   
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
tarena@tedu:~$ 
```

   **查看文件/etc/passwd内容的8-12行内容？**

```shell
tarena@tedu:~$  head  -12   /etc/passwd
tarena@tedu:~$  head  -12  /etc/passwd  |  tail  -5
tarena@tedu:~$  head  -12  /etc/passwd  |  tail  -5  |  cat  -n

tarena@tedu:~$  cat   -n  /etc/passwd  |   head  -12    |   tail  -5

tarena@tedu:~$  echo 1+1
tarena@tedu:~$  echo 1+1    |    bc
tarena@tedu:~$  echo 3*8    |    bc

tarena@tedu:~$  ifconfig
tarena@tedu:~$  ifconfig    |    head   -2
tarena@tedu:~$  ls  --help    |    grep   A
```



**快捷键：**
      – Ctrl + l:清空整个屏幕 
      – Ctrl + c:废弃当前编辑的命令行(结束正在运行的命令)
      – Esc + . 或 Alt + . :粘贴上一个命令的参数

```shell
tarena@tedu:~$ ls   /etc/lsb-release 
/etc/lsb-release
tarena@tedu:~$ ls -l   Alt  +  .

tarena@tedu:~$ cat    Alt  +  .
tarena@tedu:~$ cat  -n   Alt  +  .
```

## 十一、vi或vim文本编辑器使用

**vi：基本的文本编辑器**
**vim：vi的升级版本**

 模式：命令模式      插入模式（输入模式）    末行模式

```shell
tarena@tedu:~$ sudo  vim   /home/tarena/haha.txt
```

**命----  i 键 或 o键 ----》 插入模式（Esc键回到命令模式）**
**令**
**模**
**式----  ：键 ----》 末行模式（Esc键回到命令模式）**

  **末行模式     ：wq      #保存并退出**
                     **：q！    #强制不保存退出**

```
tarena@tedu:~$ sudo  vim   /home/tarena/dc.txt
```

**命令模式** 

```shell
$ cp   /etc/passwd    /home/tarena/p.txt
$ vim    /home/tarena/p.txt
```

**光标的跳转**：
      行首： ^或home
      行尾： $或end
      全文的首行：gg  或 1G
      全文的最后一行：G
      全文的12行：12G
   **复制粘贴删除**
       yy：复制光标所在的当前行    2yy复制两行内容
        p：粘贴
      dd：删除光标所在的当前行    3dd删除三行内容
       u  ：撤销
       /bin  : 全文查找bin    按n向下跳转匹配   按N向上跳转匹配

**末行模式：**
        ：set   nu     #开启行号功能
        ：set   ai      #开启自动缩进功能

```shell
tarena@tedu:~$ vim /home/tarena/b.txt
```

## 一、制作压缩包tar与zip

-    – -c:创建归档
-    – -z、-j、-J:调用 .gz、.bz2、.xz格式的工具进行处理
-    – -f:指定归档文件名称，必须在所有选项的最后
-    – -x:释放归档 
-    – -t:显示归档中的文件清单
-    – -C:指定释放路径

#### **Linux平台的压缩格式：**

​     gzip---->.gz
​     bzip2---->.bz2
​     xz----->.xz

1. 归档：将众多的数据，归档整理成一个文件

2. 压缩：采用压缩算法，计算数据占用空间大小

#### **制作tar包**

**格式：  tar  选项      /路径/压缩包的名字       被压缩的源数据**

```shell
$ sudo tar   -zcf    /opt/aid.tar.gz     /boot/     /etc/lsb-release 
[sudo] tarena 的密码： 
tar: 从成员名中删除开头的“/”
$ ls    /opt/

$ sudo tar   -jcf    /opt/abc.tar.bz2   /boot/   /etc/lsb-release 
$ ls    /opt/

$ sudo tar  -Jcf   /opt/file.tar.xz    /boot/    /etc/lsb-release
$ ls    /opt/
```

- -z：利用gzip进行压缩   ==>gz
- -j：利用bzip2进行压缩   ==>bz2
- -J：利用xz压缩 ==>xz

#### **查看压缩包内容**

```shell
tarena@tedu:~$ tar    -tf     /opt/abc.tar.bz2  
```

#### **解包：**

**格式：tar  选项   /路径/tar包的名字    -C   释放的位置**

```shell
tarena@tedu:~$ sudo mkdir /aid01
tarena@tedu:~$ sudo  tar   -xf   /opt/abc.tar.bz2    -C     /aid01
tarena@tedu:~$ ls   /aid01/
tarena@tedu:~$ ls   /aid01/etc/

tarena@tedu:~$ sudo mkdir /aid02
tarena@tedu:~$ sudo  tar   -xf   /opt/file.tar.xz    -C     /aid02
tarena@tedu:~$ ls   /aid02
tarena@tedu:~$ ls   /aid02/etc/
```

#### zip跨平台的压缩格式（windows与Linux）

**制作压缩包：**
**格式：zip   -r     /路径/压缩包名字      被压缩的源数据**

```shell
$ sudo   zip    -r     /opt/stu.zip    /boot/    /etc/lsb-release 
$ ls   /opt/
```

**释放压缩包：**

```shell
$ sudo   mkdir  /aid03
$ sudo   unzip   /opt/stu.zip   -d    /aid03/
$ ls   /aid03
$ ls   /aid03/etc
$ ls   /aid03/boot
```



## 二、管理用户与组：

**系统用户：**1.登录操作系统    2.权限不同
       组：方便管理用户
       唯一标识： UID    GID
       

**组分类：**基本组   附加组
   一个用户必须至少属于 一个组

```shell
tarena@tedu:~$ useradd aid01
```

创建同名组：aid01组      将aid01用户加入到aid01组
自行创建组：财务组  销售组  帅哥组   美女组     将aid01用户加入

#### 总结：

aid01用户一共属于5各组：aid01组  财务组  销售组  帅哥组   美女组 
            aid01组为aid01用户的基本组
            财务组  销售组  帅哥组   美女组为aid01用户的 附加组

#### 一、创建用户：adduser   useradd

```shell
tarena@tedu:~$ sudo adduser aid02           #交互式创建
tarena@tedu:~$ sudo useradd  -m  aid03    #非交互式创建
             -m：创建用户的家目录

tarena@tedu:~$ id  aid02     #查询存在用户的信息
tarena@tedu:~$ id  aid03     #查询存在用户的信息
```

用户家目录：存放用户个性化信息的目录
管理员root的家目录：/root
存放 所有普通用户的家目录：/home

  **~:表示家目录**

```shell
tarena@tedu:~$ sudo useradd -m aid04
tarena@tedu:~$ ls /home/
```

**/etc/passwd:存放所有用户信息的配置文件**

```shell
tarena@tedu:~$ tail -1 /etc/passwd
aid04:x:1003:1003::/home/aid04:/bin/sh
```

用户名:密码占位符:UID:基本组GID:用户描述:家目录:解释器程序

**/etc/shadow：存放密码信息的配置文件**

```shell
tarena@tedu:~$ sudo grep   aid   /etc/shadow
```



#### 二、设置用户密码

```shell
tarena@tedu:~$ sudo passwd aid0
输入新的 UNIX 密码： 
重新输入新的 UNIX 密码： 
passwd：已成功更新密码
tarena@tedu:~$ sudo grep aid /etc/shadow

```

**非交互式设置密码  echo    用户名：密码     |    sudo  chpasswd** 

```shell
$ sudo   useradd   -m  tom    #创建用户并且创建家目录
$ id  tom

$ sudo  grep  tom   /etc/shadow
#修改密码
$ echo  tom:123    |    sudo    chpasswd 
$ sudo  grep    tom    /etc/shadow
```

#### 三、删除用户

   **userdel**
    **-r：递归删除，删除用户的家目录以及用户的邮件文件**

```shell
tarena@tedu:~$ sudo    userdel    aid02
tarena@tedu:~$ id    aid02
id: "aid02": no such user
tarena@tedu:~$ ls   /home/

tarena@tedu:~$ sudo   userdel    -r    aid03
userdel: aid03 邮件池 (/var/mail/aid03) 未找到
tarena@tedu:~$ ls    /home/
```

#### 四、 组管理  

```shell
tarena@tedu:~$ sudo  groupadd   tedu           #创建组账号
```

**组信息存放的配置文件:/etc/group**

```shell
tarena@tedu:~$ grep   tedu   /etc/group
  tedu:x:1005:
```

**组名:密码占位符:GID:组的成员列表**

```shell
tarena@tedu:~$ sudo  gpasswd   -a   tom    tedu    #添加组成员
tarena@tedu:~$ grep   tedu   /etc/group
tarena@tedu:~$ id   tom

tarena@tedu:~$ sudo   gpasswd   -a   aid04   tedu   #添加组成员
tarena@tedu:~$ grep  tedu   /etc/group

tarena@tedu:~$ sudo   gpasswd  -d   aid04    tedu  #删除组成员
tarena@tedu:~$ grep   tedu   /etc/group
```

**组的删除：groupdel  组名**

```shell
tarena@tedu:~$ sudo   groupdel   tedu
tarena@tedu:~$ grep  tedu    /etc/group
```

## 三、权限和归属：

**基本权限** 
            r：读入权限
           w：写入权限
            x：执行权限
**文本文件**：
            r：cat  head  tail  
            w：vim    >     >> 
            x: Shell脚本  Python脚本 cd
**归属关系：**
        所有者（属主）：数据创建者			u
        所属组（属组）：所有者的基本组
        其他人：除了所有者与所属组成员其余的用户    o

​	d  rwx  r-x  r-x    d表示目录文件,前3个rwx 表示所有者权限，中间3个为所属组，后面三个为其他人

​	   zhangsan    zhangsan组    1.txt

**查看权限：  ls  -l  或  ls  -ld**

- 以-开头为文本文件
- 以d开头为目录

```shell
tarena@tedu:~$ ls   -ld   /etc
tarena@tedu:~$ ls   -ld   /home/tarena
tarena@tedu:~$ ls   -ld   /root
tarena@tedu:~$ ls   -l    /etc/passwd
tarena@tedu:~$ ls   -l    /etc/shaow
```

**Linux判断用户具备的权限：匹配即停止(短路原则)**
  1.判断用户对于该数据所处的身份      所有者>所属组>其他人
  2.查看相应身份权限位置表示

**命令行临时切换用户身份： su  -   用户**

```shell
$ sudo  useradd   -m   harry
$ echo  harry:123   |    sudo  chpasswd 
$ sudo  usermod  -s  /bin/bash   harry     #修改用户解释器程序
$ grep  harry  /etc/passwd
```

  **Ctrl + shift  +t  : 新开一个终端**

```shell
tarena@tedu:~$ sudo   mkdir  /aid10 
tarena@tedu:~$ sudo   touch  /aid10/1.txt
tarena@tedu:~$ sudo   vim    /aid10/1.txt 
AAAAAAAAAA

$ sudo  chmod   o+w   /aid10/1.txt      #o表示其他人加上w权限,u表示拥有者,直接+w,所有人加读权限
$ ls   -l   /aid10/1.txt
```

**目录权限管理：** 
    r：显示目录内容
    w：可以在此目录下新建  删除  复制 移动.... 子文件或子目录
    x：用户切换到该目录

**归属关系的修改： chown   所有者：所属组      参数**

```shell
tarena@tedu:~$ sudo  mkdir   /aid11
tarena@tedu:~$ ls -ld  /aid11
tarena@tedu:~$ sudo   groupadd   study
tarena@tedu:~$ sudo  chown   harry:study    /aid11#仅修改所有者和所属组
tarena@tedu:~$ ls   -ld   /aid11

tarena@tedu:~$ sudo  chown   root    /aid11         #仅修改所有者
tarena@tedu:~$ ls   -ld   /aid11

tarena@tedu:~$ sudo  chown   :tarena    /aid11     #仅修改所属组
tarena@tedu:~$ ls   -ld   /aid11



sudo chown -R ubuntu:ubuntu Travel/ #递归修改目录下的所有文件的权限
```



## 四、进程管理：

  **程序：**静态的代码  占用硬盘空间

  **进程：**动态执行的代码    占用CPU 与 内存

  父进程与子进程   树型结构     僵尸进程/孤儿进程
   		进程标识：PID

#### 1.查看进程：

**systemd：**所有进程父进程，上帝进程

**pstree ：**结构非常优秀
		-p：进程的PID            

```shell
tarena@tedu:~$ pstree  -p   |   grep   mysql
```

 **ps  aux ：**正在运行的所有进程详细信息

```shell
tarena@tedu:~$ ps  aux
```

**pgrep :检索进程信息**,PID

```shell
tarena@tedu:~$ pgrep   oneko
15490
tarena@tedu:~$ pgrep   -l  oneko      #-l：显示完整进程名
15490 oneko
```

**top：**动态的排名    按P（大写）进行CPU排序(默认)
                                  按M（大写）进行内存排序

####  2.进程前后台调度

​	**• 后台启动** 
​	– 在命令行末尾添加“&”符号,不占用当前终端,后台启动
​	**• Ctrl + z 组合键**
​	– 挂起当前进程(暂停并转入后台)	
​	**• jobs 命令**
​	– 查看后台任务列表
​	**• fg 命令**
​	– 将后台任务恢复到前台运行
​	**• bg 命令**
​	– 激活后台被挂起的任务

####   3.杀死进程

​      **kill：** 结合PID进行杀死，支持 -9选项  强制杀
​      **killall:**结合进程名进行杀死，支持 -9选项  强制杀
​      **pkill：**模糊进行匹配进程名

​	**杀死一个用户开启的所有进程：有登录的状态变成未登录**

```shell
killall  -9  -u   用户名
```

####   4.查看当前系统监听的端口：netstat  -anptu  

​     -a：所有正在监听         -n：数字方式显示
​     -p：显示协议信息          -t：tcp协议
​     -u：udp协议
