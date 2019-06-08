## centos

### 1.centos7安装python3以及jupyter

```bash
# 1.1centos7安装python3
# https://docs.conda.io/en/latest/miniconda.html
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
sudo sh ./Miniconda3....
conda create -n jupyter
conda activate jupyter

```



### 1.2设置pip镜像源

```bash
# 1.2.1 直接使用pip安装
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ xxx

numpy pandas 

#### 1.2.2 设置永久镜像源

cat > ~/.pip/pip.conf

#文件内容如下：
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```

### 安装jupyter lab
```bash
pip install jupyterlab

Consider using the `--user` option or check the permissions

pip install --user jupyterlab



jupyter notebook --generate-config

打开ipython
ipython
from notebook.auth import passwd
passwd()
Enter password: 123456
Verify password: 123456
‘sha1:e00ee9ab9a42:22e8c0dc771612348eeee698cde8ec77fba42e7f’
exit()

sha1:1ee6f09f898e:e352babd3864f2221d538de2b001d4db95da0e2a

把生成的密文‘sha:xx…’复制下来
修改默认配置文件 vi ~/.jupyter/jupyter_notebook_config.py

c.NotebookApp.ip='*'
c.NotebookApp.allow_root = True
c.NotebookApp.password = u'sha1:e00ee9ab9a42:22e8c0dc771612348eeee698cde8ec77fba42e7f'
c.NotebookApp.open_browser = False
c.NotebookApp.port =8888
c.ContentsManager.root_dir = '/data/jupyter/root'

c.NotebookApp.allow_remote_access = True

```
### 端口操作

```bash
# centos7开启端口

添加端口
firewall-cmd --zone=public --add-port=80/tcp --permanent # 添加端口 
firewall-cmd --reload # 重新载入端口
查看
firewall-cmd --zone=public --query-port=80/tcp
删除
firewall-cmd --zone=public --remove-port=80/tcp --permanent


# 防火墙开放8888端口

firewall-cmd --zone=public --add-port=8888/tcp --permanent
systemctl restart firewalld.service
iptables -L -n

启动jupyter notebook：

nohup jupyter lab --allow-root &

登录jupyter lab

http://服务器ip地址:8888/lab

10.10.10.100:8888/lab


2、安装firewalld
root执行 # yum install firewalld firewall-config
 
3、运行、停止、禁用firewalld
启动：# systemctl start  firewalld
查看状态：# systemctl status firewalld 或者 firewall-cmd --state
停止：# systemctl disable firewalld
禁用：# systemctl stop firewalld

# 启动时自动开启
systemctl enable firewalld
```
### ssh

```bash
rpm -qa | grep openssh-server
systemctl start sshd
# ifconfig命令不存在
sudo yum install net-tools
在安装的时候选择 网络部分，网络地址转换(NAT) 模式，安装好之后 ：
这里宿主机是win7，ip是192.168.52.238  虚拟机ip为10.0.2.15  我们用端口40001来转发虚拟机的22端口 

设置好之后就能在宿主机里用 sercurecrt 登陆虚拟机了

用这种方式，虚拟机既能访问外网，主机又能ssh上去管理虚拟机，而且最重要的是虚拟机在局域网环境内不需要再分配独立的ip（用主机的ip加指定端口）

同样的，在虚拟机里也能通过ssh 访问宿主机同网段的其他机器

在本机ssh远程
ssh root@本机ip -p 40001

### 2.1关闭ssh服务

systemctl stop sshd

### 2.2禁止自动启动

system disable sshd
```
### docker
```bash
4、安装需要的软件包， yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的

$ sudo yum install -y yum-utils device-mapper-persistent-data lvm2

5、设置yum源

$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

6、可以查看所有仓库中所有docker版本，并选择特定版本安装

$ yum list docker-ce --showduplicates | sort -r

7、安装docker

$ sudo yum install docker-ce  #由于repo中默认只开启stable仓库，故这里安装的是最新稳定版17.12.0
$ sudo yum install <FQPN>  # 例如：sudo yum install docker-ce-17.12.0.ce

8、启动并加入开机启动

$ sudo systemctl start docker
$ sudo systemctl enable docker

9、验证安装是否成功(有client和service两部分表示docker安装启动都成功了)

$ docker version


二、问题

1、因为之前已经安装过旧版本的docker，在安装的时候报错如下：

Transaction check error:
  file /usr/bin/docker from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
  file /usr/bin/docker-containerd from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
  file /usr/bin/docker-containerd-shim from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
  file /usr/bin/dockerd from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64

2、卸载旧版本的包

$ sudo yum erase docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64

3、再次安装docker
$ sudo yum install docker-ce

```


### wifi连接
```bash
一：所用命令
dmesg | grep firmware（看看有没有来自无线网卡的固件请求）
iw：
     iw dev(查找无线网卡口)
     iw wls1 link(查看wls1网口无线网络连接情况)
     iw wls1 scan | grep SSID(查看wls1网口可连接的wifi)
ip：
     ip link set wls1 up(将无线网口wls1开启)
     ip link show wls1(显示无线网口wls1连接情况)
     ip addr  show wls1(显示分配的ip地址，特别适用于查看是否成功地通过dhcp自动获取了ip地址) 
wpa_supplican:
     wpa_supplicant -B -i wlp3s0 -c <(wpa_passphrase "ssid" "psk") (连接无线网ssid，密码psk)
dhclient:
     dhclient wls1(为wls1分配ip地址)
如需使用上述命令，只需将wls1直接更换成自己网口就行了

二：具体过程：
查看是否需要安装固件
大多无线网卡还需要固件。内核一般会自动探测并加载两者，如果您得到类似 SIOCSIFFLAGS: No such file or directory 的输出，意味着您得手动加载固件。若不确定，用 dmesg 查询内核日志，看看有没有来自无线网卡的固件请求。比如您有 Intel 芯片组，输出大概是这样：

### dmesg | grep firmware

firmware: requesting iwlwifi-5000-1.ucode
若无输出，表明系统的无线芯片不需要固件。
查看无线网口：

### iw dev(interface后面即为无线网口号)

激活无线网络接口：

### ip link set wls1 up 

为了检验接口是否激活成功，您可以查看以下命令的输出：

### ip link show wls1

3: wls1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state DOWN mode DORMANT group default qlen 1000 link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff 
<BROADCAST,MULTICAST,UP,LOWER_UP> 中的UP 表明该接口激活成功，后面的 state DOWN 无关紧要。
查看无线网络连接情况：

### iw wls1 link

刚开始应该会显示无连接
扫描可连接的wifi

### iw wls1 scan | grep SSID

扫描可用的网络
连接指定的SSID

### wpa_supplicant -B -i wlp3s0 -c <(wpa_passphrase "ssid" "psk") 

将ssid 替换为实际的网络名称，psk 替换为无线密码，请保留引号。
用dhcp 获得 IP 分配：

### dhclient wlp3s0 

测试是否成功地从路由器获取了ip(重要)

### ip addr  show wls1

如果分配有ip，即可上网，也可以有ping直接测试

```



### Linux下 is not in the sudoers file

```bash
xxx is not in the sudoers file. This incident will be reported

解决办法

用su换为root用户，并输入以下命令进入sudo配置文件
$ su – root
输入以下命令进入sudo配置文件

# visudo

在配置文件里找到下边的位置，并加入用户权限，保存退出

# Allow root to run any commands anywhere
user ALL=(ALL) ALL

这里使用/root可以快速定位
```

### 查找centos7的openjdk
```
# which java

# cd /usr/lib/jvm

/etc/alternatives/java_sdk_1.8.0_openjdk/lib
查找jdk

查找jdk的执行命令

$ which java

/usr/bin/java

$ ls -lrt /usr/bin/java

/usr/bin/java -> /etc/alternatives/java

$ ls -lrt /etc/alternatives/java

/etc/alternatives/java -> /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.191.b12-1.el7_6.x86_64/jre/bin/java

$ cd /etc/alternatives/java-1.8.0-openjdk-1.8.0.191.b12-1.el7_6.x86_64/
```

### centos 没有pip

```bash
pip在centos也没有，所以网上找来资料，3条语句就搞定啦！

1。查看是否安装依赖包，没安装先安装：

yum install epel-release

2。更新文件库

yum -y update

3。安装pip

yum -y install python-pip

```

### 安装openjdk

```bash

安装jre：

sudo yum install java-1.8.0-openjdk

然后会有些安装提示信息，一直“y”回车就好。

安装jdk：

sudo yum install java-1.8.0-openjdk-devel

也有些安装提示信息，一直“y”回车就好。

查看jre安装情况：

java -version

显示：

openjdk version "1.8.0_181"
OpenJDK Runtime Environment (build 1.8.0_181-b13)
OpenJDK 64-Bit Server VM (build 25.181-b13, mixed mode)

查看jdk安装情况：

javac -version

显示：
javac 1.8.0_181


2.配置环境变量。

运行命令：vim  /etc/profile

会提示文件已存在，输入“e”回车。

编辑文件，在最后加上：

#Java
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.181-3.b13.el7_5.x86_64
export CALSSPATH=$JAVA_HOME/lib/*.*
export PATH=$PATH:$JAVA_HOME/bin 

然后键盘按下“Esc”，再按下“：”双引号，输入wq回车保存退出vim编辑模式。

最后需要：

source  /etc/profile

使修改生效。

其中/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.181-3.b13.el7_5.x86_64是你的jdk的默认安装路径。
--------------------- 
作者：yzh_1346983557 
来源：CSDN 
原文：https://blog.csdn.net/yzh_1346983557/article/details/81509329 
版权声明：本文为博主原创文章，转载请附上博文链接！
```

## 安装nginx

### 一、安装编译工具及库文件

```bash
yum -y install make zlib zlib-devel gcc-c++ libtool  openssl openssl-devel
```

### 二、首先要安装 PCRE

PCRE 作用是让 Nginx 支持 Rewrite 功能。

1、下载 PCRE 安装包，下载地址： [http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz](http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz)

```bash
[root@bogon src]# cd /usr/local/src/
[root@bogon src]# wget http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz
```

2、解压安装包:

```
[root@bogon src]# tar zxvf pcre-8.35.tar.gz
```

3、进入安装包目录

```
[root@bogon src]# cd pcre-8.35
```

4、编译安装 

```
[root@bogon pcre-8.35]# ./configure
[root@bogon pcre-8.35]# make && make install
```

5、查看pcre版本

```
[root@bogon pcre-8.35]# pcre-config --version
```

### 安装 Nginx

1、下载 Nginx，下载地址：[http://nginx.org/download/nginx-1.6.2.tar.gz](http://nginx.org/download/nginx-1.6.2.tar.gz)

```
[root@bogon src]# cd /usr/local/src/
[root@bogon src]# wget http://nginx.org/download/nginx-1.6.2.tar.gz
```

2、解压安装包

```
[root@bogon src]# tar zxvf nginx-1.6.2.tar.gz
```

3、进入安装包目录

```
[root@bogon src]# cd nginx-1.6.2
```

4、编译安装

```
[root@bogon nginx-1.6.2]# ./configure --prefix=/usr/local/webserver/nginx --with-http_stub_status_module --with-http_ssl_module --with-pcre=/usr/local/src/pcre-8.35
[root@bogon nginx-1.6.2]# make
[root@bogon nginx-1.6.2]# make install
```

5、查看nginx版本

```
[root@bogon nginx-1.6.2]# /usr/local/webserver/nginx/sbin/nginx -v
```

到此，nginx安装完成。



### Nginx 配置

创建 Nginx 运行使用的用户 www：

```
[root@bogon conf]# /usr/sbin/groupadd www 
[root@bogon conf]# /usr/sbin/useradd -g www www
```

配置nginx.conf ，将/usr/local/webserver/nginx/conf/nginx.conf替换为以下内容



```
[root@bogon conf]#  cat /usr/local/webserver/nginx/conf/nginx.conf

user www www;
worker_processes 2; #设置值和CPU核心数一致
error_log /usr/local/webserver/nginx/logs/nginx_error.log crit; #日志位置和日志级别
pid /usr/local/webserver/nginx/nginx.pid;
#Specifies the value for maximum file descriptors that can be opened by this process.
worker_rlimit_nofile 65535;
events
{
  use epoll;
  worker_connections 65535;
}
http
{
  include mime.types;
  default_type application/octet-stream;
  log_format main  '$remote_addr - $remote_user [$time_local] "$request" '
               '$status $body_bytes_sent "$http_referer" '
               '"$http_user_agent" $http_x_forwarded_for';
  
#charset gb2312;
     
  server_names_hash_bucket_size 128;
  client_header_buffer_size 32k;
  large_client_header_buffers 4 32k;
  client_max_body_size 8m;
     
  sendfile on;
  tcp_nopush on;
  keepalive_timeout 60;
  tcp_nodelay on;
  fastcgi_connect_timeout 300;
  fastcgi_send_timeout 300;
  fastcgi_read_timeout 300;
  fastcgi_buffer_size 64k;
  fastcgi_buffers 4 64k;
  fastcgi_busy_buffers_size 128k;
  fastcgi_temp_file_write_size 128k;
  gzip on; 
  gzip_min_length 1k;
  gzip_buffers 4 16k;
  gzip_http_version 1.0;
  gzip_comp_level 2;
  gzip_types text/plain application/x-javascript text/css application/xml;
  gzip_vary on;
 
  #limit_zone crawler $binary_remote_addr 10m;
 #下面是server虚拟主机的配置
 server
  {
    listen 80;#监听端口
    server_name localhost;#域名
    index index.html index.htm index.php;
    root /usr/local/webserver/nginx/html;#站点目录
      location ~ .*\.(php|php5)?$
    {
      #fastcgi_pass unix:/tmp/php-cgi.sock;
      fastcgi_pass 127.0.0.1:9000;
      fastcgi_index index.php;
      include fastcgi.conf;
    }
    location ~ .*\.(gif|jpg|jpeg|png|bmp|swf|ico)$
    {
      expires 30d;
  # access_log off;
    }
    location ~ .*\.(js|css)?$
    {
      expires 15d;
   # access_log off;
    }
    access_log off;
  }

}
```

检查配置文件nginx.conf的正确性命令：

```
[root@bogon conf]# /usr/local/webserver/nginx/sbin/nginx -t
```



### 启动 Nginx

Nginx 启动命令如下：

```
[root@bogon conf]# /usr/local/webserver/nginx/sbin/nginx
```

检测是否正常启动

```bash
ps -ef | grep nginx
```

### 访问站点

从浏览器访问我们配置的站点ip：

### Nginx 其他命令

以下包含了 Nginx 常用的几个命令：

```
/usr/local/webserver/nginx/sbin/nginx -s reload            # 重新载入配置文件
/usr/local/webserver/nginx/sbin/nginx -s reopen            # 重启 Nginx
/usr/local/webserver/nginx/sbin/nginx -s stop              # 停止 Nginx
```



## 在centos7上安装mongodb

### 添加源

> vim /etc/yum.repos.d/MongoDB.repo

```
[mongodb-org-3.6]

name=MongoDB Repository

baseurl=https://repo.mongodb.org/yum/redhat/\$releasever/mongodb-org/3.6/x86_64/

gpgcheck=1

enabled=1

gpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc
```

> yum -y install mongodb-org

---> Package mongodb-org.x86_64 0:3.6.11-1.el7 will be installed
--> Processing Dependency: mongodb-org-tools = 3.6.11 for package: mongodb-org-3.6.11-1.el7.x86_64
--> Processing Dependency: mongodb-org-shell = 3.6.11 for package: mongodb-org-3.6.11-1.el7.x86_64
--> Processing Dependency: mongodb-org-server = 3.6.11 for package: mongodb-org-3.6.11-1.el7.x86_64
--> Processing Dependency: mongodb-org-mongos = 3.6.11 for package: mongodb-org-3.6.11-1.el7.x86_64
--> Running transaction check

太慢可以使用清华rpm安装







法二

https://mirrors.tuna.tsinghua.edu.cn/help/mongodb/

mongodb安装镜像帮助

新建 /etc/yum.repos.d/mongodb.repo，内容为

```
[mongodb-org]
name=MongoDB Repository
baseurl=https://mirrors.tuna.tsinghua.edu.cn/mongodb/yum/el$releasever/


```

## repo

/etc/yum.repos.d/
目录下是常用的repo文件
如sublime-text.repo