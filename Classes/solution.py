from food import food as fc
from copy import deepcopy as copy

ZERO_V = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ANS_V = [2000,2500,300,65,2400,300,25,100,50,100,5000,50000,50,20000,800,1600,10,30]
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
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1,  0]
,[  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1]
]

SAMPLE = [
    [ -1,  5, -1,  0,  0,  0,  10],
    [  2,  5,  0,  1,  0,  0,  40],
    [  1,  1,  0,  0, -1,  0,   8],
    [ -1,  3,  0,  0,  0,  1,   0]
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
        
        #solution.printMatrix(matrix)

        solution.fixNegaBasic(matrix)

        solution.printMatrix(matrix)

        # find largest negative in last row -> y
        # find least positive ratio -> x
        # solve(matrix,x,y)
        # repeat
        


        pass

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
        
    def fixNegaBasic(matrix:list):
        while(True):
            basicVars = (solution.findBasicVars(matrix))[:-1]
            basicVars.reverse()
            leave = False
            solution.printMatrix(matrix)
            input()
            for a in basicVars:
                if matrix[a[0]][-1]/matrix[a[0]][a[1]] < 0: 
                    for c in range(len(matrix[a[0]])):
                        if matrix[a[0]][c] > 0 and c != a[1]:
                            solution.operate(matrix, a[0], c)
                            leave = True
                            break
                elif matrix[a[0]][a[1]] == -1:
                    for b in range(len(matrix[a[0]])):
                        matrix[a[0]][b] = -1*matrix[a[0]][b]
                        leave = True
                if leave:
                    break
            else:
                break
    
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