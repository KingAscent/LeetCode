class Solution(object):
    def checkIfPangram(self, sentence):
        panagram = set()

        for i in range(len(sentence)):
            if sentence[i] not in panagram:
                panagram.add(sentence[i])
        
        return len(panagram) == 26
