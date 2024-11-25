from food import food as fc
import copy

ZERO_V = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ANS_V = [2000,2500,300,65,2400,300,25,100,50,100,5000,50000,50,20000,800,1600,10,30]
S_VARS = [
[-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
,[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
,[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
,[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
,[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
,[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
,[0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0]
,[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
,[0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0]
,[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
,[0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0]
,[0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0]
,[0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0]
,[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0]
,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0]
,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
]

class solution():

    def __init__(self, foods:list):
        __initTableau: list
        __workingTableaus: list
        __basicSolutions: list
        __Z: float
        self.constructTableau(foods)
        #self.solve()
        solution.printMatrix(self.__initTableau)
    
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
                    matrix.append(copy.deepcopy(coefficients[c]) + copy.deepcopy(S_VARS[c]) + copy.deepcopy(serve_0))
                    matrix.append(copy.deepcopy(coefficients[c]) + copy.deepcopy(S_VARS[c+1]) + copy.deepcopy(serve_0))
                elif c >= 5:
                    matrix.append(copy.deepcopy(coefficients[c]) + copy.deepcopy(S_VARS[2*c-4]) + copy.deepcopy(serve_0))
                    matrix.append(copy.deepcopy(coefficients[c]) + copy.deepcopy(S_VARS[2*c-3]) + copy.deepcopy(serve_0))
                else:
                    matrix.append(copy.deepcopy(coefficients[c]) + copy.deepcopy(S_VARS[c+1]) + copy.deepcopy(serve_0))
            elif c < len(coefficients) - 1 + len(serve_0):
                temp = copy.deepcopy(serve_0)
                temp[c - len(coefficients) + 1] = 1
                matrix.append(copy.deepcopy(temp) + copy.deepcopy(ZERO_V) + copy.deepcopy(temp))
            else:
                matrix.append(copy.deepcopy(coefficients[-1]) + copy.deepcopy(ZERO_V) + copy.deepcopy(serve_0))
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
        
        self.__initTableau = copy.deepcopy(matrix)

    def solve(self):
        pass

    def getTableaus(self):
        return self.__workingTableaus
    
    def getBasicSolutions(self):
        return self.__basicSolutions
    
    def printMatrix(matrix:list):
        for i in matrix:
            for j in i:
                print(f"{j}", end="\t")
            print()