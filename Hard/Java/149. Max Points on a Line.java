class Solution {
    public int maxPoints(int[][] points) {
        int count = 2; // Initialize count at 2 since every line needs at least 2 points
        int n = points.length;
        if(n <= 2)
            return n;

        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j++){
                int temp = 2; // Initialize temp count at 2 since every line needs at least 2 points

                /*
                    See if a point k is the line that has a slope of (y2 - y1)/(x2 - x1)
                    This can be expressed with (ky - y1)/(kx - x1) == (y2 - ky) / (x2 - kx)
                    And rewritten as (ky - y1)(x2 - kx) == (y2 - ky)(kx - x1)
                */
                for(int k = 0; k < n; k++){
                    if(k != i && k != j){
                        int a = points[j][1] - points[i][1]; // ky - y1
                        int b = points[i][0] - points[k][0]; // x2 - kx
                        int c = points[i][1] - points[k][1]; // y2 - ky
                        int d = points[j][0] - points[i][0]; // kx - x1
                        if(a * b == c * d)
                            temp++;
                    }
                }
                count = Math.max(count, temp);
            }

        }

        return count;
    }
}
