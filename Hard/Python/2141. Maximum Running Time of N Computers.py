class Solution(object):
    def maxRunTime(self, n, batteries):
        batteries.sort()
        total = 0
        k = 0
        length = len(batteries)

        for b in batteries:
            total += b
        
        while total / (n - k) < batteries[length - 1 - k]:
            total -= batteries[length - 1 - k]
            k += 1

        return total / (n - k)
