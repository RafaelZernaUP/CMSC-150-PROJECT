from food import food as fc

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

    def solution(self, foods:list):
        __initTableau: list
        __workingTableaus: list
        __basicSolutions: list
        __Z: float
        self.constructTableau(foods)
        self.solve()
    
    def constructTableau(foods:list): # include self here later
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
                    matrix.append(coefficients[c] + S_VARS[c].deepcopy() + serve_0.deepcopy())
                    matrix.append(coefficients[c] + S_VARS[c+1].deepcopy() + serve_0.deepcopy())
                elif c >= 5:
                    matrix.append(coefficients[c] + S_VARS[2*c-4].deepcopy() + serve_0.deepcopy())
                    matrix.append(coefficients[c] + S_VARS[2*c-3].deepcopy() + serve_0.deepcopy())
                else:
                    matrix.append(coefficients[c] + S_VARS[c+1].deepcopy() + serve_0.deepcopy())
            elif c < len(coefficients) - 1 + len(serve_0):
                temp = serve_0.deepcopy()
                temp[c - len(coefficients) + 1] = 1
                matrix.append(temp + ZERO_V + temp)
            else:
                matrix.append(coefficients[-1] + ZERO_V.deepcopy() + serve_0.deepcopy())
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
        
        # self.__initTableau = matrix.deepcopy()
        solution.printMatrix(matrix)

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