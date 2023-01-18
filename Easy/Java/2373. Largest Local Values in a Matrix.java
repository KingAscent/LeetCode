class Solution {
    public int[][] largestLocal(int[][] grid) {
        int matrix[][] = new int[grid.length - 2][grid.length - 2];

        for(int i = 0; i < grid.length - 2; i++){
            for(int j = 0; j < grid.length - 2; j++){
                matrix[i][j] = getMax(i, j, grid);
            }
        }

        return matrix;
    }

    private int getMax(int row, int col, int[][] grid){
        int max = 0;

        for(int i = row; i < row + 3; i++){
            for(int j = col; j < col + 3; j++){
                max = Math.max(max, grid[i][j]);
            }
        }
        
        return max;
    }
}
