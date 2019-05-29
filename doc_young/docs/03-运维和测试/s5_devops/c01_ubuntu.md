# ubuntu

## 1.端口

### 1.1查看本地端口开启情况（启动）

```bash
sudo ufw status|start
```

### 1.2打开80端口

```bash
sudo ufw allow 80
```

### 1.3防火墙开启开机自启

```bash
sudo ufw enable
```

### 1.4防火墙重启

```bash
sudo ufw reload
```

## 2.重置root密码

```bash
sudo passwd
```

更新密码即可

## 3.ubuntu 软件安装

### 3.1chrome

```bash
sudo wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add
sudo apt update
sudo apt install google-chrome-stable
```

### 3.2输入法

default
当然Ubuntu已经为我们提供了ppa源来安装

```bash
sudo add-apt-repository ppa:jonathonf/vim
sudo apt update
sudo apt install vim
```

如果您想要卸载它, 请使用如下命令

```bash
sudo apt remove vim
sudo add-apt-repository --remove ppa:jonathonf/vim
```



