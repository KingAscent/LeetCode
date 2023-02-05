class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        // Sort the array, then initialize a min and max variable
        Arrays.sort(nums);
        int min = 0;
        int max = nums[nums.length - 1] - nums[0];

        // Binary search algorithm
        while(min < max){
            int mid = (min + max) / 2;
            int count = 0;
            int i = 0;

            // Find pairs with distance less than or equal to middle
            for(int j = 0; j < nums.length; j++){
                // Run through this segment of the code once, then break
                while(true){
                    int diff = nums[j] - nums[i];
                    if(mid < diff)
                        i++;
                    else
                        break;
                }
                count += j - i;
            }
            
            if(k <= count)
                max = mid;
            else
                min = mid + 1;
        }

        // Return the smallest distance found
        return min;
    }
}
