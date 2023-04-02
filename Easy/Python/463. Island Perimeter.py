class Solution(object):
    def islandPerimeter(self, grid):
        island = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island += 4
                    if 0 < i and grid[i - 1][j] == 1:
                        island -= 2
                    if 0 < j and grid[i][j - 1] == 1:
                        island -= 2

        return island
