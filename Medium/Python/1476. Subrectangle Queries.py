class SubrectangleQueries(object):
    def __init__(self, rectangle):
        self.matrix = rectangle
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        # Assign every value in the matrix to the newValue
        # Upper left coordinate is (row1, col1)
        # Lower right coordinate is (row2, col2)
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.matrix[i][j] = newValue
        

    def getValue(self, row, col):
        return self.matrix[row][col]
