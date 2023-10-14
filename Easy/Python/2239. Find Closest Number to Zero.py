class Solution(object):
    def findClosestNumber(self, nums):
        num = 100001

        for i in nums:
            if abs(i) < abs(num) or i == abs(num):
                num = i
        
        return num
