class Solution(object):
    def firstBadVersion(self, n):
        first = 0
        last = n
        ver = 0

        while first <= last:
            temp = first + (last - first) / 2
            if isBadVersion(temp):
                ver = temp
                last = temp - 1
            else:
                first = temp + 1
        
        return ver
