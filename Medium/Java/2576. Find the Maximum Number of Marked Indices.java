class Solution {
    public int maxNumOfMarkedIndices(int[] nums) {
        int i = 0;
        int j = (nums.length + 1) / 2;
        Arrays.sort(nums);

        while(j < nums.length){
            if(2 * nums[i] <= nums[j])
                i++;
            j++;
        }

        return 2 * i;
    }
}
