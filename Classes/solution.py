from food import food as fc
from copy import deepcopy as copy


SOLVED = 0
NO_ANS = 1
MULTI_ANS = 2

ZERO_V = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ANS_V = [2000,2250,300,65,2400,300,25,100,50,100,5000,50000,50,20000,800,1600,10,30]
S_VARS = [
 [ -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
,[  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
,[  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
,[  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1]
]

SAMPLE4 = [
    [ -1,  5, -1,  0,  0,  0,  10],
    [  2,  5,  0,  1,  0,  0,  40],
    [  1,  1,  0,  0, -1,  0,   8],
    [ -1,  3,  0,  0,  0,  1,   0]
]

SAMPLE3 = [
    [ 7,  11, 1,  0,  0,  0,  0, 77],
    [  10,  8,  0,  1,  0,  0,  0, 80],
    [  1,  0,  0,  0, 1,  0,   0, 9],
    [  0,  1,  0,  0, 0,  1,   0, 6],
    [ -150,  -175,  0,  0,  0,  0,   1, 0]
]

SAMPLE2 = [
    [  3,  2,  5,  1,  0,  0,  0,  18],
    [  4,  2,  3,  0,  1,  0,  0,  16],
    [  2,  1,  1,  0,  0, -1,  0,   4],
    [ -3, -2, -4,  0,  0,  0,  1,   0]
]

SAMPLE = [
    [ -1, -1,  1,  0,  0,  0,  -20],
    [ -1, -2,  0,  1,  0,  0,  -25],
    [ -5,  1,  0,  0,  1,  0,   4],
    [  3,  4,  0,  0,  0,  1,   0]
]

class solution():

    def __init__(self, foods:list):
        __initTableau: list
        __workingTableaus: list
        __basicSolutions: list
        __Z: float
        self.constructTableau(foods)
        #self.
        solution.solve(self.__initTableau)
        #solution.printMatrix(self.__initTableau)
    
    def constructTableau(self, foods:list): # include self here later
        matrix = []
        coefficients = [[],[],[],[],[],[],[],[],[],[],[],[]]
        serve_0 = []
        for a in range(len(foods)):
            serve_0.append(0)
            coeffs = foods[a].getCoefficients()
            for b in range(len(coeffs)):
                coefficients[b].append(coeffs[b])

        for c in range(len(coefficients) + len(serve_0)):
            if c < len(coefficients) - 1:
                if c == 0:
                    matrix.append(copy(coefficients[c]) + copy(S_VARS[c]) + copy(serve_0))
                    matrix.append(copy(coefficients[c]) + copy(S_VARS[c+1]) + copy(serve_0))
                elif c >= 5:
                    matrix.append(copy(coefficients[c]) + copy(S_VARS[2*c-4]) + copy(serve_0))
                    matrix.append(copy(coefficients[c]) + copy(S_VARS[2*c-3]) + copy(serve_0))
                else:
                    matrix.append(copy(coefficients[c]) + copy(S_VARS[c+1]) + copy(serve_0))
            elif c < len(coefficients) - 1 + len(serve_0):
                temp = copy(serve_0)
                temp[c - len(coefficients) + 1] = 1
                matrix.append(copy(temp) + copy(ZERO_V) + copy(temp))
            else:
                matrix.append(copy(coefficients[-1]) + copy(ZERO_V) + copy(serve_0))
                for d in range(len(matrix)):
                    if d < len(S_VARS):
                        matrix[d].append(0)
                        matrix[d].append(ANS_V[d])
                    elif d < len(matrix) - 1:
                        matrix[d].append(0)
                        matrix[d].append(10)
                    else:
                        matrix[d].append(1)
                        matrix[d].append(0)
        
        self.__initTableau = copy(matrix)

    def solve(matrix:list):
        sample = copy(SAMPLE)
        sample2 = copy(SAMPLE2)
        sample3 = copy(SAMPLE3)

        solution.fixNegaBasic(matrix)
        solution.fixNegaLastRow(matrix)

        solution.printMatrix(matrix)
        print()
        solution.findBasicSoln(matrix)

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
    
    def fixNegaLastRow(matrix:list) -> int:
        while(True):
            
            solution.findBasicSoln(matrix)
            print()

            # find largest negative
            col = -1
            max = 0
            for a in range(len(matrix[-1])-2): # -2 tanggal ans at Z cols
                if matrix[-1][a] < max: # max negative kaya <
                    max = matrix[-1][a]
                    col = a
            
            # no more negatives in the last row
            if col == -1:
                return SOLVED

            # find least positive ratio
            row = -1
            min = 0
            for b in range(len(matrix)-1): # -1 tanggal last row
                if matrix[b][col] > 0 and (matrix[b][-1]/matrix[b][col] < min or min == 0):
                    min = matrix[b][-1]/matrix[b][col]
                    row = b

            # no least positive ratio
            if row == -1:
                return NO_ANS

            # operate
            solution.operate(matrix, row, col)

    def operate(matrix:list, x:int, y:int):
        n = len(matrix) # rows
        m = len(matrix[0]) # cols

        # normalize pivot row
        pivotE = matrix[x][y]
        for a in range(len(matrix[x])):
            matrix[x][a] = matrix[x][a]/pivotE
        
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
    
    def printMatrix(matrix:list):
        for i in matrix:
            for j in i:
                print(f"{j:.1f}", end="\t")
            print()

    def printRow(list:list):
        for i in list:
            print(f"{i:.1f}", end="\t")
        print()