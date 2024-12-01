from food import food
from copy import deepcopy as copy
from matrix import matrix

DEBUG = False

SOLVED = 0
NO_ANS = -1

LASTROW_V = [-2000,2250,300,65,2400,300,-25,100,-50,100,-5000,50000,-50,20000,-800,1600,-10,30]

class solution():

    def __init__(self, foods:list[food]):
        
        self.__foods: list[food] = copy(foods)
        self.__initTableau: matrix
        self.__workingTableaus: list[matrix] = []
        self.__basicSolutions: list[list] = []
        self.__Z: float
        
        self.constructTableau()

        if DEBUG:
            self.__initTableau.printMatrix()
            print()
        
        while(True):

            pivotElement = self.findPivotElement()

            if DEBUG:
                print(pivotElement)

            if pivotElement == SOLVED:
                self.__Z = self.__workingTableaus[-1].getElem(-1,-1)
                break
            elif pivotElement == NO_ANS:
                self.__Z = NO_ANS
                break

            self.rowReduce(pivotElement)

            if DEBUG:
                self.__workingTableaus[-1].printMatrix()
                print()
                input()

        if DEBUG:
                matrix.printRow(matrix.getRow(self.__workingTableaus[-1], -1))
                print(self.__Z)

    def constructTableau(self):
        
        new:matrix = matrix(len(self.__foods)+1, len(LASTROW_V)+2*len(self.__foods)+2)

        for a in range(len(self.__foods)):

            coeffs = self.__foods[a].getCoefficients()
                
            row = [] 
            [row.extend([coeffs[b], -1*coeffs[b]]) if (b==0 or b>=5) else row.append(-1*coeffs[b]) for b in range(len(coeffs)-1)]
            row += [-1 if a==c else 0 for c in range(len(self.__foods))] + [1 if a==d else 0 for d in range(len(self.__foods))] + [0] + [copy(coeffs)[-1]]

            new.setRow(a, row)

        lastRow = copy(LASTROW_V) + [10 for x in self.__foods] + [0 for x in self.__foods] + [1] + [0]
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

    def rowReduce(self, pivotElement:list[int:2]):
        
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
        self.__basicSolutions.append(copy(mat.getRow(-1)))
    
    def getInitTableau(self):
        return self.__initTableau

    def getTableaus(self):
        return self.__workingTableaus
    
    def getBasicSolutions(self):
        return self.__basicSolutions
    
    def getZ(self):
        return self.__Z
    
    def getFoods(self):
        return self.__foods