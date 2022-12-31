class Solution(object):
    def sumZero(self, n):
        myList = []
        sum = 0

        for i in range(1, n):
            sum = sum + i
            myList.append(i)
        
        myList.append(0 - sum)

        return myList
