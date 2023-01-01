class Solution(object):
    def divideArray(self, nums):
        seen = set()

        for i in nums:
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)

        return len(seen) == 0
