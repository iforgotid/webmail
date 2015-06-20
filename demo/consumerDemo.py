__author__ = 'philipp'
import sys,os
sys.path.append(os.path.join(os.path.abspath('..'),'service'))
from sqs import SQS
queue = SQS()
rs = queue.read()
print len(rs)
print rs[0].get_body()

rs = queue.read()
print len(rs)
print rs[0].get_body()
