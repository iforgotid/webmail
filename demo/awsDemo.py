__author__ = 'philipp'
import boto,base64
from boto import sqs
from boto.sqs.message import Message
access_key_id = base64.decodestring('QUtJQUlOQUdCVkRONks1RU5FNVE=')
access_key_value = base64.decodestring('T2t6elFSdGFpMjk2OUh0aEhBTStNYjFZZHdGK09KeXhESUlIcWV4cQ==')
conn = sqs.connect_to_region('us-west-2',aws_access_key_id=access_key_id,aws_secret_access_key=access_key_value)
demo_queue = conn.get_queue('demoqueue')
print demo_queue

rs = demo_queue.get_messages(10)
for record in rs:
    print record.get_body()