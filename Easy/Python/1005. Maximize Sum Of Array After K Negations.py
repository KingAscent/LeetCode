class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()
        n = len(nums)

        for i in range(n):
            if k != 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1
            else:
                break
        
        if k != 0:
            nums.sort()
            while k != 0:
                nums[0] *= -1
                k -= 1
        
        this_sum = 0
        for i in range(n):
            this_sum += nums[i]
        
        return this_sum
