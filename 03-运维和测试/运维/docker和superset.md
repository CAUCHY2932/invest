##  linux上利用docker安装superset

>https://blog.csdn.net/m0_37805167/article/details/81069644

### 拉取

1.docker search superset

2.docker pull amancevice/superset

docker images  查看镜像

### superset的使用

**创建本地目录**（让容器中的superset挂载本地机的配置文件）

**开启docker容器内的superset应用，开启的同时进行端口映射，并挂载宿主机的数据**

docker ps  查**看开启的应用** 


**设定superset的用户名和密码** 
docker exec -it 容器ID  fabmanager create-admin –app superset 

**初始化数据库** 
docker exec -it 容器ID superset db upgrade



**创建默认角色和许可** 
 docker exec -it 容器ID superset init

**启动服务** 
 docker exec -it  容器ID superset runserver

## Docker容器中搭建superset

> https://blog.51cto.com/1
>
> 4033037/2329635

### 1.创建本地映射文件夹。

    mkdir opt\docker\superset

### 2.创建superset容器

    docker run -d -p 8087:8088 -v /opt/docker/superset:/home/superset amancevice/superset
    将主机的8087端口映射到容器的8088端口，同时将主机的/opt/docker/superset目录映射到容器的/home/superset目录。

### 3.配置用户名和密码。

    docker exec -it 420 fabmanager create-admin --app superset


备注：420为容器ID前三位。

### 4.初始化数据库

    docker exec -it 420 superset db upgrade

### 5.初始化superset

    docker exec -it 420 superset init

### 6.开启superset服务

    docker exec -it 420 superset runserver

### 7.访问superset

在本地浏览器地址栏输入下面的地址即可访问superset。8087为创建容器时映射的主机端口。

http://localhost:8087





## superset docker部署

> https://mp.weixin.qq.com/s?__biz=MzUyNzk4MjA5NQ==&mid=2247483743&idx=1&sn=9ccec34faf307aab2868faca6a3fdabc&chksm=fa760a3fcd018329f618320f7e4f51e01c82e739ed02817df377c7f76c39c6a07bf8f8049be8&token=1986779450&lang=zh_CN#rd



> https://www.cnblogs.com/vickey-wu/p/10205031.html

### 一、使用自己的数据库

#### 1. 拉取项目

```
// 创建目录用于存放项目
mkdir -p /mnt/superset
cd /mnt/superset
git clone https://github.com/amancevice/superset.git
```

#### 2. 配置数据库等

> 这里默认你已创建了你自己的空数据库和具有读写该数据库权限的用户，到下面初始化时会自动在你的数据库创建表结构用于导入你的数据。如果没有可以使用项目自带的demo数据库

```
进入项目目录
cd /mnt/superset/superset
按照官网文档填写配置信息
```

- `superset_config.py`[link](https://superset.incubator.apache.org/installation.html#configuration)

```
ROW_LIMIT = 5000

SUPERSET_WEBSERVER_PORT = 8088

SECRET_KEY = 'set_your_own_key'

SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@host:port/db'


# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = True
# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []
# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''
```

#### 3. 启动容器

> 注意：
>
> 1. -v 挂载配置文件必须挂载到容器的/etc/superset/superset_config.py或者/home/superset/superset_config.py，因为容器里面的环境变量是这两个，挂载到其他路径初始化数据库会不生效。
> 2. SECRET_KEY必须与superset_config.py的设置一致
> 3. 填写你自己数据库连接信息

```
docker run -d --name superset_name \
    --env SECRET_KEY="set_your_own_key" \
    --env SQLALCHEMY_DATABASE_URI="mysql://user:pass@host:port/db" \
    -p 8089:8088 \
    amancevice/superset
```

#### 4. 初始化容器

```
进入superset-init文件目录
cd /mnt/superset/superset/superset
初始化
docker exec -it superset_name superset-init
输入你设置登录superset前端的admin相关信息
Username [admin]: admin
User first name [admin]: vickey
User last name [user]: vickey
password: mypassword
repeat passwd: mypassword
输入完毕开始初始化，等待完成即可
```

#### 5.前端访问

```
http://ip:8088/
```

### 二、使用项目demo数据库

```
启动容器（假设我们创建了/mnt/superset）
cd /mnt/superset/
git clone https://github.com/amancevice/superset.git
cd superset
docker-compose up -d
docker-compose exec superset demo
前端访问
http://ip:8088/
```

### 三、参考链接

- [项目教程链接](https://github.com/amancevice/superset/blob/master/README.md)
- [配置文件链接](https://superset.incubator.apache.org/installation.html#configuration)
- [他人教程链接](https://devhub.io/repos/amancevice-superset)