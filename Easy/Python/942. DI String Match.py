class Solution(object):
    def diStringMatch(self, s):
        n = len(s)
        perm = []
        start = 0
        end = n

        for i in range(len(s)):
            if s[i] == 'I':
                perm.append(start)
                start += 1
            else:
                perm.append(end)
                end -= 1
        perm.append(start)

        return perm
