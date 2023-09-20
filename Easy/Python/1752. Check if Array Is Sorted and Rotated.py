class Solution(object):
    def check(self, nums):
        count = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                count += 1
        
        if 1 < count or (count != 0 and nums[0] < nums[n - 1]):
            return False
        return True
