class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        int[][] mat = new int[rowSum.length][colSum.length];

        // Fill each spot of the matrix by finding the min of
        // rowSum[i] and colSum[j], then place it into the
        // matrix. Subtract mat[i][j] from rowSum[i]
        // and colSum[j]
        for(int i = 0; i < rowSum.length; i++){
            for(int j = 0; j < colSum.length; j++){
                mat[i][j] = Math.min(rowSum[i], colSum[j]);
                rowSum[i] -= mat[i][j];
                colSum[j] -= mat[i][j];
            }
        }

        return mat;
    }
}
