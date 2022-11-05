class Solution(object):
    def restoreString(self, s, indices):
        shuffled = [''] * len(s)
        for i in range(len(s)):
            shuffled[indices[i]] = s[i]
        return ''.join(shuffled)
