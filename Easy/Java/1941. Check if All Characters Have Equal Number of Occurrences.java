class Solution {
    public boolean areOccurrencesEqual(String s) {
        int[] count = new int[26];
        int max = 0;
        
        for(int i = 0; i < s.length(); i++){
            count[s.charAt(i) - 'a']++;
        }

        for(int x : count){
            max = Math.max(x, max);
        }

        for(int i = 0; i < count.length; i++){
            if(count[i] != 0 && max != count[i])
                return false;
        }

        return true;
    }
}
