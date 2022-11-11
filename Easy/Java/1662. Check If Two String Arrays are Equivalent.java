class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String firstWord = "";
        String secondWord = "";
        
        for(int i = 0; i < word1.length; i++){
            firstWord += word1[i];
        }

        for(int i = 0; i < word2.length; i++){
            secondWord += word2[i];
        }

        return firstWord.equals(secondWord);
    }
}
