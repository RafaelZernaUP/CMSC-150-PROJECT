import http.server as hs
import webbrowser
from os import path
from food import food
from solution import solution
import socket
import mimetypes

HOST = socket.getfqdn()
PORT = 8080

INDEXPATH = path.join('..','Pages','index.html')
SOLUTIONPATH = path.join('..','Pages','solution.html')
STYLEPATH = path.join('..','Pages','style.css')
FOODNAMES = food.getNames()
FOODLIST = food.getList()

class server(hs.BaseHTTPRequestHandler):

    def start(browser:bool):
        server.makeIndex()
        if browser:
            webbrowser.open(f'http://{HOST}:{PORT}', 2)
        server.makeIndex()
        hs.HTTPServer((HOST,PORT), server).serve_forever()

    def setResponse(self, filetype, to):
        self.send_response(200)
        file = open(to).read()
        self.send_header('Content-type', filetype)
        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))

    def writeToFile(filepath, string):
        file = open(filepath, "w")
        file.write(string)
        file.close()

    def do_GET(self):
        if self.path == '/favicon.ico':
            pass
        elif self.path == '/' or self.path == '/?':
            filetype = 'text/html'
            to = INDEXPATH
        elif self.path == f'/style.css':
            filetype = 'text/css'
            to = STYLEPATH
        elif self.path[0:6] == '/?food':
            filetype = 'text/html'
            to = SOLUTIONPATH
            formData = [int(i[4:-3]) for i in self.path[2:].split('&')]
            chosen = []
            for a in formData:
                chosen.append(FOODLIST[FOODNAMES[a]])
            server.makeSolPage(solution(chosen))

        self.setResponse(filetype,to)

    def makeIndex():

        css = open(STYLEPATH, "r")

        toWrite = ''
        
        toWrite += f'<head><link rel="stylesheet", href=style.css><title>title</title></head><body>\n<form>\n<button type="submit">Solve</button><br>\n'

        for a in range(len(FOODNAMES)):
            toWrite += f'<label><input type="checkbox" name="food{a}">{FOODNAMES[a]}</label><br>\n'

        toWrite += f'</form>'

        toWrite += f'</body></html>'
        
        server.writeToFile(INDEXPATH, toWrite)
    
    def makeSolPage(sol:solution):

        basicSols = sol.getBasicSolutions()
        z = sol.getZ()
        foods = sol.getFoods()

        css = open(STYLEPATH, "r")

        toWrite = ''

        toWrite += f'<!DOCTYPE html><html>'
        toWrite += f'<head><link rel="stylesheet", href=style.css></head>'
        
        toWrite += f'<body><form action="/"><button type="submit">Return to Home</button></form></body></html>'
        toWrite += f'<p>You selected {len(foods)} food{'' if len(foods) == 0 else 's'} to consider in your diet.</p><br>\n'

        for i in foods:
            toWrite += f'{i.getName()}<br>\n'
            
        if z == -1:
            toWrite += f'<p>The problem is infeasible.</p>\n'
            
        else:
            toWrite += f'<p>The cost of this optimal diet is ${z:.2f} per day.</p>\n'

            toWrite += f'<table>\n'
            
            toWrite += f'<tr><td>Food</td><td>Servings</td><td>Cost($)</td></tr>\n'

            for a in range(len(foods)):
                toWrite += f'<tr>\n'
                toWrite += f'<td>{foods[a].getName()}</td><td>{basicSols[-1][-(len(foods)-a+2)]:.2f}</td><td>{basicSols[-1][-(len(foods)-a+2)]*foods[a].getCost():.2f}</td>\n'
                toWrite += f'</tr>\n'

            toWrite += f'</table>\n'

        toWrite += sol.printSolutionHTML()

        toWrite += '</body></html>'

        server.writeToFile(SOLUTIONPATH, toWrite)