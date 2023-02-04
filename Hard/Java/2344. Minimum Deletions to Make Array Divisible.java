class Solution {
    public int minOperations(int[] nums, int[] numsDivide) {
        // Initialize a greatest common divisor and a temp value
        int gcd = numsDivide[0];
        int temp = 0;

        // Find the greatest common divisor of numsDivide
        for(int i : numsDivide){
            while(0 < i){
                temp = gcd % i;
                gcd = i;
                i = temp;
            }
        }

        // Sort the nums array, then ignore any elements in nums that
        // are smaller than gcd. Return the smallest element nums[i]
        // that divides gcd
        Arrays.sort(nums);
        for(int i = 0; i < nums.length && nums[i] <= gcd; i++){
            if(gcd % nums[i] == 0)
                return i;
        }

        // No such element exists in nums, return -1
        return -1;
    }
}
