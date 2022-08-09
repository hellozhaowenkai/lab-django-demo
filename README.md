# lab-django-demo

## 介绍

Django 示例项目，作为相关项目的基础实践规范。

## 代号

`django-demo` -> `Django 示例`

## 开发

### 拉取仓库

```bash
# Clone repository with submodules.
git clone --recursive git@gitee.com:dyai/lab-django-demo.git
# Pull repository force to overwrite local files.
git fetch --all && git reset --hard origin/master && git pull
```

### 启动服务

```bash
# DO
sh run/entry-point.sh
# OR
python manage.py runserver --settings=my_site.config.development
```

## Checklist

When you use this template, try follow the checklist to update your info properly:

- [ ] Replace all `name` sections in project
- [ ] Use a new port for docker container when deploying
- [ ] Change the `base-url` value in `config/settings.toml`
- [ ] Update the `deploy.sh` and `deploy-dev.sh`
- [ ] Clean up the READMEs and update project's descriptions
- [ ] Remove the `.idea` and `.vscode` folder which contains the editor info

And, enjoy :)

## Docker

See [Deploy Script](deploy.sh).

## Git LFS

See [Git Large File Storage](https://git-lfs.github.com/).

## 依赖

### 收集依赖

```bash
pip freeze > ./requirements.txt
# OR
poetry export --format=requirements.txt --output=./requirements.txt
```

### 安装依赖

```bash
# If you want to add dependencies to your project.
pip install pendulum
# OR
poetry add pendulum

# To install the defined dependencies for your project.
pip install -r requirements.txt
# OR
poetry install
```

### 虚拟环境

```bash
# Run the script within your virtual environment.
poetry run python example.py
# Spawn a shell within your virtual environment.
poetry shell

# If you want to get basic information about the currently activated virtual environment.
poetry env info
# If you only want to know the path to the virtual environment.
poetry env info --path
# You can also list all the virtual environments associated with the current project.
poetry env list

# You can tell Poetry which Python version to use for the current project.
poetry env use test-O3eWbxRl-py3.9
# Finally, you can delete existing virtual environments.
poetry env remove test-O3eWbxRl-py3.9
```

## Database

### Admin

```bash
# Creates a superuser account.
docker container exec -it lab-django-demo sh -c 'export DJANGO_SETTINGS_MODULE=my_site.config.production && python manage.py createsuperuser'
```

### Backups

```bash
# Outputs to standard output all data in the database associated with the named application(s).
django-admin dumpdata --exclude=auth --exclude=contenttypes --database=sqlite3 --output=foo/bar/my_data.json.gz
# Searches for and loads the contents of the named fixture into the database.
django-admin loaddata --exclude=auth --exclude=contenttypes --database=mysql foo/bar/my_data.json.gz

# Loading from stdin is useful with standard input and output redirections.
django-admin dumpdata --format=json --exclude=auth --exclude=contenttypes --database=sqlite3 | django-admin loaddata --format=json --exclude=auth --exclude=contenttypes --database=mysql -
```

### Flush

```bash
# Removes all data from the database and re-executes any post-synchronization handlers.
# The table of which migrations have been applied is not cleared.
django-admin flush

# If you would rather start from an empty database and re-run all migrations, you should drop and recreate the database and then run migrate instead.
docker container exec -i lab-mysql sh -c 'exec mysql -uroot -p"$MYSQL_ROOT_PASSWORD"' < 'DROP DATABASE IF EXISTS lab-django-demo;CREATE DATABASE IF NOT EXISTS lab-django-demo;'
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
