FROM python:3-alpine

ENV PYTHONUNBUFFERED=1
# ENV DJANGO_SETTINGS_MODULE=my_site.config.production

WORKDIR /app

# Alpine
RUN echo "START" \
  && sed -i "s/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g" /etc/apk/repositories \
  && apk update \
  && apk add --virtual mysqlclient-need \
    --no-cache alpine-sdk mariadb-connector-c mariadb-connector-c-dev \
  && apk add --virtual uwsgi-need \
    --no-cache gcc make libc-dev linux-headers pcre-dev \
  # && apk del mysqlclient-need uwsgi-need \
  && echo "END"

COPY requirements.txt ./

RUN pip install --no-cache-dir \
  --index-url https://pypi.tuna.tsinghua.edu.cn/simple/ \
  --requirement requirements.txt

COPY . .

# TODO: Need To Be Optimized.
RUN chmod 777 /app/logs

EXPOSE 80

ENTRYPOINT ["/bin/sh", "./entry-point.sh"]

CMD ["-m", "production"]
