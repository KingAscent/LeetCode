class Solution(object):
    def countPrefixes(self, words, s):
        count = 0

        for word in words:
            if word in s[0:len(word)]:
                count += 1

        return count
