class Solution(object):
    def sumOfUnique(self, nums):
        used = {}
        count = 0

        for i in nums:
            used[i] = used.get(i, 0) + 1
        
        for key, value in used.items():
            if value == 1:
                count += key
        
        return count
