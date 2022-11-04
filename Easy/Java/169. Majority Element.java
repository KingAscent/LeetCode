class Solution {
    public int majorityElement(int[] nums) {
        // Sort the array to group similar numbers
        Arrays.sort(nums);

        // Return the integer that is present in more than half
        // of the array
        return nums[nums.length / 2];
    }
}
