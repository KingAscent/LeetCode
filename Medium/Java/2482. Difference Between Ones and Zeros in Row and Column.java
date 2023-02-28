class Solution {
    public int[][] onesMinusZeros(int[][] grid) {
        int rowLength = grid.length;
        int colLength = grid[0].length;
        int[] rowZeros = new int[rowLength];
        int[] rowOnes = new int[rowLength];
        int[] colZeros = new int[colLength];
        int[] colOnes = new int[colLength];

        // Use a for loop to find the ones and zeros and increment relevant values
        for(int i = 0; i < rowLength; i++){
            for(int j = 0; j < colLength; j++){
                if(grid[i][j] == 1){
                    rowOnes[i]++;
                    colOnes[j]++;
                }else{
                    rowZeros[i]++;
                    colZeros[j]++;
                }
            }
        }

        // Use a for loop to calculate the result for each value in grid
        for(int i = 0; i < rowLength; i++){
            for(int j = 0; j < colLength; j++){
                grid[i][j] = rowOnes[i] + colOnes[j] - rowZeros[i] - colZeros[j];
            }
        }

        return grid;
    }
}
