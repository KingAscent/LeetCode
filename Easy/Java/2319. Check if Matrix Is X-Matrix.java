class Solution {
    public boolean checkXMatrix(int[][] grid) {
        boolean x = true;
        int n = grid.length;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if((i == j || (i + j) == n - 1) && grid[i][j] == 0){
                    x = false;
                }else if(i != j && (i + j) != n - 1 && grid[i][j] != 0){
                    x = false;
                }
            }
        }

        return x;
    }
}
