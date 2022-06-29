FROM python:3-alpine

ENV TZ=Asia/Shanghai
ENV PYTHONUNBUFFERED=1
# ENV DJANGO_SETTINGS_MODULE=my_site.config.production

WORKDIR /app

RUN echo "START." \
  && sed -i "s/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g" /etc/apk/repositories \
  && apk update \
  && apk add --no-cache \
    --virtual=mysqlclient-env alpine-sdk mariadb-connector-c mariadb-connector-c-dev \
  && apk add --no-cache \
    --virtual=uwsgi-env gcc make libc-dev linux-headers pcre-dev \
  # && apk del mysqlclient-env uwsgi-env \
  && echo "END."

COPY requirements.txt ./

RUN echo "START." \
  && pip install \
    --index-url    https://pypi.tuna.tsinghua.edu.cn/simple/ \
    --requirement  ./requirements.txt \
    --no-cache-dir \
  && echo "END."

COPY . .

EXPOSE 8888

ENTRYPOINT ["/bin/sh", "./entry-point.sh"]

CMD ["-m", "production"]
