class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        int len = 0;
        int count = 0;

        for(int[] rect : rectangles){
            len = Math.max(len, Math.min(rect[0], rect[1]));
        }

        for(int[] rect : rectangles){
            if(Math.min(rect[0], rect[1]) == len)
                count++;
        }

        return count;
    }
}
