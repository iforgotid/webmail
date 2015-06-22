__author__ = 'philipp'
import unittest,sys,os
sys.path.append(os.path.join(os.path.abspath('..'),'service'))
from mailer import mailer
class MailerTestCase(unittest.TestCase):
    def test_send_mail_to_single(self):
        message = {
            'to' : [
                {
                    'email' : 'philipp.xue@gmail.com',
                    'type' : 'to'
                }
            ],
            'subject' : 'This is a mail from python unittest'
        }
        result = mailer().send(message)
        self.assertEqual(result[0].get('status'), 'sent')

