class Solution(object):
    def onesMinusZeros(self, grid):
        rowLength = len(grid)
        colLength = len(grid[0])
        rowZeros = [0] * rowLength
        rowOnes = [0] * rowLength
        colZeros = [0] * colLength
        colOnes = [0] * colLength

        # Use a for loop to find the ones and zeros and increment relevant values
        for i in range(rowLength):
            for j in range(colLength):
                if grid[i][j] == 1:
                    rowOnes[i] += 1
                    colOnes[j] += 1
                else:
                    rowZeros[i] += 1
                    colZeros[j] += 1
        
        # Use a for loop to calculate the result for each value in grid
        for i in range(rowLength):
            for j in range(colLength):
                grid[i][j] = rowOnes[i] + colOnes[j] - rowZeros[i] - colZeros[j]
        
        return grid
