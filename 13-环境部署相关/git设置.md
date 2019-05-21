### git安装后初始化
    

```
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"

```

```
git config --global user.name "young" 
git config --global user.email "2932045582@qq.com"
```

一次提交多个文件
```
git status 
git add -A
git commit -a -m"first commit"
```
提交到版本库
```
git push
```



```

git add -A  提交所有变化
git add -u  提交被修改(modified)和被删除(deleted)文件，不包括新文件(new)
git add .  提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件
```

```
ssh-keygen -t rsa -C "youremail@example.com"

```

提交到远程
```

git push origin master
```
