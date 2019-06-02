## superset

```bash
docker search superset # docker 查找镜像
docker pull amancevice/superset # 拉取镜像
docker images # 查看镜像
docker run -d -p 8087:8088 -v /Users/young/super:/home/superset amancevice/superset # -v指定本地目录，冒号后面为容器内自动创建的目录
docker exec -it bi superset-init # bi替换为id或是容器名，初始化superset
docker exec -it bi superset load_examples # 载入示例数据（可选）
```

