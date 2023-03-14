class Solution {
    public int minMaxGame(int[] nums) {
        if(nums.length == 1)
            return nums[0];
        
        int[] minMaxed = new int[nums.length / 2];
        for(int i = 0; i < minMaxed.length; i++){
            if(i % 2 == 0)
                minMaxed[i] = Math.min(nums[2 * i], nums[2 * i + 1]);
            else
                minMaxed[i] = Math.max(nums[2 * i], nums[2 * i + 1]);
        }

        return minMaxGame(minMaxed);
    }
}
