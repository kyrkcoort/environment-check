#!/usr//bin/python
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
import configparser
import requests
from datetime import timedelta, datetime
# import logging

# logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

def connect_elasticsearch():
    es = None
    hosts = [
        "https://10.38.31.11:9200",
        "https://10.38.31.11:9201",
        "https://10.38.31.11:9202",
    ]
    # context = create_default_context(cafile="wistron-root.pem")
    es = Elasticsearch(
        hosts,
        verify_certs=False,
        http_auth=(Username, Password),
    )
    # ca_certs='./wistron-root.pem',
    # http_auth=(Username,Password),
    # use_ssl=True,
    # timeout=20,
    # max_retries=4,
    # retry_on_timeout=True

    # sniff_on_start=True,
    # sniff_on_connection_fail=True,
    # sniffer_timeout=60,
    # verify_certs=False,
    # ssl_show_warn=False,
    # connection_class=RequestsHttpConnection

    if es.ping():
        status = "Connected to ES"
        print(status)
        # logging.info("Connected to ES")
    else:
        status = "Not able to connect!"
        print(status)
        # logging.info("Not able to connect!")

    authorization = config.get("line", "line_me_authorization")
    message = f"[efp-crontab-test]\nDatetime: {datetime}\nStatus: {status}"
    line_notify(authorization, message)

    return es


def line_notify(authorization, message):
    url = "https://notify-api.line.me/api/notify"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Bearer {authorization}",
    }
    body = {"Message": f"{message}"}

    proxies = {
        "http": "http://whqproxys.wistron.com:8080",
        "https": "http://whqproxys.wistron.com:8080",
    }

    try:
        r = requests.post(url, data=body, headers=headers, proxies=proxies)
        print(r.content)

    except Exception as e:
        # 输出详细的异常信息
        print(f"Fail to request API, Error: {repr(e)}")
        # logging.error(e)



if __name__ == "__main__":
    config = configparser.RawConfigParser()
    config.read(f"/usr/src/app/config.cfg")
    Username = config.get("LoginData", "Username")
    Password = config.get("LoginData", "Password")

    datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    es = connect_elasticsearch()
