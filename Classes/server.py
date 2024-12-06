import http.server as hs
import webbrowser
from os import path
from food import food
from solution import solution

HOST = 'localhost'
PORT = 8080

INDEXPATH = path.join('..','Pages','index.html')
SOLUTIONPATH = path.join('..','Pages','solution.html')
STYLEPATH = path.join('style.css')
FOODNAMES = food.getNames()
FOODLIST = food.getList()

class server(hs.BaseHTTPRequestHandler):

    def start():
        server.makeIndex()
        webbrowser.open(f'http://{HOST}:{PORT}', 2)
        hs.HTTPServer((HOST,PORT), server).serve_forever()

    def setResponse(self):
        self.send_response(200)
        self.end_headers()

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

    def writeToFile(filepath, string):
        file = open(filepath, "w")
        file.write(string)
        file.close()

    def makeIndex():

        toWrite = ''

        toWrite += f'<!DOCTYPE html><html><link rel="stylesheet" href="{STYLEPATH}"><body>\n<form>\n<button type="submit">Solve</button><br>\n'

        for a in range(len(FOODNAMES)):
            toWrite += f'<label><input type="checkbox" name="food{a}">{FOODNAMES[a]}</label><br>\n'

        toWrite += f'</form></body></html>'
        
        server.writeToFile(INDEXPATH, toWrite)
    
    def makeSolPage(sol:solution):

        solutionPage = open(SOLUTIONPATH, "w")

        basicSols = sol.getBasicSolutions()
        z = sol.getZ()
        foods = sol.getFoods()

        solutionPage.write(
            f'<!DOCTYPE html><html><link rel="stylesheet" href="{STYLEPATH}"><body>\n'
        )

        solutionPage.write(
            f'<form action="/"><button type="submit">Return to Home</button></form></body></html>'
        )

        solutionPage.write(
            f'<p>You selected {len(foods)} food{'' if len(foods) == 0 else 's'} to consider in your diet.</p><br>\n'
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

        solutionPage.write(sol.printSolutionHTML())
        
        solutionPage.close()