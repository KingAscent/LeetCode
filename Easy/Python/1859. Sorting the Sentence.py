class Solution(object):
    def sortSentence(self, s):
        words = s.split(" ")
        sentence = ["a"] * len(words)

        for word in words:
            n = int(word[-1]) - 1
            sentence[n] = word[:-1]

        return " ".join(sentence)
