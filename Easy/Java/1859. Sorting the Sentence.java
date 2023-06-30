class Solution {
    public String sortSentence(String s) {
        String[] words = s.split(" ");
        String[] sentence = new String[words.length];

        for(String word : words){
            int n = word.length() - 1;
            sentence[word.charAt(n) - '1'] = word.substring(0, n);
        }

        return String.join(" ", sentence);
    }
}
