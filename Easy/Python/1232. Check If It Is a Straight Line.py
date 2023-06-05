class Solution(object):
    def checkStraightLine(self, coordinates):
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]

        for i in range(2, len(coordinates)):
            x = coordinates[i][0]
            y = coordinates[i][1]

            if (y - y1) * (x - x2) != (y - y2) * (x - x1):
                return False

        return True
