import http.server

class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        open('index.html')
        self.send_response(200)

http.server.HTTPServer(('localhost',8080), handler).serve_forever()