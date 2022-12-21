class Solution {
    public String reversePrefix(String word, char ch) {
        char[] wordChars = word.toCharArray();

        for(int i = 0; i <= word.indexOf(ch); i++){
            wordChars[i] = word.charAt(word.indexOf(ch) - i);
        }

        return String.valueOf(wordChars);
    }
}
