class Solution(object):
    def isMonotonic(self, nums):
        if len(nums) == 1:
            return True
        
        inc = True
        dec = True

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                dec = False
            if nums[i + 1] < nums[i]:
                inc = False
            if not inc and not dec:
                return False
        
        return inc or dec
