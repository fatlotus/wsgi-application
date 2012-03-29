import util
import sys
import template
from google.appengine.ext import db
import cgi

class Person(db.Model):
  name = db.StringProperty()
  email = db.StringProperty()
  status = db.StringListProperty(default=['unvisited'])
  flash = db.StringProperty(default=None)
  
  def update_status(self, *updates):
    lst = list(self.status)
    
    for update in updates:
      if update[0] == '+':
        lst.append(update[1:])
      elif update[0] == '-':
        if update[1:] in lst:
          lst.remove(update[1:])
      else:
        lst.append(update)
    
    self.status = list(set(lst))
  
  def has_status(self, status):
    return status in self.status 

class Comment(db.Model):
  author = db.ReferenceProperty(Person)
  value = db.StringProperty()
  reply_all = db.BooleanProperty()
  from_web = db.BooleanProperty(default=True)

def handle(environ, start_response):
  try:
    code = environ['PATH_INFO'][1:]
    
    me = Person.get_by_key_name(code)
    
    if not me:
      return util.redirect(environ, start_response, '/')
    
    me.update_status('+visited', '-unvisited')
    
    if environ['REQUEST_METHOD'].upper() == 'POST':
      env = environ.copy()
      env['QUERY_STRING'] = ''
      fs = cgi.FieldStorage(
        fp = env['wsgi.input'],
        environ = env,
        keep_blank_values = True
      )
      
      cmt = Comment()
      cmt.author = me
      cmt.reply_all = (fs.getfirst('replyall', False) != False)
      cmt.value = fs.getfirst('value', '')
      cmt.from_web = True
      cmt.put()
      
      me.flash = 'Submitted comment.'
      me.put()
      
      return util.redirect(environ, start_response, '/%s' % code)
    else:
      start_response('200 Okay', [('Content-type', 'text/html; enctype=text/html')])
      
      if me.flash != None:
        flash = '<div id="overlay">%s</div>' % str(me.flash)
        me.flash = None
      else:
        flash = ""
      
      me.put()
      
      return (template.MAIN_PAGE.replace('%{OVERLAY}%', flash),)
  except Exception, exc:
    return util.handle_errors(sys.exc_info(), environ, start_response)