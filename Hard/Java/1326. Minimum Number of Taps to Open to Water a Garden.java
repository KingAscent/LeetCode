class Solution {
    public int minTaps(int n, int[] ranges) {
        int[] range = new int[n + 1];

        for(int i = 0; i < ranges.length; i++){
            int left = Math.max(0, i - ranges[i]);
            int right = Math.min(n, i + ranges[i]);
            range[left] = Math.max(range[left], right);
        }

        int end = 0;
        int maxRange = 0;
        int taps = 0;
        int i = 0;

        while(end < n){
            while(i <= end){
                maxRange = Math.max(maxRange, range[i]);
                i++;
            }

            if(maxRange <= end)
                return -1; // Can't water the garden
            end = maxRange;
            taps++;
        }

        return taps;
    }
}
