class Solution(object):
    def strStr(self, haystack, needle):
        left = 0
        right = len(needle) - 1

        while right < len(haystack):
            temp = haystack[left:right + 1]
            if temp == needle:
                return left
            left += 1
            right += 1

        return -1
