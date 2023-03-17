class Solution(object):
    def generateMatrix(self, n):
        mat = [[0] * n for _ in range(n)]

        temp = 1
        row = 0
        rowEnd = n - 1
        col = 0
        colEnd = n - 1

        while temp <= n * n:
            # Shift from left to right
            for i in range(col, colEnd + 1):
                mat[row][i] = temp
                temp += 1
            row += 1

            # Shift from top to bot
            for i in range(row, rowEnd + 1):
                mat[i][colEnd] = temp
                temp += 1
            colEnd -= 1

            # Shift from right to left
            for i in range(colEnd, col - 1, -1):
                mat[rowEnd][i] = temp
                temp += 1
            rowEnd -= 1

            # Shift from bot to top
            for i in range(rowEnd, row - 1, -1):
                mat[i][col] = temp
                temp += 1
            col += 1

        return mat
