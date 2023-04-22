class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int xInt = points[0][0];
        int yInt = points[0][1];
        int sec = 0;

        for(int i = 0; i < points.length; i++){
            int x = points[i][0];
            int y = points[i][1];
            int dx = Math.abs(x - xInt);
            int dy = Math.abs(y - yInt);
            int temp = Math.max(dx, dy);
            dx -= temp;
            dy -= temp;
            sec += temp + Math.max(0, dx) + Math.max(0, dy);
            xInt = x;
            yInt = y;
        }

        return sec;
    }
}
