__author__ = 'philipp'
import time
while True:
    try:
        a = 1/0
    except StandardError, e:
        print 'Error:',e
    finally:
        time.sleep(10)