class Solution(object):
    def maxPoints(self, points):
        count = 2 # Initilize count at 2 since every line needs at least 2 points
        n = len(points)
        if n <= 2:
            return n
        
        for i in range(n):
            for j in range(i + 1, n):
                temp = 2 # Initialize temp count at 2 since every line needs at least 2 points

                '''
                See if a point k is the line that has a slope of (y2 - y1)/(x2 - x1)
                This can be expressed with (ky - y1)/(kx - x1) == (y2 - ky) / (x2 - kx)
                And rewritten as (ky - y1)(x2 - kx) == (y2 - ky)(kx - x1)
                '''
                for k in range(n):
                    if k != i and k != j:
                        a = points[j][1] - points[i][1]; # ky - y1
                        b = points[i][0] - points[k][0]; # x2 - kx
                        c = points[i][1] - points[k][1]; # y2 - ky
                        d = points[j][0] - points[i][0]; # kx - x1
                        if a * b == c * d:
                            temp += 1
                count = max(count, temp)

        return count
