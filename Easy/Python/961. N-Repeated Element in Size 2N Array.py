class Solution(object):
    def repeatedNTimes(self, nums):
        appearance = {}
        num = 0

        for i in nums:
            if i in appearance:
                appearance[i] = appearance[i] + 1
            else:
                appearance[i] = 1
         
        for i in nums:
            if appearance[i] == len(nums) / 2:
                num = i
                break
        
        return num
