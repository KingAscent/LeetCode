class Solution(object):
    def firstPalindrome(self, words):
        for s in words:
            left = 0
            right = len(s) - 1
            isPalindrome = True

            # Use 2 pointers to compare each character in each word
            while left <= right:
                if s[left] != s[right]:
                    isPalindrome = False
                left += 1
                right -= 1
            
            # If the word is a palindrome, return it
            if(isPalindrome):
                return s
        
        return ""
