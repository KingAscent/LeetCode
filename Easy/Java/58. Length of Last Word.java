class Solution {
    public int lengthOfLastWord(String s) {
        // Boolean value to keep track of when a word is found
        // Length of the longest last word
        boolean wordFound = false;
        int length = 0;
        
        // Go over the string looking for the last word
        for(int i = s.length() - 1; 0 <= i; i--){
            if(Character.isLetter(s.charAt(i))){
                wordFound = true;
                length++;
            }
            if(wordFound && !Character.isLetter(s.charAt(i)))
                return length;
        }
        
        return length;
    }
}
