class Solution(object):
    def isValid(self, s):
        map = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []

        for c in s:
            if c in map:
                stack.append(map[c])
            elif not stack or stack[-1] != c:
                return False
            else:
                stack.pop()

        return not stack
