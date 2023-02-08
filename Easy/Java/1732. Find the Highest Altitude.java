class Solution {
    public int largestAltitude(int[] gain) {
        int high = 0;
        int point = 0;
        
        for(int i = 0; i < gain.length; i++){
            point += gain[i];
            high = Math.max(high, point);
        }

        return high;
    }
}
