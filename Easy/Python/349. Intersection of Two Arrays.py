class Solution(object):
    def intersection(self, nums1, nums2):
        freq = []

        for n in nums1:
            if n in nums2 and n not in freq:
                freq.append(n)
        
        return freq
