class Solution {
    public String reverseWords(String s) {
        // Split all of the words by whitespaces
        // Initialize a StringBuilder so the word can be reversed
        // Initialize an index to keep track of which word is being reversed
        String[] split = s.split(" ");
        StringBuilder reversedWord = new StringBuilder();
        int index = 0;

        // For each word in the split array, reverse the word
        for(String word : split){
            StringBuilder backwards = new StringBuilder();
            backwards.append(word);
            backwards.reverse();
            reversedWord.append(backwards.toString());  // Add the now reversed word to the result
            if(index != split.length - 1){   // Check if the word is the last word in the split array
                reversedWord.append(" ");
                index++;
            }
        }
        
        // Return the StringBuilder as a string
        return reversedWord.toString();
    }
}
