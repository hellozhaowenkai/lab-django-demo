FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories && \
  apk update && \
  apk add --no-cache alpine-sdk mariadb-connector-c mariadb-connector-c-dev && \
  apk add --no-cache gcc make libc-dev linux-headers pcre-dev

COPY requirements.txt ./

RUN pip install --no-cache-dir \
    -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
    -r requirements.txt

COPY . .

EXPOSE 80

ENTRYPOINT ["sh", "./run/entry-point.sh"]
