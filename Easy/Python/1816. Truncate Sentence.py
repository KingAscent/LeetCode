class Solution(object):
    def truncateSentence(self, s, k):
        words = s.split(' ')
        truncated = ''

        for i in range(k):
            truncated = truncated + words[i]
            if i + 1 < k:
                truncated = truncated + ' '

        return truncated
