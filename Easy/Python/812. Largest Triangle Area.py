class Solution(object):
    def area(self, a, b):
        base = b[0] - a[0]
        height = a[1] + b[1]
        return 0.5 * base * height

    def largestTriangleArea(self, points):
        n = len(points)
        largest = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    temp = 0
                    a = points[i]
                    b = points[j]
                    c = points[k]
                    temp = abs(self.area(a, b) + self.area(b, c) + self.area(c, a))
                    largest = max(largest, temp)

        return largest
