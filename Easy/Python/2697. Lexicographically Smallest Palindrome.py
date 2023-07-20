class Solution(object):
    def makeSmallestPalindrome(self, s):
        palin = list(s)
        n = len(s)

        for i in range(len(s) / 2):
            j = n - i - 1
            if palin[i] != palin[j]:
                if palin[i] < palin[j]:
                    palin[j] = palin[i]
                palin[i] = palin[j]

        return ''.join(palin)
