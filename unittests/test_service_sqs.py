__author__ = 'philipp'
import unittest,sys,os
sys.path.append(os.path.join(os.path.abspath('..'),'service'))
from sqs import SQS
class MailerTestCase(unittest.TestCase):
    def test_sqs(self):
        self.assertEqual(1,1)


