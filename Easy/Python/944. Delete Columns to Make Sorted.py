class Solution(object):
    def minDeletionSize(self, strs):
        row = len(strs)
        col = len(strs[0])
        count = 0

        for i in range(col):
            for j in range(row - 1):
                if strs[j][i] > strs[j + 1][i]:
                    count += 1
                    break

        return count
