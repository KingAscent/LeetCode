var largestLocal = function(grid) {
    let matrix = [];
    for(let i = 0; i < grid.length - 2; i++){
        matrix[i] = [];
    }

    for(let i = 0; i < grid.length - 2; i++){
        for(let j = 0; j < grid.length - 2; j++){
            matrix[i][j] = getMax(i, j, grid);
        }
    }

    return matrix;
};

var getMax = function(row, col, grid){
    let max = 0;
    
    for(let i = row; i < row + 3; i++){
        for(let j = col; j < col + 3; j++){
            max = Math.max(max, grid[i][j]);
        }
    }

    return max;
}
