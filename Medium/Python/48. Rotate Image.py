class Solution(object):
    def rotate(self, matrix):
        for i in range((len(matrix) + 1) / 2):
            for j in range(len(matrix) / 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[len(matrix) - j - 1][i]
                matrix[len(matrix) - j - 1][i] = matrix[len(matrix) - i - 1][len(matrix) - j - 1]
                matrix[len(matrix) - i - 1][(len(matrix) - j - 1)] = matrix[j][len(matrix) - i - 1]
                matrix[j][len(matrix) - i - 1] = temp
