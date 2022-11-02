class Solution {
    public int mostWordsFound(String[] sentences) {
        // Keep track of the max number of words
        int max = 0;
        
        // Go over the array of strings, counting each word
        // in each sentence
        for(int i = 0; i < sentences.length; i++){
            int count = 1;
            for(int j = 1; j < sentences[i].length() - 1; j++){
                if(sentences[i].charAt(j) == ' ')
                    count++;
            }
            if(max < count)
                max = count;
        }
        
        // Return the max number of words
        return max;
    }
}
