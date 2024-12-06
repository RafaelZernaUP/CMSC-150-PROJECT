from server import server
from matrix import matrix
from food import food
from solution import solution
from os import path

CONSOLE = False if input()==0 else True

CSVPATH = path.join('..','Data','Food Data.csv')
food.load(CSVPATH)



# For debugging using terminal

chosenName = []
chosenIndex = []
toDo = []

def runOnConsole():

    # Menu
    while(True):
        foodNames = food.getNames()
        for i in range(len(foodNames)):
            if i not in chosenIndex:
                print(f'{i+1}: {foodNames[i]}')
        choice = int(input(": "))
        if choice == 0:
            break
        if foodNames[choice-1] not in chosenName:
            chosenName.append(foodNames[choice-1])
            chosenIndex.append(choice-1)
    
    # Get get chosen food objects
    list = food.getList()
    for e in chosenName:
        toDo.append(list[e])

    # Solve and print solution
    sol = solution(toDo)
    sol.printSolutionConsole()


if CONSOLE:
    runOnConsole()
else:
    server.start()