class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        maximum = 0
        for i in growTime:
            maximum = max(maximum, i)
        
        my_list = [0] * (maximum + 1)
        temp = 0
        minimum = 0

        for i in range(len(plantTime)):
            my_list[growTime[i]] += plantTime[i]
        
        for i in range(maximum, 0, -1):
            if my_list[i] != 0:
                temp += my_list[i]
                minimum = max(minimum, temp + i)
        
        return minimum
