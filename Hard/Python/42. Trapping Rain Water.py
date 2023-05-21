class Solution(object):
    def trap(self, height):
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        count = 0

        # Use two pointers to find out where water is trapped
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                count += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                count += maxRight - height[right]

        return count
