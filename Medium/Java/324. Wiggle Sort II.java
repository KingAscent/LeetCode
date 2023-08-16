class Solution {
    public void wiggleSort(int[] nums) {
        Arrays.sort(nums);
        int mid = (nums.length - 1) / 2;
        int end = nums.length - 1;
        int[] store = new int[end + 1];
        int count = 0;
        
        while(0 <= mid || (nums.length - 1) / 2 < end){
            if(count % 2 == 0){
                store[count] = nums[mid];
                mid--;
            }else{
                store[count] = nums[end];
                end--;
            }
            count++;
        }

        for(int i = 0; i < nums.length; i++){
            nums[i] = store[i];
        }
    }
}
