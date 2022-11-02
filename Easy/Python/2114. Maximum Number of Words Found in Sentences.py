class Solution(object):
    def mostWordsFound(self, sentences):
        # Keep track of the max number of words
        max = 0
        
        # Go over the array of strings, counting each word
        # in each sentence
        for i in range(len(sentences)):
            count = 1
            for j in range(1, len(sentences[i]) - 1):
                if sentences[i][j] == ' ':
                    count += 1
            if max < count:
                max = count
        
        # Return the max number of words
        return max
