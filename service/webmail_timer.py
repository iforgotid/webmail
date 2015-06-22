__author__ = 'philipp'
import time
import datetime
import leancloud
import os

from leancloud import Query,Object

from sqs import SQS
from mailer import mailer
os.environ['TZ'] = 'Asia/Shanghai'
time.tzset()
leancloud.init('73b6c6p6lgs8s07m6yaq5jeu7e19j3i3x7fdt234ufxw9ity', 'h5lu7ils6mutvirgrxeodo6xfuqcgxh4ny0bdar3utl076cu')

class mail_timer:
    def produce(self):
        now = datetime.datetime.now()
        oneMinuteAfter = now + datetime.timedelta(seconds = 300)
        timestamp = int(time.mktime(oneMinuteAfter.timetuple()))
        print 'Start producing:',timestamp
        Timer = Object.extend('Timer')
        query = Query(Timer)
        query.equal_to('status', 'unsent')
        query.less_than('timestamp',timestamp)
        timers = query.find()
        for timer in timers:
            print timer.get('mailId')
            mailId = timer.get('mailId')
            queue = SQS()
            queue.write(mailId)
            timer.set('status','queued')
            timer.save()
        return self;

    def consume(self):
        queue = SQS()
        rs = queue.read()
        print 'Start consuming:'
        for record in rs:
            mailId = record.get_body()
            print mailId
            Timer = Object.extend('Timer')
            timerQuery = Query(Timer)
            timerQuery.equal_to('mailId', mailId)
            firstTimer = timerQuery.first()
            if firstTimer.get('status') != 'sent':
                Mail = Object.extend('Mail')
                query = Query(Mail)
                mailObj = query.get(mailId)
                sender = mailer()
                mailToSent = {
                    'to':mailObj.get('to'),
                    'html':mailObj.get('html'),
                    'subject':mailObj.get('subject')
                }
                sender.send(mailToSent)
                firstTimer.set('status','sent')
                firstTimer.save()
            queue.remove(record)
        return self;

