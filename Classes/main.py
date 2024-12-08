from server import server
from matrix import matrix
from food import food
from solution import solution
from os import path

CSVPATH = path.join('..','Data','Food Data.csv')
food.load(CSVPATH)



# For debugging using terminal



def runOnConsole():

    chosenName = []
    chosenIndex = []
    toDo = []

    # Menu
    while(True):
        foodNames = food.getNames()
        for i in range(len(foodNames)):
            if i not in chosenIndex:
                print(f'{i+1}: {foodNames[i]}')
        print("0: Solve")
        choice = int(input("Please choose an operation: "))
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




# Menu

while True:
    CONSOLE = input("Run on terminal? [y/n]: ").lower()
    if CONSOLE == 'y':
        runOnConsole()
        break
    elif CONSOLE == 'n':
        while True:
            BROWSER = input("Open browser? [y/n]: ").lower()
            if BROWSER == 'y':
                server.start(True)
            elif BROWSER == 'n':
                server.start(False)
            else:
                print("Invalid option. Please try again.")
    else:
        print("Invalid option. Please try again.")