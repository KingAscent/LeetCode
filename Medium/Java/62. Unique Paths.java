class Solution {
    public int uniquePaths(int m, int n) {
        int[] row = new int[n];
        for(int i = 0; i < row.length; i++){
            row[i] = 1;
        }
        
        for(int i = 1; i < m; i++){
            int[] currRow = new int[n];
            currRow[0] = 1;
            for(int j = 1; j < n; j++){
                currRow[j] = 1;
                currRow[j] = currRow[j - 1] + row[j];
            }
            row = currRow;
        }

        return row[n - 1];
    }
}
