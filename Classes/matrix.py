class matrix():
    def __init__(self, row, col):
        self = []
        for a in range(row):
            self.append([])
            for b in range(col):
                self[a].append(0)

    def printMatrix(matrix:list):
        for i in matrix:
            for j in i:
                print(f"{j:.1f}", end="\t")
            print()

    def printRow(list:list):
        for i in list:
            print(f"{i:.1f}", end="\t")
        print()

    def multiplyRow(row:list, x):
        for a in range(len(row)):
            row[a] *= x

    def divideRow(row:list, x):
        for a in range(len(row)):
            row[a] *= x

    def addRow(row:list, list:list):
        for a in range(len(row)):
            row[a] += list[a]

    def subtractRow(row:list, list:list):
        for a in range(len(row)):
            row[a] -= list[a]