from http.server import HTTPServer, CGIHTTPRequestHandler

cgi_server = HTTPServer(('localhost', 8000), CGIHTTPRequestHandler)
cgi_server.serve_forever()
