class matrix():
    DIST = "\t"

    def __init__(self, row, col):
        self.__row:int = row
        self.__col:int = col
        self.__data:list[list] = []
        for a in range(row):
            self.__data.append([])
            for b in range(col):
                self.__data[a].append(0)

    def printMatrix(self):
        for i in self.__data:
            for j in i:
                print(f"{j:.2f}", end=matrix.DIST)
            print()

    def printRow(row:list):
        for i in row:
            print(f"{i:.2f}", end=matrix.DIST)
        print()

    def multiplyRow(row:list, x):
        for a in range(len(row)):
            row[a] *= x
        return row

    def divideRow(row:list, x):
        for a in range(len(row)):
            row[a] /= x
        return row

    def addRow(row:list, x):
        for a in range(len(row)):
            row[a] += x
        return row

    def subtractRow(row:list, x):
        for a in range(len(row)):
            row[a] -= x
        return row

    def addRowToRow(row:list, x):
        for a in range(len(row)):
            row[a] += x[a]
        return row

    def subtractRowFromRow(row:list, x):
        for a in range(len(row)):
            row[a] -= x[a]
        return row

    def getRowNum(self):
        return self.__row
    
    def getColNum(self):
        return self.__col
    
    def getElem(self, x, y):
        if x < 0:
            x = self.__row + x
        if y < 0:
            y = self.__col + y
        return self.__data[x][y]
    
    def setElem(self, x, y, z):
        if x < 0:
            x = self.__row + x
        if y < 0:
            y = self.__col + y
        self.__data[x][y] = z
    
    def setRow(self, index, row:list):
        if index < 0:
            index = self.__row + index
        for a in range(len(self.__data[index])):
            self.__data[index][a] = row[a]
    
    def setCol(self, index, col:list):
        if index < 0:
            index = self.__row + index
        for a in range(len(self.__data)):
            self.__data[a][index] = col[a]