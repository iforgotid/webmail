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
    try:
        newMail = Mail()
        newMail.set('subject','producer mail')
        newMail.set('to',[{'email':'philipp.xue@gmail.com','type':'to'}])
        newMail.set('html','this is a mail from producer.')
        newMail.save()
        print newMail.id
        a = 1/0
    except StandardError, e:
        print 'Error:',e
    finally:
        time.sleep(60)
