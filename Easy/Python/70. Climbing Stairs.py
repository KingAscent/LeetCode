class Solution(object):
    def climbStairs(self, n):
        # Initial steps
        one_step = 1
        two_step = 1
        
        # Climb up the stairs, taking either 1 or 2 steps
        # The distinct ways of climbing to the top are tracked
        # using the one_step variable
        for i in range(1, n):
            step = one_step + two_step
            two_step = one_step
            one_step = step
        
        # Return one_step
        return one_step
        
