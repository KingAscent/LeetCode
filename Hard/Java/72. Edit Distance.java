class Solution {
    public int minDistance(String word1, String word2) {
        // Create two dimensional array of size (word1.length + 1) * (word2.length + 1)
        int length1 = word1.length();
        int length2 = word2.length();
        int[][] md = new int[length1 + 1][length2 + 1];

        // Initialize the first row and column of the array with the corresponding indices
        for(int i = 1; i <= length1; i++){
            md[i][0] = i;
        }
        for(int i = 1; i <= length2; i++){
            md[0][i] = i;
        }

        // For each [i, j] calculate the minimum edit distances
        for(int i = 1; i <= length1; i++){
            for(int j = 1; j <= length2; j++){
                if(word1.charAt(i - 1) == word2.charAt(j - 1)){ // Same characters
                    md[i][j] = md[i - 1][j - 1];
                }else{
                    //                  Deletion      Insertion
                    int temp = Math.min(md[i - 1][j], md[i][j - 1]);
                    // Substitution
                    md[i][j] = Math.min(md[i - 1][j - 1], temp) + 1;
                }
            }
        }

        // Return md[length1][length2] containing the minimum edit distance between
        // word1 and word2
        return md[length1][length2];
    }
}
