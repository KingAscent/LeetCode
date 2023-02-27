class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        Arrays.sort(satisfaction);
        int n = satisfaction.length;
        int[] sums = new int[n + 1];
        int score = 0;
        int maxScore = 0;

        // Use a for loop to calculate the sums from right to left
        for(int i = (n - 1); 0 <= i; i--){
            sums[i] = sums[i + 1] + satisfaction[i];
            score += (i + 1) * satisfaction[i];
        }

        if(0 < score)
            maxScore = score;

        for(int i = 0; i < n; i++){
            score -= satisfaction[i];
            score -= sums[i + 1];
            if(maxScore < score)
                maxScore = score;
        }

        return maxScore;
    }
}
