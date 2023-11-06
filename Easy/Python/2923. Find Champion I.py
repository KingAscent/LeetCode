class Solution(object):
    def findChampion(self, grid):
        for i in range(len(grid)):
            champ = True
            for j in range(len(grid)):
                if i != j and grid[i][j] == 0:
                    champ = False
            if champ:
                return i
        
        return -1
