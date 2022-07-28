#!/bin/sh

# nc(netcat) 主要用於TCP、UDP相關操作
# nc -z -v -n 通訊埠掃瞄(port scan)
# -n 不進行DNS查詢
# -v 顯示指令執行過程
# -z 只進行掃描 不進行任何的資料傳輸

echo "Waiting for PostreSQL..."
while ! nc -zvn 10.38.31.11 5432; do
  sleep 1
done
echo "PostreSQL started"

echo "Waiting for ElasticSearch Node 1-3..."
while ! ((nc -zvn 10.38.31.11 9200) & (nc -zvn 10.38.31.11 9201) & (nc -zvn 10.38.31.11 9202)); do
  sleep 1
done
echo "ElasticSearch Node 1-3 started"

#echo "Waiting for MQTT..."
#
#while ! nc -z mosquitto 1883; do
#  sleep 1
#done
#
#echo "MQTT started"

python test.py
