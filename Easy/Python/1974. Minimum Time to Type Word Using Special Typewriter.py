class Solution(object):
    def minTimeToType(self, word):
        count = len(word)
        prev = 'a'

        for i in range(len(word)):
            curr = word[i]
            diff = abs(ord(curr) - ord(prev))
            count += min(diff, 26 - diff)
            prev = curr

        return count
