from food import food as fc

ZERO_V        = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

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
    
    def constructTableau(foods:list):
        matrix = []
        coefficients = [[],[],[],[],[],[],[],[],[],[],[],[]]
        servings = []
        serve_0 = []
        for a in range(len(foods)):
            serve_0.append(0)
            coeffs = foods[a].getCoefficients()
            for b in range(len(coeffs)):
                coefficients[b].append(coeffs[b])

        for c in range(len(coefficients) + len(serve_0)):
            if c < len(coefficients) - 1:
                print(c)
                if c == 0:
                    matrix.append(coefficients[c] + S_VARS[c].copy() + serve_0.copy())
                    matrix.append(coefficients[c] + S_VARS[c+1].copy() + serve_0.copy())
                elif c >= 5:
                    matrix.append(coefficients[c] + S_VARS[2*c-4].copy() + serve_0.copy())
                    matrix.append(coefficients[c] + S_VARS[2*c-3].copy() + serve_0.copy())
                else:
                    matrix.append(coefficients[c] + S_VARS[c+1].copy() + serve_0.copy())






        solution.printMatrix(matrix)

    def solve(self):
        pass

    def getTableaus(self):
        return self.__workingTableaus
    
    def getBasicSolutions(self):
        return self.__basicSolutions
    
    def transpose(matrix):
        new = []
        for i in matrix:
            new.append()
    
    def printMatrix(matrix:list):
        for i in matrix:
            for j in i:
                print(f"{j}", end="\t")
            print()