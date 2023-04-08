class Solution {
    public int firstMissingPositive(int[] nums) {
        int len = nums.length;
        int i = 0;

        while(i < len){
            int temp = nums[i];
            if(1 <= temp && temp <= len){
                if(nums[temp - 1] != temp){
                    nums[i] = nums[temp - 1];
                    nums[temp - 1] = temp;
                }else{
                    i++;
                }
            }else{
                i++;
            }
        }

        for(int j = 0; j < len; j++){
            if(nums[j] != j + 1)
                return j + 1;
        }

        return len + 1;
    }
}
