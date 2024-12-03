from food import food
from copy import deepcopy as copy
from matrix import matrix

# Constants for easy adjustments and code readability

DEBUG = False

SOLVED = 0
NO_ANS = -1

LASTROW_V = [-2000,2250,300,65,2400,300,-25,100,-50,100,-5000,50000,-50,20000,-800,1600,-10,30]



# Solution Class

class solution():

    # Constructor
    def __init__(self, foods:list[food]):
        
        # Initialize all attributes
        self.__foods: list[food] = copy(foods)
        self.__initTableau: matrix
        self.__workingTableaus: list[matrix] = []
        self.__basicSolutions: list[list] = []
        self.__Z: float
        
        # Constructs and sets initial tableau
        self.__constructTableau()

        if DEBUG:
            self.__initTableau.printMatrixConsole()
            print()
        
        # Main loop
        while(True):

            # Determines pivot element
            pivotElement = self.__findPivotElement()

            if DEBUG:
                print(pivotElement)

            # Breaks out of loop when found feasible/infeasible
            if pivotElement == SOLVED:
                self.__Z = self.__workingTableaus[-1].getElem(-1,-1)
                break
            elif pivotElement == NO_ANS:
                self.__Z = NO_ANS
                break
            
            # Perform row reductions given a pivot element
            self.__rowReduce(pivotElement)

            if DEBUG:
                self.__workingTableaus[-1].printMatrixConsole()
                print()
                input()

        if DEBUG:
                matrix.printRowConsole(matrix.getRow(self.__workingTableaus[-1], -1))
                print(self.__Z)

    # END OF CONSTRUCTOR



    # Prints the full solution (for console debugging)
    def printSolutionConsole(self):

        print("\nInitial Tableau")
        self.__initTableau.printMatrixConsole()

        for a in range(len(self.__workingTableaus)):

            print(f"\n\n\nIteration {a+1}:")
            self.__workingTableaus[a].printMatrixConsole()
            
            print("\nBasic Solution:")
            matrix.printRowConsole(self.__basicSolutions[a])

        print(f"\n\nZ: {self.__Z}\n")



    # Prints the full solution (for HTML pages)
    def printSolutionHTML(self):

        toReturn = '<br><br><br><br>Initial Tableau<br>'
        toReturn += f'{self.__initTableau.printMatrixHTML()}<br>'

        for a in range(len(self.__workingTableaus)):

            toReturn += f"<br>Iteration {a+1}:<br>"
            toReturn += f'{self.__workingTableaus[a].printMatrixHTML()}<br>'
            
            toReturn += "<br>Basic Solution:<br>"
            toReturn += f'{matrix.printRowHTML(self.__basicSolutions[a][0:-2]+self.__basicSolutions[a][-1:])}<br>'

        return toReturn



    # Constructs the initial tableau
    def __constructTableau(self):
        
        # Instantiate a new matrix object (refer to matrix.py)
        new:matrix = matrix(len(self.__foods)+1, len(LASTROW_V)+2*len(self.__foods)+2)

        # Constructs a row of the tableau for each of the chosen foods
        for a in range(len(self.__foods)):

            # Gets the coefficients of the food
            coeffs = self.__foods[a].getCoefficients()
            
            # Sets surplus and x columns based on food's coefficients
            row = []
            # For the nutrients' lower (positive) and upper (negative) bounds
            [row.extend([coeffs[b], -1*coeffs[b]]) if (b==0 or b>=5) else row.append(-1*coeffs[b]) for b in range(len(coeffs)-1)]
            # For the serving sizes (negative since upper bound), x columns, and answer (cost per serving) column
            row += [-1 if a==c else 0 for c in range(len(self.__foods))] + [1 if a==d else 0 for d in range(len(self.__foods))] + [0] + [copy(coeffs)[-1]]

            # Sets row in the tableau
            new.setRow(a, row)

        # Sets the last row of the tableau. All surplus columns already negated
        lastRow = copy(LASTROW_V) + [10 for x in self.__foods] + [0 for x in self.__foods] + [1] + [0]
        new.setRow(-1, lastRow)

        # Sets the new matrix object as the initial tableau
        self.__initTableau = copy(new)

    # END OF constructTableau()
    


    # Finds the pivot element in the tableau
    def __findPivotElement(self):
        
        # Determines tableau to be performed on
        if len(self.__workingTableaus) == 0:
            mat:matrix = self.__initTableau
        else:
            mat:matrix = self.__workingTableaus[-1]
        
        
        # Finds smallest negative number in the last row
        entry:int = -1
        max:float = 0
        
        for a in range(mat.getColNum()-1):
            if mat.getElem(-1, a) < max:
                max = mat.getElem(-1, a)
                entry = a
        
        # Deem feasible when none found
        if entry == -1:
            return SOLVED
        

        # Finds least positivie ratio
        departure:int = -1
        min: float = 0

        for b in range(mat.getRowNum()-1):
            if mat.getElem(b, entry) > 0 and (mat.getElem(b, -1) / mat.getElem(b, entry) < min or min == 0):
                departure = b
                min = mat.getElem(b, -1) / mat.getElem(b, entry)

        # Deem infeasible when none found
        if departure == -1:
            return NO_ANS
        
        # Returns pivot element row and column coordinates
        return [departure, entry]
    
    # END OF findPivotElement()



    # Performs row reductions given a pivot element
    def __rowReduce(self, pivotElement:list[int:2]):
        
        # Unpacks pivot element coordinates
        x, y = pivotElement[0], pivotElement[1]

        # Determines tableau to be operated on
        if len(self.__workingTableaus) == 0:
            mat:matrix = copy(self.__initTableau)
        else:
            mat:matrix = copy(self.__workingTableaus[-1])

        # Saves pivot element value
        pivotElementValue = mat.getElem(x, y)

        # Normalizes pivot row
        normalized_row = matrix.divideRow(mat.getRow(x), pivotElementValue)

        # Performs row reductions on the other rows
        for a in range(mat.getRowNum()):
            
            if a != x:
                row = copy(matrix.multiplyRow(copy(normalized_row), mat.getElem(a,y)))
                matrix.subtractRowFromRow(mat.getRow(a), row)
        
        # Adds new iteration to working tableaus and basic solutions
        self.__workingTableaus.append(copy(mat))
        self.__basicSolutions.append(copy(mat.getRow(-1)))

    # END OF rowReduce()
    


    # Getter methods

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