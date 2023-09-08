class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int n = grid.length;
        int sum = 0;
        int[] row = new int[n];
        int[] col = new int[n];

        for(int i = 0; i < n; i++){
            row[i] = grid[i][0];
            col[i] = grid[0][i];
            for(int j = 0; j < n; j++){
                row[i] = Math.max(row[i], grid[i][j]);
                col[i] = Math.max(col[i], grid[j][i]);
            }
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                sum += Math.min(row[i], col[j]) - grid[i][j];
            }
        }

        return sum;
    }
}
