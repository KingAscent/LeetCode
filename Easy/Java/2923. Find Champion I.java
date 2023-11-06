class Solution {
    public int findChampion(int[][] grid) {
        for(int i = 0; i < grid.length; i++){
            boolean champ = true;
            for(int j = 0; j < grid.length; j++){
                if(i != j && grid[i][j] == 0)
                    champ = false;
            }
            if(champ)
                return i;
        }

        return -1;
    }
}
