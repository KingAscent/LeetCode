class Solution(object):
    def largestLocal(self, grid):
        matrix = [[0] * (len(grid) - 2) for i in range(len(grid) - 2)]

        for i in range(len(grid) - 2):
            for j in range(len(grid) - 2):
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        matrix[i][j] = max(matrix[i][j], grid[x][y])

        return matrix
