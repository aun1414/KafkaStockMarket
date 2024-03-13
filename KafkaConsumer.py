from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json

consumer = KafkaConsumer(
    'demo_testing2',
     bootstrap_servers=['3.94.116.179:9092'], 
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for c in consumer:
    print(c.value)