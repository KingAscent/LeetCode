class Solution(object):
    def isCircularSentence(self, sentence):
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                if sentence[i - 1] != sentence[i + 1]:
                    return False
        
        return sentence[0] == sentence[len(sentence) - 1]
