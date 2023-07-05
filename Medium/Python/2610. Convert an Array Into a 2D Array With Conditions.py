class Solution(object):
    def findMatrix(self, nums):
        count = Counter(nums)
        this_max = max(count.values())
        n = list(count.elements())
        return [n[i::this_max] for i in range(this_max)]
