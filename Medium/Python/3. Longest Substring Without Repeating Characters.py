class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
        word = set()

        # Go over the string, comparing each character
        # to the next. If a character is new, place it
        # into the set. Once a repeat is found, the size
        # of the set is the length of the substring
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in word:
                    break
                else:
                    word.add(s[j])
            longest = max(len(word), longest)
            word = set()

        return longest
