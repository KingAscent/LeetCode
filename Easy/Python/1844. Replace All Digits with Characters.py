class Solution(object):
    def replaceDigits(self, s):
        word = list(s)

        for i in range(1, len(word), 2):
            word[i] = chr(ord(word[i - 1]) + ord(word[i]) - ord('0'))

        return ''.join(word)
