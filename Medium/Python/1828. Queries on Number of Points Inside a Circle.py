class Solution(object):
    def countPoints(self, points, queries):
        nums = [0] * len(queries)
        i = 0

        for q in queries:
            x0 = q[0]
            y0 = q[1]
            r = q[2]
            for p in points:
                x = p[0]
                y = p[1]
                dx = x - x0
                dy = y - y0
                if (dx * dx) + (dy * dy) <= (r * r):
                    nums[i] += 1
            i += 1
        
        return nums
