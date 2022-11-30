class Solution(object):
    def rearrangeArray(self, nums):
        # Create a new list, an even index, and an odd index variable
        rearranged = [0] * len(nums)
        i = 0 # Even index
        j = 1 # Odd index

        # Go over the list, adding positives, then negatives, to the list
        for k in nums:
            if 0 < k:
                rearranged[i] = k
                i = i + 2
            else:
                rearranged[j] = k
                j = j + 2

        # Return the new list
        return rearranged
