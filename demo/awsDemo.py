__author__ = 'philipp'
import boto
from boto import sqs
conn = sqs.connect_to_region('us-west-2',aws_access_key_id='AKIAJFOWHN3R7UYL3GFA',aws_secret_access_key='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 ')
print conn.get_all_queues()