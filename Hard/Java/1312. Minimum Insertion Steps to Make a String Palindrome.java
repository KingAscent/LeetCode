class Solution {
    public int minInsertions(String s) {
        int n = s.length();
        int[] min = new int[n];
        
        for(int i = n - 1; 0 <= i; i--){
            int prev = 0;
            for(int j = i; j < n; j++){
                int temp = min[j];
                if(s.charAt(i) == s.charAt(j))
                    min[j] = prev;
                else
                    min[j] = Math.min(min[j], min[j - 1]) + 1;
                prev = temp;
            }
        }

        return min[n - 1];
    }
}
