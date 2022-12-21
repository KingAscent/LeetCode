class Solution(object):
    def reversePrefix(self, word, ch):
        wordChars = []

        if ch in word:
            for c in word:
                wordChars.append(c)
                if c == ch:
                    break
            
            wordChars.reverse()
            word = ''.join(wordChars) + word[word.index(ch) + 1:]

        return word
