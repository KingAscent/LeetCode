class Solution(object):
    def generate(self, numRows):
        pas = []

        for i in range(numRows):
            row = [0] * (i + 1)
            row[0] = 1
            row[i] = 1
            for j in range(1, i):
                row[j] = pas[i - 1][j - 1] + pas[i - 1][j]
            pas.append(row)

        return pas
