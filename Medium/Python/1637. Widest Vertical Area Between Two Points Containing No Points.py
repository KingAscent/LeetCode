class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        width = 0
        x = [0] * len(points)

        for i in range(len(points)):
            x[i] = points[i][0]
        x.sort()
        for i in range(len(points) - 1):
            width = max(width, (x[i + 1] - x[i]))

        return width
