class Solution {
    public int maxVowels(String s, int k) {
        int maxSub = 0;
        int window = 0;

        for(int i = 0; i < s.length(); i++){
            if(isVowel(s.charAt(i)))
                window++;
            maxSub = Math.max(maxSub, window);

            // Move window to the right one character
            if(k - 1 <= i && isVowel(s.charAt(i - k + 1)))
                window--;
        }

        return maxSub;
    }

    public boolean isVowel(char c){
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}
