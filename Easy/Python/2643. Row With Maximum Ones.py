class Solution(object):
    def rowAndMaximumOnes(self, mat):
        row = 0
        count = 0

        for i in range(len(mat)):
            temp = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    temp += 1
            if count < temp:
                row = i
                count = temp

        return [row, count]
