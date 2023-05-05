class Solution(object):
    def maxVowels(self, s, k):
        max_sub = 0
        window = 0
        vowels = 'aeiou'

        for i in range(len(s)):
            if s[i] in vowels:
                window += 1
            max_sub = max(max_sub, window)

            # Move the window to the right one character
            if k - 1 <= i and s[i - k + 1] in vowels:
                window -= 1
        
        return max_sub
