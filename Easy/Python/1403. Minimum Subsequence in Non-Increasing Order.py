class Solution(object):
    def minSubsequence(self, nums):
        n = len(nums)
        this_sum = 0
        total = 0
        ans = []
        nums.sort()

        for i in range(n):
            total += nums[i]
        
        for i in range(n - 1, -1, -1):
            ans.append(nums[i])
            this_sum += nums[i]
            if total - this_sum < this_sum:
                break
        
        return ans
