class Solution(object):
    def alternatingSubarray(self, nums):
        n = len(nums)
        alt = 0

        """
            Alternating pattern:
            x1 - x0 = 1
            x2 - x1 = -1
            x3 - x2 = 1
            Substitution:
            x1 - x0 = i % 2
        """

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + (j - i) % 2 == nums[j]:
                    alt = max(alt, j - i + 1)
                else:
                    break
        
        return alt if 1 < alt else -1
