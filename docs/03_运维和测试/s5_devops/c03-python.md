# python_devops

> python运维相关内容

conda使用
```bash
# conda创建指定版本
# 清华大学配置conda镜像源
conda #创建指定Python版本环境
conda create -n data python=3.6.8
# 冻结包
pip freeze > requirement.txt
# 可以输出已经安装的Python相关包
pip install -r requirement.txt
# 可以安装所有指定的包
```

数据分析
```bash
# 数据分析
conda install jupyter
conda install pandas
conda install xxx
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
```

爬虫
```bash
# python 爬虫环境配置
conda install scrapy=1.5.2
conda install requests=2.21.0
pip install -i https://pypi.doubanio.com/simple pillow==6.0.0
pip install -i https://pypi.doubanio.com/simple PyExecJS=1.5.1
pip install -i https://pypi.doubanio.com/simple wget==3.2
pip install -i https://pypi.doubanio.com/simple BeautifulSoup4==4.7.1
# conda
conda install scrapy
conda install requests
conda install xxx
conda install bs4
```
web开发
```bash
# web开发
conda install flask
conda install django
conda install pymysql
conda install pymongo
conda install xxx
```

运维
```bash
### 运维
```





## python gui开发

pycharm和pyqt5

> https://blog.csdn.net/zhangziju/article/details/80243858

## 环境配置

pip install PyQt5 -i https://pypi.douban.com/simple
pip install PyQt5-tools -i https://pypi.douban.com/simple

在pycharm，然后在设置里面点击external tools，点击“+”，需要添加Qt Designer 和pyuic 两个选项。

### Qt Designer

```
Name：可自己定义
program：Qt Designer的安装路径
parameter：不填
directory： $FileDir$
```

### pyuic

```
Name：可自己定义
program：pyuic的安装路径
parameter：$FileName$ -o $FileNameWithoutExtension$.py

directory： $FileDir $
```



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





conda创建环境
    

```
conda create -n py_env python=python_versiion
```

conda删除环境

```
conda remove -n py_env --all
```

conda安装第三方包

```
conda install
```

conda查看当前的虚拟环境

```
conda env list
```

​    
conda查看安装的包
​    
​    conda list

conda切换清华源
    
    
https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

激活conda环境

```bash
win下

source activate py_env
source deactivate

mac下
conda activate py_env
conda deactivate
```



