class Solution(object):
    def findLucky(self, arr):
        arr.sort()
        count = [0] * (arr[len(arr) - 1] + 1)
        largest = -1

        for n in arr:
            count[n] += 1
        for i in range(1, len(count)):
            if count[i] == i:
                largest = i
        
        return largest
        
