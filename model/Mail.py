__author__ = 'philipp'
from leancloud import Object

class Mail(Object):
    @property
    def subject(self):
        # 可以使用property装饰器，方便获取属性
        return self.get('subject')

    @subject.setter
    def subject(self, value):
        # 同样的，可以给对象的score增加setter
        return self.set('subject', value)
