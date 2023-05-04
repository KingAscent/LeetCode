class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        int width = 0;
        int[] x = new int[points.length];

        for(int i = 0; i < points.length; i++){
            x[i] = points[i][0];
        }
        Arrays.sort(x);
        for(int i = 0; i < x.length - 1; i++){
            width = Math.max(width, (x[i + 1] - x[i]));
        }

        return width;
    }
}
