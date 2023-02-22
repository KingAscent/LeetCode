class Solution(object):
    def oddCells(self, m, n, indices):
        row = [0] * m
        col = [0] * n

        for i in range(len(indices)):
            row[indices[i][0]] += 1
            col[indices[i][1]] += 1
        
        oddRows = 0
        for i in range(m):
            if row[i] % 2 == 1:
                oddRows += 1
        
        oddCols = 0
        for i in range(n):
            if col[i] % 2 == 1:
                oddCols += 1
        
        return (oddRows * n) + (oddCols * m) - (2 * oddRows * oddCols)
