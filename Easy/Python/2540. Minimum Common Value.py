class Solution(object):
    def getCommon(self, nums1, nums2):
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums2[j] < nums1[i]:
                j += 1
            else:
                i += 1
        
        return -1
