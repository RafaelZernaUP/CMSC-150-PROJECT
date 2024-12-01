import http.server as hs
import webbrowser
from threading import Thread
from os import path
from food import food
from solution import solution

HOST = 'localhost'
PORT = 8080

INDEXPATH = path.join('..','Pages','index.html')
FOODNAMES = food.getNames()
FOODLIST = food.getList()

class server(hs.BaseHTTPRequestHandler):

    __serverThread: Thread

    def setResponse(self):
        self.send_response(200)
        self.end_headers()

    def serve(httpsServer:hs.HTTPServer):
        with httpsServer:
            httpsServer.serve_forever()

    def start():
        server.makeIndex()
        server.__serverThread = Thread(target = server.serve, args=(hs.HTTPServer((HOST,PORT), server),))
        #server.__serverThread.setDaemon(True)
        server.__serverThread.start()
        webbrowser.open(f'http://{HOST}:{PORT}', new=2)

    def do_GET(self):
        to = INDEXPATH
        file = open(to).read()
        self.setResponse()
        self.wfile.write(bytes(file, 'utf-8'))

    def do_POST(self):
        chosen = []
        formData = [int(i[4:-3]) for i in self.rfile.read().decode("utf-8").split('&')] 
        print(formData)
        for a in formData:
            chosen.append(FOODLIST[FOODNAMES[a]])
        self.setResponse()
        solution(chosen).printSolution()
        server.stop()

    def stop():
        exit()

    def makeIndex():

        indexPage = open(INDEXPATH, "w")

        indexPage.write(
            f'<!DOCTYPE html><html><body>\n<form method="POST">\n'
        )

        indexPage.write(
            f'<button type="submit">Solve</button><br>\n'
        )

        for a in range(len(FOODNAMES)):
            indexPage.write(
                f'<label><input type="checkbox" name="food{a}">{FOODNAMES[a]}</label><br>\n'
            )

        indexPage.write(
            f'</form></body></html>'
        )
        
        indexPage.close()
    # initialize index page using food list