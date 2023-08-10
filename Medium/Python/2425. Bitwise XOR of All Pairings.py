class Solution(object):
    def xorAllNums(self, nums1, nums2):
        if len(nums1) % 2 == 0 and len(nums2) % 2 == 0:
            return 0
        n = 0

        if len(nums2) % 2 == 1:
            for num in nums1:
                n ^= num
        if len(nums1) % 2 == 1:
            for num in nums2:
                n ^= num
        
        return n
