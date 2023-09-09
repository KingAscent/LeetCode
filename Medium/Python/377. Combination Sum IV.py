class Solution(object):
    def combinationSum4(self, nums, target):
        cases = [0] * (target + 1)
        cases[0] = 1

        for i in range(1, target + 1):
            for n in nums:
                if n <= i:
                    cases[i] += cases[i - n]
        
        return cases[target]
