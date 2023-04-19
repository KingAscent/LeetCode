class Solution {
    public int minDeletion(int[] nums) {
        int del = 0;

        for(int i = 0; i < nums.length - 1; i += 2){
            if(nums[i] == nums[i + 1]){
                del++;
                i--;
            }
        }

        if((nums.length - del) % 2 == 0)
            return del;
        return del + 1;
    }
}
