# 1.ubuntu

端口操作


```bash
# 1.端口操作
sudo ufw status|start  # 查看端口开启情况
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

# 2.centos
```bash

# centos7相关

## 1.centos7安装python3以及jupyter

### 1.1centos7安装python3

wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh
sudo sh ./Miniconda3....
conda create -n jupyter
conda activate jupyter

### 1.2设置pip镜像源

#### 1.2.1 直接使用pip安装

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ xxx

numpy pandas 


#### 1.2.2 设置永久镜像源

cat > ~/.pip/pip.conf

文件内容如下：

[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com

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

防火墙开放8888端口

firewall-cmd --zone=public --add-port=8888/tcp --permanent
systemctl restart firewalld.service
iptables -L -n

启动jupyter notebook：

nohup jupyter lab --allow-root &

登录jupyter lab

http://服务器ip地址:8888/lab

10.10.10.100:8888/lab


### 2.1关闭ssh服务

systemctl stop sshd

### 2.2禁止自动启动

system disable sshd

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
## centos7开启端口

添加端口
firewall-cmd --zone=public --add-port=80/tcp --permanent # 添加端口 
firewall-cmd --reload # 重新载入端口
查看
firewall-cmd --zone= public --query-port=80/tcp
删除
firewall-cmd --zone= public --remove-port=80/tcp --permanent

## wifi连接

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

## Linux下 is not in the sudoers file

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

## 查找centos7的openjdk

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


### 启动ssh服务

rpm -qa | grep openssh-server
systemctl start sshd

```

# 3.vim
```bash
# vim settings

> author:young

## change dir to current usr profile


$ cd ~

## edit the vimrc file

$ vim ~/.vimrc

## set the file

set ts=4
set expandtab
set autoindent
set number



## 在vim编辑器python实现tab补全功能

### 第一步:安装配置pydiction

$ wget https://github.com/rkulla/pydiction/archive/master.zip

$ unzip master.zip

$ mv pydiction-master pydiction

$ mkdir -p ~/.vim/tools/pydiction

$ cp -r pydiction/after ~/.vim

$ cp pydiction/complete-dict ~/.vim/tools/pydiction


# 确保文件结构如下

$ tree ~/.vim

/root/.vim

├── after

│ └── ftplugin

│ └── python_pydiction.vim

└── tools

└── pydiction

└── complete-dict


### 第二步:创建~/.vimrc,确保其中内容如下

$ vim ~/.vimrc

filetype plugin on

let g:pydiction_location = '~/.vim/tools/pydiction/complete-dict'

### 第三步:用vim编辑一个py文件，再输入函数时按tab补全





# 另外，Python编程是靠缩进来规定语法的，当你使用vim写python时，要注意tab与空格的区别。一般我们写Python都是以4个空格表缩进标准的，所以在代码中不要把空格与tab混用（两者ASCII码是不同的），要不一直用空格，要不就一直用tab，不然会导致程序报错。推荐把vim的tab变为4个空格，增加编程效率。

# 设置Tab键的宽度[等同的空格个数]

 set tabstop=4

# 每一次缩进对应的空格数

 set shiftwidth=4

# 按退格键时可以一次删掉4个空格

 set softtabstop=4
# 在root用户家目录下的.vimrc中设置，对所有用户生效

## setting python-mode ide

### install pathogen

mkdir -p ~/.vim/autoload ~/.vim/bundle

curl -LSso ~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim


vim ~/.vimrc
put the content in vimrc file

execute pathogen#infect()
syntax on
filetype plugin indent on


### put python-mode module in ~/.vim.bundle

cd ~/.vim/bundle

git clone https://github.com/klen/python-mode.git

### in vim file rebuild helptags

:helptags

:help filetype-plugin-on
:help filetype-indent-on

vim 
操作

# 如何与外界剪贴板进行交互

# 在按下esc后
"+y 复制到系统寄存器
"+p 粘贴到vim

# 查看当前寄存器的内容

:reg

# 安装vim

rpm -qa|grep vim
yum -y install vim*

# 复制

n+yy
复制n行
块选择模式，选中然后y复制

# 粘贴

# 删除

n+dd
# 删除连当前行的n行
# 可视化选择模式，选中然后按d删除

# 插入

i
从当前插入
A
从当前行插入

# 搜索

# 保存和退出

# 撤销


# vi/vim 中如何在每行行首或行尾插入指定字符串
行首 :%s/^/your_word/
行尾 :%s/$/your_word/

按键操作：

注释：ctrl+v 进入列编辑模式,向下或向上移动光标,把需要注释的行的开头标记起来,然后按大写的I,再插入注释符,比如”#”,再按Esc,就会全部注释了。

删除：ctrl+v 进入列编辑模式,向下或向上移动光标,选中注释部分,然后按d, 就会删除注释符号（#）。

PS：当然不一定是shell的注释符”#”，也可以是”//”，或者其他任意的字符；vim才不知道什么是注释符呢，都是字符而已。

使用替换命令：

在全部内容的行首添加//号注释

:% s/^/\/\//g

在2~50行首添加//号注释

:2,50 s/^/\/\//g

在2~50行首删除//号

:2,50 s/^\/\///g
--------------------- 
作者：sunweixiang1002 
来源：CSDN 
原文：https://blog.csdn.net/sunweixiang1002/article/details/84628287 
版权声明：本文为博主原创文章，转载请附上博文链接！

```


# 4.zsh
```bash
## check you have zsh

cat /etc/shells

# if you have not, I suggest you have a try

## install the zsh

### centos install
sudo yum -y install zsh

### ubuntu install

sudo apt-get -y install zsh


# and you can check you have zsh when you have execute above


## change your default shell to zsh

chsh -s /bin/zsh

## install enhance setting - oh my zsh!

sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"


## index back

# if you have install miniconda or conda and so on (like some setting in ~/.bashrc), it can be not work, you should copy this setting to ~/.zshrc, and use the script

source ~/.zshrc
```
# 5.docker

常用可选参数说明：

```bash
-i # 表示以“交互模式”运行容器
-t # 表示容器启动后会进入其命令行。加入这两个参数后，容器创建就能登录进去。即 分配一个伪终端。
--name # 为创建的容器命名
-v # 表示目录映射关系(前者是宿主机目录，后者是映射到宿主机上的目录，即 宿主机目录:容器中目录)，可以使 用多个-v 做多个目录或文件映射。注意:最好做目录映射，在宿主机上做修改，然后 共享到容器上。
-d # 在run后面加上-d参数,则会创建一个守护式容器在后台运行(这样创建容器后不 会自动登录容器，如果只加-i -t 两个参数，创建后就会自动进去容器)。
-p # 表示端口映射，前者是宿主机端口，后者是容器内的映射端口。可以使用多个-p 做多个端口映射
-e # 为容器设置环境变量
--network=host # 表示将主机的网络环境映射到容器中，容器的网络与主机相同
```


# 6.mkdocs

安装mkdocs
```bash
# 安装mkdocs
pip install mkdocs
# mkdocs生成工程
mkdocs new doc_young
# mkdocs设置

# 切换文件夹
cd doc_young
# 修改配置文件mkdocs.yml
site_name: My Docs
theme: readthedoc
# 启动
mkdocs serve
```

# 7.linux
```bash
# linux命令-用户、权限管理
useradd xxx # 增加一个用户
userdel -rf xxx # 删除一个用户
whoami ## 查看当前用户
who ## 查看当前登录用户
exit ## 退出登录账户

## 添加用户账号
useradd [参数] 新建用户账号
-d #指定用户登录系统时的主目录，如果不使用该参数，系统自动在/home目录下建立与用户名同名目录为主目录
-m #自动建立目录
-g #指定组名称
#linux每个用户都要有一个主目录，主目录就是第一次登录系统，用户的默认当前目录（/home/用户）
#每一个用户都必须有一个主目录，所以用useradd创建用户的时候，一定给用户指定一个主目录
#用户的主目录一般要放到根目录的home目录下，用户的主目录和用户名是相同的
# 如果创建用户的时候，不指定组名，那么系统会自动创建一个和用户名一样的组名
useradd -d /home/abc abc -m #创建一个abc用户，如果目录不存在，就自动创建这个目录，同时用户属于abc组
useradd -d /home/a a -g test -m #创建一个用户名字叫a，主目录在/home/a，如果主目录不存在，就自动创建主目录，同时用户属于test组
cat /etc/passwd #查看系统当前用户名

passwd # 设置用户密码
# 超级用户可以使用passwd命令为普通用户设置或修改用户口令，用户也可以直接使用该命令来修改自己的口令，而无需再命令后面使用用户名
sudo passwd user1


userdel # 删除用户
userdel abc #删除abc用户，但不会自动删除用户的主目录
userdel -r abc #删除用户，同时删除用户的主目录

# 切换用户
su # su后面可以加“-”，加与不加的区别在于，su-会切换到对应的用户时，会将当前的工作目录自动转换到切换后的用户主目录
# 有些平台需要在命令前加sudo，这是因为某些操作需要管理员才能操作，
sudo su - root #切换到超级用户
su - 普通用户 # 切换到普通用户

# 查看有哪些用户组
cat /etc/group
或者
groupmod + 三次tab键

# 添加、删除组账号
groupadd groupdel
groupadd 新建组账号
groupdel 删除组账号

# 修改用户所在组
usermod

## linux命令-系统管理
# 查询端口
netstat -tulpn ### 查询端口
lsof -i:9090

# 查询进程
ps -ef | grep xxx # 查询进程
ps aux | grep xxx

# 文件与目录操作
cp -r sourcePath targetPath # 复制文件
rm -rf xxx # 删除文件
mv -r sourcePath targetPath ### 移动文件
mv sourcePath targetPath ### 重命名文件

ls -lah # 列举所有文件，以人性化的方式
ls -l # 列举文件，以列表形式
cd # 切换工作目录
pwd # 显示当前路径

mkdir # 创建目录
rm -rf # 删除目录或文件 -f强制删除 -r 递归删除
cp # -r 递归拷贝 -v 显示进度 -f 强制性操作
mv # 移动文件 -f 强制性操作 -v 显示移动进度

# 建立链接文件
ln 源文件 链接文件
ln -s 源文件 链接文件 # 不加 -s 表示建立一个硬链接文件

# 压缩、解压
tar -zcvf target.tar.gz xxx ### 打包、压缩
tar -zxvf target.tar.gz ### 解压tar.gz
unzip xxx.zip ### 解压zip

### 上传和拷贝

从远处复制文件到本地目录
scp root@10.10.10.10:/opt/soft/nginx-0.5.38.tar.gz /opt/soft/
从远处复制目录到本地（将mongodb的目录复制到本地）
scp -r root@10.10.10.10:/opt/soft/mongodb /opt/soft/
上传本地文件到远程机器指定目录
scp /opt/soft/nginx-0.5.38.tar.gz root@10.10.10.10:/opt/soft/scptest
上传本地目录到远程机器指定目录
scp -r /opt/soft/mongodb root@10.10.10.10:/opt/soft/scptest


### 重定向命令

ls > test.txt # 如果不存在，则创建，存在则覆盖其内容
ls >> 001.txt # 如果不存在，则创建，存在则追加
管道
ls -lh | more

clear # 清屏

# 查看或者合并文件内容
cat xxx.file
cat test1.file test2.file > hebing.txt
cat test1.file test2.file >> hebing.txt

# 文本搜索

grep [-选项] '搜索内容串' 文件名
-v 显示不包含匹配文件的所有行，求反
-n 显示匹配行及行号
-i 忽略大小写
搜索内容串可以是正则表达式

# 查找文件

find
find ./ -name test.sh 查找当前目录下所有名为test.sh的文件
find ./ -size 2M 查找在当前目录下等于2M的文件
find ./ -size +2M 查找在当前目录下大于2M的文件
find ./ -size -2M 查找在当前目录下小于2M的文件
find ./ -size +4k -size -5M 查找在当前目录下大于4K，小于5M的文件


# 归档管理

tar
-c 生成档案文件，创建打包文件
-v 列出详细过程，显示进度
-f 指定档案文件名称，f后面一定是tar文件， 所以必须放在选项最后
-t 列出档案中包含的文件
-x 解开档案文件
tar -cvf test.tar *
tar -xvf test.tar

# 文档压缩解压

gzip [选项] 被压缩文件

-d 解压
-r 压缩所有子目录

tar只进行打包，不进行压缩
但是在tar的命令中增加一个压缩的功能，实行一个先打包后压缩的过程
如 tar -zcvf xx.tar.gz *
解压为
tar -zxvf file.tar.gz
解压到指定目录
-C 大写
tar -zxvf test.tar.gz -C xxx/

# 文件压缩解压 bzip2

压缩用法
tar -jcvf xx.tar.bz2 *
解压用法
tar -jxvf xx.tar.bz2

# 文件压缩解压 zip unzip

zip压缩的目标文件不要指定扩展名，默认扩展名为zip
压缩文件
zip [-r] 目标文件（没有扩展名） 源文件
解压文件
unzip -d 解压后目录文件 压缩文件

# 查看命令位置 which

which ls


```

# 8.python


anaconda安装python及其学习教程

| 方向     |      工具       |           包 | 包管理方式 |
| -------- | :-------------: | -----------: | ---------- |
| 数据分析 | pycharm，vscode | numpy,pandas | pip,conda  |
| 运维     |     pycharm     |          etc | pip, conda |
| 爬虫     |     pycharm     |       scrapy | pip,conda  |
| web      |     pycharm     |        flask | pip,conda  |

服务器部署常用镜像源

| 名字    | 源                                    |
| ------- | ------------------------------------- |
| Alibaba | https://opsx.alibaba.com/mirror       |
| 清华    | https://mirrors.tuna.tsinghua.edu.cn/ |
| 中科大  | https://mirrors.ustc.edu.cn/          |
| 豆瓣    | http://pypi.doubanio.com/simple/      |
```bash
# python运维相关内容
# conda使用
conda create -n py_env python=python_version # conda创建环境
conda remove -n py_env --all # conda删除环境
conda install # conda安装第三方包
conda env list # conda查看当前的虚拟环境
conda list  # conda查看安装的包
# conda切换清华源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes

source activate py_env # win下激活conda
source deactivate

conda activate py_env # mac下激活conda
conda deactivate

pip freeze > requirement.txt # 冻结包
pip install -r requirement.txt # 可以安装所有指定的包

# conda配置数据分析环境
conda create -n xxx python=3.6.8
conda install numpy=1.16.2
conda install pandas=0.24.2
conda install matplotlib=3.0.3
conda install scikit-learn=0.20.3
conda install scikit-surprise=1.0.6
conda install seaborn=0.9.0
conda install scipy=1.2.1
conda install jupyter=1.0.0
pip install -i https://pypi.doubanio.com/simple dash==0.39.0
pip install -i https://pypi.doubanio.com/simple dash-daq==0.1.0
pip install -i https://pypi.doubanio.com/simple plotly_express==0.1.3
pip install -i https://pypi.doubanio.com/simple pymysql==0.9.3

# python 爬虫环境配置
conda install scrapy=1.5.2
conda install requests=2.21.0
pip install -i https://pypi.doubanio.com/simple pillow==6.0.0
pip install -i https://pypi.doubanio.com/simple PyExecJS=1.5.1
pip install -i https://pypi.doubanio.com/simple wget==3.2
pip install -i https://pypi.doubanio.com/simple BeautifulSoup4==4.7.1
conda install scrapy
conda install requests
conda install xxx
conda install bs4

# web开发
conda install flask
conda install django
conda install pymysql
conda install pymongo

### 运维


## python gui开发

pycharm和pyqt5

> https://blog.csdn.net/zhangziju/article/details/80243858

## 环境配置

pip install PyQt5 -i https://pypi.douban.com/simple
pip install PyQt5-tools -i https://pypi.douban.com/simple

# 在pycharm，然后在设置里面点击external tools，点击“+”，需要添加Qt Designer 和pyuic 两个选项。

### Qt Designer

Name：可自己定义
program：Qt Designer的安装路径
parameter：不填
directory： $FileDir$

### pyuic

Name：可自己定义
program：pyuic的安装路径
parameter：$FileName$ -o $FileNameWithoutExtension$.py

directory： $FileDir $

## 教程

完成之后可以在pycharm中的外部工具打开qtdesigner
生成的ui文件必须是在工程文件的根目录中，然后使用pyuic生成Python文件

## python mac配置pip

mkdir ~/.pip

vim ~/.pip/pip.conf
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com

```
# 9.git

```bash

### 1.git用户配置
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
### 2.ssh-keygen
$ cat ~/.ssh/id_rsa.pub
### 3.copy to github
### 4.git clone
git clone github.com...
或者
### 5.git init

mkdir mygit
cd mygit
git init
git remote add origin github.com..

### 6.git跟踪操作

$ git add -A

### 7.git提交操作

$ git commit -m 'descriptions'

### 8.git推送操作

$ git push

### 9.git push usage

- 为了提高克隆效率，我们统一采用新的仓库方式进行代码托管
  -- 首先在github生成仓库，并克隆到本地，再推送到云端
  -- 其次，在gitee中同步github，在另一台设备进行克隆
  --两台机器都使用git remote add origin/mirror xxx进行代码远程分支的管理

git remote add origin gitee.com...
git remote add mirror github.com...
git remote -v
git push origin master/dev
git push mirror master/dev

## 经常使用的组合

### 1.配置好本地和github、gitee的秘钥

### 2.在github新建一个仓库，初始化，并在gitee导入该仓库

### 3.再进行如下操作

#### git clone git@giteexxx

使用gitee克隆，速度较快

#### git remote add mirror git@githubxxx
添加远程分支

#### git push origin master

推送到远程分支,gitee

#### git push mirror master

推送到远程分支，github

### git安装后初始化

$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"

一次提交多个文件

git status 
git add -A
git commit -a -m"first commit"

提交到版本库

git push

git add -A  提交所有变化
git add -u  提交被修改(modified)和被删除(deleted)文件，不包括新文件(new)
git add .  提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件

ssh-keygen -t rsa -C "youremail@example.com"
提交到远程

git push origin master
```

