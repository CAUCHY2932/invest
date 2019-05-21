conda创建环境
    
    conda create -n py_env python=python_versiion


conda删除环境

    conda remove -n py_env --all

conda安装第三方包

    conda install

conda查看当前的虚拟环境

    conda env list


​    
conda查看安装的包
​    
    conda list

conda切换清华源
    
    
https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
    conda config --set show_channel_urls yes

激活conda环境

```bash
win下

source activate py_env
source deactivate

mac下
conda activate py_env
conda deactivate
```
