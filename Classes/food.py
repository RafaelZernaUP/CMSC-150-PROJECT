import csv

NAME = 0
COSTPERSERVING = 1
SERVINGSIZE = 2
CALORIES = 3
CHOLESTEROL = 4
TOTALFAT = 5
SODIUM = 6
CARBOHYDRATES = 7
DIETARYFIBER = 8
PROTEIN = 9
VITAMINA = 10
VITAMINC = 11
CALCIUM = 12
IRON = 13

class food():

    __foodList = {}
    __headings: list
    __foodNames = []

    def __init__(self, data:list):
        self.__name:str = data[NAME]
        self.__costPerServing:float = float(data[COSTPERSERVING])
        self.__servingSize:str = data[SERVINGSIZE]
        self.__calories:float = float(data[CALORIES])
        self.__cholesterol:float = float(data[CHOLESTEROL])
        self.__totalFat:float = float(data[TOTALFAT])
        self.__sodium:float = float(data[SODIUM])
        self.__carbohydrates:float = float(data[CARBOHYDRATES])
        self.__dietaryFiber:float = float(data[DIETARYFIBER])
        self.__protein:float = float(data[PROTEIN])
        self.__vitaminA:float = float(data[VITAMINA])
        self.__vitaminC:float = float(data[VITAMINC])
        self.__calcium:float = float(data[CALCIUM])
        self.__iron:float = float(data[IRON])
        food.__foodList[self.__name] = self
        food.__foodNames.append(self.__name)
    
    def load(path):
        with open(path, mode ='r') as file:
            csvFile = csv.reader(file)
            for line in csvFile:
                if line[0] == 'Foods':
                    food.__headings = line
                    continue
                food(line)
    
    def getList():
        return food.__foodList
    
    def getNames():
        return food.__foodNames
    
    def getCoefficients(self):
        return [
            self.__calories,
            self.__cholesterol,
            self.__totalFat,
            self.__sodium,
            self.__carbohydrates,
            self.__dietaryFiber,
            self.__protein,
            self.__vitaminA,
            self.__vitaminC,
            self.__calcium,
            self.__iron,
            self.__costPerServing
            ]
    
    def getHeadings():
        return food.__headings

    def getName(self):
        return self.__name
    def getCost(self):
        return self.__costPerServing
    def getServingSize(self):
        return self.__servingSize
    def getCalories(self):
        return self.__calories
    def getFat(self):
        return self.__totalFat
    def getSodium(self):
        return self.__sodium
    def getCarbs(self):
        return self.__carbohydrates
    def getFiber(self):
        return self.__dietaryFiber
    def getProtein(self):
        return self.__protein
    def getVitA(self):
        return self.__vitaminA
    def getVitC(self):
        return self.__vitaminC
    def getCalcium(self):
        return self.__calcium
    def getIron(self):
        return self.__iron