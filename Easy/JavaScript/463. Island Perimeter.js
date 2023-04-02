var islandPerimeter = function(grid) {
    let island = 0;

    for(let i = 0; i < grid.length; i++){
        for(let j = 0; j < grid[0].length; j++){
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
};
