class Solution(object):
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])
        if r * c != m * n:
            return mat
        
        rs = [[0] * c for _ in range(r)]
        for i in range(r * c):
            rs[i / c][i % c] = mat[i / n][i % n]

        return rs
