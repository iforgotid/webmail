__author__ = 'philipp'
from leancloud import Object

class Timer(Object):
    @property
    def mailId(self):
        return self.get('mailId')

    @mailId.setter
    def subject(self, value):
        return self.set('mailId', value)