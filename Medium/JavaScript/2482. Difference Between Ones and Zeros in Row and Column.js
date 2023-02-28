var onesMinusZeros = function(grid) {
    let rowLength = grid.length;
    let colLength = grid[0].length;
    let rowZeros = Array(rowLength).fill(0);
    let rowOnes = Array(rowLength).fill(0);
    let colZeros = Array(colLength).fill(0);
    let colOnes = Array(colLength).fill(0);

    // Use a for loop to find the ones and zeros and increment relevant values
    for(let i = 0; i < rowLength; i++){
        for(let j = 0; j < colLength; j++){
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
    for(let i = 0; i < rowLength; i++){
        for(let j = 0; j < colLength; j++){
            grid[i][j] = rowOnes[i] + colOnes[j] - rowZeros[i] - colZeros[j];
        }
    }

    return grid;
};
