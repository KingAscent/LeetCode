class Solution(object):
    def threeConsecutiveOdds(self, arr):
        for i in range(len(arr) - 2):
            odd1 = arr[i] % 2 == 1
            odd2 = arr[i + 1] % 2 == 1
            odd3 = arr[i + 2] % 2 == 1
            if odd1 and odd2 and odd3:
                return True
        
        return False
