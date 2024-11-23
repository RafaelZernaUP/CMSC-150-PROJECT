import http.server as hs
import webbrowser
from threading import Thread

HOST = 'localhost'
PORT = 8080

class server(hs.BaseHTTPRequestHandler):
    def do_GET(self):
        file = open('index.html').read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))

    def serve(httpsServer:hs.HTTPServer):
        with httpsServer:
            httpsServer.serve_forever()

    def start():
        serverThread = Thread(target = server.serve, args=(hs.HTTPServer((HOST,PORT), server),))
        #serverThread.setDaemon(True)
        serverThread.start()
        webbrowser.open(f'http://{HOST}:{PORT}', new=2)
