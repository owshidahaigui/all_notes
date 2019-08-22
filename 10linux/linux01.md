Linux系统第一天：
    1）Linux系统简介
    2 ) Linux系统目录结构

安装包地址：/var/cache/apt/archives/
软件源位置：/etc/apt/sources.list

![01](01.jpg)

​    3）Linux硬盘表示

```
/   根目录，也是进入文件系统的点；

/boot   系统引导启动时要加载的静态文件，内核，grub等；

/bin   系统自身启动和运行时可能会用到的核心二进制程序，不能关联至独立分区；

/sbin   管理类基本命令，不能关联至独立分区，系统启动时需要；

/lib    基本共享库文件，内核模块文件；

/lib64  64位系统辅助共享库文件存放位置；

/etc  大多数应用程序的配置文件的集中存放位置；

/home  普通用户的家目录的存放位置；

/root   管理员root的主目录；

/media 便携式设备挂载点；

/dev   设备文件及特殊文件存放位置；

/opt   第三方应用程序存放位置；

/usr  UNIX操作系统软件资源存放位置；

/var   经常发生变化的文件的存放位置；

/selinux  相关安全策略等信息的存放位置   等其他目录。
```



​    4）系统常见命令

```shell
cat /etc/lsb_release  hostname  ifconfig  lscpu
cat /proc/meminfo
cat /etc/resolv.conf   bc  date
ls  pwd  cd(绝对路径)   mkdir  touch
```

5) Linux命令行完整格式：  命令字   选项    参数
6）常见命令选项

```shell
ls：-l  -h  -A  -d
cat： -n
head与tail
rm： -r   -f
mkdir： -p
route： -n
wc: -l
du: -sh
df：-h
```

7）命令的别名
8）常见通配符使用  *  ？  []   {}
9) 常见命令与选项的使用
    cp：-r
    mv
    grep ：^开头  $结尾
    find :-name   -size

10) 命令行技巧
        重定向  
        管道操作
        Tab补全
        快捷键：
	– Ctrl + l:清空整个屏幕 
	– Ctrl + c:废弃当前编辑的命令行(结束正在运行的命令)
	– Esc + . 或 Alt + .:粘贴上一个命令的参数

## 一、Linux系统简介

什么是Linux?
Linux是一种操作系统：可以让计算机硬件正常工作

Unix/Linux发展史
• UNIX诞生，1970-1-1

Linux的诞生 
• Linux之父,Linus Torwalds
– 1991年10月,发布0.02版(第一个公开版)内核
– 1994年03月,发布1.0版内核
– 标准读音:　哩呐科斯

版本号:主版本.次版本.修订号

Linux发行版本
• 发行版的名称/版本由发行方决定
– Red Hat Enterprise Linux（RHEL） 5/6/7
– Suse Linux Enterprise 12
– Debian Linux 7.8
– Ubuntu Linux 15.04/18.04

## 二、Linux系统目录结构：树型结构

​      /  根目录：所有的数据都在此目录下（Linux系统的起点）
​       /dev:设备（键盘 鼠标  硬盘 .....）相关的数据



## 三、Linux硬盘表示:一切皆文件

```shell
 hd：IDE类型
 sd：SCSI类型

 /dev/sda :SCSI类型第一块硬盘
 /dev/sdb :SCSI类型第二块硬盘
 /dev/sdc :SCSI类型第三块硬盘
 /dev/sdd :SCSI类型第四块硬盘

 /dev/sda1 :SCSI类型第一块硬盘的第一个分区
 /dev/sda2 :SCSI类型第一块硬盘的第二个分区
```

## 四、系统常见命令

uname  -r :查看Linux内核版本

cat    /etc/lsb-release ：查看系统的版本
hostname  ：查看主机名

```shell
tarena@tedu:~$ sudo  hostname  aid 
[sudo] tarena 的密码： 
tarena@tedu:~$ hostname
aid
tarena@tedu:~$ exit
```

ifconfig  ：查看IP地址命令
IP地址：唯一标识一个节点的地址，由32个二进制数组成

```shell
tarena@tedu:~$  ifconfig  
```

127.0.0.1 ：本地回环地址   永远代表本机

```shell
tarena@tedu:~$ ping  127.0.0.1
```

Ctrl + c :结束正在运行的命令

用于实现远程管理的软件

```shell
tarena@aid:~$ sudo apt-get install openssh-server
```

lscpu：查看CPU信息

```shell
tarena@aid:~$ lscpu 
.......
型号名称：       Intel(R) Core(TM) i5-6500 CPU @ 3.20GHz
.........
    CPU:             2
.........
```

cat    /proc/meminfo ：显示内存的信息

```shell
tarena@aid:~$ cat   /proc/meminfo 
MemTotal:       10208624 kB     #一共有多少内存
.........
```

cat：查看文本文件内容
ls：查看目录内容

颜色：
    蓝色为目录
    黑色为文本文件

```shell
tarena@aid:~$ ls   /
tarena@aid:~$ ls   /dev
tarena@aid:~$ ls   /bin
tarena@aid:~$ ls   /boot
tarena@aid:~$ sudo  ls   /root
tarena@aid:~$ ls   /home
tarena@aid:~$ ls   /tmp
tarena@aid:~$ ls   /etc
tarena@aid:~$ ls   /dev/sda    #SCSI类型的设备，第一块硬盘
路径后面的/结尾，只有目录才可以有/结尾
```

pwd ：输出当前所在的位置
cd ：切换路径的操作

```shell
tarena@aid:~$ pwd
tarena@aid:~$ cd    /
tarena@aid:/$ pwd

tarena@aid:/$ cd   /boot
tarena@aid:/boot$ cd   /opt
tarena@aid:/opt$ pwd

tarena@aid:/opt$ cd   /boot
tarena@aid:/boot$ ls      #显示当前目录内容
```

绝对路径：以根起始的路径
相对路径：不以根起始的路径（以当前路径为参照的路径）

```shell
$ cd   /opt/google/
$ pwd
$ ls
$ cd   /opt/google/chrome     #绝对路径
$ pwd

$ cd     /opt/google/
$ pwd
$ ls
$ cd   chrome       #相对路径
$ pwd

  .. :上一级目录（父目录）
$ cd   /opt/
$ cd   ..
$ pwd

$ cd   /opt/google/
$ cd    ../..
$ pwd

$ cd   /opt/google/
$ cd   ..
$ pwd
```

 mkdir ：创建目录
 touch ：创建文本文件 

```shell
$ sudo  mkdir   /aid1903
[sudo] tarena 的密码： 
$ ls  /

$ sudo   mkdir  /opt/aid02    /tmp/aid03
$ ls /opt
$ ls /tmp

$ sudo  mkdir  aidfile
$ ls 

$ sudo  touch  /opt/1.txt
$ ls /opt/
```

/etc/resolv.conf ：指定DNS服务器地址的配置文件

```shell
$ cat   /etc/resolv.conf 
```

nameserver  DNS服务器地址

bc ：计算器 

```shell
tarena@aid:/$ bc
 10/3
 3
 quit
tarena@aid:/$ 
```

 date：显示日期和时间

```shell
tarena@aid:/$ date
2019年 08月 01日 星期四 11:49:50 CST
tarena@aid:/$ date  -s   '年-月-日    时：分：秒'

tarena@aid:/$ date  -s   '2008-12-1  12：12：12'
```

## 五、Linux命令行完整格式：  命令字     选项      参数

命令字：指定操作
选项：功能不同，决定执行后的结果不同
参数：命令作用的对象

```shell
$ cat  --help
$ cat  -n   /etc/lsb-release      #显示行号

$ date +%F    #显示年-月-日
2019-08-01
$ date +%Y    #显示年
2019
```



## 六、常见命令选项        最高权限的用户：root

ls   查看
        -l：以长格式显示，显示详细信息
        -h：结合-l选项以长格式显示，显示易读的容量单位
        -A ：显示目录所有内容，包括隐藏数据
        -d：显示目录本身的详细属性，结合-l选项

```shell
$ sudo  ls   /root/
$ sudo  ls   -A    /root/ 
$ sudo   mkdir    /opt/.test 
$ ls      /opt/
$ ls  -A    /opt/        #显示目录所有的内容包含，隐藏数据
$ ls    -l    /opt/
$ ls    -lh   /opt/     #显示/opt目录内容的详细属性，加上易读的单位
$ ls    -lh   /boot
$ ls    -ld   /boot     #显示/boot目录本身的详细属性
$ ls    -ld   /             #显示/目录本身的详细属性
```

cat： -n 显示行号

```shell
tarena@aid:/$ cat -n /etc/passwd
```

head与tail 查看文件

```shell
tarena@aid:/$ head -3  /etc/passwd     #显示文件内容的头3行
tarena@aid:/$ head -1  /etc/passwd    #显示文件内容的头1行
tarena@aid:/$ head -2  /etc/passwd    #显示文件内容的头2行

tarena@aid:/$ tail +2   /etc/passwd     #显示文件内容的第2行开始到结尾
tarena@aid:/$ tail -1   /etc/passwd     #显示文件内容的最后一行

tarena@aid:/$ tail -2  /etc/passwd     #显示文件内容的尾2行
```

rm： 删除
            -r:递归，目录本身以及目录下所有        
            -f：强制删除

```shell
tarena@aid:~$ sudo  rm  -rf  /mnt/aid01
tarena@aid:~$ ls   /mnt/
```

mkdir：  创建文件夹
             -p：连同父目录一同创建

```shell
tarena@aid:~$ sudo mkdir  -p   /mnt/a/b/c/d 
tarena@aid:~$ ls /mnt/

tarena@aid:~$ sudo mkdir  -p   /mnt/aid/1903 
tarena@aid:~$ ls /mnt/
```

网关地址：解决不同网络之间通信。
                   一个网络到另一个网络的关口地址

```shell
tarena@aid:~$ route  -n     #查看网关地址
内核    IP    路由表
目标             网关               子网掩码        标志  跃点   引用  使用 接口
0.0.0.0         172.40.91.1     0.0.0.0         UG    100    0        0 ens33
```

wc   -l    ：统计文本的行数

```shell
tarena@aid:~$ wc  -l   /etc/passwd
45 /etc/passwd
tarena@aid:~$ wc  -l   /etc/lsb-release 
4 /etc/lsb-release
tarena@aid:~$ 
```

du   -sh  ：统计目录总共的占用空间的大小

```shell
tarena@aid:~$ sudo  du  -sh   /opt/   /etc/   /root
tarena@aid:~$ sudo  du  -sh   /
```

/proc : 不占用硬盘的空间，反应内存数据的目录

   挂载点(访问点)：访问设备内容的入口
   挂载：mount  设备路径   挂载点目录

   由挂载点(访问点)作为入口，进行访问设备内容
   挂载点(访问点)：在Linux都为一个目录

```shell
tarena@aid:/$ sudo mkdir /mypart
tarena@aid:/$ ls /
tarena@aid:/$ ls /mypart/

tarena@aid:/$ sudo mount   /dev/sda1    /mypart/
tarena@aid:/$ ls /mypart/

tarena@aid:/$ sudo umount  /mypart    #卸载挂载点的设备
tarena@aid:/$ ls /mypart/
```

df    -h：显示所有正在挂载使用设备的使用情况

```shell
设备                                                             挂载点
/dev/sda1        20G     16G    3.1G    84%    /
```

## 七、命令的别名：简化复杂的命令

alias 自定义命名

```shell
tarena@aid:/$ hostname
tarena@aid:/$ hn
hn：未找到命令
tarena@aid:/$ alias    hn='hostname'        #定义别名
tarena@aid:/$ hn

tarena@aid:/$ alias    myls='ls    -lhA'
tarena@aid:/$ myls    /opt/

tarena@aid:/$ alias     pwd='hostname'
tarena@aid:/$ pwd
tarena@aid:/$ unalias     pwd            #删除别名
tarena@aid:/$ pwd
tarena@aid:/$ alias                         #查看当前系统所有生效的别名
```

## 八、常见通配符使用   *   ？    []     {}

/etc/：大多数配置文件所在的目录

​     *：任意多个字符
​    ？：单个字符

```shell
tarena@aid:/$ ls   /etc/*tab
tarena@aid:/$ ls   /etc/*.conf
tarena@aid:/$ ls   /etc/r*.conf
tarena@aid:/$ ls   /dev/tty*

tarena@aid:/$ ls   /dev/tty？
tarena@aid:/$ ls   /dev/tty？？
tarena@aid:/$ ls   /dev/tty？？？
```

​     []：匹配连续范围
​     {}：匹配多种不同的情况

```shell
tarena@aid:/$ ls    /dev/tty[0-9]

tarena@aid:/$ ls    /dev/tty1[0-9]

tarena@aid:/$ ls   /dev/tty{1,3,5,7,9}
tarena@aid:/$ ls   /dev/tty{1,3,5,7,9,S0}

tarena@aid:/$ ls    /dev/tty1[0-9]       /dev/tty20
tarena@aid:/$ ls    /dev/tty{1[0-9],20}
```

## 九、常见命令与选项的使用

cp 格式： cp   选项     源数据    目标路径
	 -r：递归，目录本身以及目录下所有

```shell
tarena@aid:/$ sudo   cp    /etc/passwd     /opt/
[sudo] tarena 的密码： 

tarena@aid:/$ ls   /opt/

tarena@aid:/$ sudo   cp   -r    /boot/       /opt/
tarena@aid:/$ ls   /opt/

tarena@aid:/$ sudo   cp    /etc/fstab      /opt/
tarena@aid:/$ ls   /opt/

两个参数以上，永远将最后一个参数作为目标，其余所有的参数均作为源
tarena@aid:/$ sudo cp -r /etc/shadow  /etc/lsb-release /opt/
tarena@aid:/$ ls /opt/
```

  ..  :上一级目录

  .  :代表当前路径   经常与cp连用，将数据复制到当前目录下

```shell
$ cd /etc/network/
$ pwd
$ sudo    cp    /etc/passwd     .
$ ls
```

  复制时，可以重新命名目标路径下的名称

```shell
tarena@aid:/$ sudo   cp   /etc/lsb-release     /opt/ubuntu
tarena@aid:/$ ls   /opt/

tarena@aid:/$ sudo cp -r /boot/  /opt/abc
tarena@aid:/$ ls /opt/
```

两次复制的不同：

```shell
tarena@aid:/$ sudo   mkdir      /test
tarena@aid:/$ sudo   rm -rf      /test/*
tarena@aid:/$ sudo   cp   -r   /boot/     /test/abc
                     复制/boot目录到/test目录下重新命名为abc

tarena@aid:/$ sudo   cp   -r   /boot/     /test/abc
                      复制/boot目录到/test/abc目录下

tarena@aid:/$ ls  /test
tarena@aid:/$ ls  /test/abc
```


mv格式：  mv    源数据    目标路径 

```shell
tarena@aid:/$ sudo    touch     /opt/a.txt
[sudo] tarena 的密码： 
tarena@aid:/$ sudo    mkdir    /opt/stu
tarena@aid:/$ ls     /opt/
tarena@aid:/$ ls    /opt/stu/

tarena@aid:/$ sudo   mv    /opt/a.txt     /opt/stu/
tarena@aid:/$ ls    /opt/
tarena@aid:/$ ls    /opt/stu/
```

重命名：路径不变的移动

```shell
tarena@aid:/$ sudo  mv    /opt/stu/     /opt/1903
tarena@aid:/$ ls   /opt/

tarena@aid:/$ sudo  mv    /opt/1903     /opt/aid19
tarena@aid:/$ ls   /opt/

tarena@aid:/$ sudo  mv    /opt/aid19     /opt/love
tarena@aid:/$ ls   /opt/
```

grep ：可以从文本文件内容中，过滤包含指定字符串的行

```shell
tarena@aid:/$ grep   root   /etc/passwd   #包含root的行
tarena@aid:/$ grep   bin    /etc/passwd   #包含bin的行

tarena@aid:/$ grep    ^root     /etc/passwd   #必须要以root开头
tarena@aid:/$ grep    bash$    /etc/passwd   #必须要以bash结尾
```

find ：在指定路径下查找符合条件的数据
             -name ：按照名字去查找，支持通配符
             -type：按照类型去查找，d（目录）  f（文本文件）
             -size：按照大小去查找

find格式： find  路径   条件 

```shell
tarena@aid:/$ sudo  find  /etc/  -name   "passwd"
tarena@aid:/$ sudo  find  /etc/   -name    "*tab"

tarena@aid:/$ sudo  find   /root/   -type   f      #查找是文件
tarena@aid:/$ sudo  find   /boot    -type   d     #查找是目录

tarena@aid:/$ sudo   find  /boot/   -size  +10M   #查找大于10M
tarena@aid:/$ sudo   find  /boot/   -size   -10M   #查找小于10M
```

## 十、命令行技巧

Tab补全：命令字    选项      路径

```shell
tarena@aid:/$ if（tab）（tab）  #连续按两次tab，显示已if开头的
```

if        ifdown    ifup
ifconfig  ifquery 

if        ifdown    ifup
ifconfig  ifquery 

```shell
tarena@aid:/$ ifc（tab）

tarena@aid:/$ ls    /et（tab）/ls（tab）
tarena@aid:/$ cat    /et（tab）/ls（tab）
```

重定向命令的输出： 将前面命令的输出，写入到文本文件中
       >：覆盖重定向
      >>：追加重定向

```shell
tarena@aid:/$ ls  --help 
tarena@aid:/$ ls  --help   >   /home/tarena/ls.txt 

tarena@aid:/$ hostname
1903
tarena@aid:/$ hostname    >   /home/tarena/ls.txt 
tarena@aid:/$ cat    /home/tarena/ls.txt 

tarena@aid:/$ hostname   >>    /home/tarena/ls.txt 
tarena@aid:/$ cat   /home/tarena/ls.txt 

tarena@aid:/$ echo  123
tarena@aid:/$ echo  hello
tarena@aid:/$ echo  123456

tarena@aid:/$ cat   /home/tarena/ls.txt 
```

echo 输入，input

```shell
tarena@aid:/$ echo   123456    >>   /home/tarena/ls.txt 
tarena@aid:/$ cat    /home/tarena/ls.txt 
```



  ###快捷键：
– Ctrl + l:清空整个屏幕 
– Ctrl + c:废弃当前编辑的命令行(结束正在运行的命令)
– Esc + . 或 Alt + .:粘贴上一个命令的参数
