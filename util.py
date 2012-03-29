import sys
import traceback

def redirect(environ, start_response, url):
	start_response('303 Go Away', [('Location', url)])
	
	return ('Foo',)

def handle_errors(exc_info, environ, start_response):
	start_response('500 Internal Server Error', [('Content-type', 'text/html; enctype=utf-8')], exc_info=exc_info)
	
	return (
		'<style type="text/css">*{margin:0;padding:0;}h1{font:bold 3em Helvetica, sans-serif;margin:0.5em 0em;}',
		'body{width:40em;margin:1em auto;}html{background-color:#900;color:white;}',
		'pre{background-color:#fff;padding:3em 2em;color:#111;white-space:pre-wrap;}',
		'pre{border:1px solid #700;font:11px Monaco,monospace;}',
		'pre{border-radius:0.5em 0em;}',
		'</style>',
		'<body><h1>Unhandled Exception: %s</h1>' % str(exc_info[1]),
		'<pre>%s</pre></body>' % ('<br/>'.join(traceback.format_tb(exc_info[2]))),
	)