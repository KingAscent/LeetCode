class Solution(object):
    def shuffle(self, nums, n):
        ans = []
        for i in range(len(nums)):
            if(i % 2 == 0):
                ans.append(nums[i / 2])
            else:
                ans.append(nums[n + (i / 2)])
        return ans
