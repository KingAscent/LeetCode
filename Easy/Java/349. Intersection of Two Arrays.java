class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        int[] freq = new int[1001];

        for(int n : nums1){
            if(freq[n] == 0)
                freq[n]++;
        }

        int count = 0;
        for(int n : nums2){
            if(freq[n] == 1){
                freq[n]++;
                count++;
            }
        }

        int[] ans = new int[count];
        int index = 0;
        
        for(int i = 0; i < freq.length; i++){
            if(freq[i] == 2){
                ans[index] = i;
                index++;
            }
        }
        
        return ans;
    }
}
