class Solution(object):
    def numberOfSteps(self, num):
        count = 0
        while 0 < num:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            count += 1
        return count
