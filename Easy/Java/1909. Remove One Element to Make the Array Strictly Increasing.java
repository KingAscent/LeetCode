class Solution {
    public boolean canBeIncreasing(int[] nums) {
        int count = 0;

        for(int i = 1; i < nums.length; i++){
            if(nums[i] <= nums[i - 1]){
                count++;
                if(1 < count)
                    return false;
                if(1 < i && nums[i] <= nums[i - 2])
                    nums[i] = nums[i - 1];
            }
        }

        return true;
    }
}
