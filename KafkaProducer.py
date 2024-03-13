import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers=['3.94.116.179:9092'], #change ip here
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
producer.send('demo_testing2', {"dataObjectID": "test1"})



