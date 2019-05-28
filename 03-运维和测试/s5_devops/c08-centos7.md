# centos7相关

## 1.centos7安装python3以及jupyter

### 1.1centos7安装python3

```bash
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
sudo sh ./Miniconda3....
conda create -n jupyter
conda activate jupyter
```

### 1.2设置pip镜像源

#### 1.2.1 直接使用pip安装

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ xxx

numpy pandas 
```

#### 1.2.2 设置永久镜像源

```bash
cat > ~/.pip/pip.conf
```

文件内容如下：

```bash
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```

```bash
pip install jupyterlab

Consider using the `--user` option or check the permissions

pip install --user jupyterlab



jupyter notebook --generate-config
```

打开ipython
ipython
from notebook.auth import passwd
passwd()
Enter password: 123456
Verify password: 123456
‘sha1:e00ee9ab9a42:22e8c0dc771612348eeee698cde8ec77fba42e7f’
exit()

sha1:1ee6f09f898e:e352babd3864f2221d538de2b001d4db95da0e2a

```
把生成的密文‘sha:xx…’复制下来
修改默认配置文件 vi ~/.jupyter/jupyter_notebook_config.py
```

c.NotebookApp.ip='*'
c.NotebookApp.allow_root = True
c.NotebookApp.password = u'sha1:e00ee9ab9a42:22e8c0dc771612348eeee698cde8ec77fba42e7f'
c.NotebookApp.open_browser = False
c.NotebookApp.port =8888
c.ContentsManager.root_dir = '/data/jupyter/root'

c.NotebookApp.allow_remote_access = True

防火墙开放8888端口

```
firewall-cmd --zone=public --add-port=8888/tcp --permanent
systemctl restart firewalld.service
iptables -L -n
```

启动jupyter notebook：

```
nohup jupyter lab --allow-root &
```

登录jupyter lab

```
http://服务器ip地址:8888/lab
```

10.10.10.100:8888/lab





## 2.关闭centos ssh服务

### 2.1关闭ssh服务

```bash
systemctl stop sshd
```

### 2.2禁止自动启动

```bash
system disable sshd
```

4、安装需要的软件包， yum-util 提供yum-config-manager功能，另外两个是devicemapper驱动依赖的

```bash
$ sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```

5、设置yum源

```bash
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

6、可以查看所有仓库中所有docker版本，并选择特定版本安装

```bash
$ yum list docker-ce --showduplicates | sort -r
```

7、安装docker

```bash
$ sudo yum install docker-ce  #由于repo中默认只开启stable仓库，故这里安装的是最新稳定版17.12.0
$ sudo yum install <FQPN>  # 例如：sudo yum install docker-ce-17.12.0.ce
```

8、启动并加入开机启动

```bash
$ sudo systemctl start docker
$ sudo systemctl enable docker
```

9、验证安装是否成功(有client和service两部分表示docker安装启动都成功了)

```bash
$ docker version

```

二、问题

1、因为之前已经安装过旧版本的docker，在安装的时候报错如下：

Transaction check error:
  file /usr/bin/docker from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
  file /usr/bin/docker-containerd from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
  file /usr/bin/docker-containerd-shim from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
  file /usr/bin/dockerd from install of docker-ce-17.12.0.ce-1.el7.centos.x86_64 conflicts with file from package docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64

2、卸载旧版本的包

```bash
$ sudo yum erase docker-common-2:1.12.6-68.gitec8512b.el7.centos.x86_64
​```bash

3、再次安装docker
​```bash
$ sudo yum install docker-ce

```

