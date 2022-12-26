class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        mat = [[0] * len(colSum) for i in range(len(rowSum))]

        # Fill each spot of the matrix by finding the min of
        # rowSum[i] and colSum[j], then place it into the
        # matrix. Subtract mat[i][j] from rowSum[i]
        # and colSum[j]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                mat[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] = rowSum[i] - mat[i][j]
                colSum[j] = colSum[j] - mat[i][j]

        return mat
