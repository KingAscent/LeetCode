class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int sec = duration;

        for(int i = 1; i < timeSeries.length; i++){
            sec += Math.min(duration, timeSeries[i] - timeSeries[i - 1]);
        }

        return sec;
    }
}
