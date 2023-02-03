class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Create a new array
        int[] merged = new int[nums1.length + nums2.length];

        // Use a while loop to add values from nums1 and nums2 to the new array
        int i = 0;
        int j = 0;
        while(i < nums1.length || j < nums2.length){
            if(i < nums1.length){
                merged[i] = nums1[i];
                i++;
            }
            if(j < nums2.length){
                merged[j + nums1.length] = nums2[j];
                j++;
            }
        }

        // Sort the array without the sort function (Bubble Sort)
        for(int m = 0; m < merged.length; m++){
            for(int n = m + 1; n < merged.length; n++){
                int temp = 0;
                if(merged[n] < merged[m]){
                    temp = merged[m];
                    merged[m] = merged[n];
                    merged[n] = temp;
                }
            }
        }

        // Find the median double, and return it
        int middle = merged.length / 2;
        if(merged.length % 2 != 0)
            return (double) merged[middle];
        else
            return (double) (merged[middle] + merged[middle - 1]) / 2;
    }
}
