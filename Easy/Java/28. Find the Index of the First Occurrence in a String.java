class Solution {
    public int strStr(String haystack, String needle) {
        int left = 0;
        int right = needle.length() - 1;

        while(right < haystack.length()){
            String temp = haystack.substring(left, right + 1);
            if(temp.equals(needle))
                return left;
            left++;
            right++;
        }
        
        return -1;
    }
}
