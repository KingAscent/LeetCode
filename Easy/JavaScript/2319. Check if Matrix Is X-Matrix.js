var checkXMatrix = function(grid) {
    let x = true;
    let n = grid.length;

    for(let i = 0; i < n; i++){
        for(let j = 0; j < n; j++){
            if((i == j || (i + j) == n - 1) && grid[i][j] == 0){
                x = false;
            }else if(i != j && (i + j) != n - 1 && grid[i][j] != 0){
                x = false;
            }
        }
    }

    return x;
};
