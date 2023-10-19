class Solution {
    public int subsetXORSum(int[] nums) {
        return subsetXORSumHelper(nums, 0, 0);
    }

    public int subsetXORSumHelper(int[] nums, int i, int j){
        if(i == nums.length)
            return j;
        return subsetXORSumHelper(nums, i + 1, j^nums[i]) + subsetXORSumHelper(nums, i + 1, j);
    }
}
