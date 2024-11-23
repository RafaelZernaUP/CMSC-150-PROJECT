import csv

NAME = 0
COSTPERSERVING = 1
SERVINGSIZE = 2
CALORIES = 3
TOTALFAT = 4
SODIUM = 5
CARBOHYDRATES = 6
DIETARYFIBER = 7
PROTEIN = 8
VITAMINA = 9
VITAMINC = 10
CALCIUM = 11
IRON = 12

class food():

    __foodList = {}

    def __init__(self, data:list):
        self.__name:str = data[NAME]
        self.__costPerServing:float = data[COSTPERSERVING]
        self.__servingSize:str = data[SERVINGSIZE]
        self.__calories:float = data[CALORIES]
        self.__totalFat:float = data[TOTALFAT]
        self.__sodium:float = data[SODIUM]
        self.__carbohydrates:float = data[CARBOHYDRATES]
        self.__dietaryFiber:float = data[DIETARYFIBER]
        self.__protein:float = data[PROTEIN]
        self.__vitaminA:float = data[VITAMINA]
        self.__vitaminC:float = data[VITAMINC]
        self.__calcium:float = data[CALCIUM]
        self.__iron:float = data[IRON]
        food.__foodList[self.__name] = self
    
    def getList():
        return food.__foodList
    
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