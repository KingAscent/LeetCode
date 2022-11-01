class Solution(object):
    def runningSum(self, nums):
        ans = [len(nums)]
        ans[0] = nums[0]
        for i in range(1, len(nums)):
            ans.append(ans[i - 1] + nums[i])
        return ans
