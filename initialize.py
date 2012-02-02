def application(request, start_response):
   start_response('200 OK')
   return [ 'Hello, world -- this is version 2.0!' ]