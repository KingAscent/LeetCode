class Solution(object):
    def countEven(self, num):
        count = 0

        for i in range(2, num + 1):
            temp = i
            this_sum = 0
            while 0 < temp:
                this_sum += temp % 10
                temp /= 10
            if this_sum % 2 == 0:
                count += 1

        return count
