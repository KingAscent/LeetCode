class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        this_map = {}

        for i in range(len(nums)):
            if nums[i] in this_map and abs(i - this_map[nums[i]]) <= k:
                return True
            this_map[nums[i]] = i
        
        return False
