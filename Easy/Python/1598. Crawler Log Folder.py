class Solution(object):
    def minOperations(self, logs):
        folder = 0

        for s in logs:
            if s[1] == '.':
                folder = max(0, folder - 1)
            elif s[0] != '.':
                folder += 1

        return folder
