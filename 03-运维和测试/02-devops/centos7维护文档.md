# 维护文档


## centos7开启端口

添加端口
firewall-cmd --zone=public --add-port=80/tcp --permanent    （--permanent永久生效，没有此参数重启后失效）
重新载入
firewall-cmd --reload
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
```bash
# visudo
```
在配置文件里找到下边的位置，并加入用户权限，保存退出
```bash
# Allow root to run any commands anywhere
user ALL=(ALL) ALL
```
这里使用/root可以快速定位

## 查找centos7的openjdk
```bash
# which java

# cd /usr/lib/jvm
```


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


## pscp传输文件

-r 拷贝整个目录

在程序所在目录启动powershell

scp root@192.168.1.1:/home/person/hww /home/person/hww/abc.sql 

输入密码

## vim相关内容



## centos关机命令

## centos7防火墙



## centos学习资料



## linux命令-系统管理



# python相关
## anaconda安装python及其学习教程

方向|工具|包|包管理方式
--|:--:|--:|--
数据分析|pycharm，vscode|numpy,pandas|pip,conda
运维|pycharm|etc|pip, conda
爬虫|pycharm|scrapy|pip,conda
web|pycharm|flask|pip,conda

## 服务器部署

### 常用镜像源

| 名字    | 源                                    |
| ------- | ------------------------------------- |
| Alibaba | https://opsx.alibaba.com/mirror       |
| 清华    | https://mirrors.tuna.tsinghua.edu.cn/ |
| 中科大  | https://mirrors.ustc.edu.cn/          |
| 豆瓣    | http://pypi.doubanio.com/simple/      |

### 查询端口

netstat -tulpn

lsof -i:9090

### 查询进程

ps -ef | grep xxx

ps aux | grep xxx

### 复制文件

cp -r sourcePath targetPath

### 删除文件

rm -rf xxx

### 移动文件

mv -r sourcePath targetPath

### 重命名文件

mv sourcePath targetPath

### 目录操作

ls -lh

### 打包、压缩

tar -zcvf target.tar.gz xxx

### 解压tar.gz

tar -zxvf target.tar.gz

### 解压zip

unzip xxx.zip

### 上传和拷贝

从远处复制文件到本地目录
scp root@10.10.10.10:/opt/soft/nginx-0.5.38.tar.gz /opt/soft/
从远处复制目录到本地（将mongodb的目录复制到本地）
scp -r root@10.10.10.10:/opt/soft/mongodb /opt/soft/
上传本地文件到远程机器指定目录
scp /opt/soft/nginx-0.5.38.tar.gz root@10.10.10.10:/opt/soft/scptest
上传本地目录到远程机器指定目录
scp -r /opt/soft/mongodb root@10.10.10.10:/opt/soft/scptest



### 启动ssh服务

rpm -qa | grep openssh-server
systemctl start sshd

### 重定向命令

ls > test.txt 如果不存在，则创建，存在则覆盖其内容

管道



ls -lh | more
# 清屏
clear
# 切换工作目录
cd
# 显示当前路径
pwd
# 创建目录
mkdir
# 删除目录
rmdir 离开目录，并且目录必须为空目录
# 删除文件
rm -f强制删除 -r 递归删除
# 建立链接文件
ln 源文件 链接文件
ln -s 源文件 链接文件
不加 -s 表示建立一个硬链接文件
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
# 拷贝文件
cp
-r 递归拷贝
-v 显示进度
-f 强制性操作
# 移动文件
mv
-f 强制性操作
-v 显示移动进度
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
# linux命令-用户、权限管理
## 查看当前用户
whoami
## 查看当前登录用户
who
## 退出登录账户
exit
## 添加用户账号
useradd [参数] 新建用户账号
-d 指定用户登录系统时的主目录，如果不使用该参数，系统自动在/home目录下建立与用户名同名目录为主目录
-m 自动建立目录
-g 指定组名称
linux每个用户都要有一个主目录，主目录就是第一次登录系统，用户的默认当前目录（/home/用户）
每一个用户都必须有一个主目录，所以用useradd创建用户的时候，一定给用户指定一个主目录
用户的主目录一般要放到根目录的home目录下，用户的主目录和用户名是相同的
如果创建用户的时候，不指定组名，那么系统会自动创建一个和用户名一样的组名
useradd -d /home/abc abc -m 创建一个abc用户，如果目录不存在，就自动创建这个目录，同时用户属于abc组
useradd -d /home/a a -g test -m 创建一个用户名字叫a，主目录在/home/a，如果主目录不存在，就自动创建主目录，同时用户属于test组
cat /etc/passwd 查看系统当前用户名
# 设置用户密码
passwd
超级用户可以使用passwd命令为普通用户设置或修改用户口令，用户也可以直接使用该命令来修改自己的口令，而无需再命令后面使用用户名
sudo passwd user1
# 删除用户
userdel
userdel abc 删除abc用户，但不会自动删除用户的主目录
userdel -r abc 删除用户，同时删除用户的主目录
# 切换用户
su
su后面可以加“-”，加与不加的区别在于，su-会切换到对应的用户时，会将当前的工作目录自动转换到切换后的用户主目录
有些平台需要在命令前加sudo，这是因为某些操作需要管理员才能操作，
sudo su - root
su - 普通用户
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



