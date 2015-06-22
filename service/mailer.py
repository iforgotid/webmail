__author__ = 'philipp'
import mandrill
mandrill_client = mandrill.Mandrill('kSeK7plXVJ0b2JuCfSLJ5A')

class mailer:
    def send(self,message):
        message['from_email'] = 'philipp.xue@gmail.com'
        message['from_name'] = 'Xue Jiaqi'
        result = mandrill_client.messages.send(message=message, async=False)
        print result
        return result