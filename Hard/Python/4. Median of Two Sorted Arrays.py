class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Create a new list
        merged = []

        # Use a while loop to add values from nums1 and nums2 to the new list
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            if i < len(nums1):
                merged.append(nums1[i])
                i += 1
            if j < len(nums2):
                merged.append(nums2[j])
                j += 1
        
        # Sort the array without the sort function (Bubble sort)
        for m in range(len(merged)):
            for n in range(m + 1, len(merged)):
                if merged[n] < merged[m]:
                    temp = merged[m]
                    merged[m] = merged[n]
                    merged[n] = temp

        # Find the median double, and return it
        middle = len(merged) / 2
        if len(merged) % 2 != 0:
            return merged[middle]
        else:
            return (merged[middle] + merged[middle - 1]) * 0.5
