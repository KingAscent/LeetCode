class Solution(object):
    def sortTheStudents(self, score, k):
        temp = []
        for i in score:
            temp.append(i[k])
        
        temp_list = list(sorted(temp, reverse = True))
        indeces = []
        for i in temp_list:
            indeces.append(temp.index(i))
        
        scores_by_k = []
        for i in indeces:
            scores_by_k.append(score[i])
        
        return scores_by_k

        # Pythonic One-liner
        # return sorted(score, key = lambda b: -b[k])
