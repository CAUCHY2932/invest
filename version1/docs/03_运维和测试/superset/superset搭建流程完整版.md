## docker安装

## 搜索镜像

## docker拉取镜像

## docker运行镜像指定目录

docker初始化配置

账号密码

初始样例



我使用docker进行安装, 本以为很简单, 中间还是遇到一些坑.

首先安装docker
创建相关目录

mkdir /dockerfs/superset/conf -p
mkdir /dockerfs/superset/data -p


创建容器

docker run -p 8088:8088 -v /dockerfs/superset/conf:/etc/superset -v mkdir /dockerfs/superset/data:/data  --name superset -d amancevice/superset:0.18.5


使用配置文件

vi /dockerfs/superset/conf/superset_config.py

输入内容
#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
ROW_LIMIT = 5000
SUPERSET_WORKERS = 4

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
SQLALCHEMY_DATABASE_URI = 'sqlite:////data/superset.db'

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''

问题就出现在sqlite的路径上, sqlite默认存储在sqlite:////home/superset/.superset/superset.db, 我这里为了以后升级, 所以切换了存储路径, 这里有两种做法

直接将/home/superset/.superset/路径映射出来
将/home/superset/.superset/superset.db文件拷贝到/data目录

我这里选择的是第二种, 坑也在这, 使用
docker exec -it superset /bin/bash
cp /home/superset/.superset/superset.db /data

失败, 发现没有权限, ls了一下才发现当前用户是非root用户, 而/data目录是root权限.
经过一番查找, 发现可以使用以下命令用root账号登陆容器
docker exec -u 0 -it superset /bin/bash

0号用户就是root用户, 剩下来的就简单了
mv /home/superset/.superset/superset.db /data


退出容器, 重启容器, 然后进行用户初始化

docker restart superset 
docker exec -it superset superset-init

作者：一根弦的风筝
链接：https://www.jianshu.com/p/a6fe79d0b1b3
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。


