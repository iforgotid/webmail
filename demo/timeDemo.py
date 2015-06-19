__author__ = 'philipp'
import os
import time
import datetime

os.environ['TZ'] = 'Asia/Shanghai'
time.tzset()

timeStr = '2015-6-23 19:00'
timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M")

timeStamp = int(time.mktime(timeArray))
print timeStamp

now = datetime.datetime.now()
threeDayAfter = now + datetime.timedelta(days = 3)

print threeDayAfter
print int(time.mktime(threeDayAfter.timetuple()))