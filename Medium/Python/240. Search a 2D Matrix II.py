class Solution(object):
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col - 1

        while i < row and 0 <= j:
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1

        return False
