def application(request, start_response):
   start_response('200 OK')
   return [ 'Hello, world!' ]