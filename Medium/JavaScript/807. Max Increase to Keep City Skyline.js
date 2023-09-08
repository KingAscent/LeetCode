var maxIncreaseKeepingSkyline = function(grid) {
    let n = grid.length;
    let sum = 0;
    let row = Array(n).fill(0);
    let col = Array(n).fill(0);

    for(let i = 0; i < n; i++){
        row[i] = grid[i][0];
        col[i] = grid[0][i];
        for(let j = 0; j < n; j++){
            row[i] = Math.max(row[i], grid[i][j]);
            col[i] = Math.max(col[i], grid[j][i]);
        }
    }

    for(let i = 0; i < n; i++){
        for(let j = 0; j < n; j++){
            sum += Math.min(row[i], col[j]) - grid[i][j];
        }
    }

    return sum;
};
