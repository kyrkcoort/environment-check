# 這個Image由IT打包，已經有一些Net tools, Crontab, Nano and Python3
FROM harbor.wistron.com/base_image/python:3.8-buster
MAINTAINER Kyrk_Coort@wistron.com

RUN apt-get update && apt-get install -y netcat

# 指定WORKDIR並複製程式碼至container中/usr/src/app的路徑下
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN chmod u+x /usr/src/app/entrypoint.sh

# 安裝套件
RUN pip --default-timeout=1000 install --upgrade pip && \
    pip3 --default-timeout=1000 install --no-cache-dir -r requirements.txt

CMD ["/usr/src/app/entrypoint.sh"]
