class Solution(object):
    def numberOfBeams(self, bank):
        count = 0
        prev = 0

        for s in bank:
            temp = 0
            for i in range(len(s)):
                if s[i] == '1':
                    temp += 1
            count += prev * temp
            if 0 < temp:
                prev = temp

        return count
