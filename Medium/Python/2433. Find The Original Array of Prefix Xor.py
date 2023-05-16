class Solution(object):
    def findArray(self, pref):
        lis = [0] * len(pref)
        lis[0] = pref[0]

        for i in range(len(pref) - 1, 0, -1):
            lis[i] = pref[i] ^ pref[i - 1]

        return lis
