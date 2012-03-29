import util

def handle(environ, start_response):
  start_response('200 Okay', [('Content-type', 'text/html; enctype=text/html')])
  
  yield '<title>Under Construction</title><h1>This Site is Under Construction!</h1>'