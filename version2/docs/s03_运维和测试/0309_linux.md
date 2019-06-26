## linux

### linux命令

> http://www.magedu.com/74163.html?linux_wenzhang_zhihu_jinke_tiaocaobibei40ti_33967414

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
```

### 系统管理
```bash
## linux命令-系统管理
# 查询端口
netstat -tulpn ### 查询端口
lsof -i:9090

# 查询进程
ps -ef | grep xxx # 查询进程
ps aux | grep xxx

```
### 文件和目录操作
```bash

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
```
### 文本操作
```bash
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

```
### 压缩解压
```bash
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

## 查看当前日历

cal
-y 显示整年日历

## 显示或设置时间

date
date [MMDDhhmm[[CC]YY[.ss]]+format
CC为年前两位yy为年的后两位
前两位的mm为月，后两位的mm为分钟，dd为天，hh为小时，ss为秒。如： date 010203042016.55
显示时间格式
（date '+%y,%m,%d,%H,%M,%S'）

## 查看进程信息

ps process status
-a 显示终端上的所有进程，包括其他用户的进程
-u 显示进程的详细状态
-x 显示没有控制终端的进程
-w 显示加宽，以便显示更多的信息
-r 只显示正在运行的进程
常用的为
ps -aux



## 动态显示进程

top 加上-d可以指定显示信息更新的时间间隔
执行top命令之后，可以按下按键得到对显示结果进行排序
M 根据内存使用量来排序

## 终止进程

kill
kill [-signal] pid

## 关机重启

reboot 重新启动操作系统
shutdown -r now 重新启动操作系统，shutdown会给别的用户提示
shutdown -h now 立刻关机，其中now相当于时间为0的状态
shutdown -h 20:25
init

## 传输文件

```powershell
.\pscp.exe root@129.28.189.50://root/git_repos/superset.tar.gz ./
```

<<<<<<< HEAD
## 远程命令

```bash
ssh -p 4645 root@192.168.52.12
=======
## 查看有多少行文件

```bash
ls | nl
>>>>>>> f1efb493c416682a09d5487123ad3cdeadd82e56
```

