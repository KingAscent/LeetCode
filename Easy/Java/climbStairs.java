class Solution {
    public int climbStairs(int n) {
        // Initial steps
        int oneStep = 1;
        int twoStep = 1;
        
        // Climb up the stairs, taking either 1 or 2 steps
        // The distinct ways of climbing to the top are tracked
        // using the oneStep variable
        for(int i = 1; i < n; i++){
            int step = oneStep + twoStep;
            twoStep = oneStep;
            oneStep = step;
        }
        
        // Return oneStep
        return oneStep;
    }
}
