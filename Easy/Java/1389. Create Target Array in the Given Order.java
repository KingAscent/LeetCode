class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        // Initialize a target array that will be returned
        int[] target = new int[nums.length];

        // Use a for loop to add all of the nums into the corresponding indeces
        // provided from the index array
        for(int i = 0; i < nums.length; i++){
            if(index[i] < i){
                for(int j = i; index[i] < j; j--){
                    target[j] = target[j - 1];
                }
            }
            target[index[i]] = nums[i];
        }

        // Return the target array
        return target;
    }
}
