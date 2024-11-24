from food import food as fc
from server import server as sv
from solution import solution
from os import path


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
    list = fc.getList()
    for e in chosen:
        toDo.append(list[e])

# load food list
csv_path = path.join('Data','Food Data.csv')
fc.load(csv_path)
foodNames = fc.getNames()


chosen = []
i_s = []
toDo = []
chooser()
finder()
solution.constructTableau(toDo)



# initialize index page using food list


# start server
#sv.start()

# listen for form submission

# parse submission

# solve and prepare solution page

# set page to solution page




#print(fc.getList())