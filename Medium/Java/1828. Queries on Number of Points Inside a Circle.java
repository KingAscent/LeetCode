class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        int[] nums = new int[queries.length];
        int i = 0;

        for(int[] q : queries){
            int x0 = q[0];
            int y0 = q[1];
            int r = q[2];
            for(int[] p : points){
                int x = p[0];
                int y = p[1];
                int dx = x - x0;
                int dy = y - y0;
                if((dx * dx) + (dy * dy) <= (r * r))
                    nums[i]++;
            }
            i++;
        }

        return nums;
    }
}
