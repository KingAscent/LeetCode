class Solution {
    public String makeSmallestPalindrome(String s) {
        char[] palin = s.toCharArray();
        int n = s.length();

        for(int i = 0; i < n / 2; i++){
            int j = n - i - 1;
            if(palin[i] != palin[j]){
                if(palin[i] < palin[j])
                    palin[j] = palin[i];
                palin[i] = palin[j];
            }
        }

        return new String(palin);
    }
}
