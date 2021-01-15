# lab-django-demo

## 介绍

Django 示例项目，作为相关项目的基础实践规范。

## Docker

### 构建镜像

```bash
docker build --tag lab-django-demo/lasted .
```

### 启动容器

```bash
docker container run \
  --name lab-django-demo \
  --publish 10301:80 \
  --env TZ=Asia/Shanghai \
  --interactive \
  --detach \
  --restart unless-stopped \
  lab-django-demo/lasted
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

