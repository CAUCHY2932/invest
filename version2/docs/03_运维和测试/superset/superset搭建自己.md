## 安装docker



sudo apt-get install docker.io

## 拉取镜像

sudo docker search superset

sudo docker pull amancevice/superset

## 创建启动文件夹

mkdir /opt/docker/superset

## 查看docker启动状态

sudo service docker start| stauts

## 进入命令行

然后我们使用docker ps查看到该容器信息，接下来就使用docker attach进入该容器

1. $ sudo docker attach 44fc0f0582d9 

> https://www.jianshu.com/p/e1d3e25abcba

您可以使用attach命令在docker容器中获取bash shell访问。但是您的docker容器必须以/ bin / bash启动。 使用以下语法来获取docker容器的shell访问。$ sudo docker attach <CONTAINER ID/NAME>

## docker exec

- docker exec -it {docker_id/name} /bin/bash：进入后台运行的容器的交互模式

## docker root用户进入命令行界面

exec -it --user root <container id> /bin/bash

apt-get update

apt-get isntall vim

```bash
docker exec -u 0 -it superset /bin/bash
```

0号用户就是root用户, 剩下来的就简单了



## 初始化载入样例数据

sudo docker exec -it bi superset-init

sudo docker exec -it bi superset load_examples



## 文件目录

which python

查找python的执行路径

python

查找版本

确定执行路径的包的路径



/usr/local/lib/python3.6/site-packages/superset

```
➜  ~ docker search superset
NAME                               DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
amancevice/superset                [0.26.3] Superset on Debian+Python3             129                                     [OK]
tylerfowler/superset               An extendable Docker image for Airbnb's Supe…   3

➜  ~ docker pull amancevice/superset
Using default tag: latest
latest: Pulling from amancevice/superset
0bd44ff9c2cf: Pull complete
2576b77b8a87: Pull complete
4d2fed87d171: Pull complete
Digest: sha256:d85229d3bae54cc5281e52d615a0c4752bfefa0ae62c754c598411b4f8e529cd
Status: Downloaded newer image for amancevice/superset:latest

➜  ~ mkdir /opt/docker/superset/conf & mkdir /opt/docker/superset/data

➜  ~ docker run --name superset -u 0 -d -p 8088:8088 -v /opt/docker/superset/conf:/etc/superset -v /opt/docker/superset/data:/var/lib/superset amancevice/superset
aa3fc2b4aadeecc949771844384110e7813ee028cb38bf21d8bbd73fc54c71a5

➜  ~ docker exec -it superset superset-init
Username [admin]: admin
User first name [admin]: admin
User last name [user]: admin
Email [admin@fab.org]: admin@qq.com
Password:
Repeat for confirmation:
Recognized Database Authentications.
Admin User admin created.
```

作者：adeng2016

链接：https://www.jianshu.com/p/e1d3e25abcba

来源：简书

简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。



```
#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
ROW_LIMIT = 5000

SUPERSET_WEBSERVER_PORT = 8088
#---------------------------------------------------------

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = 'sqlite:////var/lib/superset/superset.db'

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''
```



`SECRET_KEY`注意在容器启动前就设置好，值好像跟某些元数据有关系，笔者在第一次启动后修改重启容器，遇到数据源无法查看的问题。

`MAPBOX_API_KEY`是支持地图类报表的服务提供商[mapbox](https://www.mapbox.com/)的密钥，注册一个account后可得，如下图：

样例数据

```
 docker exec -it superset superset load_examples
```

## 启动命令

sudo docker run -d -p 8087:8088 -v /opt/docker/superset:/home/superset amancevice/superset

sudo docker run --detach --name bi -d -p 8087:8088 -v /opt/docker/superset:/home/superset amancevice/superset

## 查看启动的镜像

sudo docker images

## 查看启动的容器



sudo docker ps -a

查看镜像前三位id



## 创建用户和密码

sudo docker exec -it id fabmanager create-admin --app superset

## 初始化数据库

sudo docker exec -it 容器ID superset db upgrade

## 浏览器访问

http://ip:8088/

## 停止容器

sudo docker stop xxx（id）

## 文件配置

${home}/superset_config.py

## 查看docker日志

docker logs xx

```bash
python superset db upgrade
python superset load_examples
python superset init
python superset runserver
```

**创建默认角色和许可** 
docker exec -it 容器ID superset init

## 创建用户时出错



```
docker exec -it superset superset-init
```

## 移除应用容器

```
sudo docker ps -a
sudo docker rm 3b9
```

## 重启应用容器

## 重启WEB应用容器

已经停止的容器，我们可以使用命令 docker start 来启动。

```bash
runoob@runoob:~$ docker start wizardly_chandrasekhar
```

## 官方docker superset命令


