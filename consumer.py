__author__ = 'philipp'
import sys,os,time
sys.path.append(os.path.join(os.path.abspath('.'),'service'))
from sqs import SQS
from mailer import mailer
import leancloud
from leancloud import Object
from leancloud import Query
leancloud.init('73b6c6p6lgs8s07m6yaq5jeu7e19j3i3x7fdt234ufxw9ity', 'h5lu7ils6mutvirgrxeodo6xfuqcgxh4ny0bdar3utl076cu')

while True:
    try:
        print 'start consuming:'
        queue = SQS()
        rs = queue.read()

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
    except StandardError, e:
        print 'Error:',e
    finally:
        time.sleep(60)
