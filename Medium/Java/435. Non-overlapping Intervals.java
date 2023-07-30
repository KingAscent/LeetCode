class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        int count = 0;
        int prev = 0;

        for(int i = 1; i < intervals.length; i++){
            if(intervals[i][0] < intervals[prev][1])
                count++;
            else
                prev = i;
        }

        return count;
    }
}
