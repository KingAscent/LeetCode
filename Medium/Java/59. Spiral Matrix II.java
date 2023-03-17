class Solution {
    public int[][] generateMatrix(int n) {
        int[][] mat = new int[n][n];

        int temp = 1;
        int row = 0;
        int rowEnd = n - 1;
        int col = 0;
        int colEnd = n - 1;

        while(temp <= n * n){
            // Shift from left to right
            for(int i = col; i <= colEnd; i++){
                mat[row][i] = temp;
                temp++;
            }
            row++;

            // Shift from top to bot
            for(int i = row; i <= rowEnd; i++){
                mat[i][colEnd] = temp;
                temp++;
            }
            colEnd--;

            // Shift from right to left
            for(int i = colEnd; col <= i; i--){
                mat[rowEnd][i] = temp;
                temp++;
            }
            rowEnd--;

            // Shift from bot to top
            for(int i = rowEnd; row <= i; i--){
                mat[i][col] = temp;
                temp++;
            }
            col++;
        }

        return mat;
    }
}
