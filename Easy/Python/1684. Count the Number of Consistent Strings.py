class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count = 0

        for s in words:
            # Check if each character in String s is present in allowed
            for i in range(len(s)):
                # If it isn't, exit the loop
                # If each letter is present in allowed, increase count by 1
                if s[i] not in allowed:
                    break
                if i == len(s) - 1:
                    count += 1

        return count
