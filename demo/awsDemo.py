__author__ = 'philipp'
import boto
from boto import sqs
from boto.sqs.message import Message
conn = sqs.connect_to_region('us-west-2',aws_access_key_id='AKIAI26Z4PMM2TY53CTQ',aws_secret_access_key='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')
webmail_queue = conn.get_queue('webmail')
print webmail_queue

for i in range(1, 11):
    m = Message()
    m.set_body('This is message %d' % i)
    webmail_queue.write(m)


rs = webmail_queue.get_messages(10)
print len(rs)
print rs[0].get_body()