class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = [0] * len(nums1)

        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found = True
                if found and nums1[i] < nums2[j]:
                    ans[i] = nums2[j]
                    break
            if ans[i] == 0:
                ans[i] -= 1
        
        return ans
