class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        count = 0

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i][::1] == words[j][::-1]:
                    count += 1
                    break

        return count
