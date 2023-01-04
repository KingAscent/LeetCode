class Solution(object):
    def transpose(self, matrix):
        newMatrix = []

        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            newMatrix.append(temp)

        return newMatrix
