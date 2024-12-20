
# Distance between columns when printing
DIST = ""



# Matrix Class

class matrix():

    # Constructor
    def __init__(self, row, col):

        # Sets rows and columns
        self.__row:int = row
        self.__col:int = col

        # Initializes all matrix elements to 0
        self.__data:list[list[float]] = []
        for a in range(row):
            self.__data.append([])
            for b in range(col):
                self.__data[a].append(0)



    # Print methods for matrices and rows (for console debugging)
    def printMatrixConsole(self):
        for i in self.__data:
            matrix.printRowConsole(i)
            print()
    def printRowConsole(row:list[float]):
        for i in row:
            print(f"{i:10.2f}", end=DIST)
        print()



    # Print methods for matrices and rows (for HTML pages)
    def printMatrixHTML(self, headers):
        toReturn = '<div style="overflow-x: auto"><table>'
        for j in headers:
            toReturn += f'<th>{j}</th>'
        for i in self.__data: 
            toReturn += matrix.printRowHTML(i)
        toReturn += '</table></div>'
        return toReturn
    def printRowHTML(row:list[float]):
        toReturn = '<tr>'
        for i in row:
            toReturn += f'<td>{i}</td>'
        toReturn += '</tr>'
        return toReturn


    # Row operations

    # Multiply row by a constant
    def multiplyRow(row:list[float], x:float):
        for a in range(len(row)):
            row[a] *= x
        return row
    
    # Divide row by a constant
    def divideRow(row:list[float], x:float):
        for a in range(len(row)):
            row[a] /= x
        return row

    # Add a constant to a row
    def addRow(row:list[float], x:float):
        for a in range(len(row)):
            row[a] += x
        return row

    # Subtract a constant from a row
    def subtractRow(row:list[float], x:float):
        for a in range(len(row)):
            row[a] -= x
        return row

    # Adds two rows
    def addRowToRow(row:list[float], x:list[float]):
        for a in range(len(row)):
            row[a] += x[a]
        return row

    # Subtracts a row from a row
    def subtractRowFromRow(row:list[float], x:list[float]):
        for a in range(len(row)):
            row[a] -= x[a]
        return row
    
    # END OF ROW OPERATIONS



    # Getter and setter methods

    def getRowNum(self):
        return self.__row
    
    def getColNum(self):
        return self.__col
    
    def getElem(self, x:int, y:int):
        if x < 0:
            x = self.__row + x
        if y < 0:
            y = self.__col + y
        return self.__data[x][y]
    
    def setElem(self, x:int, y:int, z:float):
        if x < 0:
            x = self.__row + x
        if y < 0:
            y = self.__col + y
        self.__data[x][y] = z

    def getRow(self, x:int):
        if x < 0:
            x = self.__row + x
        return self.__data[x]
    
    def setRow(self, index:int, row:list[float]):
        if index < 0:
            index = self.__row + index
        for a in range(len(self.__data[index])):
            self.__data[index][a] = row[a]
    
    def setCol(self, index:int, col:list[float]):
        if index < 0:
            index = self.__row + index
        for a in range(len(self.__data)):
            self.__data[a][index] = col[a]

    # END OF GETTER AND SETTER METHODS