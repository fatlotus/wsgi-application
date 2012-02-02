def application(request, start_response):
   start_response('200 OK', [('Content-type' : 'text/html')])
   return [ '<h1>Hello, world -- this is version 2.0!</h1>' ]