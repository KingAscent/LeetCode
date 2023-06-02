class Solution(object):
    def spiralOrder(self, matrix):
        top = 0
        bot = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        spiral = []

        # Find all the elements of the matrix in spiral order
        while top <= bot and left <= right:
            # Top row
            for i in range(left, right + 1):
                spiral.append(matrix[top][i])
            top += 1
            
            # Right column
            for i in range(top, bot + 1):
                spiral.append(matrix[i][right])
            right -= 1

            # Bot row
            if top <= bot:
                for i in range(right, left - 1, -1):
                    spiral.append(matrix[bot][i])
                bot -= 1

            # Left column
            if left <= right:
                for i in range(bot, top - 1, -1):
                    spiral.append(matrix[i][left])
                left += 1
        
        return spiral
