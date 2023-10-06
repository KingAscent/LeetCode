class Solution(object):
    def intersection(self, nums):
        ans = []
        count = [0] * 1001

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                count[nums[i][j]] += 1
        
        for i in range(1, 1001):
            if count[i] == len(nums):
                ans.append(i)
        
        return ans
