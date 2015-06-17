__author__ = 'philipp'
import webapp2
from webapp2_extras import jinja2
import leancloud
import os, sys
sys.path.append(os.getcwd()+'\\model')
form Mail import Mail
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
        newMail.set('subject','Test mail 2 subject')
        newMail.set('to',['253902456@qq.com'])
        newMail.set('html','<p>This is a test mail.</p>')
        context = {'message': 'Hello, world!'}
        self.render_response('main.html', **context)

app = webapp2.WSGIApplication([
    ('/', SendMailPage),
], debug=True)
