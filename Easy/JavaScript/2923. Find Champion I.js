var findChampion = function(grid) {
    for(let i = 0; i < grid.length; i++){
        let champ = true;
        for(let j = 0; j < grid.length; j++){
            if(i != j && grid[i][j] == 0)
                champ = false;
        }
        if(champ)
            return i;
    }

    return -1;
};
