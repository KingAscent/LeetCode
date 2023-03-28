class Solution(object):
    def maxArea(self, height):
        water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            min_height = min(height[left], height[right])
            water = max(water, min_height * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return water
