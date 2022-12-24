class Solution(object):
    def selfDividingNumbers(self, left, right):
        myList = []

        for i in range(left, right + 1):
            number = i
            while(0 < number):
                if(number % 10) != 0 and i % (number % 10) == 0:
                    number = number / 10
                else:
                    number = -1
            if number != -1:
                myList.append(i)

        return myList
