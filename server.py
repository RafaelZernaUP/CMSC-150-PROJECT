import http.server as hs

class handler(hs.BaseHTTPRequestHandler):
    def do_GET(self):
        file = open('index.html').read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))

hs.HTTPServer(('localhost',8080), handler).serve_forever()