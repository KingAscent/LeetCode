class Solution(object):
    def minDeletion(self, nums):
        delete = 0

        for i in range(len(nums) - 1):
            index = delete % 2 == i % 2
            if index and nums[i] == nums[i + 1]:
                delete += 1

        if (len(nums) - delete) % 2 == 0:
            return delete
        return delete + 1
