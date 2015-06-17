__author__ = 'philipp'
from leancloud import Object

class Mail(Object):
    @property
    def subject(self):
        return self.get('subject')

    @subject.setter
    def subject(self, value):
        return self.set('subject', value)
