class Solution {
    public int minPairSum(int[] nums) {
        // Sort the array, initialize an index for a new array, initialize new array
        Arrays.sort(nums);
        int index = 0;
        int[] pairs = new int[nums.length / 2];

        // Use a for loop to travel over nums, placing each pair
        // Increase the index value after each pair is added
        for(int i = 0; i < nums.length / 2; i++){
            pairs[index] = nums[i] + nums[nums.length - i - 1];
            index++;
        }

        // Initialize a max value equal to the first integer in pairs
        // For each integer in pairs, compare it to max and set max to the larger
        int max = 0;
        for(int n : pairs)
            max = Math.max(n, max);
        
        // Return max
        return max;
    }
}
