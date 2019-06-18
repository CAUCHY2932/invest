## ubuntu

```bash

# 1.端口操作
sudo ufw status  # 查看端口开启情况
sudo ufw allow 80  # 打开80端口
sudo ufw enable  # 防火墙开启开机自启
sudo ufw reload  # 防火墙重启
# 2.重置密码
sudo passwd

# 3.软件安装
# 3.1.chrome
sudo wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add
sudo apt update
sudo apt install google-chrome-stable
# 3.2输入法
# 1.1 安装命令（ppa源）
sudo add-apt-repository ppa:jonathonf/vim
sudo apt update
sudo apt install vim
# 1.2 卸载命令
sudo apt remove vim
sudo add-apt-repository --remove ppa:jonathonf/vim

```
## 中科大源

ubuntu 18.04

```bash 
deb https://mirrors.ustc.edu.cn/ubuntu/ cosmic main restricted universe multiverse 


deb-src https://mirrors.ustc.edu.cn/ubuntu/ cosmic main restricted universe multiverse 
deb https://mirrors.ustc.edu.cn/ubuntu/ cosmic-updates main restricted universe multiverse 
deb-src https://mirrors.ustc.edu.cn/ubuntu/ cosmic-updates main restricted universe multiverse 
deb https://mirrors.ustc.edu.cn/ubuntu/ cosmic-backports main restricted universe multiverse 
deb-src https://mirrors.ustc.edu.cn/ubuntu/ cosmic-backports main restricted universe multiverse 
deb https://mirrors.ustc.edu.cn/ubuntu/ cosmic-security main restricted universe multiverse 
deb-src https://mirrors.ustc.edu.cn/ubuntu/ cosmic-security main restricted universe multiverse 
deb https://mirrors.ustc.edu.cn/ubuntu/ cosmic-proposed main restricted universe multiverse 
deb-src https://mirrors.ustc.edu.cn/ubuntu/ cosmic-proposed main restricted universe multiverse
```

## 安装mysql

>https://blog.csdn.net/weixx3/article/details/80782479

```bash
sudo apt install mysql-client-core-5.7 
sudo apt install mysql-server
sudo mysql_secure_installation
密码1234
sudo mysql -uroot -p # 无需密码正确

GRANT ALL PRIVILEGES ON *.* TO root@localhost IDENTIFIED BY "123456";
```

## 安装docker

```bash
# 配置镜像站
curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io
sudo apt-get install docker.io
sudo docker search superset
sudo docker pull amancevice/superset
sudo docker image ls
mkdir -p /opt/docker/superset
docker run -d -p 8087:8088 -v /opt/docker/superset:/home/superset amancevice/superset
sudo docker container ls
docker exec -it bi superset-init # bi替换为id或是容器名，初始化superset
docker exec -it bi superset load_examples # 载入示例数据（可选）
```

## 安装ssh

```bash
sudo apt install openssh-server

```

## 安装jdk

```bash
sudo apt install openjdk-8-jdk-headless
```





## 更改root密码

```bash
sudo passwd root
```

## sudo命令执行慢

解决 Ubuntu 下 sudo 命令执行速度慢的问题
1、首先如果当用登录的用户名不在"/etc/sudoers"文件中，是不能执行sudo命令的。可以用root身份手动修该文件，把当前登录用户名加入该文件中。
2、用"hostname "命令查看当前主机的主机名称。例如，该命令返回"yzh ".
3、用vi打开"/etc/hosts"文件，并将"ubuntu"加入到 "127.0.0.1"这行中。
例如：
127.0.0.1       localhost      ubuntu
这个问题是最近装Ubuntu Server 18.04 LTS时遇到的，之前用Ubuntu Server 16.04 LTS并没有发现这个问题.

症状：sudo速度非常慢，提交命令之后大概需要10秒左右才有输入sudo密码或者开始运行。su命令症状相同。

原因：Ubuntu Server被设计成一种类似于分布式的操作系统网结构，允许/etc/sudoers中的成员不在本机上。从而sudo时会先从网络上寻找可能的sudoer然后才是本地. 而这10s左右的时间就是整个DNS流程的最长时间.

解决方案：首先输入hostname，得到本机当前的互联网名称（大概跟windows下的计算机名称差不多）。然后使用su或sudo打开/etc/hosts，添加一行：

127.0.0.1<TAB>计算机名<TAB>计算机名.localdomain
