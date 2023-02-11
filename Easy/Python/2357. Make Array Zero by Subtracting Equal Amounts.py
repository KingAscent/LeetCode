class Solution(object):
    def minimumOperations(self, nums):
        this_set = set()

        for i in nums:
            if 0 < i:
                this_set.add(i)
        
        return len(this_set)

        # Pythonic one liner
        # return len(set(nums) - {0})
