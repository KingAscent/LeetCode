class Solution(object):
    def hIndex(self, citations):
        length = len(citations)
        my_list = [0] * (length + 1)

        for num in citations:
            if length <= num:
                my_list[length] += 1
            else:
                my_list[num] += 1
        
        count = 0
        for i in range(length, 0, -1):
            count += my_list[i]
            if i <= count:
                return i
        
        return 0
