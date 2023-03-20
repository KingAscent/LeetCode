class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        index = 0

        while index < len(flowerbed):
            if flowerbed[index] == 0 and (index == 0 or flowerbed[index - 1] == 0) and\
               (index == len(flowerbed) - 1 or flowerbed[index + 1] == 0):
                flowerbed[index] = 1
                n -= 1
            if n <= 0:
                return True
            index += 1

        return False
