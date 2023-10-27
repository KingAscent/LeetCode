class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0;
        int track = 0;

        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 1)
                track++;
            else
                track = 0;
            count = Math.max(count, track);
        }

        return count;
    }
}
