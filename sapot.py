# WSGI server
from wsgiref.simple_server import make_server

def application(environ, start_response):
    response_body = [
       '%s: %s' % (key, value) for key, value in sorted(environ.items())
    ]
    response_body = '\n'.join(response_body)
    response_body = [
        'The Beginning\n',
        '*' * 30 + '\n',
        response_body,
        '\n' + '*' * 30,
        '\nThe End'
    ]
    response_body = [body.encode('utf-8') for body in response_body]
    content_length = sum([len(s) for s in response_body])
    status = '200 ok'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(content_length))
    ]
    start_response(status, response_headers)
    return response_body

httpd = make_server('localhost', 8051, application)
httpd.handle_request()
