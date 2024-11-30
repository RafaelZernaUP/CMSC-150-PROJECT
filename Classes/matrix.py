class matrix():
    def __init__(self, row, col):
        __row:int = row
        __col:int = col
        __data:list = []
        for a in range(row):
            __data.append([])
            for b in range(col):
                __data[a].append(0)

    def print(self):
        for i in self.__data:
            for j in i:
                print(f"{j:.1f}", end="\t")
            print()

    def printRow(self, row):
        for i in self.__data[row]:
            print(f"{i:.1f}", end="\t")
        print()

    def multiplyRow(self, row, x):
        for a in range(len(self.__data[row])):
            self[row][a] *= x

    def divideRow(self, row, x):
        for a in range(len(self.__data[row])):
            self[row][a] /= x

    def addRow(self, row, x):
        for a in range(len(self.__data[row])):
            self[row][a] += x

    def subtractRow(self, row, x):
        for a in range(len(self.__data[row])):
            self[row][a] -= x

    def getRow(self):
        return self.__row
    
    def getCol(self):
        return self.__col