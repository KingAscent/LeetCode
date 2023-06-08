class Solution(object):
    def removeTrailingZeros(self, num):
        end = len(num)

        for i in range(len(num) - 1, -1, -1):
            if num[i] != '0':
                end = i + 1
                break

        return num[0:end]
