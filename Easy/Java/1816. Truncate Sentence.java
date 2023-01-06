class Solution {
    public String truncateSentence(String s, int k) {
        String[] words = s.split(" ");
        String truncated = "";
        
        for(int i = 0; i < k; i++){
            truncated += words[i];
            if(i + 1 < k)
                truncated += " ";
        }

        return truncated;
    }
}
