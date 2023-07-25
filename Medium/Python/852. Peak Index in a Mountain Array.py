class Solution(object):
    def peakIndexInMountainArray(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            temp = (left + right) / 2
            if arr[temp] < arr[temp + 1]:
                left = temp + 1
            else:
                right = temp

        return left
