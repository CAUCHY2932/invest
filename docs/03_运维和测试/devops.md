# 1.ubuntu

端口操作


```bash
# 端口操作
sudo ufw status|start  # 查看端口开启情况
sudo ufw allow 80  # 打开80端口
sudo ufw enable  # 防火墙开启开机自启
sudo ufw reload  # 防火墙重启
```
密码

```bash
# 重置密码
sudo passwd
```
软件安装

```bash
# 软件安装
# chrome
sudo wget http://www.linuxidc.com/files/repo/google-chrome.list -P /etc/apt/sources.list.d/
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add
sudo apt update
sudo apt install google-chrome-stable
# 输入法
# 1.1 安装命令（ppa源）
sudo add-apt-repository ppa:jonathonf/vim
sudo apt update
sudo apt install vim
# 1.2 卸载命令
sudo apt remove vim
sudo add-apt-repository --remove ppa:jonathonf/vim
```

# 2.centos



# 3.vim



# 4.zsh



# 5.docker

