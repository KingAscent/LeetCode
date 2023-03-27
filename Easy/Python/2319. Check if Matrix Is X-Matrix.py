class Solution(object):
    def checkXMatrix(self, grid):
        x = True
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if (i == j or (i + j) == n - 1) and grid[i][j] == 0:
                    x = False
                elif i != j and (i + j) != (n - 1) and grid[i][j] != 0:
                    x = False

        return x
