class Solution(object):
    def maxDepthAfterSplit(self, seq):
        par = [0] * len(seq)
        count = 0

        for i in range(len(seq)):
            if seq[i] == '(':
                count += 1
                par[i] = count % 2
            else:
                par[i] = count % 2
                count -= 1
        
        return par
