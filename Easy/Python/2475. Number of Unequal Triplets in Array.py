class Solution(object):
    def unequalTriplets(self, nums):
        count = 0
        n = len(nums)

        for i in range(0, n - 2, 1):
            a = nums[i]
            for j in range(i + 1, n - 1, 1):
                b = nums[j]
                for k in range(i + 2, n, 1):
                    c = nums[k]
                    if i < j and j < k:
                        if a != b and b != c and a != c:
                            count += 1

        return count
