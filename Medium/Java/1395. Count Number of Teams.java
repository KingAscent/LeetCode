class Solution {
    public int numTeams(int[] rating) {
        int count = 0;
        
        for(int i = 0; i < rating.length; i++){
            int left = 0;
            int right = 0;
            for(int j = 0; j < i; j++){
                if(rating[j] < rating[i])
                    left++;
            }
            for(int k = i + 1; k < rating.length; k++){
                if(rating[i] < rating[k])
                    right++;
            }
            count += (left * right) + (i - left) * (rating.length - i - right - 1);
        }

        return count;
    }
}
