class Solution(object):
    def countGoodRectangles(self, rectangles):
        length = 0
        count = 0

        for rectLength, rectWidth in rectangles:
            length = max(length, min(rectLength, rectWidth))
        
        for rectLength, rectWidth in rectangles:
            if min(rectLength, rectWidth) == length:
                count += 1
        
        return count
