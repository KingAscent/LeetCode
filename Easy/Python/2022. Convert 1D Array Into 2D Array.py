class Solution(object):
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []
        
        arr = [[0] * n for _ in range(m)]
        row = 0
        col = 0

        for num in original:
            arr[row][col] = num
            col += 1
            if col == n:
                col = 0
                row += 1

        return arr
