__author__ = 'philipp'
import webapp2
from webapp2_extras import jinja2
import leancloud,json
import os, sys
sys.path.append(os.path.join(os.path.abspath('.'),'model'))
sys.path.append(os.path.join(os.path.abspath('.'),'service'))
from Mail import Mail
from Timer import Timer

from mailer import mailer
leancloud.init('73b6c6p6lgs8s07m6yaq5jeu7e19j3i3x7fdt234ufxw9ity', 'h5lu7ils6mutvirgrxeodo6xfuqcgxh4ny0bdar3utl076cu')

import time,datetime,mimetypes
os.environ['TZ'] = 'Asia/Shanghai'
time.tzset()

class StaticFileHandler(webapp2.RequestHandler):
    def get(self, path):
        abs_path = os.path.abspath(os.path.join('static', path))
        if os.path.isdir(abs_path) or abs_path.find(os.getcwd()) != 0:
            self.response.set_status(403)
            return
        try:
            f = open(abs_path, 'r')
            self.response.headers['Content-Type'] = mimetypes.guess_type(abs_path)[0]
            self.response.out.write(f.read())
            f.close()
        except:
            self.response.set_status(404)

class BaseHandler(webapp2.RequestHandler):
    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)

class SendMailPage(BaseHandler):
    def get(self):
        context = {'message': 'Hello, world!'}
        self.render_response('main.html', **context)

class SendMailApi(BaseHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        data = json.loads(self.request.body)
        sender = mailer()
        sender.send(data)
        self.response.out.write(json.dumps(data))

class CreateMailTimer(BaseHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        data = json.loads(self.request.body)
        newMail = Mail()
        newMail.set('subject',data['subject'])
        newMail.set('to',data['to'])
        newMail.set('html',data['html'])
        newMail.save()
        type = data['type']
        timer = Timer()
        timer.set('mailId',newMail.id)
        timer.set('status','unsent')
        if type == 'byInterval':
            now = datetime.datetime.now()
            timeUnit = data['timeUnit']
            intervalCount = data['intervalCount']
            seconds = 0;
            if timeUnit == 'day':
                seconds = intervalCount * 86400
            elif timeUnit == 'hour':
                seconds = intervalCount * 3600
            elif timeUnit == 'minute':
                seconds = intervalCount * 60
            timeAfter = now + datetime.timedelta(seconds = seconds)
            timestamp = int(time.mktime(timeAfter.timetuple()))
        elif type == 'byTime':
            timeStr = data['timeStr']
            timeArray = time.strptime(timeStr, "%Y-%m-%d %H:%M")
            timestamp = int(time.mktime(timeArray))
        timer.set('timestamp',timestamp)
        timer.save()
        self.response.out.write(json.dumps(data))

app = webapp2.WSGIApplication([
    ('/', SendMailPage),
    ('/api/sendMail',SendMailApi),
    ('/api/createTimerForMail',CreateMailTimer),
    (r'/static/(.+)', StaticFileHandler)
], debug=True)
