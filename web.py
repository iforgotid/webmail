__author__ = 'philipp'
import webapp2
from webapp2_extras import jinja2
import leancloud,json
import os, sys
sys.path.append(os.path.join(os.path.abspath('.'),'model'))
from Mail import Mail
leancloud.init('73b6c6p6lgs8s07m6yaq5jeu7e19j3i3x7fdt234ufxw9ity', 'h5lu7ils6mutvirgrxeodo6xfuqcgxh4ny0bdar3utl076cu')

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
        newMail = Mail()
        newMail.set('subject','Test mail 3 subject')
        newMail.set('to',['philipp.xue@qq.com'])
        newMail.set('html','This is a test mail')
        newMail.save()
        context = {'message': 'Hello, world!'}
        self.render_response('main.html', **context)
class GetJson(BaseHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        obj = {
            'success': 'some var',
            'payload': 'some var',
        }
        self.response.out.write(json.dumps(obj))
    def post(self):
        self.response.headers['Content-Type'] = 'application/json'
        data = json.loads(self.request.body)
        self.response.out.write(json.dumps(data))

app = webapp2.WSGIApplication([
    ('/', SendMailPage),
    ('/json/foo',GetJson)
], debug=True)
