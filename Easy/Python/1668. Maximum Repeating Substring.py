class Solution(object):
    def maxRepeating(self, sequence, word):
        count = 0
        rep = word

        while rep in sequence:
            count += 1
            rep += word
        
        return count
