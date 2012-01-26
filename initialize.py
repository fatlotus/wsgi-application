def application(request, start_response):
   start_response('200 OK', [('Content-type' : 'text/html')])
   return [ '<h1>Hello, world!</h1>' ]