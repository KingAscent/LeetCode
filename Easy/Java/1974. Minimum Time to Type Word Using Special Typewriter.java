class Solution {
    public int minTimeToType(String word) {
        int count = word.length();
        char prev = 'a';

        for(int i = 0; i < word.length(); i++){
            char curr = word.charAt(i);
            int diff = Math.abs(curr - prev);
            count += Math.min(diff, 26 - diff);
            prev = curr;
        }

        return count;
    }
}
