class Solution(object):
    def deleteGreatestValue(self, grid):
        totalSum = 0

        for i in grid:
            i.sort()
        
        for i in range(len(grid[0])):
            maximum = 0
            for e in grid:
                if maximum <= e[i]:
                    maximum = e[i]
            
            totalSum += maximum
        
        return totalSum
