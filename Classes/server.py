import http.server as hs
import webbrowser
from threading import Thread
from os import path
from food import food
from solution import solution
from matrix import matrix

HOST = 'localhost'
PORT = 8080

INDEXPATH = path.join('..','Pages','index.html')
SOLUTIONPATH = path.join('..','Pages','solution.html')
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
        server.__serverThread.start()
        webbrowser.open(f'http://{HOST}:{PORT}', new=2)

    def do_GET(self):
        if self.path == '/' or self.path == '/?':
            to = INDEXPATH
        else:
            to = SOLUTIONPATH
            formData = [int(i[4:-3]) for i in self.path[2:].split('&')]
            chosen = []
            for a in formData:
                chosen.append(FOODLIST[FOODNAMES[a]])
            server.makeSolPage(solution(chosen))
        file = open(to).read()
        self.setResponse()
        self.wfile.write(bytes(file, 'utf-8'))

    def do_POST(self):
        
        
        file = open(SOLUTIONPATH).read()
        self.setResponse()
        self.wfile.write(bytes(file, 'utf-8'))

    def stop():
        exit()

    def makeIndex():

        indexPage = open(INDEXPATH, "w")

        indexPage.write(
            f'<!DOCTYPE html><html><body>\n<form>\n'
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
    
    def makeSolPage(sol:solution):

        solutionPage = open(SOLUTIONPATH, "w")

        initTab = sol.getInitTableau()
        tabs = sol.getTableaus()
        basicSols = sol.getBasicSolutions()
        z = sol.getZ()
        foods = sol.getFoods()

        solutionPage.write(
            f'<!DOCTYPE html><html><body>\n'
        )

        solutionPage.write(
            f'<p>You selected {len(foods)} foods to consider in your diet.</p><br>\n'
        )

        for i in foods:
            solutionPage.write(
            f'{i.getName()}<br>\n'
        )
            
        if z == -1:
            solutionPage.write(
            f'<p>The problem is infeasible.</p>\n'
            )
            
        else:
            solutionPage.write(
            f'<p>The cost of this optimal diet is ${z:.2f} per day.</p>\n'
            )

            solutionPage.write(
            f'<table>\n'
            )
            solutionPage.write(
                f'<tr><td>Food</td><td>Servings</td><td>Cost($)</td></tr>\n'
                )

            for a in range(len(foods)):
                solutionPage.write(
                f'<tr>\n'
                )
                solutionPage.write(
                f'<td>{foods[a].getName()}</td><td>{basicSols[-1][-(len(foods)-a+2)]:.2f}</td><td>{basicSols[-1][-(len(foods)-a+2)]*foods[a].getCost():.2f}</td>\n'
                )
                solutionPage.write(
                f'</tr>\n'
                )

            solutionPage.write(
            f'</table>\n'
            )
        

        solutionPage.write(
            f'<form action="/"><button type="submit">Return to Home</button></form></body></html>'
        )
        
        solutionPage.close()