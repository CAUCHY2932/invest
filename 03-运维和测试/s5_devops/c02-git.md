# git

## git常用命令

### 1.git用户配置

```bash
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

### 2.ssh-keygen

```bash
$ cat ~/.ssh/id_rsa.pub
```

### 3.copy to github

### 4.git clone

```bash
git clone github.com...
```

或者

### 5.git init

```bash
mkdir mygit
cd mygit
git init
git remote add origin github.com..
```

### 6.git跟踪操作

```bash
$ git add -A
```

### 7.git提交操作

```bash
$ git commit -m 'descriptions'
```

### 8.git推送操作

```bash
$ git push
```

### 9.git push usage

- 为了提高克隆效率，我们统一采用新的仓库方式进行代码托管
  -- 首先在github生成仓库，并克隆到本地，再推送到云端
  -- 其次，在gitee中同步github，在另一台设备进行克隆
  --两台机器都使用git remote add origin/mirror xxx进行代码远程分支的管理

```bash
git remote add origin gitee.com/...
git remote add mirror github.com/...
gitpush() {
git push origin "$1"
git push mirror "$1"
}

usage: gitpush master

```

或者

```bash
git remote add origin gitee.com...
git remote add mirror github.com...
git remote -v
git push origin master/dev
git push mirror master/dev
```



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



