# lab-django-demo

## 介绍

Django 示例项目，作为相关项目的基础实践规范。

## 开发

### 拉取仓库

```bash
git clone --recursive git@gitee.com:dyai/lab-django-demo.git
```

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
docker image build --tag lab-django-demo:latest .
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

## 父模块开发

### 克隆

```bash
git clone --recursive
```

### 拉取

```bash
git pull --recurse-submodules=on-demand
```

### 推送

```bash
git push --recurse-submodules=on-demand
```

## 子模块开发

### 添加

```bash
git submodule add -b master git@gitee.com:dyai/lab-django-restful.git ./my_site/restful
```

### 修改

```bash
cd ./my_site/restful
git add --all
git commit
git push
```

### 初始化 & 更新

```bash
git submodule update --init --recursive --remote
```

### 删除

```bash
git rm -rf --cached ./my_site/restful/
vim .gitmodules
vim .git/config
rm -rf .git/module/my_site/restful/
```
