import csv

COSTPERSERVING = 0
CALORIES = 1
CHOLESTEROL = 2
TOTALFAT = 3
SODIUM = 4
CARBOHYDRATES = 5
DIETARYFIBER = 6
PROTEIN = 7
VITAMINA = 8
VITAMINC = 9
CALCIUM = 10
IRON = 11

class food():

    __foodList = {}
    __headings: list
    __foodNames = []

    def __init__(self, data:list):

        self.__name:str
        self.__servingSize:str
        self.__coefficients: list[float] = []
        
        for e in range(len(data)):
            match(e):
                case 0:
                    self.__name:str = data[e]
                case 2:
                    self.__servingSize:str = data[e]
                case _:
                    self.__coefficients.append(float(data[e]))

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
    
    def getHeadings():
        return food.__headings
    
    def getCoefficients(self):
        return self.__coefficients[1:] + [self.__coefficients[0]]

    def getName(self):
        return self.__name
    
    def getServingSize(self):
        return self.__servingSize
    
    def getCost(self):
        return self.__coefficients[COSTPERSERVING]
    
    def getCalories(self):
        return self.__coefficients[CALORIES]
    
    def getCholesterol(self):
        return self.__coefficients[CHOLESTEROL]
    
    def getFat(self):
        return self.__coefficients[TOTALFAT]
    
    def getSodium(self):
        return self.__coefficients[SODIUM]
    
    def getCarbs(self):
        return self.__coefficients[CARBOHYDRATES]
    
    def getFiber(self):
        return self.__coefficients[DIETARYFIBER]
    
    def getProtein(self):
        return self.__coefficients[PROTEIN]
    
    def getVitA(self):
        return self.__coefficients[VITAMINA]
    
    def getVitC(self):
        return self.__coefficients[VITAMINC]
    
    def getCalcium(self):
        return self.__coefficients[CALCIUM]
    
    def getIron(self):
        return self.__coefficients[IRON]