from server import server
from matrix import matrix
from food import food
from solution import solution
from os import path

chosen = []
i_s = []
toDo = []

def chooser():
    while(True):
        for i in range(len(foodNames)):
            if i not in i_s:
                print(f'{i+1}: {foodNames[i]}')
        choice = int(input(": "))
        if choice == 0:
            return
        if foodNames[choice-1] not in chosen:
            chosen.append(foodNames[choice-1])
            i_s.append(choice-1)

def finder():
    list = food.getList()
    for e in chosen:
        toDo.append(list[e])

# load food list
csv_path = path.join('..','Data','Food Data.csv')
food.load(csv_path)
foodNames = food.getNames()

#solution.solve()

chooser()
finder()
sol = solution(toDo)

tableaus = sol.getTableaus()
basicSolns = sol.getBasicSolutions()

print("\nInitial Tableau")
sol.getInitTableau().printMatrix()

for a in range(len(tableaus)):
    print(f"\n\n\nIteration {a+1}:")
    tableaus[a].printMatrix()
    print("\nBasic Solution:")
    matrix.printRow(basicSolns[a])

print(f"\n\nZ: {sol.getZ()}\n")

# initialize index page using food list


# start server
#server.start()

# listen for form submission

# parse submission

# solve and prepare solution page

# set page to solution page




#print(food.getList())