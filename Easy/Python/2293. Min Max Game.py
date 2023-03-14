class Solution(object):
    def minMaxGame(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        minMaxed = [0] * (len(nums) / 2)
        for i in range(len(minMaxed)):
            if i % 2 == 0:
                minMaxed[i] = min(nums[2 * i], nums[2 * i + 1])
            else:
                minMaxed[i] = max(nums[2 * i], nums[2 * i + 1])
        
        return self.minMaxGame(minMaxed)
