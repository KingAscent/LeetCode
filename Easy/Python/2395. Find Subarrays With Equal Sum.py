class Solution(object):
    def findSubarrays(self, nums):
        for i in range(0, len(nums) - 2):
            sum1 = nums[i] + nums[i + 1]
            for j in range(i + 1, len(nums) - 1):
                sum2 = nums[j] + nums[j + 1]
                if sum1 == sum2:
                    return True
        
        return False
