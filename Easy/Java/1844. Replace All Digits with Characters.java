class Solution {
    public String replaceDigits(String s) {
        char[] word = s.toCharArray();

        for(int i = 1; i < word.length; i += 2){
            int digit = Integer.parseInt(String.valueOf(s.charAt(i)));
            word[i] = shift(s.charAt(i - 1), digit);
        }

        return String.valueOf(word);
    }

    public char shift(char c, int x){
        return (char)(c + x);
    }
}
