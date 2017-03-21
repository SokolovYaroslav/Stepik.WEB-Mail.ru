def wsgi_application(environ, start_responce):
	body = '\r\n'.join(environ['QUERY_STRING'].split('&'))
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	start_responce(status, headers)
	return [body]
