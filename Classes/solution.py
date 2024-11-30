from food import food as fc
from copy import deepcopy as copy
from matrix import matrix


SOLVED = 0
NO_ANS = 1
MULTI_ANS = 2

LASTROW_V = [-2000,2250,300,65,2400,300,-25,100,-50,100,-5000,50000,-50,20000,-800,1600,-10,30]

SAMPLE = [
    [1,7,1,0,0,14],
    [2,6,0,1,0,20],
    [-4,-20,0,0,1,0]
]

class solution():

    def __init__(self, foods:list[fc]):
        self.__initTableau: matrix
        self.__workingTableaus: list[matrix] = []
        self.__basicSolutions: list[list] = []
        self.__Z: float
        self.constructTableau(foods)

        #self.__initTableau = matrix(3,6)
        #for i in range(len(SAMPLE)):
        #    self.__initTableau.setRow(i, SAMPLE[i])

        self.__initTableau.printMatrix()
        while(True):
            if len(self.__workingTableaus):
                print(self.__workingTableaus[-1].getElem(-1,-1))

            pivotElement = self.findPivotElement()

            print(pivotElement)

            if pivotElement == SOLVED or pivotElement == NO_ANS:
                break

            self.rowReduce(pivotElement)

            self.__workingTableaus[-1].printMatrix()
            print()
            input()
            #self.findBasicVars()

    def constructTableau(self, foods:list[fc]):
        
        new:matrix = matrix(len(foods)+1, len(LASTROW_V)+len(foods)+2)

        for a in range(len(foods)):

            coeffs = foods[a].getCoefficients()
                
            row = [] 
            [row.extend([coeffs[b], -1*coeffs[b]]) if (b==0 or b>=5) else row.append(-1*coeffs[b]) for b in range(len(coeffs)-1)]
            row += [1 if a==c else 0 for c in range(len(foods))] + [0] + [copy(coeffs)[-1]]

            new.setRow(a, row)

        lastRow = copy(LASTROW_V) + [10 for x in foods] + [1] + [0]
        new.setRow(-1, lastRow)

        self.__initTableau = copy(new)
    
    def findPivotElement(self):
        
        if len(self.__workingTableaus) == 0:
            mat:matrix = self.__initTableau
        else:
            mat:matrix = self.__workingTableaus[-1]
        
        entry:int = -1
        max:float = 0
        
        for a in range(mat.getColNum()-1):
            if mat.getElem(-1, a) < max:
                max = mat.getElem(-1, a)
                entry = a
        
        if entry == -1:
            return SOLVED
        
        departure:int = -1
        min: float = 0

        for b in range(mat.getRowNum()-1):
            if mat.getElem(b, entry) > 0 and (mat.getElem(b, -1) / mat.getElem(b, entry) < min or min == 0):
                departure = b
                min = mat.getElem(b, -1) / mat.getElem(b, entry)

        if departure == -1:
            return NO_ANS
        
        return [departure, entry]

    def rowReduce(self, pivotElement:list[int]):
        
        x, y = pivotElement[0], pivotElement[1]

        if len(self.__workingTableaus) == 0:
            mat:matrix = copy(self.__initTableau)
        else:
            mat:matrix = copy(self.__workingTableaus[-1])

        pivotElementValue = mat.getElem(x, y)
        normalized_row = matrix.divideRow(mat.getRow(x), pivotElementValue)

        for a in range(mat.getRowNum()):
            
            if a != x:
                row = copy(matrix.multiplyRow(copy(normalized_row), mat.getElem(a,y)))
                matrix.subtractRowFromRow(mat.getRow(a), row)
        
        self.__workingTableaus.append(copy(mat))
    
    def findBasicVars(matrix:list) -> list:
        basicVars = []
        for j in range(len(matrix[0])-1):
            found = False
            x = -1
            y = -1
            for i in range(len(matrix)):
                if not found and (matrix[i][j] == -1 or matrix[i][j] == 1):
                    found = True
                    x = i
                    y = j
                elif matrix[i][j] != 0:
                    x = -1
                    y = -1
                    break
            else:
                basicVars.append((x,y))
        return copy(basicVars)

    def findBasicSoln(matrix:list) -> list:
        
        basicVars = solution.findBasicVars(matrix)
        basicCols = []
        basicRows = []
        basicSolns = []
        for a in basicVars:
            basicCols.append(a[1])
            basicRows.append(a[0])

        rowIndex = 0
        for b in range(len(matrix[0])-1):
            if b not in basicCols:
                basicSolns.append(0)
            else:
                basicSolns.append(matrix[basicRows[rowIndex]][-1])
                rowIndex += 1
        
        solution.printRow(basicSolns)
        return copy(basicSolns)
    
    

    def operate(matrix:list, x:int, y:int):
        n = len(matrix) # rows
        m = len(matrix[0]) # cols

        # normalize pivot row
        pivotE = matrix[x][y]
        solution.divideRow(matrix[x], pivotE)
        
        # operate on remaining rows
        for b in range(n):
            if b == x:
                continue
            new = copy(matrix[x])
            for d in range(len(new)):
                new[d] = new[d]*matrix[b][y]
            # copy normalized row, multiply each item with [b][y], put in new
            # subtract new from [b]
            for c in range(m):
                matrix[b][c] -= new[c] 
                

    def getTableaus(self):
        return self.__workingTableaus
    
    def getBasicSolutions(self):
        return self.__basicSolutions

    def fixNegaBasic(matrix:list):
            n = len(matrix)
            m = len(matrix[0])
            while(True):
                basicVars = (solution.findBasicVars(matrix))[:-1]
                basicVars.reverse()
                leave = False
                solution.printMatrix(matrix)

                input()
                #row = int(input())
                #column = int(input())
                #if row < 0 or column < 0:
                #    return
                #solution.operate(matrix, row, column)

                for a in basicVars:
                    if matrix[a[0]][a[1]] == -1:
                        for b in range(len(matrix[a[0]])):
                            matrix[a[0]][b] = -1*matrix[a[0]][b]

                for a in basicVars:
                    if matrix[a[0]][-1]/matrix[a[0]][a[1]] < 0: 
                        for c in range(m-1):
                            if matrix[a[0]][c] != 0 and c != a[1]:
                                solution.operate(matrix, a[0], c)
                                leave = True
                                break
                        else:
                            return NO_ANS
                    if leave:
                        break
                else:
                    break