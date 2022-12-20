class Solution(object):
    def halvesAreAlike(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        front = 0
        back = 0

        for i in range(len(s) / 2):
            if s[i].lower() in vowels:
                front += 1
            if s[i + len(s) / 2].lower() in vowels:
                back += 1

        return front == back
