class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        df = [0] * n

        if 0 < k:
            for i in range(n):
                temp = 0
                for j in range(1, k + 1, 1):
                    temp += code[(i + j) % n]
                df[i] = temp
        elif k < 0:
            for i in range(n):
                temp = 0
                for j in range(1, (k * -1) + 1, 1):
                    temp += code[(i - j + n) % n]
                df[i] = temp
        
        return df
