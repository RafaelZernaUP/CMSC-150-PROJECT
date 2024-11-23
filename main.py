import csv
import constants as C

# hello git hi    


headings: list
store = {}

class food():
    def __init__(self, data:list):
        self.name = data[C.NAME]
        self.costPerServing = data[C.COSTPERSERVING]
        self.servingSize = data[C.SERVINGSIZE]
        self.calories = data[C.CALORIES]
        self.totalFat = data[C.TOTALFAT]
        self.sodium = data[C.SODIUM]
        self.carbohydrates = data[C.CARBOHYDRATES]
        self.dietaryFiber = data[C.DIETARYFIBER]
        self.protein = data[C.PROTEIN]
        self.vitaminA = data[C.VITAMINA]
        self.vitaminC = data[C.VITAMINC]
        self.calcium = data[C.CALCIUM]
        self.iron = data[C.IRON]

csv_path = r"G:\My Drive\Personal\CMSC 150 Project\Food Data.csv"


def load_csv():
   with open(csv_path, mode ='r') as file:
      csvFile = csv.reader(file)
      counter = 0
      for line in csvFile:
        if line[0] == 'Foods':
            headings = line
            continue
        new: food = food(line)
        store[counter] = food(line)
        counter += 1

load_csv()
print(store[0].name)