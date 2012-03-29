import util
import sys
import logging

import private
import print_template
import admin_template

def setup():
  people = [
    ('First Last', 'email@address.com', 'x12345') # => http://www.domain.com/code-to-access
    # ...
  ]
  
  count = 0
  
  for person in people:
    try:
      private.Person(name=person[0], email=person[1], key_name=person[2]).put()
      count += 1
    except:
      pass
  
  return count

def handle(environ, start_response):
  try:
    action = environ['PATH_INFO'][10:]
    
    if action != '' and action[-1] == '/':
      return util.redirect(environ, start_response, '/politburo' % action[0:-1])
      
    if environ['REQUEST_METHOD'].upper() == 'POST':
      if action == '/setup':
        message = "Successfully added %i people." % setup()
      elif action == '/print':
        people = [ ]
        
        for person in private.Person.all().filter('status =', 'unvisited'):
          people.append((person.name, person.key().name()))
        
        start_response('200 Bork bork bork!', [('Content-type', 'text/html; enctype=utf-8')])
        
        return [print_template.render_page(people)]
      else:
        pass
      
      return util.redirect(environ, start_response, '/politburo?%s' % message)
    else:
      if action != '':
        return util.redirect(environ, start_response, '/politburo')
      
      start_response('200 Okay', [('Content-type', 'text/html; enctype=utf-8')])
      
      return (admin_template.PAGE,)
  except Exception, exc:
    return util.handle_errors(sys.exc_info(), environ, start_response)