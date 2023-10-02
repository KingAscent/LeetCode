class Solution {
    public int thirdMax(int[] nums) {
        Arrays.sort(nums);
        int count = 0;
        int third = nums[0];

        for(int i = nums.length - 1; 0 <= i; i--){
            if(third != nums[i]){
                third = nums[i];
                count++;
            }
            if(count == 3)
                break;
        }

        return count == 3 ? third : nums[nums.length - 1];
    }
}
