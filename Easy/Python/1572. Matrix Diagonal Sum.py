class Solution(object):
    def diagonalSum(self, mat):
        sum = 0
        top = 0
        bot = len(mat[0]) - 1

        # Subtract the value of any secondary diagonal
        if len(mat[0]) % 2 == 1:
            sum = sum - mat[bot / 2][bot / 2]
        
        # Add each value from the matrix diagonals
        for i in range(len(mat[0])):
            sum = sum + mat[i][top] + mat[i][bot]
            top += 1
            bot -= 1
        
        return sum
