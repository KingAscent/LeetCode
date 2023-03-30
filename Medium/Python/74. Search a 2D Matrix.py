class Solution(object):
    def searchMatrix(self, matrix, target):
        r = len(matrix)
        c = len(matrix[0])
        i = 0
        j = c - 1

        while 0 <= i < r and 0 <= j < c:
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                j -= 1
            else:
                i += 1

        return False
