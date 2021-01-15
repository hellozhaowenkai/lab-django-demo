FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir \
  -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
  -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "sh", "./run/setup.sh" ]
