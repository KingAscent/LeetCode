class Solution(object):
    def containsPattern(self, arr, m, k):
        count = 0

        for i in range(len(arr) - m):
            count = count + 1 if arr[i] == arr[i + m] else 0
            if count == m * (k - 1):
                return True

        return False
        
