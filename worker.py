__author__ = 'philipp'
import time

from service.webmail_timer import mail_timer

while True:
    try:
        timer = mail_timer()
        timer.produce()
        time.sleep(3)
        timer.consume()
    except StandardError, e:
        print 'Error:',e
    finally:
        time.sleep(60)