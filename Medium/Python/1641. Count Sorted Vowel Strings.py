class Solution(object):
    def countVowelStrings(self, n):
        a = e = i = o = u = 1

        for j in range(1, n):
            a += e + i + o + u
            e += i + o + u
            i += o + u
            o += u
            # u doesn't change

        return a + e + i + o + u
