class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        x_int = points[0][0]
        y_int = points[0][1]
        sec = 0

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dx = abs(x - x_int)
            dy = abs(y - y_int)
            temp = max(dx, dy)
            dx -= temp
            dy -= temp
            sec += temp + max(0, dx) + max(0, dy)
            x_int = x
            y_int = y

        return sec
