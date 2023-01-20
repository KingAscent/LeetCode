class Solution(object):
    def getRow(self, rowIndex):
        row = []

        for i in range(rowIndex + 1):
            row.append([])
            for j in range(i + 1):
                if j == 0 or i == j:
                    row[i].append(1)
                else:
                    row[i].append(row[i - 1][j - 1] + row[i - 1][j])

        return row[rowIndex]
