class Solution(object):
    def reverseWords(self, s):
        # Split all the words by whitespaces
        split = s.split(' ')

        # Reverse each word and rejoin each word, seperated by whitespaces
        return ' '.join(word[::-1] for word in split)
