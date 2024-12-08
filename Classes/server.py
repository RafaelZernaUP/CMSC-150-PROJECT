import http.server as hs
import webbrowser
from os import path
from food import food
from solution import solution
import socket

# Host and port
HOST = socket.getfqdn()
PORT = 8080

# Useful constants
INDEXPATH = path.join('..','Pages','index.html')
SOLUTIONPATH = path.join('..','Pages','solution.html')
STYLEPATH = path.join('..','Pages','style.css')
SCRIPTPATH = path.join('..','Pages','script.js')
FOODNAMES = food.getNames()
FOODLIST = food.getList()



# Server Class

class server(hs.BaseHTTPRequestHandler):
    
    # Initializes Server
    def start(browser:bool):
        server.makeIndex()
        if browser:
            webbrowser.open(f'http://{HOST}:{PORT}', 2)
        hs.HTTPServer((HOST,PORT), server).serve_forever()

    # Sends file upon request
    def setResponse(self, filetype, to):
        self.send_response(200)
        file = open(to).read()
        self.send_header('Content-type', filetype)
        self.end_headers()
        self.wfile.write(bytes(file, 'utf-8'))


    # Writes a string to a file
    def writeToFile(filepath, string):
        file = open(filepath, "w")
        file.write(string)
        file.close()



    # Handles GET requests
    def do_GET(self):
        
        # Favicon
        if self.path == '/favicon.ico':
            pass

        # Index page
        elif self.path == '/' or self.path == '/?':
            filetype = 'text/html'
            to = INDEXPATH
            self.setResponse(filetype,to)
        
        # CSS
        elif self.path == f'/style.css':
            filetype = 'text/css'
            to = STYLEPATH
            self.setResponse(filetype,to)
        
        # JavaScript
        elif self.path == f'/script.js':
            filetype = 'text/javascript'
            to = SCRIPTPATH
            self.setResponse(filetype,to)
        
        # Solution page
        elif self.path[0:6] == '/?food':
            filetype = 'text/html'
            to = SOLUTIONPATH
            formData = [int(i[4:-3]) for i in self.path[2:].split('&')]
            chosen = []
            for a in formData:
                chosen.append(FOODLIST[FOODNAMES[a]])
            server.makeSolPage(solution(chosen))
            self.setResponse(filetype,to)
    
    # END OF GET HANDLER



    # Initializes the index page

    def makeIndex():

        toWrite = ''
        
        toWrite += f'<head><link rel="stylesheet", href=style.css><script type="text/javascript" src="script.js"></script><title>title</title></head><body>\n'
        
        toWrite += f'<h2>WELCOME TO THE DIET OPTIMIZER</h2>'
        toWrite += f"<h3>Please choose among the given foods to include in your diet. Click 'Solve' when you are done.</h3>"

        toWrite += f'<form>\n'
        
        # Buttons
        toWrite += f'<button type="submit">Solve</button>\n'
        toWrite += f'<button type="reset">Reset</button>\n'
        toWrite += f'<button type="button" onclick="checkAll();">Check All</button><br>\n'

        # Foods table
        toWrite += '<table>'
        for a in range(len(FOODNAMES)):
            if a == 0:
                toWrite += '<tr>'
            elif a%8 == 0:
                toWrite += '<tr><tr>'
            toWrite += f'<td style="text-align: left"><label><input type="checkbox" name="food{a}">{FOODNAMES[a]}</label></td>\n'
            if a == (len(FOODNAMES)-1):
                toWrite += '<tr>'
        toWrite += '</table>'

        toWrite += f'</form>'

        toWrite += f'</body></html>'
        
        server.writeToFile(INDEXPATH, toWrite)

    # END OF MAKEINDEX



    # Prepares the solution page

    def makeSolPage(sol:solution):

        basicSols = sol.getBasicSolutions()
        z = sol.getZ()
        foods = sol.getFoods()

        toWrite = ''

        toWrite += f'<!DOCTYPE html><html>'
        toWrite += f'<head><link rel="stylesheet", href=style.css></head>'
        

        # Chosen foods
        toWrite += f'<body><form action="/"><button type="submit">Return to Menu</button></form></body></html>'
        toWrite += f'<h2>You selected {len(foods)} food{'' if len(foods) == 0 else 's'} to consider in your diet.</h2>\n'
        for i in foods:
            toWrite += f'{i.getName()}<br>\n'
            
        # Infeasible
        if z == -1:
            toWrite += f'<h3>The problem is infeasible.</h3>\n'
            
        # Feasible
        else:
            toWrite += f'<h3>The cost of this optimal diet is ${z:.2f} per day.</h3>\n'

            toWrite += f'<table>\n'
            
            toWrite += f'<tr><td style="text-align: left">Food</td><td style="text-align: left">Servings</td><td style="text-align: left">Cost($)</td></tr>\n'

            for a in range(len(foods)):
                toWrite += f'<tr>\n'
                toWrite += f'<td style="text-align: left">{foods[a].getName()}</td><td>{basicSols[-1][-(len(foods)-a+2)]:.2f}</td><td>{basicSols[-1][-(len(foods)-a+2)]*foods[a].getCost():.2f}</td>\n'
                toWrite += f'</tr>\n'

            toWrite += f'</table>\n'

        # Writes iterations and basic solutions
        toWrite += sol.printSolutionHTML()

        toWrite += '</body></html>'

        server.writeToFile(SOLUTIONPATH, toWrite)

    # END OF MAKESOLPAGE