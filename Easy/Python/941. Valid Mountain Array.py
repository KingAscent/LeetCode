class Solution(object):
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False
        l = 0
        r = n - 1

        # Double pointers
        while l < n - 2 and arr[l] < arr[l + 1]:
            l += 1
        while 1 < r and arr[r] < arr[r - 1]:
            r -= 1
        
        return l == r
