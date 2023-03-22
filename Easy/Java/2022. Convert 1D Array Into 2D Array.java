class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        if(original.length != m * n)
            return new int[0][];
        
        int[][] arr = new int[m][n];
        int row = 0;
        int col = 0;

        for(int num : original){
            arr[row][col] = num;
            col++;
            if(col == n){
                col = 0;
                row++;
            }
        }

        return arr;
    }
}
