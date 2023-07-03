class Solution(object):
    def countPoints(self, rings):
        count = 0
        red = [0] * 10
        blue = [0] * 10
        green = [0] * 10

        # Even position of rings
        for i in range(0, len(rings), 2):
            c = rings[i]
            index = int(rings[i + 1])
            if c == 'R':
                red[index] += 1
            if c == 'B':
                blue[index] += 1
            if c == 'G':
                green[index] += 1

        # Odd position of rings
        for i in range(10):
            if red[i] != 0 and blue[i] != 0 and green[i] != 0:
                count += 1

        return count
