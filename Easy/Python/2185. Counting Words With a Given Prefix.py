class Solution(object):
    def prefixCount(self, words, pref):
        count = 0

        for s in words:
            if s[0:len(pref)] == pref:
                count += 1

        return count
