class Solution(object):
    def longestValidParentheses(self, s):
        open_paren = 0
        close_paren = 0
        longest = 0

        for i in range(len(s)):
            if s[i] == '(':
                open_paren += 1
            else:
                close_paren += 1
            
            if open_paren == close_paren:
                longest = max(longest, 2 * close_paren)
            elif open_paren <= close_paren:
                open_paren = 0
                close_paren = 0
        
        open_paren = 0
        close_paren = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                open_paren += 1
            else:
                close_paren += 1
            
            if open_paren == close_paren:
                longest = max(longest, 2 * open_paren)
            elif close_paren <= open_paren:
                open_paren = 0
                close_paren = 0

        return longest
