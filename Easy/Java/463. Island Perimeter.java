class Solution {
    public int islandPerimeter(int[][] grid) {
        int island = 0;

        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 1){
                    island += 4;
                    if(0 < i && grid[i - 1][j] == 1)
                        island -= 2;
                    if(0 < j && grid[i][j - 1] == 1)
                        island -= 2;
                }
            }
        }

        return island;
    }
}
