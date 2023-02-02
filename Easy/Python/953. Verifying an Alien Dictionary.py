class Solution(object):
    def isAlienSortedHelper(self, w1, w2, order):
        if w1 == w2:
            return True
        
        minimum = min(len(w1), len(w2))
        j = 0
        while j < minimum and w1[j] == w2[j]:
            j += 1
        if j == minimum:
            return minimum == len(w1)
        else:
            c1 = w1[j]
            c2 = w2[j]
            return order.index(c1) < order.index(c2)
    

    def isAlienSorted(self, words, order):
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            if not self.isAlienSortedHelper(w1, w2, order):
                return False
            
        return True
