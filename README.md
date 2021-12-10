# lab-django-demo

## 介绍

Django 示例项目，作为相关项目的基础实践规范。

## 代号

`django-demo` -> `Django 示例`

## 开发

### 拉取仓库

```bash
# Pull repository with submodules.
git clone --recursive git@gitee.com:dyai/lab-django-demo.git
# Pull repository force to overwrite local files.
git fetch --all && git reset --hard origin/master && git pull
```

### 启动服务

```bash
# do
sh run/entry-point.sh

# or
python manage.py runserver --settings=my_site.config.development
```

## Docker

### 构建镜像

```bash
docker image build --tag=lab-django-demo:latest .
```

### 启动容器

```bash
docker container run \
  --user     $(id -u) \
  --name     lab-django-demo \
  --publish  10301:8888 \
  --volume   /dyai-app/back-end/lab-django-demo/logs:/app/logs \
  --volume   /dyai-app/back-end/lab-django-demo/databases:/app/databases \
  --volume   /dyai-app/lab-secret/settings.private.toml:/app/config/settings.private.toml \
  --restart  on-failure:3 \
  --interactive \
  --detach \
  lab-django-demo:latest
```

### 重启服务

```bash
docker container restart lab-django-demo
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
pip freeze > ./requirements.txt
# or
pipenv lock -r > ./requirements.txt
# or
poetry export --format=requirements.txt --output=./requirements.txt
# or
pipreqs --savepath=./requirements.txt .
```

### 安装依赖

```bash
# If you want to add dependencies to your project.
pip install pendulum
poetry add pendulum

# To install the defined dependencies for your project.
pip install -r requirements.txt
poetry install
```

### 虚拟环境

```bash
# If you want to get basic information about the currently activated virtual environment.
poetry env info
# If you only want to know the path to the virtual environment.
poetry env info --path
# You can also list all the virtual environments associated with the current project.
poetry env list
# Finally, you can delete existing virtual environments.
poetry env remove test-O3eWbxRl-py3.7
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

### 初始化

```bash
git submodule init
```

### 更新

```bash
git submodule update --remote --checkout
git submodule update --remote --merge
git submodule update --remote --rebase
```

### 删除

```bash
git rm -rf --cached ./my_site/restful/
vim .gitmodules
vim .git/config
rm -rf .git/module/my_site/restful/
```
