# 慕课网docker笔记

**注意解决连接问题:**

```shell
sudo groupadd docker     #添加docker用户组
sudo gpasswd -a $USER docker     #将登陆用户加入到docker用户组中
newgrp docker     #更新用户组
docker ps    #测试docker命令是否可以使用sudo正常使用
```

![架构图](/home/tarena/桌面/笔记/31docker/架构图.png)

![架构2](/home/tarena/桌面/笔记/31docker/架构2.png)

## 命令小结1

| 命令          | 用途                           |
| ------------- | ------------------------------ |
| docker pull   | 从远程获取image                |
| docker build  | 创建image                      |
| docker images | 列出本地的image                |
| docker run    | 运行container(容器) ，运行程序 |
| docker ps     | 列出运行的container            |

### 命令小结2

| 命令          | 用途                           |
| ------------- | ------------------------------ |
| docker stop   | 停止运行container              |
| docker rm     | 删除container                  |
| docker rmi    | 删除image                      |
| docker cp     | 在host和container 之间拷贝文件 |
| docker commit | 保存改动为新的image            |

**代码实例：**

```shell
#运行ubuntu 镜像终端运行echo 
tarena@tarena:~$ docker run ubuntu echo hello docker  
hello docker 

#列出本地镜像
tarena@tarena:~$ docker images   
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
nginx               latest              e445ab08b2be        9 days ago          126MB
ubuntu              latest              3556258649b2        9 days ago          64.2MB

#运行一个nginx 把nginx 80端口 切换到8080端口，打开浏览器localhost:8080 
tarena@tarena:~$ docker run -p 8080:80 -d nginx
c7797340ce1a42ddb3d483765b552eb30954003a87701ae76ce24e71f771eb2a 

#列出正在运行的container
tarena@tarena:~$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                  NAMES
c7797340ce1a        nginx               "nginx -g 'daemon of…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp   unruffled_elbakyan

#将本地主页复制到运行的nginx临时文件去,刷新页面
tarena@tarena:~$ docker cp 桌面/index.html c7797340ce1a://usr/share/nginx/html

#关闭一个运行的container 后面为CONTAINER ID 
tarena@tarena:~$ docker stop c7797340ce1a
c7797340ce1
```

**持久化container配置**

```shell
#先运行
tarena@tarena:~$ docker run -p 8080:80 -d nginx
77f0d4cc22f5d152209d45732c3738034d877aa7cc3d7e7d142fd54bda14b894

#查看id
tarena@tarena:~$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
77f0d4cc22f5        nginx               "nginx -g 'daemon of…"   11 seconds ago      Up 8 seconds        0.0.0.0:8080->80/tcp   kind_swartz

#添加index.html
tarena@tarena:~/桌面$ docker cp index.html 77f0d4cc22f5://usr/share/nginx/html

#提交commit
tarena@tarena:~/桌面$ docker commit -m 'fun' 77f0d4cc22f5
sha256:12dfab92daf0ab373d3e46fc25ec7a0ead9933ce52e8a6dd03deefc0e9b3f1c9

#查看镜像，生成新镜像，无名无姓
tarena@tarena:~/桌面$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
<none>              <none>              12dfab92daf0        26 seconds ago      126MB
nginx               latest              e445ab08b2be        9 days ago          126MB
ubuntu              latest              3556258649b2        9 days ago          64.2MB

#重新提交并赋值姓名，再次查看镜像
tarena@tarena:~/桌面$ docker cp index.html 77f0d4cc22f5://usr/share/nginx/html

tarena@tarena:~/桌面$ docker commit -m 'fun' 77f0d4cc22f5 nginx-fun
sha256:317f891c8fd284061fba529b7bc7b5eeb718f69cf3693ee640d8bfd6983c39d8

tarena@tarena:~/桌面$ docker images 
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
nginx-fun           latest              317f891c8fd2        11 seconds ago       126MB
<none>              <none>              12dfab92daf0        About a minute ago   126MB
nginx               latest              e445ab08b2be        9 days ago           126MB
ubuntu              latest              3556258649b2        9 days ago           64.2MB

#删除未命名镜像，并查看
tarena@tarena:~/桌面$ docker rmi 12dfab92daf0
Deleted: sha256:12dfab92daf0ab373d3e46fc25ec7a0ead9933ce52e8a6dd03deefc0e9b3f1c9
Deleted: sha256:cef6353f76bf6c14ba92ef32332a2028a1f56a62ae0edc6874fefa4bcf423ce8

tarena@tarena:~/桌面$ docker images 
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
nginx-fun           latest              317f891c8fd2        About a minute ago   126MB
nginx               latest              e445ab08b2be        9 days ago           126MB
ubuntu              latest              3556258649b2        9 days ago           64.2MB

#查看全部container，正在运行和已经结束的
tarena@tarena:~/桌面$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
77f0d4cc22f5        nginx               "nginx -g 'daemon of…"   5 minutes ago       Exited (0) 11 seconds ago                       kind_swartz
c7797340ce1a        nginx               "nginx -g 'daemon of…"   14 minutes ago      Exited (0) 6 minutes ago                        unruffled_elbakyan
6fda9e65f71d        nginx               "nginx -g 'daemon of…"   19 minutes ago      Exited (0) 16 minutes ago                       compassionate_murdock
1b0b034ffd38        ubuntu              "echo hello docker"      22 minutes ago      Exited (0) 22 minutes ago                       quirky_bouman
8cff4a3e275a        ubuntu              "echo hello docker"      22 minutes ago      Exited (0) 22 minutes ago                       nifty_jennings
d1bff916ed8d        ubuntu              "echo hello docker"      23 minutes ago      Exited (0) 23 minutes ago                       ecstatic_chaum

#删除container，
tarena@tarena:~/桌面$ docker rm 77f0d4cc22f5  c7797340ce1a
77f0d4cc22f5
c7797340ce1a
```



## dockerfile（脚本）

##  通过编写简单的文件自创docker 镜像

**新建dockerfile文件**

```shell
touch Dockerfile 
vim Dockerfile
'''
FROM alpine:latest
MAINTAINER xbf
CMD echo "hello docker "  #终端运行打印,CMD为镜像入口
'''
```

**提交到远程库**

```shell
#运行创建镜像，-t 表示增加标签（tag），hello_docker 为镜像名，  ‘.’表示文件在当前文件夹
tarena@tarena:~/桌面/docker$ docker build -t hello_docker .
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM alpine:latest	#第一步完成
latest: Pulling from library/alpine
050382585609: Pull complete 
Digest: sha256:6a92cd1fcdc8d8cdec60f33dda4db2cb1fcdcacf3410a8e05b3741f44a9b5998
Status: Downloaded newer image for alpine:latest
 ---> b7b28af77ffe
Step 2/3 : MAINTAINER xbf		#第二步完成
 ---> Running in 28f891416a13
Removing intermediate container 28f891416a13
 ---> 48f59d97b3b4
Step 3/3 : CMD echo "hello docker "	#第三步完成
 ---> Running in aaecbb6753d0
Removing intermediate container aaecbb6753d0
 ---> c7dd3b554027
Successfully built c7dd3b554027
Successfully tagged hello_docker:latest
#查看是否镜像
tarena@tarena:~/桌面/docker$ docker images hello_docker 
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello_docker        latest              c7dd3b554027        29 seconds ago      5.58MB
```

**运行新镜像**

```shell
tarena@tarena:~/桌面/docker$ docker run hello_docker
hello docker #打印成功
```

## Dockerfile 实战

**新建文件**Dockerfile

```
FROM ubuntu  #基础镜像
MAINTAINER xbf  #维护人员
#run 是创建容器。 cmd 创建后自动执行
RUN sed -i 's/archive.ubuntu.com/mirros.ustc.edu.cn/g' /etc/apt/sources.list #修改下载源
RUN apt-get update  #运行命令
RUN apt-get install -y nginx #安装nginx， -y 表示不用提醒直接安装
COPY index.html /var/www/html  #复制index.html 到指定位置
ENTRYPOINT ["/usr/sbin/nginx","-g","daemon off;"]  #给出一个容器入点，要使用的命令行，元素之间用命令行隔开,作用是将nginx 在前台来执行而不是守护进程,注意：命令和数组之间要有空格隔开
EXPOSE 80   #端口

#开始构建镜像
docker build -t xbf/hello-nginx .
#构建完成
```

**运行镜像**

```

```



## Dockerfile 语法（1）

| 命令   | 用途                             |
| ------ | -------------------------------- |
| FROM   | base image，从哪里开始           |
| RUN    | 执行命令                         |
| ADD    | 添加文件，可以将远程文件添加进去 |
| COPY   | 拷贝文件                         |
| CMD    | 执行命令，执行入口               |
| EXPOSE | 暴露端口                         |

## Dockerfile 语法（2）

| 命令       | 用途                      |
| ---------- | ------------------------- |
| WORKDIR    | 指定路径                  |
| MAINTAINER | 维护者                    |
| ENV        | 设置环境变量              |
| ENTRYPOINT | 容器入口，优先级比CMD高   |
| USER       | 指定用户                  |
| VOLUME     | mount point，容器挂载的卷 |

