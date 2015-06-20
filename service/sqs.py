__author__ = 'philipp'
from boto import sqs
from boto.sqs.message import Message
import base64
access_key_id = base64.decodestring('QUtJQUlOQUdCVkRONks1RU5FNVE=')
access_key_value = base64.decodestring('T2t6elFSdGFpMjk2OUh0aEhBTStNYjFZZHdGK09KeXhESUlIcWV4cQ==')
conn = sqs.connect_to_region('us-west-2',aws_access_key_id=access_key_id,aws_secret_access_key=access_key_value)
webmail_queue = conn.get_queue('webmail')

class SQS:
    def write(self,message):
        m = Message()
        m.set_body(message)
        webmail_queue.write(m)
    def read(self):
        rs = webmail_queue.get_messages(10)
        return rs
    def remove(self,message):
        webmail_queue.delete_message(message)