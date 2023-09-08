class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        this_sum = 0
        row = [0] * n
        col = [0] * n

        for i in range(n):
            row[i] = grid[i][0]
            col[i] = grid[0][i]
            for j in range(n):
                row[i] = max(row[i], grid[i][j])
                col[i] = max(col[i], grid[j][i])
        
        for i in range(n):
            for j in range(n):
                this_sum += min(row[i], col[j]) - grid[i][j]
        
        return this_sum
