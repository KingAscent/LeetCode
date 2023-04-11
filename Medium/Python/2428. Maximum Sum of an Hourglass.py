class Solution(object):
    def maxSum(self, grid):
        this_sum = 0
        this_max = 0

        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                this_sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j + 1]
                this_sum += grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                this_max = max(this_sum, this_max)

        return this_max
