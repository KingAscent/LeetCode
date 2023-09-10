class Solution(object):
    def uniquePaths(self, m, n):
        row = [1] * n

        for i in range(1, m):
            currRow = [1] * n
            for j in range(1, n):
                currRow[j] = currRow[j - 1] + row[j]
            row = currRow
        
        return row[-1]
