将以下内容保存到redash.yml


```yaml
# This is an example configuration for Docker Compose. Make sure to atleast update
# the cookie secret & postgres database password.
#
# Some other recommendations:
# 1. To persist Postgres data, assign it a volume host location.
# 2. Split the worker service to adhoc workers and scheduled queries workers.
version: '2'
services:
  server:
    image: redash/redash:latest
    command: server
    depends_on:
      - postgres
      - redis
    ports:
      - "5000:5000"
    environment:
      PYTHONUNBUFFERED: 0
      REDASH_LOG_LEVEL: "INFO"
      REDASH_REDIS_URL: "redis://redis:6379/0"
      REDASH_DATABASE_URL: "postgresql://postgres@postgres/postgres"
      REDASH_COOKIE_SECRET: veryverysecret
      REDASH_WEB_WORKERS: 4
    restart: always
  worker:
    image: redash/redash:latest
    command: scheduler
    environment:
      PYTHONUNBUFFERED: 0
      REDASH_LOG_LEVEL: "INFO"
      REDASH_REDIS_URL: "redis://redis:6379/0"
      REDASH_DATABASE_URL: "postgresql://postgres@postgres/postgres"
      QUEUES: "queries,scheduled_queries,celery"
      WORKERS_COUNT: 2
    restart: always
  redis:
    image: redis:3.0-alpine
    restart: always
  postgres:
    image: postgres:9.5.6-alpine
    # volumes:
    #   - /opt/postgres-data:/var/lib/postgresql/data
    restart: always
  nginx:
    image: redash/nginx:latest
    ports:
      - "80:80"
    depends_on:
      - server
    links:
      - server:redash
    restart: always
```



执行安装

```shell
docker-compose.exe -f redash.yml run --rm server create_db
```

完成后启动



```shell
docker-compose.exe -f redash.yml up 
```

OK,访问：[http://localhost/setup](https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%2Fsetup) 即可，如果设置了其他端口需要带上端口





```bash
$ docker-compose -f docker-compose.production.yml run --rm server create_db
# create tables
$ docker-compose -f docker-compose.production.yml up
```

