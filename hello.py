def wsgi_application(environ, start_responce):
	body = environ['QUERY_STRING'].replace('&', '\n')
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	start_responce(status, headers)
	return [body]
