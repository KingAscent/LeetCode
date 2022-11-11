class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        firstWord = '';
        secondWord = '';

        for i in range(len(word1)):
            firstWord = firstWord + word1[i]
        
        for i in range(len(word2)):
            secondWord = secondWord + word2[i]
        
        return firstWord == secondWord
