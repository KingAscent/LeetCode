class Solution(object):
    def isBoomerang(self, points):
        x1 = points[0][0]
        x2 = points[1][0]
        x3 = points[2][0]
        y1 = points[0][1]
        y2 = points[1][1]
        y3 = points[2][1]

        return (x3 - x2) * (y2 - y1) != (x2 - x1) * (y3 - y2)
