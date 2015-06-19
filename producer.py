__author__ = 'philipp'
import time
import leancloud
from leancloud import Object
leancloud.init('73b6c6p6lgs8s07m6yaq5jeu7e19j3i3x7fdt234ufxw9ity', 'h5lu7ils6mutvirgrxeodo6xfuqcgxh4ny0bdar3utl076cu')
class Mail(Object):
    @property
    def subject(self):
        return self.get('subject')

    @subject.setter
    def subject(self, value):
        return self.set('subject', value)
while True:
    newMail = Mail()
    newMail.set('subject','test mail123')
    newMail.set('to',[{'email':'philipp.xue@gmail.com','type':'to'}])
    newMail.set('html','this is contnet')
    newMail.save()
    print newMail.id
    time.sleep(10)
