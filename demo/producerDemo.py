__author__ = 'philipp'
import time
import datetime
import leancloud

from leancloud import Query,Object
leancloud.init('73b6c6p6lgs8s07m6yaq5jeu7e19j3i3x7fdt234ufxw9ity', 'h5lu7ils6mutvirgrxeodo6xfuqcgxh4ny0bdar3utl076cu')

import sys,os
sys.path.append(os.path.join(os.path.abspath('..'),'service'))
from sqs import SQS
now = datetime.datetime.now()
oneMinuteAfter = now + datetime.timedelta(seconds = 300)
timestamp = int(time.mktime(oneMinuteAfter.timetuple()))
print timestamp

Timer = Object.extend('Timer')
query = Query(Timer)
query.equal_to('status', 'unsent')
query.less_than('timestamp',timestamp)
timers = query.find()
for timer in timers:
    print timer.get('mailId')
    print timer.get('status')
    mailId = timer.get('mailId')
    queue = SQS()
    queue.write(mailId)
    timer.set('status','queued')
    timer.save()