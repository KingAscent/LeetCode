class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        if(nums1.length % 2 == 0 && nums2.length % 2 == 0)
            return 0;
        int n = 0;


        if(nums2.length % 2 == 1){
            for(int num : nums1)
                n ^= num;
        }
        if(nums1.length % 2 == 1){
            for(int num : nums2)
                n ^= num;
        }
        
        return n;
    }
}
