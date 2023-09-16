class Solution {
    public int dominantIndex(int[] nums) {
        int largest = 0;        // Index of largest element
        int secondLargest = 1;  // Index of second largest element

        for(int i = 1; i < nums.length; i++){
            if(nums[largest] < nums[i]){
                secondLargest = largest;
                largest = i;
            }else if(nums[secondLargest] < nums[i])
                secondLargest = i;
        }

        return nums[secondLargest] * 2 <= nums[largest] ? largest : -1;
    }
}
