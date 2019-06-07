## mkdocs

### 安装mkdocs

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

### 安装第三方主题

```bash
pip install material
theme: material
```

### 后台启动并指定端口

```bash
nohup mkdocs serve --dev-addr 10.0.18.19:8000 &
nohup mkdocs serve --dev-addr 0.0.0.0:8000 & # 全网指定端口
```

