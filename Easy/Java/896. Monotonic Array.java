class Solution {
    public boolean isMonotonic(int[] nums) {
        if(nums.length == 1)
            return true;
        
        boolean inc = true;
        boolean dec = true;

        for(int i = 0; i < nums.length - 1; i++){
            if(nums[i] < nums[i + 1])
                dec = false;
            if(nums[i + 1] < nums[i])
                inc = false;
            if(!inc && !dec)
                return false;
        }

        return inc || dec;
    }
}
