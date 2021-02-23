# lab-django-demo

## 介绍

Django 示例项目，作为相关项目的基础实践规范。

## 开发

### 启动服务

```bash
# do
sh run/entry-point.sh

# or
python manage.py runserver --settings my_site.config.development
```

## Docker

### 构建镜像

```bash
docker build --tag lab-django-demo:latest .
```

### 启动容器

```bash
docker container run \
  --user $(id -u) \
  --name lab-django-demo \
  --publish 10301:80 \
  --volume /dyai-app/back-end/lab-django-demo/logs:/app/logs \
  --volume /dyai-data/back-end/lab-django-demo/databases:/app/databases \
  --env TZ=Asia/Shanghai \
  --interactive \
  --detach \
  --restart unless-stopped \
  lab-django-demo:latest
```

### 删除服务

```bash
docker container rm -f lab-django-demo
docker image rm lab-django-demo:latest
```

### 查看日志

```bash
docker container logs lab-django-demo
```

## 依赖

### 收集依赖
    
```bash
# pip install pipreqs
pipreqs .
```

### 安装依赖

```bash
pip install -r requirements.txt
```
