class Solution {
    public boolean check(int[] nums) {
        int count = 0;
        int n = nums.length;

        for(int i = 1; i < n; i++){
            if(nums[i] < nums[i - 1])
                count++;
        }

        if(1 < count || (count != 0 && nums[0] < nums[n - 1]))
            return false;
        return true;
    }
}
